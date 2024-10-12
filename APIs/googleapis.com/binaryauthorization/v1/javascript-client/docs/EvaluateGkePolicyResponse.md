# BinaryAuthorizationApi.EvaluateGkePolicyResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**[PodResult]**](PodResult.md) | Evaluation result for each Pod contained in the request. | [optional] 
**verdict** | **String** | The result of evaluating all Pods in the request. | [optional] 



## Enum: VerdictEnum


* `VERDICT_UNSPECIFIED` (value: `"VERDICT_UNSPECIFIED"`)

* `CONFORMANT` (value: `"CONFORMANT"`)

* `NON_CONFORMANT` (value: `"NON_CONFORMANT"`)

* `ERROR` (value: `"ERROR"`)




