# TwilioOauth.OauthV1OpenidDiscovery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizationEndpoint** | **String** | The endpoint that validates all authorization requests. | [optional] 
**claimsSupported** | **[String]** | A collection of claims supported by authorization server for identity token | [optional] 
**deviceAuthorizationEndpoint** | **String** | The endpoint that validates all device code related authorization requests. | [optional] 
**idTokenSigningAlgValuesSupported** | **[String]** | A collection of JWS signing algorithms supported by authorization server to sign identity token. | [optional] 
**issuer** | **String** | The URL of the party that will create the token and sign it with its private key. | [optional] 
**jwkUri** | **String** | The URL of your JSON Web Key Set. This set is a collection of JSON Web Keys, a standard method for representing cryptographic keys in a JSON structure. | [optional] 
**responseTypeSupported** | **[String]** | A collection of response type supported by authorization server. | [optional] 
**revocationEndpoint** | **String** | The endpoint used to revoke access or refresh tokens issued by the authorization server. | [optional] 
**scopesSupported** | **[String]** | A collection of scopes supported by authorization server for identity token | [optional] 
**subjectTypeSupported** | **[String]** | A collection of subject by authorization server. | [optional] 
**tokenEndpoint** | **String** | The URL of the token endpoint. After a client has received an authorization code, that code is presented to the token endpoint and exchanged for an identity token, an access token, and a refresh token. | [optional] 
**url** | **String** |  | [optional] 
**userinfoEndpoint** | **String** | The URL of the user info endpoint, which returns user profile information to a client. Keep in mind that the user info endpoint returns only the information that has been requested. | [optional] 


