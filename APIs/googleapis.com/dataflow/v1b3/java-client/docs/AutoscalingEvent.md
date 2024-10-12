

# AutoscalingEvent

A structured message reporting an autoscaling decision made by the Dataflow service.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currentNumWorkers** | **String** | The current number of workers the job has. |  [optional] |
|**description** | [**StructuredMessage**](StructuredMessage.md) |  |  [optional] |
|**eventType** | [**EventTypeEnum**](#EventTypeEnum) | The type of autoscaling event to report. |  [optional] |
|**targetNumWorkers** | **String** | The target number of workers the worker pool wants to resize to use. |  [optional] |
|**time** | **String** | The time this event was emitted to indicate a new target or current num_workers value. |  [optional] |
|**workerPool** | **String** | A short and friendly name for the worker pool this event refers to. |  [optional] |



## Enum: EventTypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNKNOWN | &quot;TYPE_UNKNOWN&quot; |
| TARGET_NUM_WORKERS_CHANGED | &quot;TARGET_NUM_WORKERS_CHANGED&quot; |
| CURRENT_NUM_WORKERS_CHANGED | &quot;CURRENT_NUM_WORKERS_CHANGED&quot; |
| ACTUATION_FAILURE | &quot;ACTUATION_FAILURE&quot; |
| NO_CHANGE | &quot;NO_CHANGE&quot; |



