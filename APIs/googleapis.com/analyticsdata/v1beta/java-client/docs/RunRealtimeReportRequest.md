

# RunRealtimeReportRequest

The request to generate a realtime report.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimensionFilter** | [**FilterExpression**](FilterExpression.md) |  |  [optional] |
|**dimensions** | [**List&lt;Dimension&gt;**](Dimension.md) | The dimensions requested and displayed. |  [optional] |
|**limit** | **String** | The number of rows to return. If unspecified, 10,000 rows are returned. The API returns a maximum of 250,000 rows per request, no matter how many you ask for. &#x60;limit&#x60; must be positive. The API can also return fewer rows than the requested &#x60;limit&#x60;, if there aren&#39;t as many dimension values as the &#x60;limit&#x60;. For instance, there are fewer than 300 possible values for the dimension &#x60;country&#x60;, so when reporting on only &#x60;country&#x60;, you can&#39;t get more than 300 rows, even if you set &#x60;limit&#x60; to a higher value. |  [optional] |
|**metricAggregations** | [**List&lt;MetricAggregationsEnum&gt;**](#List&lt;MetricAggregationsEnum&gt;) | Aggregation of metrics. Aggregated metric values will be shown in rows where the dimension_values are set to \&quot;RESERVED_(MetricAggregation)\&quot;. |  [optional] |
|**metricFilter** | [**FilterExpression**](FilterExpression.md) |  |  [optional] |
|**metrics** | [**List&lt;Metric&gt;**](Metric.md) | The metrics requested and displayed. |  [optional] |
|**minuteRanges** | [**List&lt;MinuteRange&gt;**](MinuteRange.md) | The minute ranges of event data to read. If unspecified, one minute range for the last 30 minutes will be used. If multiple minute ranges are requested, each response row will contain a zero based minute range index. If two minute ranges overlap, the event data for the overlapping minutes is included in the response rows for both minute ranges. |  [optional] |
|**orderBys** | [**List&lt;OrderBy&gt;**](OrderBy.md) | Specifies how rows are ordered in the response. |  [optional] |
|**returnPropertyQuota** | **Boolean** | Toggles whether to return the current state of this Analytics Property&#39;s Realtime quota. Quota is returned in [PropertyQuota](#PropertyQuota). |  [optional] |



## Enum: List&lt;MetricAggregationsEnum&gt;

| Name | Value |
|---- | -----|
| METRIC_AGGREGATION_UNSPECIFIED | &quot;METRIC_AGGREGATION_UNSPECIFIED&quot; |
| TOTAL | &quot;TOTAL&quot; |
| MINIMUM | &quot;MINIMUM&quot; |
| MAXIMUM | &quot;MAXIMUM&quot; |
| COUNT | &quot;COUNT&quot; |



