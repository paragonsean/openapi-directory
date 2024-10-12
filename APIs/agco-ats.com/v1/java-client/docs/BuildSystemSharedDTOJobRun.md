

# BuildSystemSharedDTOJobRun

A DTO for an IJobRun

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activityRuns** | [**List&lt;BuildSystemSharedDTOActivityRun&gt;**](BuildSystemSharedDTOActivityRun.md) | The activity runs belonging to this JobRun |  [optional] [readonly] |
|**endDate** | **OffsetDateTime** | The UTC date and time when the job completed |  [optional] |
|**jobID** | **Integer** | The ID of the job that defines the run |  [optional] |
|**jobRunID** | **Integer** | The ID of this JobRun |  [optional] |
|**parameters** | [**List&lt;BuildSystemSharedDTOParameterValue&gt;**](BuildSystemSharedDTOParameterValue.md) | The parameters used for this run of the job |  [optional] [readonly] |
|**startDate** | **OffsetDateTime** | The UTC date and time when the job started |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of this JobRun |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| READY | &quot;Ready&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| FAILED | &quot;Failed&quot; |



