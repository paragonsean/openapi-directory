# BlueprintClient.ResourceGroupDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependsOn** | **[String]** | Artifacts which need to be deployed before this resource group. | [optional] 
**location** | **String** | Location of this resourceGroup. Leave empty if the resource group location will be specified during the blueprint assignment. | [optional] 
**metadata** | [**ParameterDefinitionMetadata**](ParameterDefinitionMetadata.md) |  | [optional] 
**name** | **String** | Name of this resourceGroup. Leave empty if the resource group name will be specified during the blueprint assignment. | [optional] 
**tags** | **{String: String}** | A dictionary of resource group tag values. | [optional] 


