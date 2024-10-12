# PhantAuth.ClientClientIdGet200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | URL of the Client&#39;s JSON representation. | [optional] 
**clientId** | **String** | OAuth 2.0 client identifier string. | 
**clientName** | **String** | Human-readable string name of the client to be presented to the end-user during authorization. | [optional] 
**clientSecret** | **String** | OAuth 2.0 client secret string.  | [optional] 
**clientUri** | **String** | URL string of a web page providing information about the client. | [optional] 
**contacts** | **[Object]** | Array of strings representing ways to contact people responsible for this client, typically email addresses. | [optional] 
**grantTypes** | **[Object]** | Array of OAuth 2.0 grant type strings that the client can use at the token endpoint. | [optional] 
**jwks** | **[Object]** | Client&#39;s JSON Web Key Set [RFC7517] document value, which contains the client&#39;s public keys.  The value of this field MUST be a JSON object containing a valid JWK Set. | [optional] 
**jwksUri** | **String** | URL string referencing the client&#39;s JSON Web Key (JWK) Set [RFC7517] document, which contains the client&#39;s public keys. | [optional] 
**logoEmail** | **String** | An email address used to generate a gravatar.com logo_uri. | [optional] 
**logoUri** | **String** | URL string that references a logo for the client. | [optional] 
**policyUri** | **String** | URL string that points to a human-readable privacy policy document that describes how the deployment organization collects, uses, retains, and discloses personal data. | [optional] 
**redirectUris** | **[Object]** | Array of redirection URI strings for use in redirect-based flows such as the authorization code and implicit flows. | [optional] 
**responseTypes** | **[Object]** | Array of the OAuth 2.0 response type strings that the client can use at the authorization endpoint. | [optional] 
**scope** | **String** | String containing a space-separated list of scope values (as described in Section 3.3 of OAuth 2.0 [RFC6749]) that the client can use when requesting access tokens. | [optional] 
**softwareId** | **String** | A unique identifier string (e.g., a Universally Unique Identifier (UUID)) assigned by the client developer or software publisher used by registration endpoints to identify the client software to be dynamically registered. | [optional] 
**softwareVersion** | **String** | A version identifier string for the client software identified by software_id. | [optional] 
**tokenEndpointAuthMethod** | **String** | String indicator of the requested authentication method for the token endpoint. | [optional] 
**tosUri** | **String** | URL string that points to a human-readable terms of service document for the client that describes a contractual relationship between the end-user and the client that the end-user accepts when authorizing the client. | [optional] 


