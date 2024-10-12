

# DestinyDefinitionsSeasonsDestinySeasonDefinition

Defines a canonical \"Season\" of Destiny: a range of a few months where the game highlights certain challenges, provides new loot, has new Clan-related rewards and celebrates various seasonal events.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**artifactItemHash** | **Integer** |  |  [optional] |
|**backgroundImagePath** | **String** |  |  [optional] |
|**displayProperties** | [**DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition**](DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.md) |  |  [optional] |
|**endDate** | **OffsetDateTime** |  |  [optional] |
|**hash** | **Integer** | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. |  [optional] |
|**index** | **Integer** | The index of the entity as it was found in the investment tables. |  [optional] |
|**preview** | [**DestinyDefinitionsSeasonsDestinySeasonPreviewDefinition**](DestinyDefinitionsSeasonsDestinySeasonPreviewDefinition.md) | Optional - Defines the promotional text, images, and links to preview this season. |  [optional] |
|**redacted** | **Boolean** | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! |  [optional] |
|**sealPresentationNodeHash** | **Integer** |  |  [optional] |
|**seasonNumber** | **Integer** |  |  [optional] |
|**seasonPassHash** | **Integer** |  |  [optional] |
|**seasonPassProgressionHash** | **Integer** |  |  [optional] |
|**seasonalChallengesPresentationNodeHash** | **Integer** |  |  [optional] |
|**startDate** | **OffsetDateTime** |  |  [optional] |



