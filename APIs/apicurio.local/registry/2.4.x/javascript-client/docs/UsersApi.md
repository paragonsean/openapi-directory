# ApicurioRegistryApiV2.UsersApi

All URIs are relative to *http://apicurio.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCurrentUserInfo**](UsersApi.md#getCurrentUserInfo) | **GET** /users/me | Get current user



## getCurrentUserInfo

> UserInfo getCurrentUserInfo()

Get current user

Returns information about the currently authenticated user.

### Example

```javascript
import ApicurioRegistryApiV2 from 'apicurio_registry_api__v2';

let apiInstance = new ApicurioRegistryApiV2.UsersApi();
apiInstance.getCurrentUserInfo((error, data, response) => {
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

[**UserInfo**](UserInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

