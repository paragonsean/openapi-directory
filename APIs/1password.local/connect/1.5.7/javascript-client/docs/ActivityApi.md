# 1PasswordConnect.ActivityApi

All URIs are relative to *http://1password.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getApiActivity**](ActivityApi.md#getApiActivity) | **GET** /activity | Retrieve a list of API Requests that have been made.



## getApiActivity

> [APIRequest] getApiActivity(opts)

Retrieve a list of API Requests that have been made.

### Example

```javascript
import 1PasswordConnect from '1_password_connect';
let defaultClient = 1PasswordConnect.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: ConnectToken
let ConnectToken = defaultClient.authentications['ConnectToken'];
ConnectToken.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new 1PasswordConnect.ActivityApi();
let opts = {
  'limit': 10, // Number | How many API Events should be retrieved in a single request.
  'offset': 50 // Number | How far into the collection of API Events should the response start
};
apiInstance.getApiActivity(opts, (error, data, response) => {
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
 **limit** | **Number**| How many API Events should be retrieved in a single request. | [optional] [default to 50]
 **offset** | **Number**| How far into the collection of API Events should the response start | [optional] [default to 0]

### Return type

[**[APIRequest]**](APIRequest.md)

### Authorization

[ConnectToken](../README.md#ConnectToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

