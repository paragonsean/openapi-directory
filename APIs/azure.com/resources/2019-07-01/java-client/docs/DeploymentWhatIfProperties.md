

# DeploymentWhatIfProperties

Deployment What-if properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**whatIfSettings** | [**DeploymentWhatIfSettings**](DeploymentWhatIfSettings.md) |  |  [optional] |
|**debugSetting** | [**DebugSetting**](DebugSetting.md) |  |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | The mode that is used to deploy resources. This value can be either Incremental or Complete. In Incremental mode, resources are deployed without deleting existing resources that are not included in the template. In Complete mode, resources are deployed and existing resources in the resource group that are not included in the template are deleted. Be careful when using Complete mode as you may unintentionally delete resources. |  |
|**onErrorDeployment** | [**OnErrorDeployment**](OnErrorDeployment.md) |  |  [optional] |
|**parameters** | **Object** | Name and value pairs that define the deployment parameters for the template. You use this element when you want to provide the parameter values directly in the request rather than link to an existing parameter file. Use either the parametersLink property or the parameters property, but not both. It can be a JObject or a well formed JSON string. |  [optional] |
|**parametersLink** | [**ParametersLink**](ParametersLink.md) |  |  [optional] |
|**template** | **Object** | The template content. You use this element when you want to pass the template syntax directly in the request rather than link to an existing template. It can be a JObject or well-formed JSON string. Use either the templateLink property or the template property, but not both. |  [optional] |
|**templateLink** | [**TemplateLink**](TemplateLink.md) |  |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| INCREMENTAL | &quot;Incremental&quot; |
| COMPLETE | &quot;Complete&quot; |



