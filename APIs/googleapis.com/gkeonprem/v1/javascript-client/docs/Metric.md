# AnthosOnPremApi.Metric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doubleValue** | **Number** | For metrics with floating point value. | [optional] 
**intValue** | **String** | For metrics with integer value. | [optional] 
**metric** | **String** | Required. The metric name. | [optional] 
**stringValue** | **String** | For metrics with custom values (ratios, visual progress, etc.). | [optional] 



## Enum: MetricEnum


* `METRIC_ID_UNSPECIFIED` (value: `"METRIC_ID_UNSPECIFIED"`)

* `NODES_TOTAL` (value: `"NODES_TOTAL"`)

* `NODES_DRAINING` (value: `"NODES_DRAINING"`)

* `NODES_UPGRADING` (value: `"NODES_UPGRADING"`)

* `NODES_PENDING_UPGRADE` (value: `"NODES_PENDING_UPGRADE"`)

* `NODES_UPGRADED` (value: `"NODES_UPGRADED"`)

* `NODES_FAILED` (value: `"NODES_FAILED"`)

* `NODES_HEALTHY` (value: `"NODES_HEALTHY"`)

* `NODES_RECONCILING` (value: `"NODES_RECONCILING"`)

* `NODES_IN_MAINTENANCE` (value: `"NODES_IN_MAINTENANCE"`)

* `PREFLIGHTS_COMPLETED` (value: `"PREFLIGHTS_COMPLETED"`)

* `PREFLIGHTS_RUNNING` (value: `"PREFLIGHTS_RUNNING"`)

* `PREFLIGHTS_FAILED` (value: `"PREFLIGHTS_FAILED"`)

* `PREFLIGHTS_TOTAL` (value: `"PREFLIGHTS_TOTAL"`)




