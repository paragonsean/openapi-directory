

# EarningWithTQS


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Float** |  |  [optional] |
|**currency** | **String** |  |  [optional] |
|**dueDate** | **OffsetDateTime** | the date-time notation as defined by RFC 3339, section 5.6, for example, 2017-07-21T17:32:28Z |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**words** | **Long** |  |  [optional] |
|**wordsApproved** | **Long** |  |  [optional] |
|**wordsTranslated** | **Long** |  |  [optional] |
|**isAboveAverage** | **Boolean** | Is this score above or below the average among other vendors in the same project? |  [optional] |
|**score** | **Float** |  |  [optional] |
|**stringsEdited** | **Long** | The number of translated strings by this translator which was edited by a proofreader. |  [optional] |
|**stringsTranslated** | **Long** | The number of translated strings by this translator. |  [optional] |
|**projectId** | **Long** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PAID | &quot;paid&quot; |
| PENDING | &quot;pending&quot; |
| FAILED | &quot;failed&quot; |



