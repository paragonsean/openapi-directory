

# IdentityProviderBaseParameters

Identity Provider Base Parameter Properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
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



