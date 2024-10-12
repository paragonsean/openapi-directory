# ShutterstockApiExplorer.CreateAccessTokenRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientId** | **String** | Client ID (Consumer Key) of your application | 
**clientSecret** | **String** | Client Secret (Consumer Secret) of your application | [optional] 
**code** | **String** | Response code from the /oauth/authorize flow; required if grant_type&#x3D;authorization_code | [optional] 
**expires** | **Boolean** | Whether or not the token expires, expiring tokens come with a refresh_token to renew the access_token | [optional] [default to false]
**grantType** | **String** | Grant type: authorization_code generates user tokens, client_credentials generates short-lived client grants | 
**realm** | **String** | User type to be authorized (usually &#39;customer&#39;) | [optional] [default to &#39;customer&#39;]
**refreshToken** | **String** | Pass this along with grant_type&#x3D;refresh_token to get a fresh access token | [optional] 



## Enum: GrantTypeEnum


* `authorization_code` (value: `"authorization_code"`)

* `client_credentials` (value: `"client_credentials"`)

* `refresh_token` (value: `"refresh_token"`)





## Enum: RealmEnum


* `customer` (value: `"customer"`)

* `contributor` (value: `"contributor"`)




