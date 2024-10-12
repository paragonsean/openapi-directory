

# GoogleCloudAiplatformV1beta1ContainerSpec

The spec of a Container.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**args** | **List&lt;String&gt;** | The arguments to be passed when starting the container. |  [optional] |
|**command** | **List&lt;String&gt;** | The command to be invoked when the container is started. It overrides the entrypoint instruction in Dockerfile when provided. |  [optional] |
|**env** | [**List&lt;GoogleCloudAiplatformV1beta1EnvVar&gt;**](GoogleCloudAiplatformV1beta1EnvVar.md) | Environment variables to be passed to the container. Maximum limit is 100. |  [optional] |
|**imageUri** | **String** | Required. The URI of a container image in the Container Registry that is to be run on each worker replica. |  [optional] |



