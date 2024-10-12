# ResourceManagementClient.DeploymentPropertiesExtended

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlationId** | **String** | The correlation ID of the deployment. | [optional] 
**debugSetting** | [**DebugSetting**](DebugSetting.md) |  | [optional] 
**dependencies** | [**[Dependency]**](Dependency.md) | The list of deployment dependencies. | [optional] 
**mode** | **String** | The deployment mode. | [optional] 
**outputs** | **Object** | Key/value pairs that represent deployment output. | [optional] 
**parameters** | **Object** | Deployment parameters. Use only one of Parameters or ParametersLink. | [optional] 
**parametersLink** | [**ParametersLink**](ParametersLink.md) |  | [optional] 
**providers** | [**[Provider]**](Provider.md) | The list of resource providers needed for the deployment. | [optional] 
**provisioningState** | **String** | The state of the provisioning. | [optional] 
**template** | **Object** | The template content. Use only one of Template or TemplateLink. | [optional] 
**templateLink** | [**TemplateLink**](TemplateLink.md) |  | [optional] 
**timestamp** | **Date** | The timestamp of the template deployment. | [optional] 



## Enum: ModeEnum


* `Incremental` (value: `"Incremental"`)

* `Complete` (value: `"Complete"`)




