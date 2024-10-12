

# PipelineStep


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**completedOn** | **OffsetDateTime** | The timestamp when the step execution was completed. This is not set if the step is still in progress. |  [optional] |
|**image** | [**PipelineImage**](PipelineImage.md) |  |  [optional] |
|**scriptCommands** | [**List&lt;PipelineCommand&gt;**](PipelineCommand.md) | The list of build commands. These commands are executed in the build container. |  [optional] |
|**setupCommands** | [**List&lt;PipelineCommand&gt;**](PipelineCommand.md) | The list of commands that are executed as part of the setup phase of the build. These commands are executed outside the build container. |  [optional] |
|**startedOn** | **OffsetDateTime** | The timestamp when the step execution was started. This is not set when the step hasn&#39;t executed yet. |  [optional] |
|**state** | [**PipelineStepState**](PipelineStepState.md) |  |  [optional] |
|**uuid** | **String** | The UUID identifying the step. |  [optional] |



