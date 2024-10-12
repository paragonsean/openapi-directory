

# FindAllGlobalAuthModules200ResponseInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adminPassword** | **String** | The admin password |  |
|**adminUsername** | **String** | The admin username |  |
|**desc** | **String** | Description of the config |  |
|**emailField** | **String** | Field name to get email from user profile |  |
|**groupFilter** | **String** | Filter for groups |  |
|**id** | **String** | Unique id of the config |  |
|**name** | **String** | Name of the config |  |
|**nameField** | **String** | Field name to get name from user profile |  |
|**otoroshiDataField** | **String** | Field name to get otoroshi metadata from. You can specify sub fields using | as separator |  |
|**searchBase** | **String** | LDAP search base |  |
|**searchFilter** | **String** | Filter for users |  |
|**serverUrl** | **String** | URL of the ldap server |  |
|**sessionMaxAge** | **Integer** | Max age of the session |  |
|**type** | **String** | Type of settings. value is oauth2 |  |
|**userBase** | **String** | LDAP user base DN |  |
|**users** | [**List&lt;InMemoryUser&gt;**](InMemoryUser.md) | List of users |  |
|**accessTokenField** | **String** | Field name to get access token |  |
|**authorizeUrl** | **String** | OAuth authorize URL |  |
|**callbackUrl** | **String** | Otoroshi callback URL |  |
|**claims** | **String** | The claims of the token |  [optional] |
|**clientId** | **String** | OAuth Client id |  |
|**clientSecret** | **String** | OAuth Client secret |  |
|**jwtVerifier** | [**GenericOauth2ModuleConfigJwtVerifier**](GenericOauth2ModuleConfigJwtVerifier.md) |  |  [optional] |
|**loginUrl** | **String** | OAuth login URL |  |
|**logoutUrl** | **String** | OAuth logout URL |  |
|**oidConfig** | **String** | URL of the OIDC config. file |  [optional] |
|**readProfileFromToken** | **Boolean** | The user profile will be read from the JWT token in id_token |  [optional] |
|**scope** | **String** | The scope of the token |  [optional] |
|**tokenUrl** | **String** | OAuth token URL |  |
|**useCookies** | **Boolean** | Use for redirection to actual service |  [optional] |
|**useJson** | **Boolean** | Use JSON or URL Form Encoded as payload with the OAuth provider |  [optional] |
|**userInfoUrl** | **String** | OAuth userinfo to get user profile |  |



