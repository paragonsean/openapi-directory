# OrbitApi.UsersApi

All URIs are relative to *https://app.orbit.love/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**userGet**](UsersApi.md#userGet) | **GET** /user | Get info about the current user



## userGet

> userGet()

Get info about the current user

### Example

```javascript
import OrbitApi from 'orbit_api';
let defaultClient = OrbitApi.ApiClient.instance;
// Configure Bearer access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new OrbitApi.UsersApi();
apiInstance.userGet((error, data, response) => {
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

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

