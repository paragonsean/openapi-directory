# ApiManagementClient.IdentityProviderUpdateProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientId** | **String** | Client Id of the Application in the external Identity Provider. It is App ID for Facebook login, Client ID for Google login, App ID for Microsoft. | [optional] 
**clientSecret** | **String** | Client secret of the Application in external Identity Provider, used to authenticate login request. For example, it is App Secret for Facebook login, API Key for Google login, Public Key for Microsoft. | [optional] 
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




