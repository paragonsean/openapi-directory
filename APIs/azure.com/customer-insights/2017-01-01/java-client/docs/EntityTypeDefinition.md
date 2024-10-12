

# EntityTypeDefinition

Describes an entity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiEntitySetName** | **String** | The api entity set name. This becomes the odata entity set name for the entity Type being referred in this object. |  [optional] |
|**entityType** | [**EntityTypeEnum**](#EntityTypeEnum) | Type of entity. |  [optional] |
|**fields** | [**List&lt;PropertyDefinition&gt;**](PropertyDefinition.md) | The properties of the Profile. |  [optional] |
|**instancesCount** | **Integer** | The instance count. |  [optional] |
|**lastChangedUtc** | **OffsetDateTime** | The last changed time for the type definition. |  [optional] [readonly] |
|**provisioningState** | **ProvisioningState** |  |  [optional] |
|**schemaItemTypeLink** | **String** | The schema org link. This helps ACI identify and suggest semantic models. |  [optional] |
|**tenantId** | **String** | The hub name. |  [optional] [readonly] |
|**timestampFieldName** | **String** | The timestamp property name. Represents the time when the interaction or profile update happened. |  [optional] |
|**typeName** | **String** | The name of the entity. |  [optional] |
|**attributes** | **Map&lt;String, List&lt;String&gt;&gt;** | The attributes for the Type. |  [optional] |
|**description** | **Map&lt;String, String&gt;** | Localized descriptions for the property. |  [optional] |
|**displayName** | **Map&lt;String, String&gt;** | Localized display names for the property. |  [optional] |
|**largeImage** | **String** | Large Image associated with the Property or EntityType. |  [optional] |
|**localizedAttributes** | **Map&lt;String, Map&lt;String, String&gt;&gt;** | Any custom localized attributes for the Type. |  [optional] |
|**mediumImage** | **String** | Medium Image associated with the Property or EntityType. |  [optional] |
|**smallImage** | **String** | Small Image associated with the Property or EntityType. |  [optional] |



## Enum: EntityTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| PROFILE | &quot;Profile&quot; |
| INTERACTION | &quot;Interaction&quot; |
| RELATIONSHIP | &quot;Relationship&quot; |



