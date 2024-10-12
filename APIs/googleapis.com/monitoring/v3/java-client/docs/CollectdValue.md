

# CollectdValue

A single data point from a collectd-based plugin.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSourceName** | **String** | The data source for the collectd value. For example, there are two data sources for network measurements: \&quot;rx\&quot; and \&quot;tx\&quot;. |  [optional] |
|**dataSourceType** | [**DataSourceTypeEnum**](#DataSourceTypeEnum) | The type of measurement. |  [optional] |
|**value** | [**TypedValue**](TypedValue.md) |  |  [optional] |



## Enum: DataSourceTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED_DATA_SOURCE_TYPE | &quot;UNSPECIFIED_DATA_SOURCE_TYPE&quot; |
| GAUGE | &quot;GAUGE&quot; |
| COUNTER | &quot;COUNTER&quot; |
| DERIVE | &quot;DERIVE&quot; |
| ABSOLUTE | &quot;ABSOLUTE&quot; |



