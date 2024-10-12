# LambdaTestScreenshotsApiDocumentation.GetProfilesApi

All URIs are relative to *https://api.lambdatest.com/screenshots/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profiles**](GetProfilesApi.md#profiles) | **GET** /profiles | Fetch login profiles



## profiles

> Profiles profiles()

Fetch login profiles

Fetch login profiles

### Example

```javascript
import LambdaTestScreenshotsApiDocumentation from 'lambda_test_screenshots_api_documentation';
let defaultClient = LambdaTestScreenshotsApiDocumentation.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new LambdaTestScreenshotsApiDocumentation.GetProfilesApi();
apiInstance.profiles((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Profiles**](Profiles.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

