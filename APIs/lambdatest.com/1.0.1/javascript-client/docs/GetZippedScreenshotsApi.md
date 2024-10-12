# LambdaTestScreenshotsApiDocumentation.GetZippedScreenshotsApi

All URIs are relative to *https://api.lambdatest.com/screenshots/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**zippedScreenshots**](GetZippedScreenshotsApi.md#zippedScreenshots) | **GET** /{test_id}/zip | Fetch Zipped Screenshots



## zippedScreenshots

> ZippedScreenshotsSuccess zippedScreenshots(testId)

Fetch Zipped Screenshots

Fetch Zipped Screenshots

### Example

```javascript
import LambdaTestScreenshotsApiDocumentation from 'lambda_test_screenshots_api_documentation';
let defaultClient = LambdaTestScreenshotsApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new LambdaTestScreenshotsApiDocumentation.GetZippedScreenshotsApi();
let testId = "testId_example"; // String | Test ID that Zipped Screenshots you want to fetch
apiInstance.zippedScreenshots(testId, (error, data, response) => {
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
 **testId** | **String**| Test ID that Zipped Screenshots you want to fetch | 

### Return type

[**ZippedScreenshotsSuccess**](ZippedScreenshotsSuccess.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

