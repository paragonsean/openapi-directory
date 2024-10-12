

# ListHubsResponse

Response for HubService.ListHubs method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hubs** | [**List&lt;Hub&gt;**](Hub.md) | The requested hubs. |  [optional] |
|**nextPageToken** | **String** | The token for the next page of the response. To see more results, use this value as the page_token for your next request. If this value is empty, there are no more results. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



