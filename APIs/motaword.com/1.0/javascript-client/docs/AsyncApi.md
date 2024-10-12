# MotaWordApi.AsyncApi

All URIs are relative to *https://api.motaword.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**downloadAsync**](AsyncApi.md#downloadAsync) | **GET** /async/download | Download result of an async operation



## downloadAsync

> File downloadAsync(asyncRequestKey)

Download result of an async operation

Download the result of an async operation that you have requested in other endpoints.

### Example

```javascript
import MotaWordApi from 'mota_word_api';
let defaultClient = MotaWordApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: mwoAuth
let mwoAuth = defaultClient.authentications['mwoAuth'];
mwoAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MotaWordApi.AsyncApi();
let asyncRequestKey = "f0db2468-6b77-41a4-bafe-70157bc166ad"; // String | Async operation key
apiInstance.downloadAsync(asyncRequestKey, (error, data, response) => {
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
 **asyncRequestKey** | **String**| Async operation key | 

### Return type

**File**

### Authorization

[mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth), [mwoAuth](../README.md#mwoAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/octet-stream, application/json

