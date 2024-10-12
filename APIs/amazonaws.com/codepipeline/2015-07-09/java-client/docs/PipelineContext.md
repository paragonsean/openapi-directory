

# PipelineContext

<p>Represents information about a pipeline to a job worker.</p> <note> <p>PipelineContext contains <code>pipelineArn</code> and <code>pipelineExecutionId</code> for custom action jobs. The <code>pipelineArn</code> and <code>pipelineExecutionId</code> fields are not populated for ThirdParty action jobs.</p> </note>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pipelineName** | [**String**](String.md) |  |  [optional] |
|**stage** | [**PipelineContextStage**](PipelineContextStage.md) |  |  [optional] |
|**action** | [**PipelineContextAction**](PipelineContextAction.md) |  |  [optional] |
|**pipelineArn** | [**String**](String.md) |  |  [optional] |
|**pipelineExecutionId** | [**String**](String.md) |  |  [optional] |



