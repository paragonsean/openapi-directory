# RubrikRestApi.VmwareHierarchyApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getVmwareHierarchyExport**](VmwareHierarchyApi.md#getVmwareHierarchyExport) | **GET** /vmware/hierarchy/export | Get Available VMware Hierarchy Objects for Export Operations
[**getVmwareHierarchyObject**](VmwareHierarchyApi.md#getVmwareHierarchyObject) | **GET** /vmware/hierarchy/{id}/export | Get VMware Hierarchy Object Information



## getVmwareHierarchyExport

> VmwareHierarchyInfoListResponse getVmwareHierarchyExport(opts)

Get Available VMware Hierarchy Objects for Export Operations

Get VMware Clusters, Hosts, and Resource Pool hierarchy objects that are available as the target for Virtual Machine Export operations.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.VmwareHierarchyApi();
let opts = {
  'rootId': "rootId_example" // String | Get child objects of given root ID.
};
apiInstance.getVmwareHierarchyExport(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rootId** | **String**| Get child objects of given root ID. | [optional] 

### Return type

[**VmwareHierarchyInfoListResponse**](VmwareHierarchyInfoListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVmwareHierarchyObject

> VmwareHierarchyInfo getVmwareHierarchyObject(id)

Get VMware Hierarchy Object Information

Get VMware Clusters, Hosts, and Resource Pool hierarchy object detail information by object ID.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.VmwareHierarchyApi();
let id = "id_example"; // String | Get VMware hierarchy objects of given ID.
apiInstance.getVmwareHierarchyObject(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Get VMware hierarchy objects of given ID. | 

### Return type

[**VmwareHierarchyInfo**](VmwareHierarchyInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

