

# DestinyDefinitionsItemsDestinyItemTierTypeDefinition

Defines the tier type of an item. Mostly this provides human readable properties for types like Common, Rare, etc...  It also provides some base data for infusion that could be useful.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayProperties** | [**DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition**](DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.md) |  |  [optional] |
|**hash** | **Integer** | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. |  [optional] |
|**index** | **Integer** | The index of the entity as it was found in the investment tables. |  [optional] |
|**infusionProcess** | [**DestinyDefinitionsItemsDestinyItemTierTypeInfusionBlock**](DestinyDefinitionsItemsDestinyItemTierTypeInfusionBlock.md) | If this tier defines infusion properties, they will be contained here. |  [optional] |
|**redacted** | **Boolean** | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! |  [optional] |



