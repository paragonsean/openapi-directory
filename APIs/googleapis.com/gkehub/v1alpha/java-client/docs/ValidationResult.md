

# ValidationResult

ValidationResults are results set by each validator running during ValidateCreateMembership.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**result** | **String** | Additional information for the validation. |  [optional] |
|**success** | **Boolean** | Whether the validation is passed or not. |  [optional] |
|**validator** | [**ValidatorEnum**](#ValidatorEnum) | Validator type to validate membership with. |  [optional] |



## Enum: ValidatorEnum

| Name | Value |
|---- | -----|
| VALIDATOR_TYPE_UNSPECIFIED | &quot;VALIDATOR_TYPE_UNSPECIFIED&quot; |
| MEMBERSHIP_ID | &quot;MEMBERSHIP_ID&quot; |
| CROSS_PROJECT_PERMISSION | &quot;CROSS_PROJECT_PERMISSION&quot; |



