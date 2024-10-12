

# IdentityServiceAuthMethod

Configuration of an auth method for a member/cluster. Only one authentication method (e.g., OIDC and LDAP) can be set per AuthMethod.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**azureadConfig** | [**IdentityServiceAzureADConfig**](IdentityServiceAzureADConfig.md) |  |  [optional] |
|**googleConfig** | [**IdentityServiceGoogleConfig**](IdentityServiceGoogleConfig.md) |  |  [optional] |
|**name** | **String** | Identifier for auth config. |  [optional] |
|**oidcConfig** | [**IdentityServiceOidcConfig**](IdentityServiceOidcConfig.md) |  |  [optional] |
|**proxy** | **String** | Proxy server address to use for auth method. |  [optional] |



