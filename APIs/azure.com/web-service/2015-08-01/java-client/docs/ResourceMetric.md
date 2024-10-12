

# ResourceMetric

Object representing a metric for any resource

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | Metric end time |  [optional] |
|**metricValues** | [**List&lt;ResourceMetricValue&gt;**](ResourceMetricValue.md) | Metric values |  [optional] |
|**name** | [**ResourceMetricName**](ResourceMetricName.md) |  |  [optional] |
|**properties** | [**List&lt;KeyValuePairStringString&gt;**](KeyValuePairStringString.md) | Properties |  [optional] |
|**resourceId** | **String** | Metric resource Id |  [optional] |
|**startTime** | **OffsetDateTime** | Metric start time |  [optional] |
|**timeGrain** | **String** | Metric granularity. E.g PT1H, PT5M, P1D |  [optional] |
|**unit** | **String** | Metric unit |  [optional] |



