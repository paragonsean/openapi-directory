

# Topic


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hitcount** | **Integer** | The number of documents within the collection that match the topic |  |
|**id** | **String** | Unique topic identifier |  |
|**sentimentPolarity** | [**SentimentPolarityEnum**](#SentimentPolarityEnum) | Verbal representation of sentiment score. Can be \&quot;negative\&quot;, \&quot;positive\&quot; or \&quot;neutral\&quot; |  |
|**sentimentScore** | **Double** | The sentiment score for documents content associated with the topic |  |
|**title** | **String** | The topic title, which is its label in the text |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the topic; can be either \&quot;concept\&quot; or \&quot;query\&quot; |  |



## Enum: SentimentPolarityEnum

| Name | Value |
|---- | -----|
| NEGATIVE | &quot;negative&quot; |
| POSITIVE | &quot;positive&quot; |
| NEUTRAL | &quot;neutral&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CONCEPT | &quot;concept&quot; |
| QUERY | &quot;query&quot; |



