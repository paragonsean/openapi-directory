# AzureMachineLearningModelManagementService.ModelDockerSection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_arguments** | **[String]** | Extra arguments to the Docker run command. | [optional] 
**baseDockerfile** | **String** | Base Dockerfile used for Docker-based runs. Mutually exclusive with BaseImage. | [optional] 
**baseImage** | **String** | Base image used for Docker-based runs. Mutually exclusive with BaseDockerfile. | [optional] 
**baseImageRegistry** | [**ContainerRegistry**](ContainerRegistry.md) |  | [optional] 
**enabled** | **Boolean** | Set True to perform this run inside a Docker container. | [optional] 
**gpuSupport** | **Boolean** | Run with NVidia Docker extension to support GPUs. | [optional] 
**sharedVolumes** | **Boolean** | Set False if necessary to work around shared volume bugs on Windows. | [optional] 
**shmSize** | **String** | The shared memory size setting for NVidia GPUs. | [optional] 


