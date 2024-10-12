

# JobStages

Job stages.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorDetails** | [**List&lt;ErrorDetails&gt;**](ErrorDetails.md) | Error details for the stage. This is optional |  [optional] |
|**jobStageDetails** | **Object** | Job Stage Details |  [optional] |
|**stageName** | **String** | Name of the job stage. |  [optional] |
|**stageStatus** | [**StageStatusEnum**](#StageStatusEnum) | Status of the job stage. |  |



## Enum: StageStatusEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| WAITING_FOR_ACTION | &quot;WaitingForAction&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| CANCELLING | &quot;Cancelling&quot; |



