

# Phrase


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**intensifyingPhrase** | **String** | If the phrase has been intensified, this gives the intensifying phrase |  |
|**isIntensified** | **Boolean** | Specifies whether the phrase has been intensified or not |  |
|**isNegated** | **Boolean** | Specifies whether the phrase has been negated or not |  |
|**negatingPhrase** | **String** | If the phrase has been negated, this gives the negating phrase |  |
|**sentimentPolarity** | [**SentimentPolarityEnum**](#SentimentPolarityEnum) | Verbal representation of sentiment score. Can be \&quot;negative\&quot;, \&quot;positive\&quot; or \&quot;neutral\&quot; |  |
|**sentimentScore** | **Double** | The sentiment score associated with this phrase |  |
|**title** | **String** | The text of the sentiment-bearing phrase |  |
|**type** | **String** | Type of phrase; can be either \&quot;possible\&quot; or \&quot;detected\&quot; value |  |



## Enum: SentimentPolarityEnum

| Name | Value |
|---- | -----|
| NEGATIVE | &quot;negative&quot; |
| POSITIVE | &quot;positive&quot; |
| NEUTRAL | &quot;neutral&quot; |



