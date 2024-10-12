

# ListSpokesResponse

The response for HubService.ListSpokes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | The token for the next page of the response. To see more results, use this value as the page_token for your next request. If this value is empty, there are no more results. |  [optional] |
|**spokes** | [**List&lt;Spoke&gt;**](Spoke.md) | The requested spokes. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



