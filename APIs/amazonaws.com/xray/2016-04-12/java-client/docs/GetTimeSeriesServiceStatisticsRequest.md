

# GetTimeSeriesServiceStatisticsRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**startTime** | **OffsetDateTime** | The start of the time frame for which to aggregate statistics. |  |
|**endTime** | **OffsetDateTime** | The end of the time frame for which to aggregate statistics. |  |
|**groupName** | **String** | The case-sensitive name of the group for which to pull statistics from. |  [optional] |
|**groupARN** | **String** | The Amazon Resource Name (ARN) of the group for which to pull statistics from. |  [optional] |
|**entitySelectorExpression** | **String** | A filter expression defining entities that will be aggregated for statistics. Supports ID, service, and edge functions. If no selector expression is specified, edge statistics are returned.  |  [optional] |
|**period** | **Integer** | Aggregation period in seconds. |  [optional] |
|**forecastStatistics** | **Boolean** | The forecasted high and low fault count values. Forecast enabled requests require the EntitySelectorExpression ID be provided. |  [optional] |
|**nextToken** | **String** | Pagination token. |  [optional] |



