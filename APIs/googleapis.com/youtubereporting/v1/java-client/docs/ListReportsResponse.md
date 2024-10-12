

# ListReportsResponse

Response message for ReportingService.ListReports.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token to retrieve next page of results. Pass this value in the ListReportsRequest.page_token field in the subsequent call to &#x60;ListReports&#x60; method to retrieve the next page of results. |  [optional] |
|**reports** | [**List&lt;Report&gt;**](Report.md) | The list of report types. |  [optional] |



