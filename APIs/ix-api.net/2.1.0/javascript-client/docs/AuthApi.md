# IxApi.AuthApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authTokenCreate**](AuthApi.md#authTokenCreate) | **POST** /auth/token | 
[**authTokenRefresh**](AuthApi.md#authTokenRefresh) | **POST** /auth/refresh | 



## authTokenCreate

> AuthToken authTokenCreate(opts)



Authenticate an API user identified by &#x60;api_key&#x60; and &#x60;api_secret&#x60;.

### Example

```javascript
import IxApi from 'ix_api';

let apiInstance = new IxApi.AuthApi();
let opts = {
  'authTokenRequest': new IxApi.AuthTokenRequest() // AuthTokenRequest | AuthTokenRequest
};
apiInstance.authTokenCreate(opts, (error, data, response) => {
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
 **authTokenRequest** | [**AuthTokenRequest**](AuthTokenRequest.md)| AuthTokenRequest | [optional] 

### Return type

[**AuthToken**](AuthToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## authTokenRefresh

> AuthToken authTokenRefresh(opts)



Reauthenticate the API user, issue a new &#x60;access_token&#x60; and &#x60;refresh_token&#x60; pair by providing the &#x60;refresh_token&#x60; in the request body.

### Example

```javascript
import IxApi from 'ix_api';

let apiInstance = new IxApi.AuthApi();
let opts = {
  'refreshTokenRequest': new IxApi.RefreshTokenRequest() // RefreshTokenRequest | RefreshTokenRequest
};
apiInstance.authTokenRefresh(opts, (error, data, response) => {
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
 **refreshTokenRequest** | [**RefreshTokenRequest**](RefreshTokenRequest.md)| RefreshTokenRequest | [optional] 

### Return type

[**AuthToken**](AuthToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

