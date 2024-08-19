

# JobProperties

Properties of the Job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**correlationData** | **Map&lt;String, String&gt;** | Customer provided key, value pairs that will be returned in Job and JobOutput state events. |  [optional] |
|**created** | **OffsetDateTime** | The UTC date and time when the Job was created, in &#39;YYYY-MM-DDThh:mm:ssZ&#39; format. |  [optional] [readonly] |
|**description** | **String** | Optional customer supplied description of the Job. |  [optional] |
|**input** | [**JobInput**](JobInput.md) |  |  |
|**lastModified** | **OffsetDateTime** | The UTC date and time when the Job was last updated, in &#39;YYYY-MM-DDThh:mm:ssZ&#39; format. |  [optional] [readonly] |
|**outputs** | [**List&lt;JobOutput&gt;**](JobOutput.md) | The outputs for the Job. |  |
|**priority** | [**PriorityEnum**](#PriorityEnum) | Priority with which the job should be processed. Higher priority jobs are processed before lower priority jobs. If not set, the default is normal. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | The current state of the job. |  [optional] [readonly] |



## Enum: PriorityEnum

| Name | Value |
|---- | -----|
| LOW | &quot;Low&quot; |
| NORMAL | &quot;Normal&quot; |
| HIGH | &quot;High&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| CANCELED | &quot;Canceled&quot; |
| CANCELING | &quot;Canceling&quot; |
| ERROR | &quot;Error&quot; |
| FINISHED | &quot;Finished&quot; |
| PROCESSING | &quot;Processing&quot; |
| QUEUED | &quot;Queued&quot; |
| SCHEDULED | &quot;Scheduled&quot; |



