

# FetchRepositoryHistoryResponse

`FetchRepositoryHistory` response message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**commits** | [**List&lt;CommitLogEntry&gt;**](CommitLogEntry.md) | A list of commit logs, ordered by &#39;git log&#39; default order. |  [optional] |
|**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |



