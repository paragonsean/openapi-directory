# ResourceManagementClient.DeploymentPropertiesExtended

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlationId** | **String** | Gets or sets the correlation ID of the deployment. | [optional] 
**dependencies** | [**[Dependency]**](Dependency.md) | Gets the list of deployment dependencies. | [optional] 
**mode** | **String** | Gets or sets the deployment mode. | [optional] 
**outputs** | **Object** | Gets or sets key/value pairs that represent deployment output. | [optional] 
**parameters** | **Object** | Deployment parameters. Use only one of Parameters or ParametersLink. | [optional] 
**parametersLink** | [**ParametersLink**](ParametersLink.md) |  | [optional] 
**providers** | [**[Provider]**](Provider.md) | Gets the list of resource providers needed for the deployment. | [optional] 
**provisioningState** | **String** | Gets or sets the state of the provisioning. | [optional] 
**template** | **Object** | Gets or sets the template content. Use only one of Template or TemplateLink. | [optional] 
**templateLink** | [**TemplateLink**](TemplateLink.md) |  | [optional] 
**timestamp** | **Date** | Gets or sets the timestamp of the template deployment. | [optional] 



## Enum: ModeEnum


* `Incremental` (value: `"Incremental"`)

* `Complete` (value: `"Complete"`)




