# LambdaTestScreenshotsApiDocumentation.StopScreenshotTestApi

All URIs are relative to *https://api.lambdatest.com/screenshots/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stopScreenshotsTest**](StopScreenshotTestApi.md#stopScreenshotsTest) | **PUT** /stop/{test_id} | Stop specified screenshot test



## stopScreenshotsTest

> StopScreenshotSuccess stopScreenshotsTest(testId)

Stop specified screenshot test

Stop specified screenshot test

### Example

```javascript
import LambdaTestScreenshotsApiDocumentation from 'lambda_test_screenshots_api_documentation';
let defaultClient = LambdaTestScreenshotsApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new LambdaTestScreenshotsApiDocumentation.StopScreenshotTestApi();
let testId = "testId_example"; // String | Test ID that details you want to stop
apiInstance.stopScreenshotsTest(testId, (error, data, response) => {
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
 **testId** | **String**| Test ID that details you want to stop | 

### Return type

[**StopScreenshotSuccess**](StopScreenshotSuccess.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

