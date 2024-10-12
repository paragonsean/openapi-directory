# EnterobaseApi.LoginApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV20LoginGet**](LoginApi.md#apiV20LoginGet) | **GET** /api/v2.0/login | 



## apiV20LoginGet

> apiV20LoginGet(opts)



Login endpoint, refresh your API token

### Example

```javascript
import EnterobaseApi from 'enterobase_api';

let apiInstance = new EnterobaseApi.LoginApi();
let opts = {
  'password': "password_example", // String | EnteroBase Password
  'username': "username_example" // String | EnteroBase username
};
apiInstance.apiV20LoginGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password** | **String**| EnteroBase Password | [optional] 
 **username** | **String**| EnteroBase username | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

