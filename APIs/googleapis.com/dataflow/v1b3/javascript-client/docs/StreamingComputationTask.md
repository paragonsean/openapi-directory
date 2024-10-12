# DataflowApi.StreamingComputationTask

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computationRanges** | [**[StreamingComputationRanges]**](StreamingComputationRanges.md) | Contains ranges of a streaming computation this task should apply to. | [optional] 
**dataDisks** | [**[MountedDataDisk]**](MountedDataDisk.md) | Describes the set of data disks this task should apply to. | [optional] 
**taskType** | **String** | A type of streaming computation task. | [optional] 



## Enum: TaskTypeEnum


* `UNKNOWN` (value: `"STREAMING_COMPUTATION_TASK_UNKNOWN"`)

* `STOP` (value: `"STREAMING_COMPUTATION_TASK_STOP"`)

* `START` (value: `"STREAMING_COMPUTATION_TASK_START"`)




