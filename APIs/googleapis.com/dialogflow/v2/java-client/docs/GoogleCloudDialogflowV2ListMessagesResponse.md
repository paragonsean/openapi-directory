

# GoogleCloudDialogflowV2ListMessagesResponse

The response message for Conversations.ListMessages.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**messages** | [**List&lt;GoogleCloudDialogflowV2Message&gt;**](GoogleCloudDialogflowV2Message.md) | The list of messages. There will be a maximum number of items returned based on the page_size field in the request. &#x60;messages&#x60; is sorted by &#x60;create_time&#x60; in descending order. |  [optional] |
|**nextPageToken** | **String** | Token to retrieve the next page of results, or empty if there are no more results in the list. |  [optional] |



