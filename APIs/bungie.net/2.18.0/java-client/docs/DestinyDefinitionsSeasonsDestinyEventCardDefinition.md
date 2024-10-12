

# DestinyDefinitionsSeasonsDestinyEventCardDefinition

Defines the properties of an 'Event Card' in Destiny 2, to coincide with a seasonal event for additional challenges, premium rewards, a new seal, and a special title. For example: Solstice of Heroes 2022.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**color** | [**DestinyMiscDestinyColor**](DestinyMiscDestinyColor.md) |  |  [optional] |
|**displayProperties** | [**DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition**](DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.md) |  |  [optional] |
|**endTime** | **Long** |  |  [optional] |
|**hash** | **Integer** | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. |  [optional] |
|**images** | [**DestinyDefinitionsSeasonsDestinyEventCardImages**](DestinyDefinitionsSeasonsDestinyEventCardImages.md) |  |  [optional] |
|**index** | **Integer** | The index of the entity as it was found in the investment tables. |  [optional] |
|**linkRedirectPath** | **String** |  |  [optional] |
|**redacted** | **Boolean** | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! |  [optional] |
|**sealPresentationNodeHash** | **Integer** |  |  [optional] |
|**ticketCurrencyItemHash** | **Integer** |  |  [optional] |
|**ticketVendorCategoryHash** | **Integer** |  |  [optional] |
|**ticketVendorHash** | **Integer** |  |  [optional] |
|**triumphsPresentationNodeHash** | **Integer** |  |  [optional] |



