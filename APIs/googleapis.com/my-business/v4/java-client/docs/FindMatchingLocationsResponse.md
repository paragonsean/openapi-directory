

# FindMatchingLocationsResponse

Response message for Locations.FindMatchingLocations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**matchTime** | **String** | When the matching algorithm was last executed for this location. |  [optional] |
|**matchedLocations** | [**List&lt;MatchedLocation&gt;**](MatchedLocation.md) | A collection of locations that are potential matches to the specified location, listed in order from best to least match. If there is an exact match, it will be in the first position. |  [optional] |



