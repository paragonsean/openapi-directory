

# GoogleCloudAiplatformV1QueryDeployedModelsResponse

Response message for QueryDeployedModels method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deployedModelRefs** | [**List&lt;GoogleCloudAiplatformV1DeployedModelRef&gt;**](GoogleCloudAiplatformV1DeployedModelRef.md) | References to the DeployedModels that share the specified deploymentResourcePool. |  [optional] |
|**deployedModels** | [**List&lt;GoogleCloudAiplatformV1DeployedModel&gt;**](GoogleCloudAiplatformV1DeployedModel.md) | DEPRECATED Use deployed_model_refs instead. |  [optional] |
|**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**totalDeployedModelCount** | **Integer** | The total number of DeployedModels on this DeploymentResourcePool. |  [optional] |
|**totalEndpointCount** | **Integer** | The total number of Endpoints that have DeployedModels on this DeploymentResourcePool. |  [optional] |



