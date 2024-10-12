

# ListTransferLogsResponse

The returned list transfer run messages.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | Output only. The next-pagination token. For multiple-page list results, this token can be used as the &#x60;GetTransferRunLogRequest.page_token&#x60; to request the next page of list results. |  [optional] [readonly] |
|**transferMessages** | [**List&lt;TransferMessage&gt;**](TransferMessage.md) | Output only. The stored pipeline transfer messages. |  [optional] [readonly] |



