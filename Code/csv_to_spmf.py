from typing import Dict, List, Tuple
import pandas as pd
import os
import json
import statistics
import csv

def transactional_to_sequential(data: pd.DataFrame, date_order: str) -> List[List[List[str]]]:
    """ Transform a temporal (or ordered) transactional database into sequential data (sequences of itemsets).
    
    Parameters:
        data (DataFrame): input transactional data  
        date_order (str): name of the column with dates or orders

    Returns:
        List[List[List[str]]]: a list of sequence of itemsets (where an itemset is a list of strings)
    """
    
    # add the column name in the values 
    # if the value is a list, then it adds the column name to each values of the list 
    data[ data.columns[2:]] = data[ data.columns[2:]].astype(str).apply(lambda x: x.str.replace('["', x.name+'=', regex=False).str.replace('"]','', regex=False).str.replace('", "', ', '+x.name+'=',regex=False) if '[' in str(x) else x.name+'='+x )

    # merge all the columns except the id and the date in a column 'itemset'
    # and convert strings into lists
    data['itemset'] = data[ data.columns[2:]].agg(', '.join, axis=1)
    data['itemset'] = data['itemset'].str.split(', ')

    # print(data['itemset'].head(10))

    # group input data by id and order by date/order
    data_grouped = data.sort_values(['Id', date_order], ascending=True).groupby('Id')

    # aggregate the itemsets associated to each id into a list (sequence)
    data_sequence = data_grouped['itemset'].apply(list).reset_index(name='sequence')

    # print(data_sequence.head(10))

    # get the list of sequences of itemsets (i.e. sets of items)
    list_sequence = data_sequence['sequence'].values.tolist()

    # returns the list of sequence of itemsets
    return list_sequence


def stat_sequences(sequences: List[List[List[str]]])-> List[Dict]:
    """ Process several stats (e.g. number, avg size, ) on an input sequential database
    
    Parameters:
        sequences (List[List[List[str]]]): input sequential database

    Returns:
        List[Dict]: a list of stats (name,value)
    """
    stats = []

    # get the number of sequences
    nber = {'database size': len(sequences)}
    stats.append(nber)

    # get the number of timeslots of each sequence
    seq_size = [len(seq) for seq in sequences]

    # get the average the number of timeslots
    avg_seq_size = {'avg number of itemsets per sequence': float(sum(seq_size)/nber['database size'])}
    stats.append(avg_seq_size)

    # get the median number of timeslots
    med_seq_size = {'median number of itemsets per sequence': statistics.median(seq_size)}
    stats.append(med_seq_size)

    # get the max the number of timeslots
    max_seq_size = {'max number of itemsets per sequence': max(seq_size)}
    stats.append(max_seq_size)

    # get the number of items in each itemset of each sequence (the lengths of sequences)
    lengths = [ sum([len(itemset) for itemset in seq]) for seq in sequences]

    # get the average the number of items
    avg_length = {'avg length': float(sum(lengths)/nber['database size'])}
    stats.append(avg_length)

    # get the median number of items
    med_length = {'median length': statistics.median(lengths)}
    stats.append(med_length)

    # get the max the number of items
    max_length = {'max length': max(lengths)}
    stats.append(max_length)

    return stats


def map_str_int( str_sequences: List[List[List[str]]]) -> Tuple[Dict,Dict]  :
    """ Map each string in the input sequences to an integer value
        
    Parameters:
        str_sequences (List[List[str]]): input sequences with original values (strings)

    Returns:
        Tuple[Dict,Dict]: two maps - the first one enables to encode values to int and the second one int to values     
    """
    # list all different values
    all_values = {val for sequence in str_sequences for itemset in sequence for val in itemset}

    # generate the mapping  string to int
    mapping_str_int = {val: i+1 for i,val in enumerate(all_values)}

    #generate the mapping int to string
    mapping_int_str = {i+1: val for i,val in enumerate(all_values)}

    return mapping_str_int,mapping_int_str


def str_seq_to_int_seq(str_sequences: List[List[List[str]]], mapping: Dict)-> List[List[List[int]]]:
    """" Convert sequences with string values to sequence with int values base on the input mapping

    Parameters:
        str_sequences (List[List[List[str]]]): sequences to convert
        mapping (Dict): string to int mapping

    Returns:
        List[List[List[int]]]: converted sequences
    """

    return [ [ [mapping[item] for item in itemsets ] for itemsets in seq] for seq in str_sequences ]


