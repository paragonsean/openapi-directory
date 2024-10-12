

# DeploymentPropertiesExtended

Deployment properties with additional details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**correlationId** | **String** | The correlation ID of the deployment. |  [optional] |
|**debugSetting** | [**DebugSetting**](DebugSetting.md) |  |  [optional] |
|**dependencies** | [**List&lt;Dependency&gt;**](Dependency.md) | The list of deployment dependencies. |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | The deployment mode. |  [optional] |
|**outputs** | **Object** | Key/value pairs that represent deployment output. |  [optional] |
|**parameters** | **Object** | Deployment parameters. Use only one of Parameters or ParametersLink. |  [optional] |
|**parametersLink** | [**ParametersLink**](ParametersLink.md) |  |  [optional] |
|**providers** | [**List&lt;Provider&gt;**](Provider.md) | The list of resource providers needed for the deployment. |  [optional] |
|**provisioningState** | **String** | The state of the provisioning. |  [optional] |
|**template** | **Object** | The template content. Use only one of Template or TemplateLink. |  [optional] |
|**templateLink** | [**TemplateLink**](TemplateLink.md) |  |  [optional] |
|**timestamp** | **OffsetDateTime** | The timestamp of the template deployment. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| INCREMENTAL | &quot;Incremental&quot; |
| COMPLETE | &quot;Complete&quot; |



