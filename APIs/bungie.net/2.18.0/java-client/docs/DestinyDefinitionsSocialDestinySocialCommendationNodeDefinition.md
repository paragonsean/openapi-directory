

# DestinyDefinitionsSocialDestinySocialCommendationNodeDefinition


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**childCommendationHashes** | **List&lt;Integer&gt;** | A list of hashes that map to child commendations. |  [optional] |
|**childCommendationNodeHashes** | **List&lt;Integer&gt;** | A list of hashes that map to child commendation nodes. Only the root commendations node is expected to have child nodes. |  [optional] |
|**color** | [**DestinyMiscDestinyColor**](DestinyMiscDestinyColor.md) | The color associated with this group of commendations. |  [optional] |
|**displayProperties** | [**DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition**](DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.md) |  |  [optional] |
|**hash** | **Integer** | The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to. |  [optional] |
|**index** | **Integer** | The index of the entity as it was found in the investment tables. |  [optional] |
|**parentCommendationNodeHash** | **Integer** |  |  [optional] |
|**redacted** | **Boolean** | If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry! |  [optional] |



