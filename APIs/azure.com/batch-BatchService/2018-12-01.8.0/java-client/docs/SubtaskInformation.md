

# SubtaskInformation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerInfo** | [**TaskContainerExecutionInformation**](TaskContainerExecutionInformation.md) |  |  [optional] |
|**endTime** | **OffsetDateTime** | This property is set only if the subtask is in the Completed state. |  [optional] |
|**exitCode** | **Integer** | This property is set only if the subtask is in the completed state. In general, the exit code for a process reflects the specific convention implemented by the application developer for that process. If you use the exit code value to make decisions in your code, be sure that you know the exit code convention used by the application process. However, if the Batch service terminates the subtask (due to timeout, or user termination via the API) you may see an operating system-defined exit code. |  [optional] |
|**failureInfo** | [**TaskFailureInformation**](TaskFailureInformation.md) |  |  [optional] |
|**id** | **Integer** |  |  [optional] |
|**nodeInfo** | [**ComputeNodeInformation**](ComputeNodeInformation.md) |  |  [optional] |
|**previousState** | **SubtaskState** |  |  [optional] |
|**previousStateTransitionTime** | **OffsetDateTime** | This property is not set if the subtask is in its initial running state. |  [optional] |
|**result** | **TaskExecutionResult** |  |  [optional] |
|**startTime** | **OffsetDateTime** |  |  [optional] |
|**state** | **SubtaskState** |  |  [optional] |
|**stateTransitionTime** | **OffsetDateTime** |  |  [optional] |



