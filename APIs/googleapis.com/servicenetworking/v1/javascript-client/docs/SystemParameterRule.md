# ServiceNetworkingApi.SystemParameterRule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**[SystemParameter]**](SystemParameter.md) | Define parameters. Multiple names may be defined for a parameter. For a given method call, only one of them should be used. If multiple names are used the behavior is implementation-dependent. If none of the specified names are present the behavior is parameter-dependent. | [optional] 
**selector** | **String** | Selects the methods to which this rule applies. Use &#39;*&#39; to indicate all methods in all APIs. Refer to selector for syntax details. | [optional] 


