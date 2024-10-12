# RubrikRestApi.VmwareHostApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getVmwareHost**](VmwareHostApi.md#getVmwareHost) | **GET** /vmware/host/{id} | Get details of a ESXi hypervisor
[**getVmwareHostDatastore**](VmwareHostApi.md#getVmwareHostDatastore) | **GET** /vmware/host/{id}/datastore | Get details of datastores in a ESXi hypervisor
[**queryVmwareHost**](VmwareHostApi.md#queryVmwareHost) | **GET** /vmware/host | Get summary of all the ESXi hypervisor
[**updateVmwareHost**](VmwareHostApi.md#updateVmwareHost) | **PATCH** /vmware/host/{id} | Update the SLA Domain for an ESXi hypervisor



## getVmwareHost

> VmwareHostDetail getVmwareHost(id)

Get details of a ESXi hypervisor

Get details of a ESXi hypervisor.

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

let apiInstance = new RubrikRestApi.VmwareHostApi();
let id = "id_example"; // String | ID of the VMWare host.
apiInstance.getVmwareHost(id, (error, data, response) => {
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
 **id** | **String**| ID of the VMWare host. | 

### Return type

[**VmwareHostDetail**](VmwareHostDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVmwareHostDatastore

> VmwareHostDatastoreDetail getVmwareHostDatastore(id)

Get details of datastores in a ESXi hypervisor

Get details of datastores in a ESXi hypervisor.

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

let apiInstance = new RubrikRestApi.VmwareHostApi();
let id = "id_example"; // String | ID of the VMWare host.
apiInstance.getVmwareHostDatastore(id, (error, data, response) => {
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
 **id** | **String**| ID of the VMWare host. | 

### Return type

[**VmwareHostDatastoreDetail**](VmwareHostDatastoreDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryVmwareHost

> VmwareHostSummaryListResponse queryVmwareHost(opts)

Get summary of all the ESXi hypervisor

Get summary of all the ESXi hypervisor.

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

let apiInstance = new RubrikRestApi.VmwareHostApi();
let opts = {
  'primaryClusterId': "primaryClusterId_example", // String | ID of the Primary cluster.
  'computeClusterId': "computeClusterId_example", // String | Filter by ID of Compute Cluster.
  'snappableStatus': "snappableStatus_example" // String | Requests additional data about VMware Hosts based on the specified query value.
};
apiInstance.queryVmwareHost(opts, (error, data, response) => {
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
 **primaryClusterId** | **String**| ID of the Primary cluster. | [optional] 
 **computeClusterId** | **String**| Filter by ID of Compute Cluster. | [optional] 
 **snappableStatus** | **String**| Requests additional data about VMware Hosts based on the specified query value. | [optional] 

### Return type

[**VmwareHostSummaryListResponse**](VmwareHostSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateVmwareHost

> VmwareHostDetail updateVmwareHost(id, vmwareHostUpdate)

Update the SLA Domain for an ESXi hypervisor

Update the SLA Domain that is configured for an ESXi hypervisor.

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

let apiInstance = new RubrikRestApi.VmwareHostApi();
let id = "id_example"; // String | ID of the ESXi hypervisor.
let vmwareHostUpdate = new RubrikRestApi.VmwareHostUpdate(); // VmwareHostUpdate | Object with changes for the ESXi hypervisor information.
apiInstance.updateVmwareHost(id, vmwareHostUpdate, (error, data, response) => {
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
 **id** | **String**| ID of the ESXi hypervisor. | 
 **vmwareHostUpdate** | [**VmwareHostUpdate**](VmwareHostUpdate.md)| Object with changes for the ESXi hypervisor information. | 

### Return type

[**VmwareHostDetail**](VmwareHostDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

