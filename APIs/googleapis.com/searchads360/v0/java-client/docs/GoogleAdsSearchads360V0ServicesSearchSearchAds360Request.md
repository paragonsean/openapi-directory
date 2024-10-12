

# GoogleAdsSearchads360V0ServicesSearchSearchAds360Request

Request message for SearchAds360Service.Search.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pageSize** | **Integer** | Number of elements to retrieve in a single page. When too large a page is requested, the server may decide to further limit the number of returned resources. |  [optional] |
|**pageToken** | **String** | Token of the page to retrieve. If not specified, the first page of results will be returned. Use the value obtained from &#x60;next_page_token&#x60; in the previous response in order to request the next page of results. |  [optional] |
|**query** | **String** | Required. The query string. |  [optional] |
|**returnTotalResultsCount** | **Boolean** | If true, the total number of results that match the query ignoring the LIMIT clause will be included in the response. Default is false. |  [optional] |
|**summaryRowSetting** | [**SummaryRowSettingEnum**](#SummaryRowSettingEnum) | Determines whether a summary row will be returned. By default, summary row is not returned. If requested, the summary row will be sent in a response by itself after all other query results are returned. |  [optional] |
|**validateOnly** | **Boolean** | If true, the request is validated but not executed. |  [optional] |



## Enum: SummaryRowSettingEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| NO_SUMMARY_ROW | &quot;NO_SUMMARY_ROW&quot; |
| SUMMARY_ROW_WITH_RESULTS | &quot;SUMMARY_ROW_WITH_RESULTS&quot; |
| SUMMARY_ROW_ONLY | &quot;SUMMARY_ROW_ONLY&quot; |



