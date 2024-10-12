

# ListServiceConnectionMapsResponse

Response for ListServiceConnectionMaps.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | The next pagination token in the List response. It should be used as page_token for the following request. An empty value means no more result. |  [optional] |
|**serviceConnectionMaps** | [**List&lt;ServiceConnectionMap&gt;**](ServiceConnectionMap.md) | ServiceConnectionMaps to be returned. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



