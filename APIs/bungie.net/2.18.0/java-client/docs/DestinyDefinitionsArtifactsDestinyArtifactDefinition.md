

# DestinyDefinitionsArtifactsDestinyArtifactDefinition

Represents known info about a Destiny Artifact.  We cannot guarantee that artifact definitions will be immutable between seasons - in fact, we've been told that they will be replaced between seasons. But this definition is built both to minimize the amount of lookups for related data that have to occur, and is built in hope that, if this plan changes, we will be able to accommodate it more easily.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayProperties** | [**DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition**](DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.md) | Any basic display info we know about the Artifact. Currently sourced from a related inventory item, but the source of this data is subject to change. |  [optional] |
|**hash** | **Integer** | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. |  [optional] |
|**index** | **Integer** | The index of the entity as it was found in the investment tables. |  [optional] |
|**redacted** | **Boolean** | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! |  [optional] |
|**tiers** | [**List&lt;DestinyDefinitionsArtifactsDestinyArtifactTierDefinition&gt;**](DestinyDefinitionsArtifactsDestinyArtifactTierDefinition.md) | Any Tier/Rank data related to this artifact, listed in display order.  Currently sourced from a Vendor, but this source is subject to change. |  [optional] |
|**translationBlock** | [**DestinyDefinitionsDestinyItemTranslationBlockDefinition**](DestinyDefinitionsDestinyItemTranslationBlockDefinition.md) | Any Geometry/3D info we know about the Artifact. Currently sourced from a related inventory item&#39;s gearset information, but the source of this data is subject to change. |  [optional] |



