# List of datasets that can be potentially transformed into sequential databases

## Clickstream data for online shopping Data Set
source : http://archive.ics.uci.edu/ml/datasets/clickstream+data+for+online+shopping

description : The dataset contains information on clickstream from online store offering clothing for pregnant women

nombre de séquences : 165 474

nombre d'attributs : 14

## microblogPCU Data Set
source : http://archive.ics.uci.edu/ml/datasets/microblogPCU

description : MicroblogPCU data is crawled from sina weibo microblog[[Web Link]]. This data can be used to study machine learning methods as well as do some social network research.

nombre de séquences : 221 579

nombre d'attributs : 20

## Online Retail Data Set
source : http://archive.ics.uci.edu/ml/datasets/Online+Retail+II

description :  A real online retail transaction data set of two years.

nombre de tuples : 1 067 371 (à transformer sous forme de séquences)

nombre d'attributs : 8 

## Deeds E-learning
source :  http://www.philippe-fournier-viger.com/spmf/EPMData.zip

description : Ce sont des données sur des apprenants qui font des activités d'apprentissage en ligne.  Un apprenant effectue plusieurs sessions et à l'intérieur de chaque session il y a des activités. Les sessions et activités sont optionnelles et un apprenant peut les faire dans différents ordres.   Dans les données, il y a plsieurs informations comme le temps, les scores obtenus à des évaluations à la fin de sessions et activités. 
Actuellement, ces données sont sous la forme de 2 séquences: séquences de sessions par des apprenants et séquence d'activités pour une session choisie. Il faudrait donc les retransformer pour avoir une séquence ou chaque itemset est une session et chaque item est une activité.

nombre de séquences : 64

nombre d'attributs : ?

## PHYSIOLOGICAL DATA SET
source : http://www.inf.ed.ac.uk/teaching/courses/dme/html/datasets0405.html (lien mort)

description : This data set was made available for the Physiological Data Modeling Contest at ICML 2004. The data was collected from subjects using BodyMedia wearable body monitors while performing their usual activities. These monitors record acceleration, heat flux, galvanic skin response, skin temperature, and near-body temperature. The training data set includes several sessions for each of multiple subjects, with measurements stored each minute during a session. The test data set includes further sessions from the same subjects, as well as sessions recording measurements from new subjects who did not feature in the training data. Each record in the data includes an annotation code giving information about the kind of activity that the subject was performing at that time. Participants in the competition were asked to train classifiers to apply two of these annotation codes to the test data, and also to train a classifier to identify subjects as men or women (this information is given in the training data sequences).

nombre de séquences : ?

nombre d'attributs : 16
