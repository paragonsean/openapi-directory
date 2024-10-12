

# LanguageStats


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alerts** | **Integer** | The number of alerts for this language. |  [optional] |
|**analysisDate** | **OffsetDateTime** | The time the commit was analyzed. |  [optional] |
|**commitDate** | **OffsetDateTime** | The time of the commit. |  [optional] |
|**commitId** | **String** | The latest successfully analyzed commit for the language. All statistics refer to this commit. |  [optional] |
|**language** | **String** | The short name for the language. |  [optional] |
|**lines** | **Integer** | The number of lines of code for this language. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the analysis of this language. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| FAILURE | &quot;failure&quot; |
| PENDING | &quot;pending&quot; |



