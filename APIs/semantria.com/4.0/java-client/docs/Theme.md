

# Theme


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mentions** | [**List&lt;Mention&gt;**](Mention.md) | Returns the concept and query defined topics determined for the text |  |
|**normalized** | **String** | The normalized form of the theme |  |
|**phrasesCount** | **Integer** | Count of sentiment-bearing phrases was used in calculating theme&#39;s sentiment |  |
|**sentimentPolarity** | [**SentimentPolarityEnum**](#SentimentPolarityEnum) | Verbal representation of sentiment score. Can be \&quot;negative\&quot;, \&quot;positive\&quot; or \&quot;neutral\&quot; |  |
|**sentimentScore** | **Double** | Sentiment score for theme’s sentences across the documents |  |
|**stemmed** | **String** | The stemmed form of the theme |  |
|**themesCount** | **Integer** | Count of themes across the documents that got rolled into this one |  |
|**title** | **String** | The text of the theme across the documents |  |



## Enum: SentimentPolarityEnum

| Name | Value |
|---- | -----|
| NEGATIVE | &quot;negative&quot; |
| POSITIVE | &quot;positive&quot; |
| NEUTRAL | &quot;neutral&quot; |



