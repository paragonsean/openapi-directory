

# SegmentMetricFilter

Metric filter to be used in a segment filter clause.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comparisonValue** | **String** | The value to compare against. If the operator is &#x60;BETWEEN&#x60;, this value is treated as minimum comparison value. |  [optional] |
|**maxComparisonValue** | **String** | Max comparison value is only used for &#x60;BETWEEN&#x60; operator. |  [optional] |
|**metricName** | **String** | The metric that will be filtered on. A &#x60;metricFilter&#x60; must contain a metric name. |  [optional] |
|**operator** | [**OperatorEnum**](#OperatorEnum) | Specifies is the operation to perform to compare the metric. The default is &#x60;EQUAL&#x60;. |  [optional] |
|**scope** | [**ScopeEnum**](#ScopeEnum) | Scope for a metric defines the level at which that metric is defined. The specified metric scope must be equal to or greater than its primary scope as defined in the data model. The primary scope is defined by if the segment is selecting users or sessions. |  [optional] |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED_OPERATOR | &quot;UNSPECIFIED_OPERATOR&quot; |
| LESS_THAN | &quot;LESS_THAN&quot; |
| GREATER_THAN | &quot;GREATER_THAN&quot; |
| EQUAL | &quot;EQUAL&quot; |
| BETWEEN | &quot;BETWEEN&quot; |



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED_SCOPE | &quot;UNSPECIFIED_SCOPE&quot; |
| PRODUCT | &quot;PRODUCT&quot; |
| HIT | &quot;HIT&quot; |
| SESSION | &quot;SESSION&quot; |
| USER | &quot;USER&quot; |



