# GroovViewPublicApi.WhoamiApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**whoAmI**](WhoamiApi.md#whoAmI) | **GET** /whoami | 



## whoAmI

> User whoAmI()



Get information about the user you are authenticated as. Authorized for admins, editors, operators, and kiosk.

### Example

```javascript
import GroovViewPublicApi from 'groov_view_public_api';
let defaultClient = GroovViewPublicApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new GroovViewPublicApi.WhoamiApi();
apiInstance.whoAmI((error, data, response) => {
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

[**User**](User.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

