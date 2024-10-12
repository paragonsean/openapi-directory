

# DocumentSentiment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**documentScores** | [**SentimentConfidenceScorePerLabel**](SentimentConfidenceScorePerLabel.md) |  |  |
|**id** | **String** | Unique, non-empty document identifier. |  |
|**sentences** | [**List&lt;SentenceSentiment&gt;**](SentenceSentiment.md) | Sentence level sentiment analysis. |  |
|**sentiment** | [**SentimentEnum**](#SentimentEnum) | Predicted sentiment for document (Negative, Neutral, Positive, or Mixed). |  |
|**statistics** | [**DocumentStatistics**](DocumentStatistics.md) |  |  [optional] |



## Enum: SentimentEnum

| Name | Value |
|---- | -----|
| POSITIVE | &quot;positive&quot; |
| NEUTRAL | &quot;neutral&quot; |
| NEGATIVE | &quot;negative&quot; |
| MIXED | &quot;mixed&quot; |



