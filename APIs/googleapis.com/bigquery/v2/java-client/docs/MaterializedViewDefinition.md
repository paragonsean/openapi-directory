

# MaterializedViewDefinition

Definition and configuration of a materialized view.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowNonIncrementalDefinition** | **Boolean** | Optional. This option declares authors intention to construct a materialized view that will not be refreshed incrementally. |  [optional] |
|**enableRefresh** | **Boolean** | Optional. Enable automatic refresh of the materialized view when the base table is updated. The default value is \&quot;true\&quot;. |  [optional] |
|**lastRefreshTime** | **String** | Output only. The time when this materialized view was last refreshed, in milliseconds since the epoch. |  [optional] [readonly] |
|**maxStaleness** | **byte[]** | [Optional] Max staleness of data that could be returned when materizlized view is queried (formatted as Google SQL Interval type). |  [optional] |
|**query** | **String** | Required. A query whose results are persisted. |  [optional] |
|**refreshIntervalMs** | **String** | Optional. The maximum frequency at which this materialized view will be refreshed. The default value is \&quot;1800000\&quot; (30 minutes). |  [optional] |



