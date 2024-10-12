# MigrationCenterApi.ReportSummaryHistogramChartData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buckets** | [**[ReportSummaryHistogramChartDataBucket]**](ReportSummaryHistogramChartDataBucket.md) | Buckets in the histogram. There will be &#x60;n+1&#x60; buckets matching &#x60;n&#x60; lower bounds in the request. The first bucket will be from -infinity to the first bound. Subsequent buckets will be between one bound and the next. The final bucket will be from the final bound to infinity. | [optional] 


