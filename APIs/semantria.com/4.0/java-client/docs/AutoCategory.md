

# AutoCategory


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categories** | [**List&lt;SubCategory&gt;**](SubCategory.md) | List of sub-categories of the current category if applicable |  |
|**sentimentPolarity** | [**SentimentPolarityEnum**](#SentimentPolarityEnum) | Verbal representation of sentiment score. Can be \&quot;negative\&quot;, \&quot;positive\&quot; or \&quot;neutral\&quot; |  |
|**sentimentScore** | **Double** | The sentiment score associated with this category |  |
|**strengthScore** | **Double** | Strength of the category matches with the document content |  |
|**title** | **String** | The category title, which is its label in the text |  |
|**type** | **String** | Type of category; can be either \&quot;node\&quot; (root level) or \&quot;leaf\&quot; (nested) value |  |



## Enum: SentimentPolarityEnum

| Name | Value |
|---- | -----|
| NEGATIVE | &quot;negative&quot; |
| POSITIVE | &quot;positive&quot; |
| NEUTRAL | &quot;neutral&quot; |



