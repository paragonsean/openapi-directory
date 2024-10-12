# ContainerRegistryManagementClient.QuickBuildRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buildArguments** | [**[BuildArgument]**](BuildArgument.md) | The collection of build arguments to be used. | [optional] 
**dockerFilePath** | **String** | The Docker file path relative to the source location. | 
**imageNames** | **[String]** | The fully qualified image names including the repository and tag. | [optional] 
**isPushEnabled** | **Boolean** | The value of this property indicates whether the image built should be pushed to the registry or not. | [optional] [default to true]
**noCache** | **Boolean** | The value of this property indicates whether the image cache is enabled or not. | [optional] [default to false]
**platform** | [**PlatformProperties**](PlatformProperties.md) |  | 
**sourceLocation** | **String** | The URL(absolute or relative) of the source that needs to be built. For Docker build, it can be an URL to a tar or github repository as supported by Docker.  If it is relative URL, the relative path should be obtained from calling getSourceUploadUrl API. | 
**timeout** | **Number** | Build timeout in seconds. | [optional] [default to 3600]


