

# OauthV1OpenidDiscovery


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationEndpoint** | **URI** | The endpoint that validates all authorization requests. |  [optional] |
|**claimsSupported** | **List&lt;String&gt;** | A collection of claims supported by authorization server for identity token |  [optional] |
|**deviceAuthorizationEndpoint** | **URI** | The endpoint that validates all device code related authorization requests. |  [optional] |
|**idTokenSigningAlgValuesSupported** | **List&lt;String&gt;** | A collection of JWS signing algorithms supported by authorization server to sign identity token. |  [optional] |
|**issuer** | **URI** | The URL of the party that will create the token and sign it with its private key. |  [optional] |
|**jwkUri** | **URI** | The URL of your JSON Web Key Set. This set is a collection of JSON Web Keys, a standard method for representing cryptographic keys in a JSON structure. |  [optional] |
|**responseTypeSupported** | **List&lt;String&gt;** | A collection of response type supported by authorization server. |  [optional] |
|**revocationEndpoint** | **URI** | The endpoint used to revoke access or refresh tokens issued by the authorization server. |  [optional] |
|**scopesSupported** | **List&lt;String&gt;** | A collection of scopes supported by authorization server for identity token |  [optional] |
|**subjectTypeSupported** | **List&lt;String&gt;** | A collection of subject by authorization server. |  [optional] |
|**tokenEndpoint** | **URI** | The URL of the token endpoint. After a client has received an authorization code, that code is presented to the token endpoint and exchanged for an identity token, an access token, and a refresh token. |  [optional] |
|**url** | **URI** |  |  [optional] |
|**userinfoEndpoint** | **URI** | The URL of the user info endpoint, which returns user profile information to a client. Keep in mind that the user info endpoint returns only the information that has been requested. |  [optional] |



