

# ListConnectivityTestsResponse

Response for the `ListConnectivityTests` method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | Page token to fetch the next set of Connectivity Tests. |  [optional] |
|**resources** | [**List&lt;ConnectivityTest&gt;**](ConnectivityTest.md) | List of Connectivity Tests. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached (when querying all locations with &#x60;-&#x60;). |  [optional] |



