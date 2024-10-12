

# ListLocationsResponse

ListLocationsResponse returns the list of all GKE locations and their recommendation state.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**locations** | [**List&lt;Location&gt;**](Location.md) | A full list of GKE locations. |  [optional] |
|**nextPageToken** | **String** | Only return ListLocationsResponse that occur after the page_token. This value should be populated from the ListLocationsResponse.next_page_token if that response token was set (which happens when listing more Locations than fit in a single ListLocationsResponse). |  [optional] |



