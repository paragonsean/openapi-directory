# GoogleIdentityToolkitApi.VerifyCustomTokenResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiresIn** | **String** | If idToken is STS id token, then this field will be expiration time of STS id token in seconds. | [optional] 
**idToken** | **String** | The GITKit token for authenticated user. | [optional] 
**isNewUser** | **Boolean** | True if it&#39;s a new user sign-in, false if it&#39;s a returning user. | [optional] 
**kind** | **String** | The fixed string \&quot;identitytoolkit#VerifyCustomTokenResponse\&quot;. | [optional] [default to &#39;identitytoolkit#VerifyCustomTokenResponse&#39;]
**refreshToken** | **String** | If idToken is STS id token, then this field will be refresh token. | [optional] 


