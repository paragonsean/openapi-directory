

# OracleSourceConfig

Oracle data source configuration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dropLargeObjects** | **Object** | Configuration to drop large object values. |  [optional] |
|**excludeObjects** | [**OracleRdbms**](OracleRdbms.md) |  |  [optional] |
|**includeObjects** | [**OracleRdbms**](OracleRdbms.md) |  |  [optional] |
|**maxConcurrentBackfillTasks** | **Integer** | Maximum number of concurrent backfill tasks. The number should be non-negative. If not set (or set to 0), the system&#39;s default value is used. |  [optional] |
|**maxConcurrentCdcTasks** | **Integer** | Maximum number of concurrent CDC tasks. The number should be non-negative. If not set (or set to 0), the system&#39;s default value is used. |  [optional] |
|**streamLargeObjects** | **Object** | Configuration to stream large object values. |  [optional] |



