

# Pipeline


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**buildNumber** | **Integer** | The build number of the pipeline. |  [optional] |
|**buildSecondsUsed** | **Integer** | The number of build seconds used by this pipeline. |  [optional] |
|**completedOn** | **OffsetDateTime** | The timestamp when the Pipeline was completed. This is not set if the pipeline is still in progress. |  [optional] |
|**createdOn** | **OffsetDateTime** | The timestamp when the pipeline was created. |  [optional] |
|**creator** | [**Account**](Account.md) |  |  [optional] |
|**repository** | [**Repository**](Repository.md) |  |  [optional] |
|**state** | [**PipelineState**](PipelineState.md) |  |  [optional] |
|**target** | [**PipelineTarget**](PipelineTarget.md) |  |  [optional] |
|**trigger** | [**PipelineTrigger**](PipelineTrigger.md) |  |  [optional] |
|**uuid** | **String** | The UUID identifying the pipeline. |  [optional] |



