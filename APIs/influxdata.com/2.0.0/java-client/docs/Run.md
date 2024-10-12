

# Run


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**finishedAt** | **OffsetDateTime** | Time run finished executing, RFC3339Nano. |  [optional] [readonly] |
|**id** | **String** |  |  [optional] [readonly] |
|**links** | [**RunLinks**](RunLinks.md) |  |  [optional] |
|**log** | [**List&lt;LogEvent&gt;**](LogEvent.md) | An array of logs associated with the run. |  [optional] [readonly] |
|**requestedAt** | **OffsetDateTime** | Time run was manually requested, RFC3339Nano. |  [optional] [readonly] |
|**scheduledFor** | **OffsetDateTime** | Time used for run&#39;s \&quot;now\&quot; option, RFC3339. |  [optional] |
|**startedAt** | **OffsetDateTime** | Time run started executing, RFC3339Nano. |  [optional] [readonly] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] [readonly] |
|**taskID** | **String** |  |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SCHEDULED | &quot;scheduled&quot; |
| STARTED | &quot;started&quot; |
| FAILED | &quot;failed&quot; |
| SUCCESS | &quot;success&quot; |
| CANCELED | &quot;canceled&quot; |



