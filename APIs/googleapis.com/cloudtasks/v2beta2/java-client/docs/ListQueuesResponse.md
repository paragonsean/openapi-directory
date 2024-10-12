

# ListQueuesResponse

Response message for ListQueues.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token to retrieve next page of results. To return the next page of results, call ListQueues with this value as the page_token. If the next_page_token is empty, there are no more results. The page token is valid for only 2 hours. |  [optional] |
|**queues** | [**List&lt;Queue&gt;**](Queue.md) | The list of queues. |  [optional] |



