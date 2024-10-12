# IdentityToolkitApi.GoogleCloudIdentitytoolkitV2PasswordPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedNonAlphanumericCharacters** | **[String]** | Output only. Allowed characters which satisfy the non_alphanumeric requirement. | [optional] [readonly] 
**customStrengthOptions** | [**GoogleCloudIdentitytoolkitV2CustomStrengthOptions**](GoogleCloudIdentitytoolkitV2CustomStrengthOptions.md) |  | [optional] 
**enforcementState** | **String** | Output only. Which enforcement mode to use for the password policy. | [optional] [readonly] 
**forceUpgradeOnSignin** | **Boolean** | Users must have a password compliant with the password policy to sign-in. | [optional] 
**schemaVersion** | **Number** | Output only. schema version number for the password policy | [optional] [readonly] 



## Enum: EnforcementStateEnum


* `ENFORCEMENT_STATE_UNSPECIFIED` (value: `"ENFORCEMENT_STATE_UNSPECIFIED"`)

* `false` (value: `"false"`)

* `ENFORCE` (value: `"ENFORCE"`)




