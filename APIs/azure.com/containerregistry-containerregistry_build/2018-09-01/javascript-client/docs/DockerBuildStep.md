# ContainerRegistryManagementClient.DockerBuildStep

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_arguments** | [**[Argument]**](Argument.md) | The collection of override arguments to be used when executing this build step. | [optional] 
**dockerFilePath** | **String** | The Docker file path relative to the source context. | 
**imageNames** | **[String]** | The fully qualified image names including the repository and tag. | [optional] 
**isPushEnabled** | **Boolean** | The value of this property indicates whether the image built should be pushed to the registry or not. | [optional] [default to true]
**noCache** | **Boolean** | The value of this property indicates whether the image cache is enabled or not. | [optional] [default to false]
**target** | **String** | The name of the target build stage for the docker build. | [optional] 


