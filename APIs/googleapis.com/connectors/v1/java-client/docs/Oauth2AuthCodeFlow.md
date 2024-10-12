

# Oauth2AuthCodeFlow

Parameters to support Oauth 2.0 Auth Code Grant Authentication. See https://www.rfc-editor.org/rfc/rfc6749#section-1.3.1 for more details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authCode** | **String** | Authorization code to be exchanged for access and refresh tokens. |  [optional] |
|**authUri** | **String** | Auth URL for Authorization Code Flow |  [optional] |
|**clientId** | **String** | Client ID for user-provided OAuth app. |  [optional] |
|**clientSecret** | [**Secret**](Secret.md) |  |  [optional] |
|**enablePkce** | **Boolean** | Whether to enable PKCE when the user performs the auth code flow. |  [optional] |
|**pkceVerifier** | **String** | PKCE verifier to be used during the auth code exchange. |  [optional] |
|**redirectUri** | **String** | Redirect URI to be provided during the auth code exchange. |  [optional] |
|**scopes** | **List&lt;String&gt;** | Scopes the connection will request when the user performs the auth code flow. |  [optional] |



