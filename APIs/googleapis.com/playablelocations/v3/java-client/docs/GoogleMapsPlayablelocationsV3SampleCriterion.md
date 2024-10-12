

# GoogleMapsPlayablelocationsV3SampleCriterion

Encapsulates a filter criterion for searching for a set of playable locations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fieldsToReturn** | **String** | Specifies which &#x60;PlayableLocation&#x60; fields are returned. &#x60;name&#x60; (which is used for logging impressions), &#x60;center_point&#x60; and &#x60;place_id&#x60; (or &#x60;plus_code&#x60;) are always returned. The following fields are omitted unless you specify them here: * snapped_point * types Note: The more fields you include, the more expensive in terms of data and associated latency your query will be. |  [optional] |
|**filter** | [**GoogleMapsPlayablelocationsV3SampleFilter**](GoogleMapsPlayablelocationsV3SampleFilter.md) |  |  [optional] |
|**gameObjectType** | **Integer** | Required. An arbitrary, developer-defined identifier of the type of game object that the playable location is used for. This field allows you to specify criteria per game object type when searching for playable locations. You should assign a unique &#x60;game_object_type&#x60; ID across all &#x60;request_criteria&#x60; to represent a distinct type of game object. For example, 1&#x3D;monster location, 2&#x3D;powerup location. The response contains a map. |  [optional] |



