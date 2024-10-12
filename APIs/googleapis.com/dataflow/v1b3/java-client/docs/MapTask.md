

# MapTask

MapTask consists of an ordered set of instructions, each of which describes one particular low-level operation for the worker to perform in order to accomplish the MapTask's WorkItem. Each instruction must appear in the list before any instructions which depends on its output.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**counterPrefix** | **String** | Counter prefix that can be used to prefix counters. Not currently used in Dataflow. |  [optional] |
|**instructions** | [**List&lt;ParallelInstruction&gt;**](ParallelInstruction.md) | The instructions in the MapTask. |  [optional] |
|**stageName** | **String** | System-defined name of the stage containing this MapTask. Unique across the workflow. |  [optional] |
|**systemName** | **String** | System-defined name of this MapTask. Unique across the workflow. |  [optional] |



