

# FileTaskRunRequest

The request parameters for a scheduling run against a task file.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentConfiguration** | [**AgentProperties**](AgentProperties.md) |  |  [optional] |
|**credentials** | [**Credentials**](Credentials.md) |  |  [optional] |
|**platform** | [**PlatformProperties**](PlatformProperties.md) |  |  |
|**sourceLocation** | **String** | The URL(absolute or relative) of the source context. It can be an URL to a tar or git repository.  If it is relative URL, the relative path should be obtained from calling listBuildSourceUploadUrl API. |  [optional] |
|**taskFilePath** | **String** | The template/definition file path relative to the source. |  |
|**timeout** | **Integer** | Run timeout in seconds. |  [optional] |
|**values** | [**List&lt;SetValue&gt;**](SetValue.md) | The collection of overridable values that can be passed when running a task. |  [optional] |
|**valuesFilePath** | **String** | The values/parameters file path relative to the source. |  [optional] |



