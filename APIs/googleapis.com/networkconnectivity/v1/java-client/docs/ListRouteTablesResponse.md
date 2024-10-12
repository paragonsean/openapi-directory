

# ListRouteTablesResponse

Response for HubService.ListRouteTables method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | The token for the next page of the response. To see more results, use this value as the page_token for your next request. If this value is empty, there are no more results. |  [optional] |
|**routeTables** | [**List&lt;RouteTable&gt;**](RouteTable.md) | The requested route tables. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Hubs that could not be reached. |  [optional] |



