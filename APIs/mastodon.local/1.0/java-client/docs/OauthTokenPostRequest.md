

# OauthTokenPostRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientId** | **String** | Client ID, obtained during app registration |  |
|**clientSecret** | **String** | Client secret, obtained during app registration |  |
|**code** | **String** | A user authorization code, obtained via /oauth/authorize |  [optional] |
|**grantType** | **String** | Set equal to authorization_code if code is provided in order to gain user-level access. Otherwise, set equal to client_credentials to obtain app-level access only. |  |
|**redirectUri** | **String** | Set a URI to redirect the user to. If this parameter is set to urn:ietf:wg:oauth:2.0:oob then the token will be shown instead. Must match one of the redirect URIs declared during app registration. |  |
|**scopes** | **String** | List of requested OAuth scopes, separated by spaces. Must be a subset of scopes declared during app registration. If not provided, defaults to read. |  [optional] |



