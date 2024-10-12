

# PoolStatistics

Contains utilization and resource usage statistics for the lifetime of a pool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lastUpdateTime** | **OffsetDateTime** | Gets or sets the time at which the statistics were last updated. All statistics are limited to the range between startTime and lastUpdateTime. |  |
|**resourceStats** | [**ResourceStatistics**](ResourceStatistics.md) |  |  [optional] |
|**startTime** | **OffsetDateTime** | Gets or sets the start time of the time range covered by the statistics. |  |
|**url** | **String** | Gets or sets the URL for the statistics. |  |
|**usageStats** | [**UsageStatistics**](UsageStatistics.md) |  |  [optional] |



