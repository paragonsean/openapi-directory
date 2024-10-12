

# PublishedBlueprintProperties

Schema for published blueprint definition properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blueprintName** | **String** | Name of the published blueprint definition. |  [optional] |
|**changeNotes** | **String** | Version-specific change notes. |  [optional] |
|**parameters** | [**Map&lt;String, ParameterDefinition&gt;**](ParameterDefinition.md) | A dictionary hold parameter name and its metadata. |  [optional] |
|**resourceGroups** | [**Map&lt;String, ResourceGroupDefinition&gt;**](ResourceGroupDefinition.md) | A dictionary which maps resource group placeholders to the resource groups which will be created. |  [optional] |
|**status** | [**BlueprintStatus**](BlueprintStatus.md) |  |  [optional] |
|**targetScope** | [**TargetScopeEnum**](#TargetScopeEnum) | The scope where this blueprint definition can be assigned. |  [optional] |
|**description** | **String** | Multi-line explain this resource. |  [optional] |
|**displayName** | **String** | One-liner string explain this resource. |  [optional] |



## Enum: TargetScopeEnum

| Name | Value |
|---- | -----|
| SUBSCRIPTION | &quot;subscription&quot; |
| MANAGEMENT_GROUP | &quot;managementGroup&quot; |



