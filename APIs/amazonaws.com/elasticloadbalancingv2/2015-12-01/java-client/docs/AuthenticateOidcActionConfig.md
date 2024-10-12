

# AuthenticateOidcActionConfig

Request parameters when using an identity provider (IdP) that is compliant with OpenID Connect (OIDC) to authenticate users.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**issuer** | [**String**](String.md) |  |  |
|**authorizationEndpoint** | [**String**](String.md) |  |  |
|**tokenEndpoint** | [**String**](String.md) |  |  |
|**userInfoEndpoint** | [**String**](String.md) |  |  |
|**clientId** | [**String**](String.md) |  |  |
|**clientSecret** | [**String**](String.md) |  |  [optional] |
|**sessionCookieName** | [**String**](String.md) |  |  [optional] |
|**scope** | [**String**](String.md) |  |  [optional] |
|**sessionTimeout** | [**Integer**](Integer.md) |  |  [optional] |
|**authenticationRequestExtraParams** | [**Map**](Map.md) |  |  [optional] |
|**onUnauthenticatedRequest** | [**AuthenticateOidcActionConditionalBehaviorEnum**](AuthenticateOidcActionConditionalBehaviorEnum.md) |  |  [optional] |
|**useExistingClientSecret** | [**Boolean**](Boolean.md) |  |  [optional] |



