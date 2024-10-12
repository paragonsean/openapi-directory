

# WorkItemDetails

Information about an individual work item execution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attemptId** | **String** | Attempt ID of this work item |  [optional] |
|**endTime** | **String** | End time of this work item attempt. If the work item is completed, this is the actual end time of the work item. Otherwise, it is the predicted end time. |  [optional] |
|**metrics** | [**List&lt;MetricUpdate&gt;**](MetricUpdate.md) | Metrics for this work item. |  [optional] |
|**progress** | [**ProgressTimeseries**](ProgressTimeseries.md) |  |  [optional] |
|**startTime** | **String** | Start time of this work item attempt. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of this work item. |  [optional] |
|**stragglerInfo** | [**StragglerInfo**](StragglerInfo.md) |  |  [optional] |
|**taskId** | **String** | Name of this work item. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;EXECUTION_STATE_UNKNOWN&quot; |
| NOT_STARTED | &quot;EXECUTION_STATE_NOT_STARTED&quot; |
| RUNNING | &quot;EXECUTION_STATE_RUNNING&quot; |
| SUCCEEDED | &quot;EXECUTION_STATE_SUCCEEDED&quot; |
| FAILED | &quot;EXECUTION_STATE_FAILED&quot; |
| CANCELLED | &quot;EXECUTION_STATE_CANCELLED&quot; |



