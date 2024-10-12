# BigRedCloudApi.CategoryTypesApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**categoryTypesGet**](CategoryTypesApi.md#categoryTypesGet) | **GET** /v1/categoryTypes | Returns a list of company&#39;s Category Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.



## categoryTypesGet

> PageResultCategoryTypeDto categoryTypesGet()

Returns a list of company&#39;s Category Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.CategoryTypesApi();
apiInstance.categoryTypesGet((error, data, response) => {
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

[**PageResultCategoryTypeDto**](PageResultCategoryTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

