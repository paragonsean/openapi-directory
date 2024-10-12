

# ResourceGroupDefinition

Represents an Azure resource group in a Blueprint definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dependsOn** | **List&lt;String&gt;** | Artifacts which need to be deployed before this resource group. |  [optional] |
|**location** | **String** | Location of this resourceGroup, leave empty if the resource group location will be specified during the Blueprint assignment. |  [optional] |
|**metadata** | [**ParameterDefinitionMetadata**](ParameterDefinitionMetadata.md) |  |  [optional] |
|**name** | **String** | Name of this resourceGroup, leave empty if the resource group name will be specified during the Blueprint assignment. |  [optional] |



