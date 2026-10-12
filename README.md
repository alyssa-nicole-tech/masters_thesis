# Masters_Thesis 

# Abstract 
Ambiguity in social-cultural language exchanges often results in a message receiver misinterpreting meaning from a message deliverer. This paper explores whether it is possible to highlight socio-cultural nuance for message recipients using a combination of quantitative, qualitative, and computational linguistics techniques. Given a corpus of multimodal data, the study decodes the underlying elements of the speaker’s expressions using inspiration and frameworks from previous studies. The study begins with a review of previous research on approaches to analyzing syntax, morphology, lexicon, semantics, sociolinguistics, and phonology. It continues to establish language as a social and cultural tool through a review of key sociolinguistic findings from anthropological studies. The literature is applied to comprise a guiding framework for classical techniques. Next, the study will implement classical approaches derived from the review of literature into a Python environment to label insight on socio-cultural subtleties. The dataset selected for this study is a body of video clips from the series, “The Daily Show with Trevor Noah” produced between 2015 and 2021. The data has been transformed from it’s original multi-media format into a text-only format for the purposes of using corpus linguistics techniques. The data is analyzed to produce insight on patterns of linguistic vehiculation of nuanced signals for meaning, sentiment, semiotics, and stylistics. The patterns abstracted are used as annotation markers for a second set of randomized satire linguistic data. The labels are used for language model training and evaluated against baseline performance for increases in socio-cultural nuance detection.   

# Methodology
What models will I assemble in Python to analyze my thesis dataset?  

I have the ultimate goal discourse analysis using transformer representations. I have previously 
Since I need social nuance detection, a TD-IDF--> Logistic Regression classifier run will  into discourse analysis using transformer representations. I have previously assembled and trained a small-scale transformer model from scratch, but it was of little use to my analysis needs without large scale training data. Therefore, I am going to try fine-tuning open-source weights on a curriculum dataset and then deploy the fine-tune model on a dataset of interest to identify curriculum patterns.

Round 1. Learning Documents-->TF-IDF-->Logistic Regression-->Softmax-->Cross-Entropy Loss-->Stochastic Gradient Descent-->Model Evaluation--> Scoring of Documents of Interest

Round 2. Learning Documents-->RoBERTa-Large model--> Fine-Tuning-->Scoring of Documents of Interest

Dual Model Discourse Score-->Average of Scores from Logistic Regression +Transformer Model
 
