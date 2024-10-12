

# DashboardFilter

A filter to reduce the amount of data charted in relevant widgets.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filterType** | [**FilterTypeEnum**](#FilterTypeEnum) | The specified filter type |  [optional] |
|**labelKey** | **String** | Required. The key for the label |  [optional] |
|**stringValue** | **String** | A variable-length string value. |  [optional] |
|**templateVariable** | **String** | The placeholder text that can be referenced in a filter string or MQL query. If omitted, the dashboard filter will be applied to all relevant widgets in the dashboard. |  [optional] |



## Enum: FilterTypeEnum

| Name | Value |
|---- | -----|
| FILTER_TYPE_UNSPECIFIED | &quot;FILTER_TYPE_UNSPECIFIED&quot; |
| RESOURCE_LABEL | &quot;RESOURCE_LABEL&quot; |
| METRIC_LABEL | &quot;METRIC_LABEL&quot; |
| USER_METADATA_LABEL | &quot;USER_METADATA_LABEL&quot; |
| SYSTEM_METADATA_LABEL | &quot;SYSTEM_METADATA_LABEL&quot; |
| GROUP | &quot;GROUP&quot; |



