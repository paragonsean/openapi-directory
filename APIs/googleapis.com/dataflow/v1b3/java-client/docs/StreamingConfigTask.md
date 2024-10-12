

# StreamingConfigTask

A task that carries configuration information for streaming computations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commitStreamChunkSizeBytes** | **String** | Chunk size for commit streams from the harness to windmill. |  [optional] |
|**getDataStreamChunkSizeBytes** | **String** | Chunk size for get data streams from the harness to windmill. |  [optional] |
|**maxWorkItemCommitBytes** | **String** | Maximum size for work item commit supported windmill storage layer. |  [optional] |
|**streamingComputationConfigs** | [**List&lt;StreamingComputationConfig&gt;**](StreamingComputationConfig.md) | Set of computation configuration information. |  [optional] |
|**userStepToStateFamilyNameMap** | **Map&lt;String, String&gt;** | Map from user step names to state families. |  [optional] |
|**windmillServiceEndpoint** | **String** | If present, the worker must use this endpoint to communicate with Windmill Service dispatchers, otherwise the worker must continue to use whatever endpoint it had been using. |  [optional] |
|**windmillServicePort** | **String** | If present, the worker must use this port to communicate with Windmill Service dispatchers. Only applicable when windmill_service_endpoint is specified. |  [optional] |



