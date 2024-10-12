# ResourceManagementClient.DeploymentProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **String** | Gets or sets the deployment mode. | [optional] 
**parameters** | **Object** | Deployment parameters. Use only one of Parameters or ParametersLink. | [optional] 
**parametersLink** | [**ParametersLink**](ParametersLink.md) |  | [optional] 
**template** | **Object** | Gets or sets the template content. Use only one of Template or TemplateLink. | [optional] 
**templateLink** | [**TemplateLink**](TemplateLink.md) |  | [optional] 



## Enum: ModeEnum


* `Incremental` (value: `"Incremental"`)

* `Complete` (value: `"Complete"`)




