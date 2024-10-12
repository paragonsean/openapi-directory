# SearchAds360ReportingApi.GoogleAdsSearchads360V0ServicesSearchSearchAds360Request

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pageSize** | **Number** | Number of elements to retrieve in a single page. When too large a page is requested, the server may decide to further limit the number of returned resources. | [optional] 
**pageToken** | **String** | Token of the page to retrieve. If not specified, the first page of results will be returned. Use the value obtained from &#x60;next_page_token&#x60; in the previous response in order to request the next page of results. | [optional] 
**query** | **String** | Required. The query string. | [optional] 
**returnTotalResultsCount** | **Boolean** | If true, the total number of results that match the query ignoring the LIMIT clause will be included in the response. Default is false. | [optional] 
**summaryRowSetting** | **String** | Determines whether a summary row will be returned. By default, summary row is not returned. If requested, the summary row will be sent in a response by itself after all other query results are returned. | [optional] 
**validateOnly** | **Boolean** | If true, the request is validated but not executed. | [optional] 



## Enum: SummaryRowSettingEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `NO_SUMMARY_ROW` (value: `"NO_SUMMARY_ROW"`)

* `SUMMARY_ROW_WITH_RESULTS` (value: `"SUMMARY_ROW_WITH_RESULTS"`)

* `SUMMARY_ROW_ONLY` (value: `"SUMMARY_ROW_ONLY"`)




