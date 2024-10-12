

# IdentitytoolkitRelyingpartySetAccountInfoRequest

Request to set the account information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**captchaChallenge** | **String** | The captcha challenge. |  [optional] |
|**captchaResponse** | **String** | Response to the captcha. |  [optional] |
|**createdAt** | **String** | The timestamp when the account is created. |  [optional] |
|**customAttributes** | **String** | The custom attributes to be set in the user&#39;s id token. |  [optional] |
|**delegatedProjectNumber** | **String** | GCP project number of the requesting delegated app. Currently only intended for Firebase V1 migration. |  [optional] |
|**deleteAttribute** | **List&lt;String&gt;** | The attributes users request to delete. |  [optional] |
|**deleteProvider** | **List&lt;String&gt;** | The IDPs the user request to delete. |  [optional] |
|**disableUser** | **Boolean** | Whether to disable the user. |  [optional] |
|**displayName** | **String** | The name of the user. |  [optional] |
|**email** | **String** | The email of the user. |  [optional] |
|**emailVerified** | **Boolean** | Mark the email as verified or not. |  [optional] |
|**idToken** | **String** | The GITKit token of the authenticated user. |  [optional] |
|**instanceId** | **String** | Instance id token of the app. |  [optional] |
|**lastLoginAt** | **String** | Last login timestamp. |  [optional] |
|**localId** | **String** | The local ID of the user. |  [optional] |
|**oobCode** | **String** | The out-of-band code of the change email request. |  [optional] |
|**password** | **String** | The new password of the user. |  [optional] |
|**phoneNumber** | **String** | Privileged caller can update user with specified phone number. |  [optional] |
|**photoUrl** | **String** | The photo url of the user. |  [optional] |
|**provider** | **List&lt;String&gt;** | The associated IDPs of the user. |  [optional] |
|**returnSecureToken** | **Boolean** | Whether return sts id token and refresh token instead of gitkit token. |  [optional] |
|**upgradeToFederatedLogin** | **Boolean** | Mark the user to upgrade to federated login. |  [optional] |
|**validSince** | **String** | Timestamp in seconds for valid login token. |  [optional] |



