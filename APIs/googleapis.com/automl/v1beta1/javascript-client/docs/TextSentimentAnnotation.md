# CloudAutoMlApi.TextSentimentAnnotation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sentiment** | **Number** | Output only. The sentiment with the semantic, as given to the AutoMl.ImportData when populating the dataset from which the model used for the prediction had been trained. The sentiment values are between 0 and Dataset.text_sentiment_dataset_metadata.sentiment_max (inclusive), with higher value meaning more positive sentiment. They are completely relative, i.e. 0 means least positive sentiment and sentiment_max means the most positive from the sentiments present in the train data. Therefore e.g. if train data had only negative sentiment, then sentiment_max, would be still negative (although least negative). The sentiment shouldn&#39;t be confused with \&quot;score\&quot; or \&quot;magnitude\&quot; from the previous Natural Language Sentiment Analysis API. | [optional] 


