

# SetAccountInfoResponse

Respone of setting the account information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | The name of the user. |  [optional] |
|**email** | **String** | The email of the user. |  [optional] |
|**emailVerified** | **Boolean** | If email has been verified. |  [optional] |
|**expiresIn** | **String** | If idToken is STS id token, then this field will be expiration time of STS id token in seconds. |  [optional] |
|**idToken** | **String** | The Gitkit id token to login the newly sign up user. |  [optional] |
|**kind** | **String** | The fixed string \&quot;identitytoolkit#SetAccountInfoResponse\&quot;. |  [optional] |
|**localId** | **String** | The local ID of the user. |  [optional] |
|**newEmail** | **String** | The new email the user attempts to change to. |  [optional] |
|**passwordHash** | **byte[]** | The user&#39;s hashed password. |  [optional] |
|**photoUrl** | **String** | The photo url of the user. |  [optional] |
|**providerUserInfo** | [**List&lt;SetAccountInfoResponseProviderUserInfoInner&gt;**](SetAccountInfoResponseProviderUserInfoInner.md) | The user&#39;s profiles at the associated IdPs. |  [optional] |
|**refreshToken** | **String** | If idToken is STS id token, then this field will be refresh token. |  [optional] |



