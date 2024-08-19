# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1betaRunAccessReportResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimensionHeaders** | [**[GoogleAnalyticsAdminV1betaAccessDimensionHeader]**](GoogleAnalyticsAdminV1betaAccessDimensionHeader.md) | The header for a column in the report that corresponds to a specific dimension. The number of DimensionHeaders and ordering of DimensionHeaders matches the dimensions present in rows. | [optional] 
**metricHeaders** | [**[GoogleAnalyticsAdminV1betaAccessMetricHeader]**](GoogleAnalyticsAdminV1betaAccessMetricHeader.md) | The header for a column in the report that corresponds to a specific metric. The number of MetricHeaders and ordering of MetricHeaders matches the metrics present in rows. | [optional] 
**quota** | [**GoogleAnalyticsAdminV1betaAccessQuota**](GoogleAnalyticsAdminV1betaAccessQuota.md) |  | [optional] 
**rowCount** | **Number** | The total number of rows in the query result. &#x60;rowCount&#x60; is independent of the number of rows returned in the response, the &#x60;limit&#x60; request parameter, and the &#x60;offset&#x60; request parameter. For example if a query returns 175 rows and includes &#x60;limit&#x60; of 50 in the API request, the response will contain &#x60;rowCount&#x60; of 175 but only 50 rows. To learn more about this pagination parameter, see [Pagination](https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination). | [optional] 
**rows** | [**[GoogleAnalyticsAdminV1betaAccessRow]**](GoogleAnalyticsAdminV1betaAccessRow.md) | Rows of dimension value combinations and metric values in the report. | [optional] 


