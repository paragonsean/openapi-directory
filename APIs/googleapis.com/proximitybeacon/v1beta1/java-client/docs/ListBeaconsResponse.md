

# ListBeaconsResponse

Response that contains list beacon results and pagination help.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**beacons** | [**List&lt;Beacon&gt;**](Beacon.md) | The beacons that matched the search criteria. |  [optional] |
|**nextPageToken** | **String** | An opaque pagination token that the client may provide in their next request to retrieve the next page of results. |  [optional] |
|**totalCount** | **String** | Estimate of the total number of beacons matched by the query. Higher values may be less accurate. |  [optional] |



