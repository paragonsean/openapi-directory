# CustomerInsightsManagementClient.ProfileTypeDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strongIds** | [**[StrongId]**](StrongId.md) | The strong IDs. | [optional] 
**apiEntitySetName** | **String** | The api entity set name. This becomes the odata entity set name for the entity Type being referred in this object. | [optional] 
**entityType** | **String** | Type of entity. | [optional] 
**fields** | [**[PropertyDefinition]**](PropertyDefinition.md) | The properties of the Profile. | [optional] 
**instancesCount** | **Number** | The instance count. | [optional] 
**lastChangedUtc** | **Date** | The last changed time for the type definition. | [optional] [readonly] 
**provisioningState** | [**ProvisioningState**](ProvisioningState.md) |  | [optional] 
**schemaItemTypeLink** | **String** | The schema org link. This helps ACI identify and suggest semantic models. | [optional] 
**tenantId** | **String** | The hub name. | [optional] [readonly] 
**timestampFieldName** | **String** | The timestamp property name. Represents the time when the interaction or profile update happened. | [optional] 
**typeName** | **String** | The name of the entity. | [optional] 
**attributes** | **{String: [String]}** | The attributes for the Type. | [optional] 
**description** | **{String: String}** | Localized descriptions for the property. | [optional] 
**displayName** | **{String: String}** | Localized display names for the property. | [optional] 
**largeImage** | **String** | Large Image associated with the Property or EntityType. | [optional] 
**localizedAttributes** | **{String: {String: String}}** | Any custom localized attributes for the Type. | [optional] 
**mediumImage** | **String** | Medium Image associated with the Property or EntityType. | [optional] 
**smallImage** | **String** | Small Image associated with the Property or EntityType. | [optional] 



## Enum: EntityTypeEnum


* `None` (value: `"None"`)

* `Profile` (value: `"Profile"`)

* `Interaction` (value: `"Interaction"`)

* `Relationship` (value: `"Relationship"`)




