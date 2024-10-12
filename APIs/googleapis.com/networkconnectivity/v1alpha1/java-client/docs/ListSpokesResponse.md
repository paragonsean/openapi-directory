

# ListSpokesResponse

The response for HubService.ListSpokes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | The next pagination token in the List response. It should be used as page_token for the following request. An empty value means no more result. |  [optional] |
|**spokes** | [**List&lt;Spoke&gt;**](Spoke.md) | Spokes to be returned. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached. |  [optional] |



