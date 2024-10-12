# IdentityToolkitApi.GoogleCloudIdentitytoolkitAdminV2PasswordPolicyConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forceUpgradeOnSignin** | **Boolean** | Users must have a password compliant with the password policy to sign-in. | [optional] 
**lastUpdateTime** | **String** | Output only. The last time the password policy on the project was updated. | [optional] [readonly] 
**passwordPolicyEnforcementState** | **String** | Which enforcement mode to use for the password policy. | [optional] 
**passwordPolicyVersions** | [**[GoogleCloudIdentitytoolkitAdminV2PasswordPolicyVersion]**](GoogleCloudIdentitytoolkitAdminV2PasswordPolicyVersion.md) | Must be of length 1. Contains the strength attributes for the password policy. | [optional] 



## Enum: PasswordPolicyEnforcementStateEnum


* `PASSWORD_POLICY_ENFORCEMENT_STATE_UNSPECIFIED` (value: `"PASSWORD_POLICY_ENFORCEMENT_STATE_UNSPECIFIED"`)

* `false` (value: `"false"`)

* `ENFORCE` (value: `"ENFORCE"`)




