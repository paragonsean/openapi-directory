# DropX.MonitorApi

All URIs are relative to *http://dropx.io/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usersUsageGet**](MonitorApi.md#usersUsageGet) | **GET** /users/usage | Get API usuage details



## usersUsageGet

> usersUsageGet()

Get API usuage details

Returns API request consumption details.

### Example

```javascript
import DropX from 'drop_x';

let apiInstance = new DropX.MonitorApi();
apiInstance.usersUsageGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

