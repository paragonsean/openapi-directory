

# GoogleCloudChannelV1FetchReportResultsResponse

Response message for CloudChannelReportsService.FetchReportResults. Contains a tabular representation of the report results.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | Pass this token to FetchReportResultsRequest.page_token to retrieve the next page of results. |  [optional] |
|**reportMetadata** | [**GoogleCloudChannelV1ReportResultsMetadata**](GoogleCloudChannelV1ReportResultsMetadata.md) |  |  [optional] |
|**rows** | [**List&lt;GoogleCloudChannelV1Row&gt;**](GoogleCloudChannelV1Row.md) | The report&#39;s lists of values. Each row follows the settings and ordering of the columns from &#x60;report_metadata&#x60;. |  [optional] |



