

# JobStepsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**completedAt** | **OffsetDateTime** | The time that the job finished, in ISO 8601 format. |  [optional] |
|**conclusion** | **String** | The outcome of the job. |  |
|**name** | **String** | The name of the job. |  |
|**number** | **Integer** |  |  |
|**startedAt** | **OffsetDateTime** | The time that the step started, in ISO 8601 format. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The phase of the lifecycle that the job is currently in. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| QUEUED | &quot;queued&quot; |
| IN_PROGRESS | &quot;in_progress&quot; |
| COMPLETED | &quot;completed&quot; |



