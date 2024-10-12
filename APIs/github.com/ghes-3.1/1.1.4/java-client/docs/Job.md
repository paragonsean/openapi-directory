

# Job

Information of a job execution in a workflow run

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkRunUrl** | **String** |  |  |
|**completedAt** | **OffsetDateTime** | The time that the job finished, in ISO 8601 format. |  |
|**conclusion** | **String** | The outcome of the job. |  |
|**headSha** | **String** | The SHA of the commit that is being run. |  |
|**htmlUrl** | **String** |  |  |
|**id** | **Integer** | The id of the job. |  |
|**name** | **String** | The name of the job. |  |
|**nodeId** | **String** |  |  |
|**runId** | **Integer** | The id of the associated workflow run. |  |
|**runUrl** | **String** |  |  |
|**startedAt** | **OffsetDateTime** | The time that the job started, in ISO 8601 format. |  |
|**status** | [**StatusEnum**](#StatusEnum) | The phase of the lifecycle that the job is currently in. |  |
|**steps** | [**List&lt;JobStepsInner&gt;**](JobStepsInner.md) | Steps in this job. |  [optional] |
|**url** | **String** |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| QUEUED | &quot;queued&quot; |
| IN_PROGRESS | &quot;in_progress&quot; |
| COMPLETED | &quot;completed&quot; |



