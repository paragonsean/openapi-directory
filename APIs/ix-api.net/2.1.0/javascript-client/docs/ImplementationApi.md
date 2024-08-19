# IxApi.ImplementationApi

All URIs are relative to */api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiImplementationRead**](ImplementationApi.md#apiImplementationRead) | **GET** /implementation | 



## apiImplementationRead

> ImplementationResponse apiImplementationRead()



Get the API implementation details.

### Example

```javascript
import IxApi from 'ix_api';
let defaultClient = IxApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new IxApi.ImplementationApi();
apiInstance.apiImplementationRead((error, data, response) => {
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

[**ImplementationResponse**](ImplementationResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

