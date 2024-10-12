

# GoogleCloudIdentitytoolkitV2PasswordPolicy

Configuration for password policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedNonAlphanumericCharacters** | **List&lt;String&gt;** | Output only. Allowed characters which satisfy the non_alphanumeric requirement. |  [optional] [readonly] |
|**customStrengthOptions** | [**GoogleCloudIdentitytoolkitV2CustomStrengthOptions**](GoogleCloudIdentitytoolkitV2CustomStrengthOptions.md) |  |  [optional] |
|**enforcementState** | [**EnforcementStateEnum**](#EnforcementStateEnum) | Output only. Which enforcement mode to use for the password policy. |  [optional] [readonly] |
|**forceUpgradeOnSignin** | **Boolean** | Users must have a password compliant with the password policy to sign-in. |  [optional] |
|**schemaVersion** | **Integer** | Output only. schema version number for the password policy |  [optional] [readonly] |



## Enum: EnforcementStateEnum

| Name | Value |
|---- | -----|
| ENFORCEMENT_STATE_UNSPECIFIED | &quot;ENFORCEMENT_STATE_UNSPECIFIED&quot; |
| FALSE | &quot;false&quot; |
| ENFORCE | &quot;ENFORCE&quot; |



