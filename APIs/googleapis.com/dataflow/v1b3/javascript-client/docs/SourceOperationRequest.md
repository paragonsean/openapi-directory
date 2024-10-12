# DataflowApi.SourceOperationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**getMetadata** | [**SourceGetMetadataRequest**](SourceGetMetadataRequest.md) |  | [optional] 
**name** | **String** | User-provided name of the Read instruction for this source. | [optional] 
**originalName** | **String** | System-defined name for the Read instruction for this source in the original workflow graph. | [optional] 
**split** | [**SourceSplitRequest**](SourceSplitRequest.md) |  | [optional] 
**stageName** | **String** | System-defined name of the stage containing the source operation. Unique across the workflow. | [optional] 
**systemName** | **String** | System-defined name of the Read instruction for this source. Unique across the workflow. | [optional] 


