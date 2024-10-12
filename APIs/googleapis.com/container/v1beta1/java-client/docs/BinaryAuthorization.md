

# BinaryAuthorization

Configuration for Binary Authorization.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | **Boolean** | This field is deprecated. Leave this unset and instead configure BinaryAuthorization using evaluation_mode. If evaluation_mode is set to anything other than EVALUATION_MODE_UNSPECIFIED, this field is ignored. |  [optional] |
|**evaluationMode** | [**EvaluationModeEnum**](#EvaluationModeEnum) | Mode of operation for binauthz policy evaluation. If unspecified, defaults to DISABLED. |  [optional] |
|**policyBindings** | [**List&lt;PolicyBinding&gt;**](PolicyBinding.md) | Optional. Binauthz policies that apply to this cluster. |  [optional] |



## Enum: EvaluationModeEnum

| Name | Value |
|---- | -----|
| EVALUATION_MODE_UNSPECIFIED | &quot;EVALUATION_MODE_UNSPECIFIED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| PROJECT_SINGLETON_POLICY_ENFORCE | &quot;PROJECT_SINGLETON_POLICY_ENFORCE&quot; |
| POLICY_BINDINGS | &quot;POLICY_BINDINGS&quot; |
| POLICY_BINDINGS_AND_PROJECT_SINGLETON_POLICY_ENFORCE | &quot;POLICY_BINDINGS_AND_PROJECT_SINGLETON_POLICY_ENFORCE&quot; |



