# ServiceControlApi.ViolationInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkedValue** | **String** | Optional. Value that is being checked for the policy. This could be in encrypted form (if pii sensitive). This field will only be emitted in LIST_POLICY types | [optional] 
**constraint** | **String** | Optional. Constraint name | [optional] 
**errorMessage** | **String** | Optional. Error message that policy is indicating. | [optional] 
**policyType** | **String** | Optional. Indicates the type of the policy. | [optional] 



## Enum: PolicyTypeEnum


* `POLICY_TYPE_UNSPECIFIED` (value: `"POLICY_TYPE_UNSPECIFIED"`)

* `BOOLEAN_CONSTRAINT` (value: `"BOOLEAN_CONSTRAINT"`)

* `LIST_CONSTRAINT` (value: `"LIST_CONSTRAINT"`)

* `CUSTOM_CONSTRAINT` (value: `"CUSTOM_CONSTRAINT"`)




