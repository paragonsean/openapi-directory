

# JobStage

The details about the specific stage of a job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**detail** | **String** | The details of the stage. |  [optional] |
|**errorCode** | **String** | The error code of the stage if any. |  [optional] |
|**message** | **String** | The message of the job stage. |  [optional] |
|**stageStatus** | [**StageStatusEnum**](#StageStatusEnum) | The stage status. |  |



## Enum: StageStatusEnum

| Name | Value |
|---- | -----|
| RUNNING | &quot;Running&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



