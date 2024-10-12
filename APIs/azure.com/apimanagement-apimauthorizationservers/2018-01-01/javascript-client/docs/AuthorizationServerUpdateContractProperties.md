# ApiManagementClient.AuthorizationServerUpdateContractProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizationEndpoint** | **String** | OAuth authorization endpoint. See http://tools.ietf.org/html/rfc6749#section-3.2. | [optional] 
**clientId** | **String** | Client or app id registered with this authorization server. | [optional] 
**clientRegistrationEndpoint** | **String** | Optional reference to a page where client or app registration for this authorization server is performed. Contains absolute URL to entity being referenced. | [optional] 
**displayName** | **String** | User-friendly authorization server name. | [optional] 
**grantTypes** | **[String]** | Form of an authorization grant, which the client uses to request the access token. | [optional] 
**authorizationMethods** | **[String]** | HTTP verbs supported by the authorization endpoint. GET must be always present. POST is optional. | [optional] 
**bearerTokenSendingMethods** | **[String]** | Specifies the mechanism by which access token is passed to the API.  | [optional] 
**clientAuthenticationMethod** | **[String]** | Method of authentication supported by the token endpoint of this authorization server. Possible values are Basic and/or Body. When Body is specified, client credentials and other parameters are passed within the request body in the application/x-www-form-urlencoded format. | [optional] 
**clientSecret** | **String** | Client or app secret registered with this authorization server. | [optional] 
**defaultScope** | **String** | Access token scope that is going to be requested by default. Can be overridden at the API level. Should be provided in the form of a string containing space-delimited values. | [optional] 
**description** | **String** | Description of the authorization server. Can contain HTML formatting tags. | [optional] 
**resourceOwnerPassword** | **String** | Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner password. | [optional] 
**resourceOwnerUsername** | **String** | Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner username. | [optional] 
**supportState** | **Boolean** | If true, authorization server will include state parameter from the authorization request to its response. Client may use state parameter to raise protocol security. | [optional] 
**tokenBodyParameters** | [**[TokenBodyParameterContract]**](TokenBodyParameterContract.md) | Additional parameters required by the token endpoint of this authorization server represented as an array of JSON objects with name and value string properties, i.e. {\&quot;name\&quot; : \&quot;name value\&quot;, \&quot;value\&quot;: \&quot;a value\&quot;}. | [optional] 
**tokenEndpoint** | **String** | OAuth token endpoint. Contains absolute URI to entity being referenced. | [optional] 



## Enum: [GrantTypesEnum]


* `authorizationCode` (value: `"authorizationCode"`)

* `implicit` (value: `"implicit"`)

* `resourceOwnerPassword` (value: `"resourceOwnerPassword"`)

* `clientCredentials` (value: `"clientCredentials"`)





## Enum: [AuthorizationMethodsEnum]


* `HEAD` (value: `"HEAD"`)

* `OPTIONS` (value: `"OPTIONS"`)

* `TRACE` (value: `"TRACE"`)

* `GET` (value: `"GET"`)

* `POST` (value: `"POST"`)

* `PUT` (value: `"PUT"`)

* `PATCH` (value: `"PATCH"`)

* `DELETE` (value: `"DELETE"`)





## Enum: [BearerTokenSendingMethodsEnum]


* `authorizationHeader` (value: `"authorizationHeader"`)

* `query` (value: `"query"`)





## Enum: [ClientAuthenticationMethodEnum]


* `Basic` (value: `"Basic"`)

* `Body` (value: `"Body"`)




