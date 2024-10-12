

# IdentityProviderContractProperties

The external Identity Providers like Facebook, Google, Microsoft, Twitter or Azure Active Directory which can be used to enable access to the API Management service developer portal for all users.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientId** | **String** | Client Id of the Application in the external Identity Provider. It is App ID for Facebook login, Client ID for Google login, App ID for Microsoft. |  |
|**clientSecret** | **String** | Client secret of the Application in external Identity Provider, used to authenticate login request. For example, it is App Secret for Facebook login, API Key for Google login, Public Key for Microsoft. |  |
|**allowedTenants** | **List&lt;String&gt;** | List of Allowed Tenants when configuring Azure Active Directory login. |  [optional] |
|**passwordResetPolicyName** | **String** | Password Reset Policy Name. Only applies to AAD B2C Identity Provider. |  [optional] |
|**profileEditingPolicyName** | **String** | Profile Editing Policy Name. Only applies to AAD B2C Identity Provider. |  [optional] |
|**signinPolicyName** | **String** | Signin Policy Name. Only applies to AAD B2C Identity Provider. |  [optional] |
|**signupPolicyName** | **String** | Signup Policy Name. Only applies to AAD B2C Identity Provider. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Identity Provider Type identifier. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| FACEBOOK | &quot;facebook&quot; |
| GOOGLE | &quot;google&quot; |
| MICROSOFT | &quot;microsoft&quot; |
| TWITTER | &quot;twitter&quot; |
| AAD | &quot;aad&quot; |
| AAD_B2_C | &quot;aadB2C&quot; |



