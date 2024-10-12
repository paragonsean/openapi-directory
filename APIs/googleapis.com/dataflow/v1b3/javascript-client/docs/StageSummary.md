# DataflowApi.StageSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endTime** | **String** | End time of this stage. If the work item is completed, this is the actual end time of the stage. Otherwise, it is the predicted end time. | [optional] 
**metrics** | [**[MetricUpdate]**](MetricUpdate.md) | Metrics for this stage. | [optional] 
**progress** | [**ProgressTimeseries**](ProgressTimeseries.md) |  | [optional] 
**stageId** | **String** | ID of this stage | [optional] 
**startTime** | **String** | Start time of this stage. | [optional] 
**state** | **String** | State of this stage. | [optional] 
**stragglerSummary** | [**StragglerSummary**](StragglerSummary.md) |  | [optional] 



## Enum: StateEnum


* `UNKNOWN` (value: `"EXECUTION_STATE_UNKNOWN"`)

* `NOT_STARTED` (value: `"EXECUTION_STATE_NOT_STARTED"`)

* `RUNNING` (value: `"EXECUTION_STATE_RUNNING"`)

* `SUCCEEDED` (value: `"EXECUTION_STATE_SUCCEEDED"`)

* `FAILED` (value: `"EXECUTION_STATE_FAILED"`)

* `CANCELLED` (value: `"EXECUTION_STATE_CANCELLED"`)




