# ObonoRksvApi.AuthApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authGet**](AuthApi.md#authGet) | **GET** /auth | 



## authGet

> AuthResult authGet()



Request a JWT access token using your obono username and password.

### Example

```javascript
import ObonoRksvApi from 'obono_rksv_api';
let defaultClient = ObonoRksvApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new ObonoRksvApi.AuthApi();
apiInstance.authGet((error, data, response) => {
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

[**AuthResult**](AuthResult.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

