# BungieNetApi.DestinyDefinitionsDestinyEquipmentSlotDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applyCustomArtDyes** | **Boolean** | If True, equipped items should have their custom art dyes applied when rendering the item. Otherwise, custom art dyes on an item should be ignored if the item is equipped in this slot. | [optional] 
**artDyeChannels** | [**[DestinyDefinitionsDestinyArtDyeReference]**](DestinyDefinitionsDestinyArtDyeReference.md) | The Art Dye Channels that apply to this equipment slot. | [optional] 
**bucketTypeHash** | **Number** | The inventory bucket that owns this equipment slot. | [optional] 
**displayProperties** | [**DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition**](DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.md) |  | [optional] 
**equipmentCategoryHash** | **Number** | These technically point to \&quot;Equipment Category Definitions\&quot;. But don&#39;t get excited. There&#39;s nothing of significant value in those definitions, so I didn&#39;t bother to expose them. You can use the hash here to group equipment slots by common functionality, which serves the same purpose as if we had the Equipment Category definitions exposed. | [optional] 
**hash** | **Number** | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. | [optional] 
**index** | **Number** | The index of the entity as it was found in the investment tables. | [optional] 
**redacted** | **Boolean** | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | [optional] 


