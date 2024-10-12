# BlueprintClient.SharedBlueprintProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**{String: ParameterDefinition}**](ParameterDefinition.md) | A dictionary hold parameter name and its metadata. | [optional] 
**resourceGroups** | [**{String: ResourceGroupDefinition}**](ResourceGroupDefinition.md) | A dictionary which maps resource group placeholders to the resource groups which will be created. | [optional] 
**status** | [**BlueprintStatus**](BlueprintStatus.md) |  | [optional] 
**targetScope** | **String** | The scope where this blueprint definition can be assigned. | [optional] 
**description** | **String** | Multi-line explain this resource. | [optional] 
**displayName** | **String** | One-liner string explain this resource. | [optional] 



## Enum: TargetScopeEnum


* `subscription` (value: `"subscription"`)

* `managementGroup` (value: `"managementGroup"`)




