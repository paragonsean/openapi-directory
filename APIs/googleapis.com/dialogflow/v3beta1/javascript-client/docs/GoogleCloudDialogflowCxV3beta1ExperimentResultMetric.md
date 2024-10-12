# DialogflowApi.GoogleCloudDialogflowCxV3beta1ExperimentResultMetric

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**confidenceInterval** | [**GoogleCloudDialogflowCxV3beta1ExperimentResultConfidenceInterval**](GoogleCloudDialogflowCxV3beta1ExperimentResultConfidenceInterval.md) |  | [optional] 
**count** | **Number** | Count value of a metric. | [optional] 
**countType** | **String** | Count-based metric type. Only one of type or count_type is specified in each Metric. | [optional] 
**ratio** | **Number** | Ratio value of a metric. | [optional] 
**type** | **String** | Ratio-based metric type. Only one of type or count_type is specified in each Metric. | [optional] 



## Enum: CountTypeEnum


* `COUNT_TYPE_UNSPECIFIED` (value: `"COUNT_TYPE_UNSPECIFIED"`)

* `TOTAL_NO_MATCH_COUNT` (value: `"TOTAL_NO_MATCH_COUNT"`)

* `TOTAL_TURN_COUNT` (value: `"TOTAL_TURN_COUNT"`)

* `AVERAGE_TURN_COUNT` (value: `"AVERAGE_TURN_COUNT"`)





## Enum: TypeEnum


* `METRIC_UNSPECIFIED` (value: `"METRIC_UNSPECIFIED"`)

* `CONTAINED_SESSION_NO_CALLBACK_RATE` (value: `"CONTAINED_SESSION_NO_CALLBACK_RATE"`)

* `LIVE_AGENT_HANDOFF_RATE` (value: `"LIVE_AGENT_HANDOFF_RATE"`)

* `CALLBACK_SESSION_RATE` (value: `"CALLBACK_SESSION_RATE"`)

* `ABANDONED_SESSION_RATE` (value: `"ABANDONED_SESSION_RATE"`)

* `SESSION_END_RATE` (value: `"SESSION_END_RATE"`)




