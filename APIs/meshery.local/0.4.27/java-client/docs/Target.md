

# Target

for an any panel

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alias** | **String** |  |  [optional] |
|**aliasBy** | **String** |  |  [optional] |
|**alignOptions** | [**List&lt;StackdriverAlignOptions&gt;**](StackdriverAlignOptions.md) |  |  [optional] |
|**alignmentPeriod** | **String** |  |  [optional] |
|**bucketAggs** | [**List&lt;TargetBucketAggsInner&gt;**](TargetBucketAggsInner.md) |  |  [optional] |
|**crossSeriesReducer** | **String** |  |  [optional] |
|**datasource** | **String** |  |  [optional] |
|**dimensions** | **Map&lt;String, String&gt;** |  |  [optional] |
|**dsType** | **String** | For Elasticsearch |  [optional] |
|**expr** | **String** | For Prometheus |  [optional] |
|**filters** | **List&lt;String&gt;** |  |  [optional] |
|**format** | **String** |  |  [optional] |
|**group** | [**List&lt;TargetGroupInner&gt;**](TargetGroupInner.md) |  |  [optional] |
|**groupBys** | **List&lt;String&gt;** |  |  [optional] |
|**hide** | **Boolean** |  |  [optional] |
|**instant** | **Boolean** |  |  [optional] |
|**interval** | **String** |  |  [optional] |
|**intervalFactor** | **Long** |  |  [optional] |
|**legendFormat** | **String** |  |  [optional] |
|**measurement** | **String** | For InfluxDB |  [optional] |
|**metricColumn** | **String** |  |  [optional] |
|**metricKind** | **String** |  |  [optional] |
|**metricName** | **String** |  |  [optional] |
|**metricType** | **String** |  |  [optional] |
|**metrics** | [**List&lt;TargetMetricsInner&gt;**](TargetMetricsInner.md) |  |  [optional] |
|**namespace** | **String** | For CloudWatch |  [optional] |
|**perSeriesAligner** | **String** |  |  [optional] |
|**period** | **String** |  |  [optional] |
|**projectName** | **String** | For the Stackdriver data source. Find out more information at https:/grafana.com/docs/grafana/v6.0/features/datasources/stackdriver/ |  [optional] |
|**query** | **String** |  |  [optional] |
|**rawQuery** | **Boolean** |  |  [optional] |
|**rawSql** | **String** |  |  [optional] |
|**refId** | **String** |  |  [optional] |
|**region** | **String** |  |  [optional] |
|**select** | **List&lt;List&lt;TargetGroupInner&gt;&gt;** |  |  [optional] |
|**statistics** | **List&lt;String&gt;** |  |  [optional] |
|**step** | **Long** |  |  [optional] |
|**table** | **String** | For PostgreSQL |  [optional] |
|**target** | **String** | For Graphite |  [optional] |
|**timeColumn** | **String** |  |  [optional] |
|**timeField** | **String** |  |  [optional] |
|**valueType** | **String** |  |  [optional] |
|**where** | [**List&lt;TargetWhereInner&gt;**](TargetWhereInner.md) |  |  [optional] |



