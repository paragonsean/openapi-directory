# SeveraPublicRestApiDocumentation.NoScopeApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**heartBeatGetAuthorization**](NoScopeApi.md#heartBeatGetAuthorization) | **GET** /heartbeat/authorized | Returns http status code 204 for successful authentication.
[**heartBeatGetDatabaseStatus**](NoScopeApi.md#heartBeatGetDatabaseStatus) | **GET** /heartbeat/database | Can be used to check the status of the database.
[**heartBeatGetServerStatus**](NoScopeApi.md#heartBeatGetServerStatus) | **GET** /heartbeat/server | Can be used to check the status of the REST Api.
[**publicBearerAuthenticationGetAccessTokenJson**](NoScopeApi.md#publicBearerAuthenticationGetAccessTokenJson) | **POST** /v1/login/oauth/access_token | Get oAuth2 access token.
[**publicBearerAuthenticationGetAccessTokenTokenFromRefreshToken**](NoScopeApi.md#publicBearerAuthenticationGetAccessTokenTokenFromRefreshToken) | **POST** /v1/refreshtoken | Get new access token using a refresh token.
[**publicBearerAuthenticationGetAuthorizationCode**](NoScopeApi.md#publicBearerAuthenticationGetAuthorizationCode) | **GET** /v1/login/oauth/authorize | Get the oAuth2 authorization code flow code.
[**publicBearerAuthenticationGetLoginToken**](NoScopeApi.md#publicBearerAuthenticationGetLoginToken) | **POST** /v1/token | Can be used to get the login information and access token for the api client.
[**publicBearerAuthenticationLogout**](NoScopeApi.md#publicBearerAuthenticationLogout) | **POST** /v1/signout | Logout. Invalidates refresh token. Access token will be invalid when it expires.



## heartBeatGetAuthorization

> heartBeatGetAuthorization()

Returns http status code 204 for successful authentication.

This route requires authentication, returns 204 http status when successful.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.NoScopeApi();
apiInstance.heartBeatGetAuthorization((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## heartBeatGetDatabaseStatus

> File heartBeatGetDatabaseStatus()

Can be used to check the status of the database.

This does not require authentication.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';

let apiInstance = new SeveraPublicRestApiDocumentation.NoScopeApi();
apiInstance.heartBeatGetDatabaseStatus((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json


## heartBeatGetServerStatus

> File heartBeatGetServerStatus()

Can be used to check the status of the REST Api.

This does not require authentication.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';

let apiInstance = new SeveraPublicRestApiDocumentation.NoScopeApi();
apiInstance.heartBeatGetServerStatus((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**File**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json


## publicBearerAuthenticationGetAccessTokenJson

> PublicAuthenticationOutputModel publicBearerAuthenticationGetAccessTokenJson(opts)

Get oAuth2 access token.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.NoScopeApi();
let opts = {
  'accessTokenCredentials': new SeveraPublicRestApiDocumentation.AccessTokenCredentials() // AccessTokenCredentials | AccessTokenCredentials model
};
apiInstance.publicBearerAuthenticationGetAccessTokenJson(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accessTokenCredentials** | [**AccessTokenCredentials**](AccessTokenCredentials.md)| AccessTokenCredentials model | [optional] 

### Return type

[**PublicAuthenticationOutputModel**](PublicAuthenticationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## publicBearerAuthenticationGetAccessTokenTokenFromRefreshToken

> PublicAuthenticationOutputModel publicBearerAuthenticationGetAccessTokenTokenFromRefreshToken(opts)

Get new access token using a refresh token.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.NoScopeApi();
let opts = {
  'body': "body_example" // String | Refresh token.
};
apiInstance.publicBearerAuthenticationGetAccessTokenTokenFromRefreshToken(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **String**| Refresh token. | [optional] 

### Return type

[**PublicAuthenticationOutputModel**](PublicAuthenticationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## publicBearerAuthenticationGetAuthorizationCode

> ExceptionModel publicBearerAuthenticationGetAuthorizationCode(opts)

Get the oAuth2 authorization code flow code.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.NoScopeApi();
let opts = {
  'responseType': "responseType_example", // String | code
  'state': "state_example", // String | Unguessable random string.
  'clientId': "clientId_example", // String | Client id.
  'redirectUri': "redirectUri_example", // String | Url where to redirect after code has been retrieved.
  'scope': "''" // String | Scopes that client requests. If scopes that are not allowed for the client are requested, returns unauthorized.
};
apiInstance.publicBearerAuthenticationGetAuthorizationCode(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **responseType** | **String**| code | [optional] 
 **state** | **String**| Unguessable random string. | [optional] 
 **clientId** | **String**| Client id. | [optional] 
 **redirectUri** | **String**| Url where to redirect after code has been retrieved. | [optional] 
 **scope** | **String**| Scopes that client requests. If scopes that are not allowed for the client are requested, returns unauthorized. | [optional] [default to &#39;&#39;]

### Return type

[**ExceptionModel**](ExceptionModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## publicBearerAuthenticationGetLoginToken

> PublicAuthenticationOutputModel publicBearerAuthenticationGetLoginToken(opts)

Can be used to get the login information and access token for the api client.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.NoScopeApi();
let opts = {
  'clientCredentials': new SeveraPublicRestApiDocumentation.ClientCredentials() // ClientCredentials | ClientCredentials of the client.
};
apiInstance.publicBearerAuthenticationGetLoginToken(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **clientCredentials** | [**ClientCredentials**](ClientCredentials.md)| ClientCredentials of the client. | [optional] 

### Return type

[**PublicAuthenticationOutputModel**](PublicAuthenticationOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## publicBearerAuthenticationLogout

> File publicBearerAuthenticationLogout(opts)

Logout. Invalidates refresh token. Access token will be invalid when it expires.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.NoScopeApi();
let opts = {
  'body': "body_example" // String | 
};
apiInstance.publicBearerAuthenticationLogout(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **String**|  | [optional] 

### Return type

**File**

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/octet-stream, application/json

