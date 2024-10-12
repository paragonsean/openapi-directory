# Api.StatusApi

All URIs are relative to *https://tl-api.azurewebsites.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statusGet**](StatusApi.md#statusGet) | **GET** /api/Status | Get the current status of message



## statusGet

> MessageStatus statusGet(opts)

Get the current status of message

### Example

```javascript
import Api from 'api';
let defaultClient = Api.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer
let bearer = defaultClient.authentications['bearer'];
bearer.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Api.StatusApi();
let opts = {
  'messageId': "messageId_example" // String | respose of POST request
};
apiInstance.statusGet(opts, (error, data, response) => {
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
 **messageId** | **String**| respose of POST request | [optional] 

### Return type

[**MessageStatus**](MessageStatus.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

