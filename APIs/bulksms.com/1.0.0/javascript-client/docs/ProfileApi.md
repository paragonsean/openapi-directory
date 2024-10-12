# BulkSmsJsonRestApi.ProfileApi

All URIs are relative to *https://api.bulksms.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**profileGet**](ProfileApi.md#profileGet) | **GET** /profile | Get profile



## profileGet

> Profile profileGet()

Get profile

Returns information about your user profile

### Example

```javascript
import BulkSmsJsonRestApi from 'bulk_sms_json_rest_api';
let defaultClient = BulkSmsJsonRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new BulkSmsJsonRestApi.ProfileApi();
apiInstance.profileGet((error, data, response) => {
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

[**Profile**](Profile.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

