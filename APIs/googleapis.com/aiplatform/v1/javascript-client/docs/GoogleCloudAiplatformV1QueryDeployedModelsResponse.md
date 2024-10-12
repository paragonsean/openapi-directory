# VertexAiApi.GoogleCloudAiplatformV1QueryDeployedModelsResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployedModelRefs** | [**[GoogleCloudAiplatformV1DeployedModelRef]**](GoogleCloudAiplatformV1DeployedModelRef.md) | References to the DeployedModels that share the specified deploymentResourcePool. | [optional] 
**deployedModels** | [**[GoogleCloudAiplatformV1DeployedModel]**](GoogleCloudAiplatformV1DeployedModel.md) | DEPRECATED Use deployed_model_refs instead. | [optional] 
**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. | [optional] 
**totalDeployedModelCount** | **Number** | The total number of DeployedModels on this DeploymentResourcePool. | [optional] 
**totalEndpointCount** | **Number** | The total number of Endpoints that have DeployedModels on this DeploymentResourcePool. | [optional] 


