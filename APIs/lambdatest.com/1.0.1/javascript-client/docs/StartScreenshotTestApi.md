# LambdaTestScreenshotsApiDocumentation.StartScreenshotTestApi

All URIs are relative to *https://api.lambdatest.com/screenshots/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**startScreenshotTest**](StartScreenshotTestApi.md#startScreenshotTest) | **POST** / | Start Screenshot Test



## startScreenshotTest

> StartScreenshotSuccess startScreenshotTest(screenshotPayload)

Start Screenshot Test

Start Screenshot Test

### Example

```javascript
import LambdaTestScreenshotsApiDocumentation from 'lambda_test_screenshots_api_documentation';
let defaultClient = LambdaTestScreenshotsApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new LambdaTestScreenshotsApiDocumentation.StartScreenshotTestApi();
let screenshotPayload = new LambdaTestScreenshotsApiDocumentation.ScreenshotPayload(); // ScreenshotPayload | start screenshot test payload.
apiInstance.startScreenshotTest(screenshotPayload, (error, data, response) => {
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
 **screenshotPayload** | [**ScreenshotPayload**](ScreenshotPayload.md)| start screenshot test payload. | 

### Return type

[**StartScreenshotSuccess**](StartScreenshotSuccess.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

