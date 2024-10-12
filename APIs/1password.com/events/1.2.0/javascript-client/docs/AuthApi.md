# EventsApi.AuthApi

All URIs are relative to *https://events.1password.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAuthIntrospect**](AuthApi.md#getAuthIntrospect) | **GET** /api/auth/introspect | Performs introspection of the provided Bearer JWT token
[**getAuthIntrospectV2**](AuthApi.md#getAuthIntrospectV2) | **GET** /api/v2/auth/introspect | Performs introspection of the provided Bearer JWT token



## getAuthIntrospect

> Introspection getAuthIntrospect()

Performs introspection of the provided Bearer JWT token

### Example

```javascript
import EventsApi from 'events_api';
let defaultClient = EventsApi.ApiClient.instance;
// Configure Bearer (JWT-SA) access token for authorization: jwtsa
let jwtsa = defaultClient.authentications['jwtsa'];
jwtsa.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EventsApi.AuthApi();
apiInstance.getAuthIntrospect((error, data, response) => {
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

[**Introspection**](Introspection.md)

### Authorization

[jwtsa](../README.md#jwtsa)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAuthIntrospectV2

> IntrospectionV2 getAuthIntrospectV2()

Performs introspection of the provided Bearer JWT token

### Example

```javascript
import EventsApi from 'events_api';
let defaultClient = EventsApi.ApiClient.instance;
// Configure Bearer (JWT-SA) access token for authorization: jwtsa
let jwtsa = defaultClient.authentications['jwtsa'];
jwtsa.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new EventsApi.AuthApi();
apiInstance.getAuthIntrospectV2((error, data, response) => {
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

[**IntrospectionV2**](IntrospectionV2.md)

### Authorization

[jwtsa](../README.md#jwtsa)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

