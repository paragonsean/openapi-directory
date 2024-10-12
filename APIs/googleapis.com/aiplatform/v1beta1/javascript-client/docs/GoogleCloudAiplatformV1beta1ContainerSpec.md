# VertexAiApi.GoogleCloudAiplatformV1beta1ContainerSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **[String]** | The arguments to be passed when starting the container. | [optional] 
**command** | **[String]** | The command to be invoked when the container is started. It overrides the entrypoint instruction in Dockerfile when provided. | [optional] 
**env** | [**[GoogleCloudAiplatformV1beta1EnvVar]**](GoogleCloudAiplatformV1beta1EnvVar.md) | Environment variables to be passed to the container. Maximum limit is 100. | [optional] 
**imageUri** | **String** | Required. The URI of a container image in the Container Registry that is to be run on each worker replica. | [optional] 


