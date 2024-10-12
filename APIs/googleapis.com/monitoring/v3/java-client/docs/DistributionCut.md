

# DistributionCut

A DistributionCut defines a TimeSeries and thresholds used for measuring good service and total service. The TimeSeries must have ValueType = DISTRIBUTION and MetricKind = DELTA or MetricKind = CUMULATIVE. The computed good_service will be the estimated count of values in the Distribution that fall within the specified min and max.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**distributionFilter** | **String** | A monitoring filter (https://cloud.google.com/monitoring/api/v3/filters) specifying a TimeSeries aggregating values. Must have ValueType &#x3D; DISTRIBUTION and MetricKind &#x3D; DELTA or MetricKind &#x3D; CUMULATIVE. |  [optional] |
|**range** | [**GoogleMonitoringV3Range**](GoogleMonitoringV3Range.md) |  |  [optional] |



