# BungieNetApi.DestinyDefinitionsLoadoutsDestinyLoadoutConstantsDefinition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blackIconImagePath** | **String** | This is a color-inverted version of the whiteIconImagePath. | [optional] 
**displayProperties** | [**DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition**](DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.md) |  | [optional] 
**hash** | **Number** | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. | [optional] 
**index** | **Number** | The index of the entity as it was found in the investment tables. | [optional] 
**loadoutColorHashes** | **[Number]** | A list of the loadout color hashes in index order, for convenience. | [optional] 
**loadoutCountPerCharacter** | **Number** | The maximum number of loadouts available to each character. The loadouts component API response can return fewer loadouts than this, as more loadouts are unlocked by reaching higher Guardian Ranks. | [optional] 
**loadoutIconHashes** | **[Number]** | A list of the loadout icon hashes in index order, for convenience. | [optional] 
**loadoutNameHashes** | **[Number]** | A list of the loadout name hashes in index order, for convenience. | [optional] 
**loadoutPreviewFilterOutSocketCategoryHashes** | **[Number]** | A list of the socket category hashes to be filtered out of loadout item preview displays. | [optional] 
**loadoutPreviewFilterOutSocketTypeHashes** | **[Number]** | A list of the socket type hashes to be filtered out of loadout item preview displays. | [optional] 
**redacted** | **Boolean** | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! | [optional] 
**whiteIconImagePath** | **String** | This is the same icon as the one in the display properties, offered here as well with a more descriptive name. | [optional] 


