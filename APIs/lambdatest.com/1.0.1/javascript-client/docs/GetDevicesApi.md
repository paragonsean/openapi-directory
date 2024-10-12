# LambdaTestScreenshotsApiDocumentation.GetDevicesApi

All URIs are relative to *https://api.lambdatest.com/screenshots/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**devices**](GetDevicesApi.md#devices) | **GET** /devices | Fetch all available device combinations.



## devices

> OsDevices devices(opts)

Fetch all available device combinations.

Fetch all os devices combinations available on lambdatest platform.

### Example

```javascript
import LambdaTestScreenshotsApiDocumentation from 'lambda_test_screenshots_api_documentation';
let defaultClient = LambdaTestScreenshotsApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new LambdaTestScreenshotsApiDocumentation.GetDevicesApi();
let opts = {
  'os': "os_example" // String | Fetch details for a particular OS
};
apiInstance.devices(opts, (error, data, response) => {
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

[**OsDevices**](OsDevices.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

