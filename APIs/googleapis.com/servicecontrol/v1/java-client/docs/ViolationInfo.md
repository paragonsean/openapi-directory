

# ViolationInfo

Provides information about the Policy violation info for this request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkedValue** | **String** | Optional. Value that is being checked for the policy. This could be in encrypted form (if pii sensitive). This field will only be emitted in LIST_POLICY types |  [optional] |
|**constraint** | **String** | Optional. Constraint name |  [optional] |
|**errorMessage** | **String** | Optional. Error message that policy is indicating. |  [optional] |
|**policyType** | [**PolicyTypeEnum**](#PolicyTypeEnum) | Optional. Indicates the type of the policy. |  [optional] |



## Enum: PolicyTypeEnum

| Name | Value |
|---- | -----|
| POLICY_TYPE_UNSPECIFIED | &quot;POLICY_TYPE_UNSPECIFIED&quot; |
| BOOLEAN_CONSTRAINT | &quot;BOOLEAN_CONSTRAINT&quot; |
| LIST_CONSTRAINT | &quot;LIST_CONSTRAINT&quot; |
| CUSTOM_CONSTRAINT | &quot;CUSTOM_CONSTRAINT&quot; |



