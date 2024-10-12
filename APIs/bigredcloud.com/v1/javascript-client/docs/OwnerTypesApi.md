# BigRedCloudApi.OwnerTypesApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ownerTypesGet**](OwnerTypesApi.md#ownerTypesGet) | **GET** /v1/ownerTypes | Returns a list of global Owner Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.



## ownerTypesGet

> PageResultOwnerTypeDto ownerTypesGet()

Returns a list of global Owner Types. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.OwnerTypesApi();
apiInstance.ownerTypesGet((error, data, response) => {
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

[**PageResultOwnerTypeDto**](PageResultOwnerTypeDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

