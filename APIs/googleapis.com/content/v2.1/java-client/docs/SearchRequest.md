

# SearchRequest

Request message for the ReportService.Search method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pageSize** | **Integer** | Number of ReportRows to retrieve in a single page. Defaults to 1000. Values above 5000 are coerced to 5000. |  [optional] |
|**pageToken** | **String** | Token of the page to retrieve. If not specified, the first page of results is returned. In order to request the next page of results, the value obtained from &#x60;next_page_token&#x60; in the previous response should be used. |  [optional] |
|**query** | **String** | Required. Query that defines performance metrics to retrieve and dimensions according to which the metrics are to be segmented. For details on how to construct your query, see the [Query Language guide](https://developers.google.com/shopping-content/guides/reports/query-language/overview). |  [optional] |



