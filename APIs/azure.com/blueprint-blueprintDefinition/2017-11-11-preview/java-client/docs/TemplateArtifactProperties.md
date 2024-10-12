

# TemplateArtifactProperties

Properties of a Template Artifact.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**parameters** | [**Map&lt;String, ParameterValueBase&gt;**](ParameterValueBase.md) | A dictionary for parameters and their corresponding values. |  |
|**resourceGroup** | **String** | If applicable, the name of the resource group placeholder to which the template will be deployed. |  [optional] |
|**template** | **Object** | The Azure Resource Manager template body. |  |
|**description** | **String** | Multi-line explain this resource. |  [optional] |
|**displayName** | **String** | One-liner string explain this resource. |  [optional] |
|**dependsOn** | **List&lt;String&gt;** | Artifacts which need to be deployed before the specified artifact. |  [optional] |



