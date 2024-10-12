# OpenApiSpace.AuthApi

All URIs are relative to *https://openapi.space/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AuthApi.md#login) | **POST** /auth/login | Log in to OpenAPI space
[**loginApinf**](AuthApi.md#loginApinf) | **POST** /auth/login/apinf | Log in to OpenAPI space using an APInf account
[**loginApinfToken**](AuthApi.md#loginApinfToken) | **POST** /auth/login/apinf_token | Log in to OpenAPI space using an APInf authentication token
[**logout**](AuthApi.md#logout) | **POST** /auth/logout | Log out from OpenAPI space
[**ping**](AuthApi.md#ping) | **POST** /auth/ping | Check whether or not you are authenticated
[**register**](AuthApi.md#register) | **POST** /auth/register | Register to OpenAPI space



## login

> LoginToken login(opts)

Log in to OpenAPI space

### Example

```javascript
import OpenApiSpace from 'open_api_space';

let apiInstance = new OpenApiSpace.AuthApi();
let opts = {
  'body': new OpenApiSpace.Credentials() // Credentials | the user credentials
};
apiInstance.login(opts, (error, data, response) => {
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
 **body** | [**Credentials**](Credentials.md)| the user credentials | [optional] 

### Return type

[**LoginToken**](LoginToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## loginApinf

> LoginToken loginApinf(opts)

Log in to OpenAPI space using an APInf account

### Example

```javascript
import OpenApiSpace from 'open_api_space';

let apiInstance = new OpenApiSpace.AuthApi();
let opts = {
  'body': new OpenApiSpace.LoginApinfRequest() // LoginApinfRequest | the APInf username and password
};
apiInstance.loginApinf(opts, (error, data, response) => {
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
 **body** | [**LoginApinfRequest**](LoginApinfRequest.md)| the APInf username and password | [optional] 

### Return type

[**LoginToken**](LoginToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## loginApinfToken

> LoginToken loginApinfToken(opts)

Log in to OpenAPI space using an APInf authentication token

### Example

```javascript
import OpenApiSpace from 'open_api_space';

let apiInstance = new OpenApiSpace.AuthApi();
let opts = {
  'body': new OpenApiSpace.LoginApinfTokenRequest() // LoginApinfTokenRequest | the APInf authentication token and user ID
};
apiInstance.loginApinfToken(opts, (error, data, response) => {
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
 **body** | [**LoginApinfTokenRequest**](LoginApinfTokenRequest.md)| the APInf authentication token and user ID | [optional] 

### Return type

[**LoginToken**](LoginToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## logout

> logout()

Log out from OpenAPI space

### Example

```javascript
import OpenApiSpace from 'open_api_space';
let defaultClient = OpenApiSpace.ApiClient.instance;
// Configure API key authorization: AuthToken
let AuthToken = defaultClient.authentications['AuthToken'];
AuthToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//AuthToken.apiKeyPrefix = 'Token';

let apiInstance = new OpenApiSpace.AuthApi();
apiInstance.logout((error, data, response) => {
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

[AuthToken](../README.md#AuthToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## ping

> Registration ping()

Check whether or not you are authenticated

### Example

```javascript
import OpenApiSpace from 'open_api_space';
let defaultClient = OpenApiSpace.ApiClient.instance;
// Configure API key authorization: AuthToken
let AuthToken = defaultClient.authentications['AuthToken'];
AuthToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//AuthToken.apiKeyPrefix = 'Token';

let apiInstance = new OpenApiSpace.AuthApi();
apiInstance.ping((error, data, response) => {
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

[**Registration**](Registration.md)

### Authorization

[AuthToken](../README.md#AuthToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## register

> LoginToken register(opts)

Register to OpenAPI space

### Example

```javascript
import OpenApiSpace from 'open_api_space';

let apiInstance = new OpenApiSpace.AuthApi();
let opts = {
  'body': new OpenApiSpace.Registration() // Registration | registration details
};
apiInstance.register(opts, (error, data, response) => {
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
 **body** | [**Registration**](Registration.md)| registration details | [optional] 

### Return type

[**LoginToken**](LoginToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

