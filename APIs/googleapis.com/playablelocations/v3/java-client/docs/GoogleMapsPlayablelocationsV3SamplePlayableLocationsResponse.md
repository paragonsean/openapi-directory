

# GoogleMapsPlayablelocationsV3SamplePlayableLocationsResponse

 Response for the SamplePlayableLocations method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**locationsPerGameObjectType** | [**Map&lt;String, GoogleMapsPlayablelocationsV3SamplePlayableLocationList&gt;**](GoogleMapsPlayablelocationsV3SamplePlayableLocationList.md) | Each PlayableLocation object corresponds to a game_object_type specified in the request. |  [optional] |
|**ttl** | **String** | Required. Specifies the \&quot;time-to-live\&quot; for the set of playable locations. You can use this value to determine how long to cache the set of playable locations. After this length of time, your back-end game server should issue a new SamplePlayableLocations request to get a fresh set of playable locations (because for example, they might have been removed, a park might have closed for the day, a business might have closed permanently). |  [optional] |



