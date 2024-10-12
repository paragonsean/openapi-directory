# ContainerRegistryManagementClient.EncodedTaskRunRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentConfiguration** | [**AgentProperties**](AgentProperties.md) |  | [optional] 
**credentials** | [**Credentials**](Credentials.md) |  | [optional] 
**encodedTaskContent** | **String** | Base64 encoded value of the template/definition file content. | 
**encodedValuesContent** | **String** | Base64 encoded value of the parameters/values file content. | [optional] 
**platform** | [**PlatformProperties**](PlatformProperties.md) |  | 
**sourceLocation** | **String** | The URL(absolute or relative) of the source context. It can be an URL to a tar or git repository.  If it is relative URL, the relative path should be obtained from calling listBuildSourceUploadUrl API. | [optional] 
**timeout** | **Number** | Run timeout in seconds. | [optional] [default to 3600]
**values** | [**[SetValue]**](SetValue.md) | The collection of overridable values that can be passed when running a task. | [optional] 


