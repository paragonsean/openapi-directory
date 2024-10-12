

# GoogleCloudDialogflowCxV3beta1ExperimentResultMetric

Metric and corresponding confidence intervals.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**confidenceInterval** | [**GoogleCloudDialogflowCxV3beta1ExperimentResultConfidenceInterval**](GoogleCloudDialogflowCxV3beta1ExperimentResultConfidenceInterval.md) |  |  [optional] |
|**count** | **Double** | Count value of a metric. |  [optional] |
|**countType** | [**CountTypeEnum**](#CountTypeEnum) | Count-based metric type. Only one of type or count_type is specified in each Metric. |  [optional] |
|**ratio** | **Double** | Ratio value of a metric. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Ratio-based metric type. Only one of type or count_type is specified in each Metric. |  [optional] |



## Enum: CountTypeEnum

| Name | Value |
|---- | -----|
| COUNT_TYPE_UNSPECIFIED | &quot;COUNT_TYPE_UNSPECIFIED&quot; |
| TOTAL_NO_MATCH_COUNT | &quot;TOTAL_NO_MATCH_COUNT&quot; |
| TOTAL_TURN_COUNT | &quot;TOTAL_TURN_COUNT&quot; |
| AVERAGE_TURN_COUNT | &quot;AVERAGE_TURN_COUNT&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| METRIC_UNSPECIFIED | &quot;METRIC_UNSPECIFIED&quot; |
| CONTAINED_SESSION_NO_CALLBACK_RATE | &quot;CONTAINED_SESSION_NO_CALLBACK_RATE&quot; |
| LIVE_AGENT_HANDOFF_RATE | &quot;LIVE_AGENT_HANDOFF_RATE&quot; |
| CALLBACK_SESSION_RATE | &quot;CALLBACK_SESSION_RATE&quot; |
| ABANDONED_SESSION_RATE | &quot;ABANDONED_SESSION_RATE&quot; |
| SESSION_END_RATE | &quot;SESSION_END_RATE&quot; |



