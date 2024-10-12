

# StreamingComputationTask

A task which describes what action should be performed for the specified streaming computation ranges.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**computationRanges** | [**List&lt;StreamingComputationRanges&gt;**](StreamingComputationRanges.md) | Contains ranges of a streaming computation this task should apply to. |  [optional] |
|**dataDisks** | [**List&lt;MountedDataDisk&gt;**](MountedDataDisk.md) | Describes the set of data disks this task should apply to. |  [optional] |
|**taskType** | [**TaskTypeEnum**](#TaskTypeEnum) | A type of streaming computation task. |  [optional] |



## Enum: TaskTypeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;STREAMING_COMPUTATION_TASK_UNKNOWN&quot; |
| STOP | &quot;STREAMING_COMPUTATION_TASK_STOP&quot; |
| START | &quot;STREAMING_COMPUTATION_TASK_START&quot; |



