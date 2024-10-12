

# JobMessage

A particular message pertaining to a Dataflow job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | Deprecated. |  [optional] |
|**messageImportance** | [**MessageImportanceEnum**](#MessageImportanceEnum) | Importance level of the message. |  [optional] |
|**messageText** | **String** | The text of the message. |  [optional] |
|**time** | **String** | The timestamp of the message. |  [optional] |



## Enum: MessageImportanceEnum

| Name | Value |
|---- | -----|
| IMPORTANCE_UNKNOWN | &quot;JOB_MESSAGE_IMPORTANCE_UNKNOWN&quot; |
| DEBUG | &quot;JOB_MESSAGE_DEBUG&quot; |
| DETAILED | &quot;JOB_MESSAGE_DETAILED&quot; |
| BASIC | &quot;JOB_MESSAGE_BASIC&quot; |
| WARNING | &quot;JOB_MESSAGE_WARNING&quot; |
| ERROR | &quot;JOB_MESSAGE_ERROR&quot; |



