# BungieNetApi.DestinyDefinitionsChecklistsDestinyChecklistDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayProperties** | [**DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition**](DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.md) |  | [optional] 
**entries** | [**[DestinyDefinitionsChecklistsDestinyChecklistEntryDefinition]**](DestinyDefinitionsChecklistsDestinyChecklistEntryDefinition.md) | The individual checklist items. Gotta catch &#39;em all. | [optional] 
**hash** | **Number** | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. | [optional] 
**index** | **Number** | The index of the entity as it was found in the investment tables. | [optional] 
**redacted** | **Boolean** | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | [optional] 
**scope** | **Number** | Indicates whether you will find this checklist on the Profile or Character components. | [optional] 
**viewActionString** | **String** | A localized string prompting you to view the checklist. | [optional] 


