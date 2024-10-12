# ConnectorsApi.Oauth2AuthCodeFlow

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authCode** | **String** | Authorization code to be exchanged for access and refresh tokens. | [optional] 
**authUri** | **String** | Auth URL for Authorization Code Flow | [optional] 
**clientId** | **String** | Client ID for user-provided OAuth app. | [optional] 
**clientSecret** | [**Secret**](Secret.md) |  | [optional] 
**enablePkce** | **Boolean** | Whether to enable PKCE when the user performs the auth code flow. | [optional] 
**pkceVerifier** | **String** | PKCE verifier to be used during the auth code exchange. | [optional] 
**redirectUri** | **String** | Redirect URI to be provided during the auth code exchange. | [optional] 
**scopes** | **[String]** | Scopes the connection will request when the user performs the auth code flow. | [optional] 


