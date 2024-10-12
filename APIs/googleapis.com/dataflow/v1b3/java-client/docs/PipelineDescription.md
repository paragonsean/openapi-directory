

# PipelineDescription

A descriptive representation of submitted pipeline as well as the executed form. This data is provided by the Dataflow service for ease of visualizing the pipeline and interpreting Dataflow provided metrics.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayData** | [**List&lt;DisplayData&gt;**](DisplayData.md) | Pipeline level display data. |  [optional] |
|**executionPipelineStage** | [**List&lt;ExecutionStageSummary&gt;**](ExecutionStageSummary.md) | Description of each stage of execution of the pipeline. |  [optional] |
|**originalPipelineTransform** | [**List&lt;TransformSummary&gt;**](TransformSummary.md) | Description of each transform in the pipeline and collections between them. |  [optional] |
|**stepNamesHash** | **String** | A hash value of the submitted pipeline portable graph step names if exists. |  [optional] |



