

# EvaluateGkePolicyResponse

Response message for PlatformPolicyEvaluationService.EvaluateGkePolicy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**results** | [**List&lt;PodResult&gt;**](PodResult.md) | Evaluation result for each Pod contained in the request. |  [optional] |
|**verdict** | [**VerdictEnum**](#VerdictEnum) | The result of evaluating all Pods in the request. |  [optional] |



## Enum: VerdictEnum

| Name | Value |
|---- | -----|
| VERDICT_UNSPECIFIED | &quot;VERDICT_UNSPECIFIED&quot; |
| CONFORMANT | &quot;CONFORMANT&quot; |
| NON_CONFORMANT | &quot;NON_CONFORMANT&quot; |
| ERROR | &quot;ERROR&quot; |



