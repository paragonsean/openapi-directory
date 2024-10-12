# Superset.SecurityApi

All URIs are relative to *http://superset.apache.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**securityCsrfTokenGet**](SecurityApi.md#securityCsrfTokenGet) | **GET** /security/csrf_token/ | 
[**securityLoginPost**](SecurityApi.md#securityLoginPost) | **POST** /security/login | 
[**securityRefreshPost**](SecurityApi.md#securityRefreshPost) | **POST** /security/refresh | 



## securityCsrfTokenGet

> SecurityCsrfTokenGet200Response securityCsrfTokenGet()



Fetch the CSRF token

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.SecurityApi();
apiInstance.securityCsrfTokenGet((error, data, response) => {
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

[**SecurityCsrfTokenGet200Response**](SecurityCsrfTokenGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## securityLoginPost

> SecurityLoginPost200Response securityLoginPost(securityLoginPostRequest)



Authenticate and get a JWT access and refresh token

### Example

```javascript
import Superset from 'superset';

let apiInstance = new Superset.SecurityApi();
let securityLoginPostRequest = new Superset.SecurityLoginPostRequest(); // SecurityLoginPostRequest | 
apiInstance.securityLoginPost(securityLoginPostRequest, (error, data, response) => {
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
 **securityLoginPostRequest** | [**SecurityLoginPostRequest**](SecurityLoginPostRequest.md)|  | 

### Return type

[**SecurityLoginPost200Response**](SecurityLoginPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## securityRefreshPost

> SecurityRefreshPost200Response securityRefreshPost()



Use the refresh token to get a new JWT access token

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt_refresh
let jwt_refresh = defaultClient.authentications['jwt_refresh'];
jwt_refresh.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.SecurityApi();
apiInstance.securityRefreshPost((error, data, response) => {
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

[**SecurityRefreshPost200Response**](SecurityRefreshPost200Response.md)

### Authorization

[jwt_refresh](../README.md#jwt_refresh)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

