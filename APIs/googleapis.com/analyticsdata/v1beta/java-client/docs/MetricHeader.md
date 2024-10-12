

# MetricHeader

Describes a metric column in the report. Visible metrics requested in a report produce column entries within rows and MetricHeaders. However, metrics used exclusively within filters or expressions do not produce columns in a report; correspondingly, those metrics do not produce headers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The metric&#39;s name. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The metric&#39;s data type. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| METRIC_TYPE_UNSPECIFIED | &quot;METRIC_TYPE_UNSPECIFIED&quot; |
| TYPE_INTEGER | &quot;TYPE_INTEGER&quot; |
| TYPE_FLOAT | &quot;TYPE_FLOAT&quot; |
| TYPE_SECONDS | &quot;TYPE_SECONDS&quot; |
| TYPE_MILLISECONDS | &quot;TYPE_MILLISECONDS&quot; |
| TYPE_MINUTES | &quot;TYPE_MINUTES&quot; |
| TYPE_HOURS | &quot;TYPE_HOURS&quot; |
| TYPE_STANDARD | &quot;TYPE_STANDARD&quot; |
| TYPE_CURRENCY | &quot;TYPE_CURRENCY&quot; |
| TYPE_FEET | &quot;TYPE_FEET&quot; |
| TYPE_MILES | &quot;TYPE_MILES&quot; |
| TYPE_METERS | &quot;TYPE_METERS&quot; |
| TYPE_KILOMETERS | &quot;TYPE_KILOMETERS&quot; |



