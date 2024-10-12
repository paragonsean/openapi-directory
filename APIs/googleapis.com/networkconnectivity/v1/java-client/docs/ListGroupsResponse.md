

# ListGroupsResponse

Response for HubService.ListGroups method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**groups** | [**List&lt;Group&gt;**](Group.md) | The requested groups. |  [optional] |
|**nextPageToken** | **String** | The token for the next page of the response. To see more results, use this value as the page_token for your next request. If this value is empty, there are no more results. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Hubs that could not be reached. |  [optional] |



