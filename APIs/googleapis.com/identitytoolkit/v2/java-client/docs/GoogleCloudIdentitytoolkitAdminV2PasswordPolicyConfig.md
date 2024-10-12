

# GoogleCloudIdentitytoolkitAdminV2PasswordPolicyConfig

The configuration for the password policy on the project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**forceUpgradeOnSignin** | **Boolean** | Users must have a password compliant with the password policy to sign-in. |  [optional] |
|**lastUpdateTime** | **String** | Output only. The last time the password policy on the project was updated. |  [optional] [readonly] |
|**passwordPolicyEnforcementState** | [**PasswordPolicyEnforcementStateEnum**](#PasswordPolicyEnforcementStateEnum) | Which enforcement mode to use for the password policy. |  [optional] |
|**passwordPolicyVersions** | [**List&lt;GoogleCloudIdentitytoolkitAdminV2PasswordPolicyVersion&gt;**](GoogleCloudIdentitytoolkitAdminV2PasswordPolicyVersion.md) | Must be of length 1. Contains the strength attributes for the password policy. |  [optional] |



## Enum: PasswordPolicyEnforcementStateEnum

| Name | Value |
|---- | -----|
| PASSWORD_POLICY_ENFORCEMENT_STATE_UNSPECIFIED | &quot;PASSWORD_POLICY_ENFORCEMENT_STATE_UNSPECIFIED&quot; |
| FALSE | &quot;false&quot; |
| ENFORCE | &quot;ENFORCE&quot; |



