**microblogPCU Data Set**  
_Download_: [Data Folder](../machine-learning-databases/00323/), [Data Set Description](#)

**Abstract**: MicroblogPCU data is crawled from sina weibo microblog\[[\[Web Link\]](https://weibo.com/)\]. This data can be used to study machine learning methods as well as do some social network research.

**Data Set Characteristics:** 

Multivariate, Univariate, Sequential, Text

**Number of Instances:**

221579

**Area:**

Computer

**Attribute Characteristics:**

Integer, Real

**Number of Attributes:**

20

**Date Donated**

2015-03-17

**Associated Tasks:**

Classification, Causal-Discovery

**Missing Values?**

Yes

**Number of Web Hits:**

57800

  

**Source:**

Jun Liu(liukeen '@' mail.xjtu.cn), Hao Chen(lechenhao '@' gmail.com) , Mengting Zhan, Jianhong Mi,Yanzhang Lv  
MOEKLINNS Lab, Department of Computer Science ,Xi'an Jiaotong University, China  

  

**Data Set Information:**

Our dataset is used by us to explore spammers in microblog and you can access our demo system at  
[\[Web Link\]](http://sd.skyclass.net/Spammer/dia.jsp)  
  
Please add :8080 after the domain name as port. The repository webpage fails to parse the weblink when it's added in the source. (under inspection)

  

**Attribute Information:**

weibo\_user.csv has the following attributes:  
\-user\_id: account ID in sina weibo;  
\-user\_name: account nicknameï¼›  
\-gender:account registration gender including maleï¼Œ female and otherï¼›  
\-class:account level given by sina weibo;  
\-message:account registration location or other personal information;  
\-post\_num: the number of posts of this account up to now;  
\-follower\_num: the number of followers of this account;  
\-followee\_num: the number of followee of this account;  
\-follow ratio: followee\_num/follower\_num;  
\-is\_spammer: manually annotated label, 1 means spammer and -1 means non-spammer;  
user\_post.csv has the following attributes:  
\-post\_id:user post ID given by sina weibo;  
\-post\_time:the time when a post is posted;  
\-poster\_id: the user ID who posted this post;  
\-repost\_num:the number of retweet by others;  
\-commnet\_num: the number of comment by others;  
followe-followee.csv has the following attributes:  
\-follower: the nickname of follower;  
\-follower\_id: the user ID of follower;  
\-followee: the nickname of followee;  
\-followee\_id: the user ID of followee;  
post.csv is almost the as user\_post.csv and the post in it are retrievalled by a certain key word related to a topic;  
  
\-content: the post text(mostly in Chinese, please set your Microsoft Office to make it readable)

  

**Relevant Papers:**

N/A

  
  

**Citation Request:**

Thanks to MOEKLINNS Lab\[[\[Web Link\]](http://labs.xjtudlc.com/labs/zscl.html)\] especially Spammer Detection Group for opening its data
