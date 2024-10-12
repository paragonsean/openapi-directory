

# SentenceSentiment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**length** | **Integer** | The length of the sentence by Unicode standard. |  |
|**offset** | **Integer** | The sentence offset from the start of the document. |  |
|**sentenceScores** | [**SentimentConfidenceScorePerLabel**](SentimentConfidenceScorePerLabel.md) |  |  |
|**sentiment** | [**SentimentEnum**](#SentimentEnum) | The predicted Sentiment for the sentence. |  |
|**warnings** | **List&lt;String&gt;** | The warnings generated for the sentence. |  [optional] |



## Enum: SentimentEnum

| Name | Value |
|---- | -----|
| POSITIVE | &quot;positive&quot; |
| NEUTRAL | &quot;neutral&quot; |
| NEGATIVE | &quot;negative&quot; |



