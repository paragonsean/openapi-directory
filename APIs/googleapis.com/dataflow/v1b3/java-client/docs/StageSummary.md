

# StageSummary

Information about a particular execution stage of a job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **String** | End time of this stage. If the work item is completed, this is the actual end time of the stage. Otherwise, it is the predicted end time. |  [optional] |
|**metrics** | [**List&lt;MetricUpdate&gt;**](MetricUpdate.md) | Metrics for this stage. |  [optional] |
|**progress** | [**ProgressTimeseries**](ProgressTimeseries.md) |  |  [optional] |
|**stageId** | **String** | ID of this stage |  [optional] |
|**startTime** | **String** | Start time of this stage. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of this stage. |  [optional] |
|**stragglerSummary** | [**StragglerSummary**](StragglerSummary.md) |  |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;EXECUTION_STATE_UNKNOWN&quot; |
| NOT_STARTED | &quot;EXECUTION_STATE_NOT_STARTED&quot; |
| RUNNING | &quot;EXECUTION_STATE_RUNNING&quot; |
| SUCCEEDED | &quot;EXECUTION_STATE_SUCCEEDED&quot; |
| FAILED | &quot;EXECUTION_STATE_FAILED&quot; |
| CANCELLED | &quot;EXECUTION_STATE_CANCELLED&quot; |



