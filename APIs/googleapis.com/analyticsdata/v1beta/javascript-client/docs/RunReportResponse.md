# GoogleAnalyticsDataApi.RunReportResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dimensionHeaders** | [**[DimensionHeader]**](DimensionHeader.md) | Describes dimension columns. The number of DimensionHeaders and ordering of DimensionHeaders matches the dimensions present in rows. | [optional] 
**kind** | **String** | Identifies what kind of resource this message is. This &#x60;kind&#x60; is always the fixed string \&quot;analyticsData#runReport\&quot;. Useful to distinguish between response types in JSON. | [optional] 
**maximums** | [**[Row]**](Row.md) | If requested, the maximum values of metrics. | [optional] 
**metadata** | [**ResponseMetaData**](ResponseMetaData.md) |  | [optional] 
**metricHeaders** | [**[MetricHeader]**](MetricHeader.md) | Describes metric columns. The number of MetricHeaders and ordering of MetricHeaders matches the metrics present in rows. | [optional] 
**minimums** | [**[Row]**](Row.md) | If requested, the minimum values of metrics. | [optional] 
**propertyQuota** | [**PropertyQuota**](PropertyQuota.md) |  | [optional] 
**rowCount** | **Number** | The total number of rows in the query result. &#x60;rowCount&#x60; is independent of the number of rows returned in the response, the &#x60;limit&#x60; request parameter, and the &#x60;offset&#x60; request parameter. For example if a query returns 175 rows and includes &#x60;limit&#x60; of 50 in the API request, the response will contain &#x60;rowCount&#x60; of 175 but only 50 rows. To learn more about this pagination parameter, see [Pagination](https://developers.google.com/analytics/devguides/reporting/data/v1/basics#pagination). | [optional] 
**rows** | [**[Row]**](Row.md) | Rows of dimension value combinations and metric values in the report. | [optional] 
**totals** | [**[Row]**](Row.md) | If requested, the totaled values of metrics. | [optional] 


