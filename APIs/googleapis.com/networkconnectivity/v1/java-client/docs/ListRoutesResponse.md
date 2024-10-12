

# ListRoutesResponse

Response for HubService.ListRoutes method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | The token for the next page of the response. To see more results, use this value as the page_token for your next request. If this value is empty, there are no more results. |  [optional] |
|**routes** | [**List&lt;Route&gt;**](Route.md) | The requested routes. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | RouteTables that could not be reached. |  [optional] |



