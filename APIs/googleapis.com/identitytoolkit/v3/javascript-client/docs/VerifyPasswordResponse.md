# GoogleIdentityToolkitApi.VerifyPasswordResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | The name of the user. | [optional] 
**email** | **String** | The email returned by the IdP. NOTE: The federated login user may not own the email. | [optional] 
**expiresIn** | **String** | If idToken is STS id token, then this field will be expiration time of STS id token in seconds. | [optional] 
**idToken** | **String** | The GITKit token for authenticated user. | [optional] 
**kind** | **String** | The fixed string \&quot;identitytoolkit#VerifyPasswordResponse\&quot;. | [optional] [default to &#39;identitytoolkit#VerifyPasswordResponse&#39;]
**localId** | **String** | The RP local ID if it&#39;s already been mapped to the IdP account identified by the federated ID. | [optional] 
**oauthAccessToken** | **String** | The OAuth2 access token. | [optional] 
**oauthAuthorizationCode** | **String** | The OAuth2 authorization code. | [optional] 
**oauthExpireIn** | **Number** | The lifetime in seconds of the OAuth2 access token. | [optional] 
**photoUrl** | **String** | The URI of the user&#39;s photo at IdP | [optional] 
**refreshToken** | **String** | If idToken is STS id token, then this field will be refresh token. | [optional] 
**registered** | **Boolean** | Whether the email is registered. | [optional] 


