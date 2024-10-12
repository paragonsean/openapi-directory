# DataflowApi.AutoscalingEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currentNumWorkers** | **String** | The current number of workers the job has. | [optional] 
**description** | [**StructuredMessage**](StructuredMessage.md) |  | [optional] 
**eventType** | **String** | The type of autoscaling event to report. | [optional] 
**targetNumWorkers** | **String** | The target number of workers the worker pool wants to resize to use. | [optional] 
**time** | **String** | The time this event was emitted to indicate a new target or current num_workers value. | [optional] 
**workerPool** | **String** | A short and friendly name for the worker pool this event refers to. | [optional] 



## Enum: EventTypeEnum


* `TYPE_UNKNOWN` (value: `"TYPE_UNKNOWN"`)

* `TARGET_NUM_WORKERS_CHANGED` (value: `"TARGET_NUM_WORKERS_CHANGED"`)

* `CURRENT_NUM_WORKERS_CHANGED` (value: `"CURRENT_NUM_WORKERS_CHANGED"`)

* `ACTUATION_FAILURE` (value: `"ACTUATION_FAILURE"`)

* `NO_CHANGE` (value: `"NO_CHANGE"`)




