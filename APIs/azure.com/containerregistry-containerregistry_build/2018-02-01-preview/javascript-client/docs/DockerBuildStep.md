# ContainerRegistryManagementClient.DockerBuildStep

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**baseImageDependencies** | [**[BaseImageDependency]**](BaseImageDependency.md) | List of base image dependencies for a step. | [optional] [readonly] 
**baseImageTrigger** | **String** | The type of the auto trigger for base image dependency updates. | [optional] 
**branch** | **String** | The repository branch name. | [optional] 
**buildArguments** | [**[BuildArgument]**](BuildArgument.md) | The custom arguments for building this build step. | [optional] 
**contextPath** | **String** | The relative context path for a docker build in the source. | [optional] 
**dockerFilePath** | **String** | The Docker file path relative to the source control root. | [optional] 
**imageNames** | **[String]** | The fully qualified image names including the repository and tag. | [optional] 
**isPushEnabled** | **Boolean** | The value of this property indicates whether the image built should be pushed to the registry or not. | [optional] [default to true]
**noCache** | **Boolean** | The value of this property indicates whether the image cache is enabled or not. | [optional] [default to false]



## Enum: BaseImageTriggerEnum


* `All` (value: `"All"`)

* `Runtime` (value: `"Runtime"`)

* `None` (value: `"None"`)




