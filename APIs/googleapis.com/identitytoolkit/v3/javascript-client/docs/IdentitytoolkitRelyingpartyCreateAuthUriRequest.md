# GoogleIdentityToolkitApi.IdentitytoolkitRelyingpartyCreateAuthUriRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appId** | **String** | The app ID of the mobile app, base64(CERT_SHA1):PACKAGE_NAME for Android, BUNDLE_ID for iOS. | [optional] 
**authFlowType** | **String** | Explicitly specify the auth flow type. Currently only support \&quot;CODE_FLOW\&quot; type. The field is only used for Google provider. | [optional] 
**clientId** | **String** | The relying party OAuth client ID. | [optional] 
**context** | **String** | The opaque value used by the client to maintain context info between the authentication request and the IDP callback. | [optional] 
**continueUri** | **String** | The URI to which the IDP redirects the user after the federated login flow. | [optional] 
**customParameter** | **{String: String}** | The query parameter that client can customize by themselves in auth url. The following parameters are reserved for server so that they cannot be customized by clients: client_id, response_type, scope, redirect_uri, state, oauth_token. | [optional] 
**hostedDomain** | **String** | The hosted domain to restrict sign-in to accounts at that domain for Google Apps hosted accounts. | [optional] 
**identifier** | **String** | The email or federated ID of the user. | [optional] 
**oauthConsumerKey** | **String** | The developer&#39;s consumer key for OpenId OAuth Extension | [optional] 
**oauthScope** | **String** | Additional oauth scopes, beyond the basid user profile, that the user would be prompted to grant | [optional] 
**openidRealm** | **String** | Optional realm for OpenID protocol. The sub string \&quot;scheme://domain:port\&quot; of the param \&quot;continueUri\&quot; is used if this is not set. | [optional] 
**otaApp** | **String** | The native app package for OTA installation. | [optional] 
**providerId** | **String** | The IdP ID. For white listed IdPs it&#39;s a short domain name e.g. google.com, aol.com, live.net and yahoo.com. For other OpenID IdPs it&#39;s the OP identifier. | [optional] 
**sessionId** | **String** | The session_id passed by client. | [optional] 
**tenantId** | **String** | For multi-tenant use cases, in order to construct sign-in URL with the correct IDP parameters, Firebear needs to know which Tenant to retrieve IDP configs from. | [optional] 
**tenantProjectNumber** | **String** | Tenant project number to be used for idp discovery. | [optional] 


