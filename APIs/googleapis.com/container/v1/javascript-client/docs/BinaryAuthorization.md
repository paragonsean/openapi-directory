# KubernetesEngineApi.BinaryAuthorization

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **Boolean** | This field is deprecated. Leave this unset and instead configure BinaryAuthorization using evaluation_mode. If evaluation_mode is set to anything other than EVALUATION_MODE_UNSPECIFIED, this field is ignored. | [optional] 
**evaluationMode** | **String** | Mode of operation for binauthz policy evaluation. If unspecified, defaults to DISABLED. | [optional] 



## Enum: EvaluationModeEnum


* `EVALUATION_MODE_UNSPECIFIED` (value: `"EVALUATION_MODE_UNSPECIFIED"`)

* `DISABLED` (value: `"DISABLED"`)

* `PROJECT_SINGLETON_POLICY_ENFORCE` (value: `"PROJECT_SINGLETON_POLICY_ENFORCE"`)




