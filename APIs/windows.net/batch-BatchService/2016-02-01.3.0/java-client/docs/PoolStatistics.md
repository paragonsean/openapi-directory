

# PoolStatistics

Contains utilization and resource usage statistics for the lifetime of a pool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lastUpdateTime** | **OffsetDateTime** | The time at which the statistics were last updated. All statistics are limited to the range between startTime and lastUpdateTime. |  |
|**resourceStats** | [**ResourceStatistics**](ResourceStatistics.md) |  |  [optional] |
|**startTime** | **OffsetDateTime** | The start time of the time range covered by the statistics. |  |
|**url** | **String** | The URL for the statistics. |  |
|**usageStats** | [**UsageStatistics**](UsageStatistics.md) |  |  [optional] |



