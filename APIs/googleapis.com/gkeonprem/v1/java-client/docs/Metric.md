

# Metric

Progress metric is (string, int|float|string) pair.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**doubleValue** | **Double** | For metrics with floating point value. |  [optional] |
|**intValue** | **String** | For metrics with integer value. |  [optional] |
|**metric** | [**MetricEnum**](#MetricEnum) | Required. The metric name. |  [optional] |
|**stringValue** | **String** | For metrics with custom values (ratios, visual progress, etc.). |  [optional] |



## Enum: MetricEnum

| Name | Value |
|---- | -----|
| METRIC_ID_UNSPECIFIED | &quot;METRIC_ID_UNSPECIFIED&quot; |
| NODES_TOTAL | &quot;NODES_TOTAL&quot; |
| NODES_DRAINING | &quot;NODES_DRAINING&quot; |
| NODES_UPGRADING | &quot;NODES_UPGRADING&quot; |
| NODES_PENDING_UPGRADE | &quot;NODES_PENDING_UPGRADE&quot; |
| NODES_UPGRADED | &quot;NODES_UPGRADED&quot; |
| NODES_FAILED | &quot;NODES_FAILED&quot; |
| NODES_HEALTHY | &quot;NODES_HEALTHY&quot; |
| NODES_RECONCILING | &quot;NODES_RECONCILING&quot; |
| NODES_IN_MAINTENANCE | &quot;NODES_IN_MAINTENANCE&quot; |
| PREFLIGHTS_COMPLETED | &quot;PREFLIGHTS_COMPLETED&quot; |
| PREFLIGHTS_RUNNING | &quot;PREFLIGHTS_RUNNING&quot; |
| PREFLIGHTS_FAILED | &quot;PREFLIGHTS_FAILED&quot; |
| PREFLIGHTS_TOTAL | &quot;PREFLIGHTS_TOTAL&quot; |



