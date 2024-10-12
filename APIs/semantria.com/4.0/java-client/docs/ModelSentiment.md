

# ModelSentiment


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mixedScore** | **Double** | Mixed sentiment score associated with the document |  |
|**modelName** | **String** | Name of the sentiment model used for scoring |  |
|**negativeScore** | **Double** | Negative (probable negative score) sentiment score associated with the document |  |
|**neutralScore** | **Double** | Neutral (probable neutral score) sentiment score associated with the document |  |
|**positiveScore** | **Double** | Positive (probable positive score) sentiment score associated with the document |  |
|**sentimentPolarity** | [**SentimentPolarityEnum**](#SentimentPolarityEnum) | Verbal representation of sentiment score that matches the best on the document. Can be \&quot;negative\&quot;, \&quot;positive\&quot; or \&quot;neutral\&quot; |  |



## Enum: SentimentPolarityEnum

| Name | Value |
|---- | -----|
| NEGATIVE | &quot;negative&quot; |
| POSITIVE | &quot;positive&quot; |
| NEUTRAL | &quot;neutral&quot; |



