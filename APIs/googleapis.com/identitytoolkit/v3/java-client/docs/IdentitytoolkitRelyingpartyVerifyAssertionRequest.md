

# IdentitytoolkitRelyingpartyVerifyAssertionRequest

Request to verify the IDP assertion.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoCreate** | **Boolean** | When it&#39;s true, automatically creates a new account if the user doesn&#39;t exist. When it&#39;s false, allows existing user to sign in normally and throws exception if the user doesn&#39;t exist. |  [optional] |
|**delegatedProjectNumber** | **String** | GCP project number of the requesting delegated app. Currently only intended for Firebase V1 migration. |  [optional] |
|**idToken** | **String** | The GITKit token of the authenticated user. |  [optional] |
|**instanceId** | **String** | Instance id token of the app. |  [optional] |
|**pendingIdToken** | **String** | The GITKit token for the non-trusted IDP pending to be confirmed by the user. |  [optional] |
|**postBody** | **String** | The post body if the request is a HTTP POST. |  [optional] |
|**requestUri** | **String** | The URI to which the IDP redirects the user back. It may contain federated login result params added by the IDP. |  [optional] |
|**returnIdpCredential** | **Boolean** | Whether return 200 and IDP credential rather than throw exception when federated id is already linked. |  [optional] |
|**returnRefreshToken** | **Boolean** | Whether to return refresh tokens. |  [optional] |
|**returnSecureToken** | **Boolean** | Whether return sts id token and refresh token instead of gitkit token. |  [optional] |
|**sessionId** | **String** | Session ID, which should match the one in previous createAuthUri request. |  [optional] |
|**tenantId** | **String** | For multi-tenant use cases, in order to construct sign-in URL with the correct IDP parameters, Firebear needs to know which Tenant to retrieve IDP configs from. |  [optional] |
|**tenantProjectNumber** | **String** | Tenant project number to be used for idp discovery. |  [optional] |



