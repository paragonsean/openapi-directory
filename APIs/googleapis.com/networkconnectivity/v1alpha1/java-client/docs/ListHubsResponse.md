

# ListHubsResponse

Response for HubService.ListHubs method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hubs** | [**List&lt;Hub&gt;**](Hub.md) | Hubs to be returned. |  [optional] |
|**nextPageToken** | **String** | The next pagination token in the List response. It should be used as page_token for the following request. An empty value means no more result. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



