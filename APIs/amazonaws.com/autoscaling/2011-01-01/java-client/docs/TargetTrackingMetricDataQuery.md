

# TargetTrackingMetricDataQuery

The metric data to return. Also defines whether this call is returning data for one metric only, or whether it is performing a math expression on the values of returned metric statistics to create a new time series. A time series is a series of data points, each of which is associated with a timestamp.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**String**](String.md) |  |  |
|**expression** | [**String**](String.md) |  |  [optional] |
|**metricStat** | [**TargetTrackingMetricDataQueryMetricStat**](TargetTrackingMetricDataQueryMetricStat.md) |  |  [optional] |
|**label** | [**String**](String.md) |  |  [optional] |
|**returnData** | [**Boolean**](Boolean.md) |  |  [optional] |