def int_seq_to_str_seq(int_sequences: List[List[List[int]]], mapping: Dict)-> List[List[List[str]]]:
    """" Convert sequences with int values to sequence with string values base on the input mapping

    Parameters:
        int_sequences (List[List[List[int]]]): sequences to convert
        mapping (Dict): int to string mapping

    Returns:
        List[List[List[str]]]: converted sequences
    """

    return [ [ [mapping[item] for item in itemsets ] for itemsets in seq] for seq in int_sequences ]


def csv_to_spmf_data(csv_file_name: str, spmf_file_name:str, order_attribute=False):
    """ Convert temporal transactional database in csv format to the spmf format.

    Parameters:
    csv_file_name (str): name of the input csv file 
    spmf_file_name (str): name of the output spmf file
    order_attribute (bool, default=False): True if the input data has an "Order" attribute instead of a "Date" one 
    """
    temporal_attribute = 'Date'

    # open csv files
    if order_attribute:
        data = pd.read_csv(csv_file_name, sep=';')
        temporal_attribute = 'Order' 
    else:
        data = pd.read_csv(csv_file_name, parse_dates=['Date'], sep=';') 

    # get sequences and print stats about the database
    sequences = transactional_to_sequential(data, temporal_attribute) 
    print(csv_file_name+': '+str(stat_sequences(sequences)))

    # convert string to int (and store the mapping)
    (mapping_str_int, mapping_int_str) = map_str_int(sequences)

    # save the mapping "int to string" into a json file
    pos_file_name = spmf_file_name.rfind('/')
    path = spmf_file_name[:pos_file_name+1]
    file_name = spmf_file_name[pos_file_name+1 : len(spmf_file_name)-4]  
    with open(path+file_name+'.json', 'w') as out_file:
        json.dump( mapping_int_str, out_file)

    # convert string to int and save in file in SPMF format
    int_sequences = str_seq_to_int_seq(sequences, mapping_str_int)
    with open(spmf_file_name, 'w') as in_file:
        for seq in int_sequences:  
            str_seq =''          
            for itemset in seq:
                str_seq += ' '.join([str(item) for item in itemset])+' -1 '
            str_seq += '-2\n'                
            in_file.write( str_seq )


def spmf_patterns_to_csv(spmf_file_name:str, csv_file_name: str, mapping_file_name: str):
    """ Convert int patterns outputed by the SPMF library to string patterns in csv format.

    Parameters:
        spmf_file_name (str): name of the spmf file with all patterns
        csv_file_name (str): name of the csv file 
        mapping_file_name (str): name of the json file in which the int to string mapping is stored
    """
    mapping = {}
    with open(mapping_file_name) as mapping_file:

        # load the mapping 
        mapping = json.load(mapping_file)

        # convert int to string and save in a csv file
        with open(spmf_file_name, 'r') as pattern_file:
            for line in pattern_file:  
                # extract the string corresponding to the current pattern and its frequency
                pos_freq = line.rfind('-1')  # get the position of the frequency
                freq = line[pos_freq+3 : len(line)-1]  
                pattern = line[:pos_freq-1]  

                # convert the pattern string to a sequence of itemsets (list of list of string)
                str_seq = [ [mapping[item] for item in itemset.split(' ')] for itemset in pattern.split(' -1 ') ]

                # concatenate itemsets into a single string separetaed by ';' and add the frequency at the beginning
                str_seq_itemsets = [freq]
                for itemset in str_seq :
                    str_seq_itemsets.append(' '.join(itemset))

                # save the converted pattern in the csv file
                with open(csv_file_name, 'a', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(str_seq_itemsets)
            

      

# convert csv files to spmf files
csv_to_spmf_data('./Data/CSV/e_shop.csv', './Data/SPMF/e_shop.txt', order_attribute=True) 
csv_to_spmf_data('./Data/CSV/microblogPCU.csv', './Data/SPMF/microblogPCU.txt') 
csv_to_spmf_data('./Data/CSV/online_retail_II_all_products.csv', './Data/SPMF/online_retail_II_all_products.txt') 
csv_to_spmf_data('./Data/CSV/online_retail_II_best_products.csv', './Data/SPMF/online_retail_II_best_products.txt') 
