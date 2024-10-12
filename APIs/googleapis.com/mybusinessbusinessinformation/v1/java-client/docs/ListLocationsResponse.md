

# ListLocationsResponse

Response message for Locations.ListLocations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**locations** | [**List&lt;Location&gt;**](Location.md) | The locations. |  [optional] |
|**nextPageToken** | **String** | If the number of locations exceeded the requested page size, this field is populated with a token to fetch the next page of locations on a subsequent call to &#x60;ListLocations&#x60;. If there are no more locations, this field is not present in the response. |  [optional] |
|**totalSize** | **Integer** | The approximate number of Locations in the list irrespective of pagination. This field will only be returned if &#x60;filter&#x60; is used as a query parameter. |  [optional] |



