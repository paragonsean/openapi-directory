

# GoogleCloudAiplatformV1SuggestTrialsMetadata

Details of operations that perform Trials suggestion.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientId** | **String** | The identifier of the client that is requesting the suggestion. If multiple SuggestTrialsRequests have the same &#x60;client_id&#x60;, the service will return the identical suggested Trial if the Trial is pending, and provide a new Trial if the last suggested Trial was completed. |  [optional] |
|**genericMetadata** | [**GoogleCloudAiplatformV1GenericOperationMetadata**](GoogleCloudAiplatformV1GenericOperationMetadata.md) |  |  [optional] |



