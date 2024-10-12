# BigRedCloudApi.OwnerTypeGroupsApi

All URIs are relative to *https://app.bigredcloud.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ownerTypeGroupsGet**](OwnerTypeGroupsApi.md#ownerTypeGroupsGet) | **GET** /v1/ownerTypeGroups | Returns a list of global Owner Type Groups. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.



## ownerTypeGroupsGet

> PageResultOwnerTypeGroupDto ownerTypeGroupsGet()

Returns a list of global Owner Type Groups. Supports OData querying protocol.  Filtering is forbidden.  Ordering is allowed by \&quot;id\&quot; field.

### Example

```javascript
import BigRedCloudApi from 'big_red_cloud_api';

let apiInstance = new BigRedCloudApi.OwnerTypeGroupsApi();
apiInstance.ownerTypeGroupsGet((error, data, response) => {
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

[**PageResultOwnerTypeGroupDto**](PageResultOwnerTypeGroupDto.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

