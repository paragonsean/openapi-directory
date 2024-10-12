# DataflowApi.StreamingConfigTask

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commitStreamChunkSizeBytes** | **String** | Chunk size for commit streams from the harness to windmill. | [optional] 
**getDataStreamChunkSizeBytes** | **String** | Chunk size for get data streams from the harness to windmill. | [optional] 
**maxWorkItemCommitBytes** | **String** | Maximum size for work item commit supported windmill storage layer. | [optional] 
**streamingComputationConfigs** | [**[StreamingComputationConfig]**](StreamingComputationConfig.md) | Set of computation configuration information. | [optional] 
**userStepToStateFamilyNameMap** | **{String: String}** | Map from user step names to state families. | [optional] 
**windmillServiceEndpoint** | **String** | If present, the worker must use this endpoint to communicate with Windmill Service dispatchers, otherwise the worker must continue to use whatever endpoint it had been using. | [optional] 
**windmillServicePort** | **String** | If present, the worker must use this port to communicate with Windmill Service dispatchers. Only applicable when windmill_service_endpoint is specified. | [optional] 


