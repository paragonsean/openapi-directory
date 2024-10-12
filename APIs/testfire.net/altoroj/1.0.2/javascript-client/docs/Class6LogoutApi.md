# AltoroJRestApi.Class6LogoutApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**doLogOut**](Class6LogoutApi.md#doLogOut) | **GET** /logout | 



## doLogOut

> doLogOut()



Logout from the bank

### Example

```javascript
import AltoroJRestApi from 'altoro_j_rest_api';

let apiInstance = new AltoroJRestApi.Class6LogoutApi();
apiInstance.doLogOut((error, data, response) => {
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

