

# BatchRunReportsResponse

The batch response containing multiple reports.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kind** | **String** | Identifies what kind of resource this message is. This &#x60;kind&#x60; is always the fixed string \&quot;analyticsData#batchRunReports\&quot;. Useful to distinguish between response types in JSON. |  [optional] |
|**reports** | [**List&lt;RunReportResponse&gt;**](RunReportResponse.md) | Individual responses. Each response has a separate report request. |  [optional] |



