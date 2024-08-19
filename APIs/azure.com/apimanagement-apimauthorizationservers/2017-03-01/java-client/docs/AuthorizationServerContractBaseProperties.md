

# AuthorizationServerContractBaseProperties

External OAuth authorization server Update settings contract.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizationMethods** | [**List&lt;AuthorizationMethodsEnum&gt;**](#List&lt;AuthorizationMethodsEnum&gt;) | HTTP verbs supported by the authorization endpoint. GET must be always present. POST is optional. |  [optional] |
|**bearerTokenSendingMethods** | [**List&lt;BearerTokenSendingMethodsEnum&gt;**](#List&lt;BearerTokenSendingMethodsEnum&gt;) | Specifies the mechanism by which access token is passed to the API.  |  [optional] |
|**clientAuthenticationMethod** | [**List&lt;ClientAuthenticationMethodEnum&gt;**](#List&lt;ClientAuthenticationMethodEnum&gt;) | Method of authentication supported by the token endpoint of this authorization server. Possible values are Basic and/or Body. When Body is specified, client credentials and other parameters are passed within the request body in the application/x-www-form-urlencoded format. |  [optional] |
|**clientSecret** | **String** | Client or app secret registered with this authorization server. |  [optional] |
|**defaultScope** | **String** | Access token scope that is going to be requested by default. Can be overridden at the API level. Should be provided in the form of a string containing space-delimited values. |  [optional] |
|**description** | **String** | Description of the authorization server. Can contain HTML formatting tags. |  [optional] |
|**resourceOwnerPassword** | **String** | Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner password. |  [optional] |
|**resourceOwnerUsername** | **String** | Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner username. |  [optional] |
|**supportState** | **Boolean** | If true, authorization server will include state parameter from the authorization request to its response. Client may use state parameter to raise protocol security. |  [optional] |
|**tokenBodyParameters** | [**List&lt;TokenBodyParameterContract&gt;**](TokenBodyParameterContract.md) | Additional parameters required by the token endpoint of this authorization server represented as an array of JSON objects with name and value string properties, i.e. {\&quot;name\&quot; : \&quot;name value\&quot;, \&quot;value\&quot;: \&quot;a value\&quot;}. |  [optional] |
|**tokenEndpoint** | **String** | OAuth token endpoint. Contains absolute URI to entity being referenced. |  [optional] |



## Enum: List&lt;AuthorizationMethodsEnum&gt;

| Name | Value |
|---- | -----|
| HEAD | &quot;HEAD&quot; |
| OPTIONS | &quot;OPTIONS&quot; |
| TRACE | &quot;TRACE&quot; |
| GET | &quot;GET&quot; |
| POST | &quot;POST&quot; |
| PUT | &quot;PUT&quot; |
| PATCH | &quot;PATCH&quot; |
| DELETE | &quot;DELETE&quot; |



## Enum: List&lt;BearerTokenSendingMethodsEnum&gt;

| Name | Value |
|---- | -----|
| AUTHORIZATION_HEADER | &quot;authorizationHeader&quot; |
| QUERY | &quot;query&quot; |



## Enum: List&lt;ClientAuthenticationMethodEnum&gt;

| Name | Value |
|---- | -----|
| BASIC | &quot;Basic&quot; |
| BODY | &quot;Body&quot; |



