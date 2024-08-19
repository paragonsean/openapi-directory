

# CodereviewLanguages


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alerts** | [**List&lt;CodereviewAlerts&gt;**](CodereviewAlerts.md) | The list of added and fixed alerts per query for this language. |  [optional] |
|**fixed** | **Integer** | The total number of alerts fixed by the patch for this language. |  [optional] |
|**language** | **String** | The language analyzed. |  [optional] |
|**_new** | **Integer** | The total number of alerts introduced by the patch for this language. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status for analysis of this language. |  [optional] |
|**statusMessage** | **String** | The current state of analysis of this langauge. When available, a summary of analysis results. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| FAILURE | &quot;failure&quot; |
| SUCCESS | &quot;success&quot; |



