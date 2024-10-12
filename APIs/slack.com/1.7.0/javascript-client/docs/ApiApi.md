# SlackWebApi.ApiApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTest**](ApiApi.md#apiTest) | **GET** /api.test | 



## apiTest

> ApiTestSuccessSchema apiTest(opts)



Checks API calling code.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.ApiApi();
let opts = {
  'error': "error_example", // String | Error response to return
  'foo': "foo_example" // String | example property to return
};
apiInstance.apiTest(opts, (error, data, response) => {
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
 **error** | **String**| Error response to return | [optional] 
 **foo** | **String**| example property to return | [optional] 

### Return type

[**ApiTestSuccessSchema**](ApiTestSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

