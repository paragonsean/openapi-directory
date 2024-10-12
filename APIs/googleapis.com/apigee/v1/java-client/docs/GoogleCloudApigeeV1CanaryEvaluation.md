

# GoogleCloudApigeeV1CanaryEvaluation

CanaryEvaluation represents the canary analysis between two versions of the runtime that is serving requests.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**control** | **String** | Required. The stable version that is serving requests. |  [optional] |
|**createTime** | **String** | Output only. Create time of the canary evaluation. |  [optional] [readonly] |
|**endTime** | **String** | Required. End time for the evaluation&#39;s analysis. |  [optional] |
|**metricLabels** | [**GoogleCloudApigeeV1CanaryEvaluationMetricLabels**](GoogleCloudApigeeV1CanaryEvaluationMetricLabels.md) |  |  [optional] |
|**name** | **String** | Output only. Name of the canary evalution. |  [optional] [readonly] |
|**startTime** | **String** | Required. Start time for the canary evaluation&#39;s analysis. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state of the canary evaluation. |  [optional] [readonly] |
|**treatment** | **String** | Required. The newer version that is serving requests. |  [optional] |
|**verdict** | [**VerdictEnum**](#VerdictEnum) | Output only. The resulting verdict of the canary evaluations: NONE, PASS, or FAIL. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |



## Enum: VerdictEnum

| Name | Value |
|---- | -----|
| VERDICT_UNSPECIFIED | &quot;VERDICT_UNSPECIFIED&quot; |
| NONE | &quot;NONE&quot; |
| FAIL | &quot;FAIL&quot; |
| PASS | &quot;PASS&quot; |



