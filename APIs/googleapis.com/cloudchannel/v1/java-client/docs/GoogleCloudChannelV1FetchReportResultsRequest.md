

# GoogleCloudChannelV1FetchReportResultsRequest

Request message for CloudChannelReportsService.FetchReportResults.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pageSize** | **Integer** | Optional. Requested page size of the report. The server may return fewer results than requested. If you don&#39;t specify a page size, the server uses a sensible default (may change over time). The maximum value is 30,000; the server will change larger values to 30,000. |  [optional] |
|**pageToken** | **String** | Optional. A token that specifies a page of results beyond the first page. Obtained through FetchReportResultsResponse.next_page_token of the previous CloudChannelReportsService.FetchReportResults call. |  [optional] |
|**partitionKeys** | **List&lt;String&gt;** | Optional. List of keys specifying which report partitions to return. If empty, returns all partitions. |  [optional] |



