# DataflowApi.WorkItemDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attemptId** | **String** | Attempt ID of this work item | [optional] 
**endTime** | **String** | End time of this work item attempt. If the work item is completed, this is the actual end time of the work item. Otherwise, it is the predicted end time. | [optional] 
**metrics** | [**[MetricUpdate]**](MetricUpdate.md) | Metrics for this work item. | [optional] 
**progress** | [**ProgressTimeseries**](ProgressTimeseries.md) |  | [optional] 
**startTime** | **String** | Start time of this work item attempt. | [optional] 
**state** | **String** | State of this work item. | [optional] 
**stragglerInfo** | [**StragglerInfo**](StragglerInfo.md) |  | [optional] 
**taskId** | **String** | Name of this work item. | [optional] 



## Enum: StateEnum


* `UNKNOWN` (value: `"EXECUTION_STATE_UNKNOWN"`)

* `NOT_STARTED` (value: `"EXECUTION_STATE_NOT_STARTED"`)

* `RUNNING` (value: `"EXECUTION_STATE_RUNNING"`)

* `SUCCEEDED` (value: `"EXECUTION_STATE_SUCCEEDED"`)

* `FAILED` (value: `"EXECUTION_STATE_FAILED"`)

* `CANCELLED` (value: `"EXECUTION_STATE_CANCELLED"`)




