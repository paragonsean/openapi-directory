

# BinaryAuthorizationConfig

BinaryAuthorizationConfig defines the fleet level configuration of binary authorization feature.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**evaluationMode** | [**EvaluationModeEnum**](#EvaluationModeEnum) | Optional. Mode of operation for binauthz policy evaluation. |  [optional] |
|**policyBindings** | [**List&lt;PolicyBinding&gt;**](PolicyBinding.md) | Optional. Binauthz policies that apply to this cluster. |  [optional] |



## Enum: EvaluationModeEnum

| Name | Value |
|---- | -----|
| EVALUATION_MODE_UNSPECIFIED | &quot;EVALUATION_MODE_UNSPECIFIED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| POLICY_BINDINGS | &quot;POLICY_BINDINGS&quot; |



