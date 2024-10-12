

# TemplateArtifactProperties

Properties of a Resource Manager template blueprint artifact.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**parameters** | [**Map&lt;String, ParameterValue&gt;**](ParameterValue.md) | A dictionary for parameters and their corresponding values. |  |
|**resourceGroup** | **String** | If applicable, the name of the resource group placeholder to which the Resource Manager template blueprint artifact will be deployed. |  [optional] |
|**template** | **Object** | The Resource Manager template blueprint artifact body. |  |
|**description** | **String** | Multi-line explain this resource. |  [optional] |
|**displayName** | **String** | One-liner string explain this resource. |  [optional] |
|**dependsOn** | **List&lt;String&gt;** | Artifacts which need to be deployed before the specified artifact. |  [optional] |



