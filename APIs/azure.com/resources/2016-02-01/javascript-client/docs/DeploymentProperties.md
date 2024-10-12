# ResourceManagementClient.DeploymentProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debugSetting** | [**DebugSetting**](DebugSetting.md) |  | [optional] 
**mode** | **String** | The deployment mode. | 
**parameters** | **Object** | Deployment parameters. It can be a JObject or a well formed JSON string. Use only one of Parameters or ParametersLink. | [optional] 
**parametersLink** | [**ParametersLink**](ParametersLink.md) |  | [optional] 
**template** | **Object** | The template content. It can be a JObject or a well formed JSON string. Use only one of Template or TemplateLink. | [optional] 
**templateLink** | [**TemplateLink**](TemplateLink.md) |  | [optional] 



## Enum: ModeEnum


* `Incremental` (value: `"Incremental"`)

* `Complete` (value: `"Complete"`)




