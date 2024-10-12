# ApiManagementClient.IdentityProviderBaseParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedTenants** | **[String]** | List of Allowed Tenants when configuring Azure Active Directory login. | [optional] 
**passwordResetPolicyName** | **String** | Password Reset Policy Name. Only applies to AAD B2C Identity Provider. | [optional] 
**profileEditingPolicyName** | **String** | Profile Editing Policy Name. Only applies to AAD B2C Identity Provider. | [optional] 
**signinPolicyName** | **String** | Signin Policy Name. Only applies to AAD B2C Identity Provider. | [optional] 
**signupPolicyName** | **String** | Signup Policy Name. Only applies to AAD B2C Identity Provider. | [optional] 
**type** | **String** | Identity Provider Type identifier. | [optional] 



## Enum: TypeEnum


* `facebook` (value: `"facebook"`)

* `google` (value: `"google"`)

* `microsoft` (value: `"microsoft"`)

* `twitter` (value: `"twitter"`)

* `aad` (value: `"aad"`)

* `aadB2C` (value: `"aadB2C"`)




