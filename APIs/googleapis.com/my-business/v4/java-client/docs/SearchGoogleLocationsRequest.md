

# SearchGoogleLocationsRequest

Request message for GoogleLocations.SearchGoogleLocations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**location** | [**Location**](Location.md) |  |  [optional] |
|**query** | **String** | Text query to search for. The search results from a query string will be less accurate than if providing an exact location, but can provide more inexact matches. |  [optional] |
|**resultCount** | **Integer** | The number of matches to return. The default value is 3, with a maximum of 10. Note that latency may increase if more are requested. There is no pagination. |  [optional] |



