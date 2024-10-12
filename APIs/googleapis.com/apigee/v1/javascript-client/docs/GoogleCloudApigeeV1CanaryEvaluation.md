# ApigeeApi.GoogleCloudApigeeV1CanaryEvaluation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**control** | **String** | Required. The stable version that is serving requests. | [optional] 
**createTime** | **String** | Output only. Create time of the canary evaluation. | [optional] [readonly] 
**endTime** | **String** | Required. End time for the evaluation&#39;s analysis. | [optional] 
**metricLabels** | [**GoogleCloudApigeeV1CanaryEvaluationMetricLabels**](GoogleCloudApigeeV1CanaryEvaluationMetricLabels.md) |  | [optional] 
**name** | **String** | Output only. Name of the canary evalution. | [optional] [readonly] 
**startTime** | **String** | Required. Start time for the canary evaluation&#39;s analysis. | [optional] 
**state** | **String** | Output only. The current state of the canary evaluation. | [optional] [readonly] 
**treatment** | **String** | Required. The newer version that is serving requests. | [optional] 
**verdict** | **String** | Output only. The resulting verdict of the canary evaluations: NONE, PASS, or FAIL. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `RUNNING` (value: `"RUNNING"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)





## Enum: VerdictEnum


* `VERDICT_UNSPECIFIED` (value: `"VERDICT_UNSPECIFIED"`)

* `NONE` (value: `"NONE"`)

* `FAIL` (value: `"FAIL"`)

* `PASS` (value: `"PASS"`)




