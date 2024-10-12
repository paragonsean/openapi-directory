# OsConfigApi.OSPolicyResourceConfigStep

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorMessage** | **String** | An error message recorded during the execution of this step. Only populated when outcome is FAILED. | [optional] 
**outcome** | **String** | Outcome of the configuration step. | [optional] 
**type** | **String** | Configuration step type. | [optional] 



## Enum: OutcomeEnum


* `OUTCOME_UNSPECIFIED` (value: `"OUTCOME_UNSPECIFIED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `VALIDATION` (value: `"VALIDATION"`)

* `DESIRED_STATE_CHECK` (value: `"DESIRED_STATE_CHECK"`)

* `DESIRED_STATE_ENFORCEMENT` (value: `"DESIRED_STATE_ENFORCEMENT"`)

* `DESIRED_STATE_CHECK_POST_ENFORCEMENT` (value: `"DESIRED_STATE_CHECK_POST_ENFORCEMENT"`)




