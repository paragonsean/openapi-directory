

# TestConformanceMetric

Represents the test conformance metrics (current score, history and evolution trend) of a Service

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregationLabelValue** | **String** | Value of the label used for metrics aggregation (if any) |  [optional] |
|**currentScore** | **Double** | Current test conformance score for the related Service |  |
|**id** | **String** | Unique identifier of coverage metric |  |
|**lastUpdateDay** | **String** | The day of latest score update (in yyyyMMdd format) |  [optional] |
|**latestScores** | **Map&lt;String, BigDecimal&gt;** | History of latest scores (key is date with format yyyyMMdd, value is score as double) |  [optional] |
|**latestTrend** | **Trend** |  |  [optional] |
|**maxPossibleScore** | **Double** | Maximum conformance score that can be reached (depends on samples expresiveness) |  |
|**serviceId** | **String** | Unique identifier of the Service this metric is related to |  |



