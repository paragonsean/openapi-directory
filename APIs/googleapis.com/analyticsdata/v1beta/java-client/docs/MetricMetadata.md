

# MetricMetadata

Explains a metric.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**apiName** | **String** | A metric name. Useable in [Metric](#Metric)&#39;s &#x60;name&#x60;. For example, &#x60;eventCount&#x60;. |  [optional] |
|**blockedReasons** | [**List&lt;BlockedReasonsEnum&gt;**](#List&lt;BlockedReasonsEnum&gt;) | If reasons are specified, your access is blocked to this metric for this property. API requests from you to this property for this metric will succeed; however, the report will contain only zeros for this metric. API requests with metric filters on blocked metrics will fail. If reasons are empty, you have access to this metric. To learn more, see [Access and data-restriction management](https://support.google.com/analytics/answer/10851388). |  [optional] |
|**category** | **String** | The display name of the category that this metrics belongs to. Similar dimensions and metrics are categorized together. |  [optional] |
|**customDefinition** | **Boolean** | True if the metric is a custom metric for this property. |  [optional] |
|**deprecatedApiNames** | **List&lt;String&gt;** | Still usable but deprecated names for this metric. If populated, this metric is available by either &#x60;apiName&#x60; or one of &#x60;deprecatedApiNames&#x60; for a period of time. After the deprecation period, the metric will be available only by &#x60;apiName&#x60;. |  [optional] |
|**description** | **String** | Description of how this metric is used and calculated. |  [optional] |
|**expression** | **String** | The mathematical expression for this derived metric. Can be used in [Metric](#Metric)&#39;s &#x60;expression&#x60; field for equivalent reports. Most metrics are not expressions, and for non-expressions, this field is empty. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of this metric. |  [optional] |
|**uiName** | **String** | This metric&#39;s name within the Google Analytics user interface. For example, &#x60;Event count&#x60;. |  [optional] |



## Enum: List&lt;BlockedReasonsEnum&gt;

| Name | Value |
|---- | -----|
| BLOCKED_REASON_UNSPECIFIED | &quot;BLOCKED_REASON_UNSPECIFIED&quot; |
| NO_REVENUE_METRICS | &quot;NO_REVENUE_METRICS&quot; |
| NO_COST_METRICS | &quot;NO_COST_METRICS&quot; |



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



