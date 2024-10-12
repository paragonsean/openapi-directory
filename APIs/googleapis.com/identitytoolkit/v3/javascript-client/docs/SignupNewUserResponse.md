# GoogleIdentityToolkitApi.SignupNewUserResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | The name of the user. | [optional] 
**email** | **String** | The email of the user. | [optional] 
**expiresIn** | **String** | If idToken is STS id token, then this field will be expiration time of STS id token in seconds. | [optional] 
**idToken** | **String** | The Gitkit id token to login the newly sign up user. | [optional] 
**kind** | **String** | The fixed string \&quot;identitytoolkit#SignupNewUserResponse\&quot;. | [optional] [default to &#39;identitytoolkit#SignupNewUserResponse&#39;]
**localId** | **String** | The RP local ID of the user. | [optional] 
**refreshToken** | **String** | If idToken is STS id token, then this field will be refresh token. | [optional] 


