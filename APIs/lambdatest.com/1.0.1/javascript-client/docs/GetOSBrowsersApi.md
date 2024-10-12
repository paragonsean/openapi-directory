# LambdaTestScreenshotsApiDocumentation.GetOSBrowsersApi

All URIs are relative to *https://api.lambdatest.com/screenshots/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**osBrowsers**](GetOSBrowsersApi.md#osBrowsers) | **GET** /os-browsers | Fetch all available os-browser combinations.



## osBrowsers

> OsBrowsers osBrowsers(opts)

Fetch all available os-browser combinations.

Fetch all os browsers combinations available on lambdatest platform.

### Example

```javascript
import LambdaTestScreenshotsApiDocumentation from 'lambda_test_screenshots_api_documentation';
let defaultClient = LambdaTestScreenshotsApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new LambdaTestScreenshotsApiDocumentation.GetOSBrowsersApi();
let opts = {
  'os': "os_example" // String | Fetch details for a particular OS
};
apiInstance.osBrowsers(opts, (error, data, response) => {
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
 **os** | **String**| Fetch details for a particular OS | [optional] 

### Return type

[**OsBrowsers**](OsBrowsers.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

