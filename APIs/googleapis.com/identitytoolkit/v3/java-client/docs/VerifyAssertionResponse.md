

# VerifyAssertionResponse

Response of verifying the IDP assertion.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | **String** | The action code. |  [optional] |
|**appInstallationUrl** | **String** | URL for OTA app installation. |  [optional] |
|**appScheme** | **String** | The custom scheme used by mobile app. |  [optional] |
|**context** | **String** | The opaque value used by the client to maintain context info between the authentication request and the IDP callback. |  [optional] |
|**dateOfBirth** | **String** | The birth date of the IdP account. |  [optional] |
|**displayName** | **String** | The display name of the user. |  [optional] |
|**email** | **String** | The email returned by the IdP. NOTE: The federated login user may not own the email. |  [optional] |
|**emailRecycled** | **Boolean** | It&#39;s true if the email is recycled. |  [optional] |
|**emailVerified** | **Boolean** | The value is true if the IDP is also the email provider. It means the user owns the email. |  [optional] |
|**errorMessage** | **String** | Client error code. |  [optional] |
|**expiresIn** | **String** | If idToken is STS id token, then this field will be expiration time of STS id token in seconds. |  [optional] |
|**federatedId** | **String** | The unique ID identifies the IdP account. |  [optional] |
|**firstName** | **String** | The first name of the user. |  [optional] |
|**fullName** | **String** | The full name of the user. |  [optional] |
|**idToken** | **String** | The ID token. |  [optional] |
|**inputEmail** | **String** | It&#39;s the identifier param in the createAuthUri request if the identifier is an email. It can be used to check whether the user input email is different from the asserted email. |  [optional] |
|**isNewUser** | **Boolean** | True if it&#39;s a new user sign-in, false if it&#39;s a returning user. |  [optional] |
|**kind** | **String** | The fixed string \&quot;identitytoolkit#VerifyAssertionResponse\&quot;. |  [optional] |
|**language** | **String** | The language preference of the user. |  [optional] |
|**lastName** | **String** | The last name of the user. |  [optional] |
|**localId** | **String** | The RP local ID if it&#39;s already been mapped to the IdP account identified by the federated ID. |  [optional] |
|**needConfirmation** | **Boolean** | Whether the assertion is from a non-trusted IDP and need account linking confirmation. |  [optional] |
|**needEmail** | **Boolean** | Whether need client to supply email to complete the federated login flow. |  [optional] |
|**nickName** | **String** | The nick name of the user. |  [optional] |
|**oauthAccessToken** | **String** | The OAuth2 access token. |  [optional] |
|**oauthAuthorizationCode** | **String** | The OAuth2 authorization code. |  [optional] |
|**oauthExpireIn** | **Integer** | The lifetime in seconds of the OAuth2 access token. |  [optional] |
|**oauthIdToken** | **String** | The OIDC id token. |  [optional] |
|**oauthRequestToken** | **String** | The user approved request token for the OpenID OAuth extension. |  [optional] |
|**oauthScope** | **String** | The scope for the OpenID OAuth extension. |  [optional] |
|**oauthTokenSecret** | **String** | The OAuth1 access token secret. |  [optional] |
|**originalEmail** | **String** | The original email stored in the mapping storage. It&#39;s returned when the federated ID is associated to a different email. |  [optional] |
|**photoUrl** | **String** | The URI of the public accessible profiel picture. |  [optional] |
|**providerId** | **String** | The IdP ID. For white listed IdPs it&#39;s a short domain name e.g. google.com, aol.com, live.net and yahoo.com. If the \&quot;providerId\&quot; param is set to OpenID OP identifer other than the whilte listed IdPs the OP identifier is returned. If the \&quot;identifier\&quot; param is federated ID in the createAuthUri request. The domain part of the federated ID is returned. |  [optional] |
|**rawUserInfo** | **String** | Raw IDP-returned user info. |  [optional] |
|**refreshToken** | **String** | If idToken is STS id token, then this field will be refresh token. |  [optional] |
|**screenName** | **String** | The screen_name of a Twitter user or the login name at Github. |  [optional] |
|**timeZone** | **String** | The timezone of the user. |  [optional] |
|**verifiedProvider** | **List&lt;String&gt;** | When action is &#39;map&#39;, contains the idps which can be used for confirmation. |  [optional] |



