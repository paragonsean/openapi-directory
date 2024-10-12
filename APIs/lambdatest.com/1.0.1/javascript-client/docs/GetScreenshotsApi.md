# LambdaTestScreenshotsApiDocumentation.GetScreenshotsApi

All URIs are relative to *https://api.lambdatest.com/screenshots/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**screenshots**](GetScreenshotsApi.md#screenshots) | **GET** /{test_id} | Fetch specified screenshot details



## screenshots

> ScreenshotTestResponse screenshots(testId)

Fetch specified screenshot details

To fetch specified screenshot details

### Example

```javascript
import LambdaTestScreenshotsApiDocumentation from 'lambda_test_screenshots_api_documentation';
let defaultClient = LambdaTestScreenshotsApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new LambdaTestScreenshotsApiDocumentation.GetScreenshotsApi();
let testId = "testId_example"; // String | Test ID that details you want to fetch
apiInstance.screenshots(testId, (error, data, response) => {
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
 **testId** | **String**| Test ID that details you want to fetch | 

### Return type

[**ScreenshotTestResponse**](ScreenshotTestResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

