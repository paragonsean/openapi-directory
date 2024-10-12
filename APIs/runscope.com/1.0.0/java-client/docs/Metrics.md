

# Metrics


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**changesFromLastPeriod** | **Object** | The changes in average response time compared to the last period. |  [optional] |
|**environmentUuid** | **String** | The environment_uuid that filters this request. |  [optional] |
|**region** | **String** | The region that filters this request. |  [optional] |
|**responseTimes** | [**List&lt;MetricsResponseTimesInner&gt;**](MetricsResponseTimesInner.md) | The list of response times based on the timeframe of the request. |  [optional] |
|**thisTimePeriod** | **Object** | The average response time for different percentiles for the request in the requested timeframe. |  [optional] |
|**timeframe** | **String** | The timeframe that filters this request. |  [optional] |



