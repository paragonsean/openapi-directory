

# DockerBuildRequest

The parameters for a docker quick build.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentConfiguration** | [**AgentProperties**](AgentProperties.md) |  |  [optional] |
|**arguments** | [**List&lt;Argument&gt;**](Argument.md) | The collection of override arguments to be used when executing the run. |  [optional] |
|**credentials** | [**Credentials**](Credentials.md) |  |  [optional] |
|**dockerFilePath** | **String** | The Docker file path relative to the source location. |  |
|**imageNames** | **List&lt;String&gt;** | The fully qualified image names including the repository and tag. |  [optional] |
|**isPushEnabled** | **Boolean** | The value of this property indicates whether the image built should be pushed to the registry or not. |  [optional] |
|**noCache** | **Boolean** | The value of this property indicates whether the image cache is enabled or not. |  [optional] |
|**platform** | [**PlatformProperties**](PlatformProperties.md) |  |  |
|**sourceLocation** | **String** | The URL(absolute or relative) of the source context. It can be an URL to a tar or git repository.  If it is relative URL, the relative path should be obtained from calling listBuildSourceUploadUrl API. |  [optional] |
|**target** | **String** | The name of the target build stage for the docker build. |  [optional] |
|**timeout** | **Integer** | Run timeout in seconds. |  [optional] |



