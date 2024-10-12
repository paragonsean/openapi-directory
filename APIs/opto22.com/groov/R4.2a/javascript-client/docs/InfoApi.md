# GroovViewPublicApi.InfoApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groovInfo**](InfoApi.md#groovInfo) | **GET** /info | 



## groovInfo

> GroovInfo groovInfo()



Get information about groov View. No authorization required.

### Example

```javascript
import GroovViewPublicApi from 'groov_view_public_api';

let apiInstance = new GroovViewPublicApi.InfoApi();
apiInstance.groovInfo((error, data, response) => {
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

[**GroovInfo**](GroovInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

