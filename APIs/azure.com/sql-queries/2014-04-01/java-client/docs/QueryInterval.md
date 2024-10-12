

# QueryInterval

A database query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**executionCount** | **BigDecimal** | The number of times the query was executed during this interval. |  [optional] [readonly] |
|**intervalStartTime** | **OffsetDateTime** | The start time of the measurement interval (ISO8601 format). |  [optional] [readonly] |
|**metrics** | [**List&lt;QueryMetric&gt;**](QueryMetric.md) | The list of query metrics during this interval. |  [optional] [readonly] |



