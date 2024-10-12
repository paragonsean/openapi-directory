

# ResourceGroupDefinition

Represents an Azure resource group in a blueprint definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dependsOn** | **List&lt;String&gt;** | Artifacts which need to be deployed before this resource group. |  [optional] |
|**location** | **String** | Location of this resourceGroup. Leave empty if the resource group location will be specified during the blueprint assignment. |  [optional] |
|**metadata** | [**ParameterDefinitionMetadata**](ParameterDefinitionMetadata.md) |  |  [optional] |
|**name** | **String** | Name of this resourceGroup. Leave empty if the resource group name will be specified during the blueprint assignment. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | A dictionary of resource group tag values. |  [optional] |



