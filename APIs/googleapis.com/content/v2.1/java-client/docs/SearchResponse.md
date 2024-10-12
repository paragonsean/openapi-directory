

# SearchResponse

Response message for the ReportService.Search method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | Token which can be sent as &#x60;page_token&#x60; to retrieve the next page. If omitted, there are no subsequent pages. |  [optional] |
|**results** | [**List&lt;ReportRow&gt;**](ReportRow.md) | Rows that matched the search query. |  [optional] |



