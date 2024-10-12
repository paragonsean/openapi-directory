# CloudMonitoringApi.CollectdValue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataSourceName** | **String** | The data source for the collectd value. For example, there are two data sources for network measurements: \&quot;rx\&quot; and \&quot;tx\&quot;. | [optional] 
**dataSourceType** | **String** | The type of measurement. | [optional] 
**value** | [**TypedValue**](TypedValue.md) |  | [optional] 



## Enum: DataSourceTypeEnum


* `UNSPECIFIED_DATA_SOURCE_TYPE` (value: `"UNSPECIFIED_DATA_SOURCE_TYPE"`)

* `GAUGE` (value: `"GAUGE"`)

* `COUNTER` (value: `"COUNTER"`)

* `DERIVE` (value: `"DERIVE"`)

* `ABSOLUTE` (value: `"ABSOLUTE"`)




