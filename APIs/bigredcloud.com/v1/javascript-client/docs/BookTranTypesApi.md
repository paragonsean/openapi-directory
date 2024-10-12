# BigRedCloudApi.BookTranTypesApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bookTranTypesGet**](BookTranTypesApi.md#bookTranTypesGet) | **GET** /v1/bookTranTypes | Returns a list of global Book Transactions&#39; Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.



## bookTranTypesGet

> PageResultBookTranTypeDto bookTranTypesGet()

Returns a list of global Book Transactions&#39; Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.BookTranTypesApi();
apiInstance.bookTranTypesGet((error, data, response) => {
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

[**PageResultBookTranTypeDto**](PageResultBookTranTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

