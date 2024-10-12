

# DeploymentProperties

Deployment properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mode** | [**ModeEnum**](#ModeEnum) | Gets or sets the deployment mode. |  [optional] |
|**parameters** | **Object** | Deployment parameters. Use only one of Parameters or ParametersLink. |  [optional] |
|**parametersLink** | [**ParametersLink**](ParametersLink.md) |  |  [optional] |
|**template** | **Object** | Gets or sets the template content. Use only one of Template or TemplateLink. |  [optional] |
|**templateLink** | [**TemplateLink**](TemplateLink.md) |  |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| INCREMENTAL | &quot;Incremental&quot; |
| COMPLETE | &quot;Complete&quot; |



