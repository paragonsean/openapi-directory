

# DestinyDefinitionsDestinyLocationReleaseDefinition

A specific \"spot\" referred to by a location. Only one of these can be active at a time for a given Location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activityBubbleName** | **Integer** | The Activity Bubble within the Destination. Look this up in the DestinyDestinationDefinition&#39;s bubbles and bubbleSettings properties. |  [optional] |
|**activityGraphHash** | **Integer** | The Activity Graph being pointed to by this location. |  [optional] |
|**activityGraphNodeHash** | **Integer** | The Activity Graph Node being pointed to by this location. (Remember that Activity Graph Node hashes are only unique within an Activity Graph: so use the combination to find the node being spoken of) |  [optional] |
|**activityHash** | **Integer** | The Activity being pointed to by this location. |  [optional] |
|**activityPathBundle** | **Integer** | If we had map information, this would tell us something cool about the path this location wants you to take. I wish we had map information. |  [optional] |
|**activityPathDestination** | **Integer** | If we had map information, this would tell us about path information related to destination on the map. Sad. Maybe you can do something cool with it. Go to town man. |  [optional] |
|**destinationHash** | **Integer** | The Destination being pointed to by this location. |  [optional] |
|**displayProperties** | [**DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition**](DestinyDefinitionsCommonDestinyDisplayPropertiesDefinition.md) | Sadly, these don&#39;t appear to be populated anymore (ever?) |  [optional] |
|**largeTransparentIcon** | **String** |  |  [optional] |
|**mapIcon** | **String** |  |  [optional] |
|**navPointType** | **Integer** | The type of Nav Point that this represents. See the enumeration for more info. |  [optional] |
|**smallTransparentIcon** | **String** |  |  [optional] |
|**spawnPoint** | **Integer** | If we had map information, this spawnPoint would be interesting. But sadly, we don&#39;t have that info. |  [optional] |
|**worldPosition** | **List&lt;Integer&gt;** | Looks like it should be the position on the map, but sadly it does not look populated... yet? |  [optional] |



