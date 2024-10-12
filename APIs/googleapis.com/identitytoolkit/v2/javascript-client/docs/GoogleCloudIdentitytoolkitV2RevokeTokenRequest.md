# IdentityToolkitApi.GoogleCloudIdentitytoolkitV2RevokeTokenRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idToken** | **String** | Required. A valid Identity Platform ID token to link the account. If there was a successful token revocation request on the account and no tokens are generated after the revocation, the duplicate requests will be ignored and returned immediately. | [optional] 
**providerId** | **String** | Required. The idp provider for the token. Currently only supports Apple Idp. The format should be \&quot;apple.com\&quot;. | [optional] 
**redirectUri** | **String** | The redirect URI provided in the initial authorization request made by the client to the IDP. The URI must use the HTTPS protocol, include a domain name, and can&#39;t contain an IP address or localhost. Required if token_type is CODE. | [optional] 
**tenantId** | **String** | The ID of the Identity Platform tenant the user is signing in to. If not set, the user will sign in to the default Identity Platform project. | [optional] 
**token** | **String** | Required. The token to be revoked. If an authorization_code is passed in, the API will first exchange the code for access token and then revoke the token exchanged. | [optional] 
**tokenType** | **String** | Required. The type of the token to be revoked. | [optional] 



## Enum: TokenTypeEnum


* `TOKEN_TYPE_UNSPECIFIED` (value: `"TOKEN_TYPE_UNSPECIFIED"`)

* `REFRESH_TOKEN` (value: `"REFRESH_TOKEN"`)

* `ACCESS_TOKEN` (value: `"ACCESS_TOKEN"`)

* `CODE` (value: `"CODE"`)




