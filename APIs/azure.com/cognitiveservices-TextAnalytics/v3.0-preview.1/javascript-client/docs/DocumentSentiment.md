# TextAnalyticsClient.DocumentSentiment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documentScores** | [**SentimentConfidenceScorePerLabel**](SentimentConfidenceScorePerLabel.md) |  | 
**id** | **String** | Unique, non-empty document identifier. | 
**sentences** | [**[SentenceSentiment]**](SentenceSentiment.md) | Sentence level sentiment analysis. | 
**sentiment** | **String** | Predicted sentiment for document (Negative, Neutral, Positive, or Mixed). | 
**statistics** | [**DocumentStatistics**](DocumentStatistics.md) |  | [optional] 



## Enum: SentimentEnum


* `positive` (value: `"positive"`)

* `neutral` (value: `"neutral"`)

* `negative` (value: `"negative"`)

* `mixed` (value: `"mixed"`)




