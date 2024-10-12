

# Opinion


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**quotation** | **String** | The text of the expressed opinion |  |
|**sentimentPolarity** | [**SentimentPolarityEnum**](#SentimentPolarityEnum) | Verbal representation of sentiment score. Can be \&quot;negative\&quot;, \&quot;positive\&quot; or \&quot;neutral\&quot; |  |
|**sentimentScore** | **Double** | The sentiment score associated with the opinion |  |
|**speaker** | **Float** | An entity title identifying the author of the opinion |  |
|**topic** | **String** | An entity title identifying the subject of the opinion, if applicable |  |
|**type** | [**TypeEnum**](#TypeEnum) | Type of opinion according to extracted entity |  |



## Enum: SentimentPolarityEnum

| Name | Value |
|---- | -----|
| NEGATIVE | &quot;negative&quot; |
| POSITIVE | &quot;positive&quot; |
| NEUTRAL | &quot;neutral&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NAMED | &quot;named&quot; |
| USER | &quot;user&quot; |



