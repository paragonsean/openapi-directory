

# UserInfo

Template for an individual account info.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **String** | User creation timestamp. |  [optional] |
|**customAttributes** | **String** | The custom attributes to be set in the user&#39;s id token. |  [optional] |
|**customAuth** | **Boolean** | Whether the user is authenticated by the developer. |  [optional] |
|**disabled** | **Boolean** | Whether the user is disabled. |  [optional] |
|**displayName** | **String** | The name of the user. |  [optional] |
|**email** | **String** | The email of the user. |  [optional] |
|**emailVerified** | **Boolean** | Whether the email has been verified. |  [optional] |
|**lastLoginAt** | **String** | last login timestamp. |  [optional] |
|**localId** | **String** | The local ID of the user. |  [optional] |
|**passwordHash** | **byte[]** | The user&#39;s hashed password. |  [optional] |
|**passwordUpdatedAt** | **Double** | The timestamp when the password was last updated. |  [optional] |
|**phoneNumber** | **String** | User&#39;s phone number. |  [optional] |
|**photoUrl** | **String** | The URL of the user profile photo. |  [optional] |
|**providerUserInfo** | [**List&lt;UserInfoProviderUserInfoInner&gt;**](UserInfoProviderUserInfoInner.md) | The IDP of the user. |  [optional] |
|**rawPassword** | **String** | The user&#39;s plain text password. |  [optional] |
|**salt** | **byte[]** | The user&#39;s password salt. |  [optional] |
|**screenName** | **String** | User&#39;s screen name at Twitter or login name at Github. |  [optional] |
|**validSince** | **String** | Timestamp in seconds for valid login token. |  [optional] |
|**version** | **Integer** | Version of the user&#39;s password. |  [optional] |



