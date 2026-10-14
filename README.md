# Masters_Thesis 

# Abstract 
Ambiguity in social-cultural language exchanges often results in a message receiver misinterpreting meaning from a message deliverer. This paper explores whether it is possible to highlight socio-cultural nuance for message recipients using a combination of quantitative, qualitative, and computational linguistics techniques. Given a corpus of text data, the study decodes the underlying elements of the speaker’s expressions using computational approaches for decoding lexicon semantics. 

# Methodology
What models are used to analyze the dataset?  

The overall procedure is discourse analysis using dual model representations.

Step 1: N-grams
Output: Lexical Content Trends 

Step 2: Vectorization: TD - IDF
Output: Word Vectors 

Step 3: Logistic Regression Classifier 
Build: Logistic Regression--> Softmax--> Cross-Entropy Loss--> Stochastic Gradient Descent--> Model Evaluation--> Scoring of Documents of Lexical Trends
Output: Scoring of Documents on Lexical Trends

Step 4: RoBERTa-Large Fine Tuning
Build: RoBERTa-Large Fine Tuning-->Softmax-->Cross-Entropy Loss-->Stochastic Gradient Descent-->Model Evaluation--> Scoring of Documents of Lexical Trends


 
