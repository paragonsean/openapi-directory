# CloudMonitoringApi.DashboardFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filterType** | **String** | The specified filter type | [optional] 
**labelKey** | **String** | Required. The key for the label | [optional] 
**stringValue** | **String** | A variable-length string value. | [optional] 
**templateVariable** | **String** | The placeholder text that can be referenced in a filter string or MQL query. If omitted, the dashboard filter will be applied to all relevant widgets in the dashboard. | [optional] 



## Enum: FilterTypeEnum


* `FILTER_TYPE_UNSPECIFIED` (value: `"FILTER_TYPE_UNSPECIFIED"`)

* `RESOURCE_LABEL` (value: `"RESOURCE_LABEL"`)

* `METRIC_LABEL` (value: `"METRIC_LABEL"`)

* `USER_METADATA_LABEL` (value: `"USER_METADATA_LABEL"`)

* `SYSTEM_METADATA_LABEL` (value: `"SYSTEM_METADATA_LABEL"`)

* `GROUP` (value: `"GROUP"`)




