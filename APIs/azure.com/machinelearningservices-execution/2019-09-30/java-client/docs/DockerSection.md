

# DockerSection


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arguments** | **List&lt;String&gt;** | Extra arguments to the Docker run command. |  [optional] |
|**baseDockerfile** | **String** | Base Dockerfile used for Docker-based runs. Mutually exclusive with BaseImage. |  [optional] |
|**baseImage** | **String** | Base image used for Docker-based runs. Mutually exclusive with BaseDockerfile. |  [optional] |
|**baseImageRegistry** | [**ContainerRegistry**](ContainerRegistry.md) |  |  [optional] |
|**enabled** | **Boolean** | Set true to perform this run inside a Docker container. |  [optional] |
|**sharedVolumes** | **Boolean** | Set false to disable AzureML&#39;s usage of the Docker shared volumes feature to work around bugs in certain versions of Docker for Windows. |  [optional] |



