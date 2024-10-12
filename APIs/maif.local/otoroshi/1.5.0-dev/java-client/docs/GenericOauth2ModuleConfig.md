

# GenericOauth2ModuleConfig

Settings to authenticate users using a generic OAuth2 provider

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessTokenField** | **String** | Field name to get access token |  |
|**authorizeUrl** | **String** | OAuth authorize URL |  |
|**callbackUrl** | **String** | Otoroshi callback URL |  |
|**claims** | **String** | The claims of the token |  [optional] |
|**clientId** | **String** | OAuth Client id |  |
|**clientSecret** | **String** | OAuth Client secret |  |
|**desc** | **String** | Description of the config |  |
|**emailField** | **String** | Field name to get email from user profile |  |
|**id** | **String** | Unique id of the config |  |
|**jwtVerifier** | [**GenericOauth2ModuleConfigJwtVerifier**](GenericOauth2ModuleConfigJwtVerifier.md) |  |  [optional] |
|**loginUrl** | **String** | OAuth login URL |  |
|**logoutUrl** | **String** | OAuth logout URL |  |
|**name** | **String** | Name of the config |  |
|**nameField** | **String** | Field name to get name from user profile |  |
|**oidConfig** | **String** | URL of the OIDC config. file |  [optional] |
|**otoroshiDataField** | **String** | Field name to get otoroshi metadata from. You can specify sub fields using | as separator |  |
|**readProfileFromToken** | **Boolean** | The user profile will be read from the JWT token in id_token |  [optional] |
|**scope** | **String** | The scope of the token |  [optional] |
|**sessionMaxAge** | **Integer** | Max age of the session |  |
|**tokenUrl** | **String** | OAuth token URL |  |
|**type** | **String** | Type of settings. value is oauth2 |  |
|**useCookies** | **Boolean** | Use for redirection to actual service |  [optional] |
|**useJson** | **Boolean** | Use JSON or URL Form Encoded as payload with the OAuth provider |  [optional] |
|**userInfoUrl** | **String** | OAuth userinfo to get user profile |  |



