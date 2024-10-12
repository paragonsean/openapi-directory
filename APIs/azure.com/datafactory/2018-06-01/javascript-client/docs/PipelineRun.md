# DataFactoryManagementClient.PipelineRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**durationInMs** | **Number** | The duration of a pipeline run. | [optional] [readonly] 
**invokedBy** | [**PipelineRunInvokedBy**](PipelineRunInvokedBy.md) |  | [optional] 
**isLatest** | **Boolean** | Indicates if the recovered pipeline run is the latest in its group. | [optional] [readonly] 
**lastUpdated** | **Date** | The last updated timestamp for the pipeline run event in ISO8601 format. | [optional] [readonly] 
**message** | **String** | The message from a pipeline run. | [optional] [readonly] 
**parameters** | **{String: String}** | The full or partial list of parameter name, value pair used in the pipeline run. | [optional] [readonly] 
**pipelineName** | **String** | The pipeline name. | [optional] [readonly] 
**runDimensions** | **{String: String}** | Run dimensions emitted by Pipeline run. | [optional] [readonly] 
**runEnd** | **Date** | The end time of a pipeline run in ISO8601 format. | [optional] [readonly] 
**runGroupId** | **String** | Identifier that correlates all the recovery runs of a pipeline run. | [optional] [readonly] 
**runId** | **String** | Identifier of a run. | [optional] [readonly] 
**runStart** | **Date** | The start time of a pipeline run in ISO8601 format. | [optional] [readonly] 
**status** | **String** | The status of a pipeline run. | [optional] [readonly] 


