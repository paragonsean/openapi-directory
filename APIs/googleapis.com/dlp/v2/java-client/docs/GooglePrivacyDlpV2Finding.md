

# GooglePrivacyDlpV2Finding

Represents a piece of potentially sensitive content.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Timestamp when finding was detected. |  [optional] |
|**findingId** | **String** | The unique finding id. |  [optional] |
|**infoType** | [**GooglePrivacyDlpV2InfoType**](GooglePrivacyDlpV2InfoType.md) |  |  [optional] |
|**jobCreateTime** | **String** | Time the job started that produced this finding. |  [optional] |
|**jobName** | **String** | The job that stored the finding. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | The labels associated with this &#x60;Finding&#x60;. Label keys must be between 1 and 63 characters long and must conform to the following regular expression: &#x60;[a-z]([-a-z0-9]*[a-z0-9])?&#x60;. Label values must be between 0 and 63 characters long and must conform to the regular expression &#x60;([a-z]([-a-z0-9]*[a-z0-9])?)?&#x60;. No more than 10 labels can be associated with a given finding. Examples: * &#x60;\&quot;environment\&quot; : \&quot;production\&quot;&#x60; * &#x60;\&quot;pipeline\&quot; : \&quot;etl\&quot;&#x60; |  [optional] |
|**likelihood** | [**LikelihoodEnum**](#LikelihoodEnum) | Confidence of how likely it is that the &#x60;info_type&#x60; is correct. |  [optional] |
|**location** | [**GooglePrivacyDlpV2Location**](GooglePrivacyDlpV2Location.md) |  |  [optional] |
|**name** | **String** | Resource name in format projects/{project}/locations/{location}/findings/{finding} Populated only when viewing persisted findings. |  [optional] |
|**quote** | **String** | The content that was found. Even if the content is not textual, it may be converted to a textual representation here. Provided if &#x60;include_quote&#x60; is true and the finding is less than or equal to 4096 bytes long. If the finding exceeds 4096 bytes in length, the quote may be omitted. |  [optional] |
|**quoteInfo** | [**GooglePrivacyDlpV2QuoteInfo**](GooglePrivacyDlpV2QuoteInfo.md) |  |  [optional] |
|**resourceName** | **String** | The job that stored the finding. |  [optional] |
|**triggerName** | **String** | Job trigger name, if applicable, for this finding. |  [optional] |



## Enum: LikelihoodEnum

| Name | Value |
|---- | -----|
| LIKELIHOOD_UNSPECIFIED | &quot;LIKELIHOOD_UNSPECIFIED&quot; |
| VERY_UNLIKELY | &quot;VERY_UNLIKELY&quot; |
| UNLIKELY | &quot;UNLIKELY&quot; |
| POSSIBLE | &quot;POSSIBLE&quot; |
| LIKELY | &quot;LIKELY&quot; |
| VERY_LIKELY | &quot;VERY_LIKELY&quot; |



