# RubrikRestApi.VmwareVcenterApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createRefresh**](VmwareVcenterApi.md#createRefresh) | **POST** /vmware/vcenter/{id}/refresh | Refresh vCenter Server metadata
[**createRefreshVmV1**](VmwareVcenterApi.md#createRefreshVmV1) | **POST** /vmware/vcenter/{id}/refresh_vm | Refresh single virtual machine metadata in a vcenter
[**createVcenter**](VmwareVcenterApi.md#createVcenter) | **POST** /vmware/vcenter | Add vCenter Server
[**deleteVcenter**](VmwareVcenterApi.md#deleteVcenter) | **DELETE** /vmware/vcenter/{id} | Remove vCenter Server
[**getHotAddBandwidth**](VmwareVcenterApi.md#getHotAddBandwidth) | **GET** /vmware/vcenter/{id}/hotadd/bandwidth | Get the ingest and export bandwidth limits for HotAdd with the vCenter
[**getHotAddNetwork**](VmwareVcenterApi.md#getHotAddNetwork) | **GET** /vmware/vcenter/{id}/hotadd/network | Retrieve the user-configured network for HotAdd operations
[**getNetworks**](VmwareVcenterApi.md#getNetworks) | **GET** /vmware/vcenter/{id}/networks | Get the user-configured networks in the vCenter
[**getNumProxiesNeeded**](VmwareVcenterApi.md#getNumProxiesNeeded) | **GET** /vmware/vcenter/{id}/hotadd/needed | Get the number of HotAdd proxies needed for the vCenter
[**getVcenter**](VmwareVcenterApi.md#getVcenter) | **GET** /vmware/vcenter/{id} | Get the details of a vCenter Server
[**getVcenterAsyncRequestStatus**](VmwareVcenterApi.md#getVcenterAsyncRequestStatus) | **GET** /vmware/vcenter/request/{id} | Get vCenter Server async request
[**patchVcenter**](VmwareVcenterApi.md#patchVcenter) | **PATCH** /vmware/vcenter/{id} | Update the SLA Domain for a vCenter Server
[**queryHotAddProxyVm**](VmwareVcenterApi.md#queryHotAddProxyVm) | **GET** /vmware/vcenter/hotadd/vm | Get a list of HotAdd proxy virtual machines
[**queryVcenter**](VmwareVcenterApi.md#queryVcenter) | **GET** /vmware/vcenter | Get list of vCenters
[**setHotAddBandwidth**](VmwareVcenterApi.md#setHotAddBandwidth) | **POST** /vmware/vcenter/{id}/hotadd/bandwidth | Set the ingest and export bandwidth limits for HotAdd with the vCenter
[**setHotAddNetwork**](VmwareVcenterApi.md#setHotAddNetwork) | **POST** /vmware/vcenter/{id}/hotadd/network | Set the user-configured network for HotAdd backup and recovery
[**updateVcenter**](VmwareVcenterApi.md#updateVcenter) | **PUT** /vmware/vcenter/{id} | Update vCenter Server



## createRefresh

> AsyncRequestStatus createRefresh(id)

Refresh vCenter Server metadata

Create a job to refresh the metadata for the specified vCenter Server.

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

let apiInstance = new RubrikRestApi.VmwareVcenterApi();
let id = "id_example"; // String | ID of the vCenter Server.
apiInstance.createRefresh(id, (error, data, response) => {
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
 **id** | **String**| ID of the vCenter Server. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createRefreshVmV1

> createRefreshVmV1(id, body)

Refresh single virtual machine metadata in a vcenter

Refresh the metadata for a single virtual machine controlled by vCenter.

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

let apiInstance = new RubrikRestApi.VmwareVcenterApi();
let id = "id_example"; // String | The ID of the vCenter server that controls the management of the virtual machine whose metadata will be refreshed.
let body = "body_example"; // String | The vCenter managed object ID (MOID) of the virtual machine whose metadata will be refreshed.
apiInstance.createRefreshVmV1(id, body, (error, data, response) => {
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
 **id** | **String**| The ID of the vCenter server that controls the management of the virtual machine whose metadata will be refreshed. | 
 **body** | **String**| The vCenter managed object ID (MOID) of the virtual machine whose metadata will be refreshed. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## createVcenter

> AsyncRequestStatus createVcenter(vcenterConfig)

Add vCenter Server

(DEPRECATED) Create a vCenter Server object by providing the address and account credentials of the vCenter Server. Initiates an asynchronous job to establish a connection with the vCenter Server and retrieve all metadata. Use GET /vcenter/{id}/status to check status. The recommended endpoint is /v2/vmware/vcenter. This endpoint will remain available in future releases despite deprecation.

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

let apiInstance = new RubrikRestApi.VmwareVcenterApi();
let vcenterConfig = new RubrikRestApi.VcenterConfig(); // VcenterConfig | IP address and account credentials of the vCenter Server server, and ID of the managing Rubrik cluster.
apiInstance.createVcenter(vcenterConfig, (error, data, response) => {
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
 **vcenterConfig** | [**VcenterConfig**](VcenterConfig.md)| IP address and account credentials of the vCenter Server server, and ID of the managing Rubrik cluster. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteVcenter

> AsyncRequestStatus deleteVcenter(id)

Remove vCenter Server

Initiates an asynchronous job to remove a vCenter Server object. The vCenter Server cannot have VMs mounted through the Rubrik cluster.

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

let apiInstance = new RubrikRestApi.VmwareVcenterApi();
let id = "id_example"; // String | ID of the vCenter Server. to remove.
apiInstance.deleteVcenter(id, (error, data, response) => {
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
 **id** | **String**| ID of the vCenter Server. to remove. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getHotAddBandwidth

> HotAddBandwidthInfo getHotAddBandwidth(id)

Get the ingest and export bandwidth limits for HotAdd with the vCenter

Get the ingest and export bandwidth limits in Mbps when using HotAdd with the vCenter. These limits are shared across all HotAdd proxies for the Center.

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

let apiInstance = new RubrikRestApi.VmwareVcenterApi();
let id = "id_example"; // String | The ID of the vCenter server from which to derive the number of proxies needed.
apiInstance.getHotAddBandwidth(id, (error, data, response) => {
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
 **id** | **String**| The ID of the vCenter server from which to derive the number of proxies needed. | 

### Return type

[**HotAddBandwidthInfo**](HotAddBandwidthInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getHotAddNetwork

> HotAddNetworkConfigWithName getHotAddNetwork(id)

Retrieve the user-configured network for HotAdd operations

Retrieve the user-configured network for HotAdd backup and recovery operations on VMware on AWS.

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

let apiInstance = new RubrikRestApi.VmwareVcenterApi();
let id = "id_example"; // String | ID of the vCenter server for which the Rubrik cluster is retrieving the configured HotAdd network information.
apiInstance.getHotAddNetwork(id, (error, data, response) => {
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
 **id** | **String**| ID of the vCenter server for which the Rubrik cluster is retrieving the configured HotAdd network information. | 

### Return type

[**HotAddNetworkConfigWithName**](HotAddNetworkConfigWithName.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNetworks

> NetworkInfoListResponse getNetworks(id)

Get the user-configured networks in the vCenter

Get the names and IDs of the user configured networks in the vCenter. This information enables users to choose a desired network for backups to go through for VMware Cloud on AWS setups.

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

let apiInstance = new RubrikRestApi.VmwareVcenterApi();
let id = "id_example"; // String | The ID of the vCenter server for which to retrieve user-configured networks.
apiInstance.getNetworks(id, (error, data, response) => {
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
 **id** | **String**| The ID of the vCenter server for which to retrieve user-configured networks. | 

### Return type

[**NetworkInfoListResponse**](NetworkInfoListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNumProxiesNeeded

> HotAddProxiesNeededInfo getNumProxiesNeeded(id)

Get the number of HotAdd proxies needed for the vCenter

Get the number of HotAdd proxies that need to be deployed to the vCenter to support the maximum number of ingest jobs.

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

let apiInstance = new RubrikRestApi.VmwareVcenterApi();
let id = "id_example"; // String | The ID of the vCenter server for which to get the number of proxies needed.
apiInstance.getNumProxiesNeeded(id, (error, data, response) => {
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
 **id** | **String**| The ID of the vCenter server for which to get the number of proxies needed. | 

### Return type

[**HotAddProxiesNeededInfo**](HotAddProxiesNeededInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVcenter

> VcenterDetail getVcenter(id)

Get the details of a vCenter Server

Retrieve detailed information for a vCenter Server object.

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

let apiInstance = new RubrikRestApi.VmwareVcenterApi();
let id = "id_example"; // String | ID of the vCenter Server.
apiInstance.getVcenter(id, (error, data, response) => {
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
 **id** | **String**| ID of the vCenter Server. | 

### Return type

[**VcenterDetail**](VcenterDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVcenterAsyncRequestStatus

> AsyncRequestStatus getVcenterAsyncRequestStatus(id)

Get vCenter Server async request

Get details about a vcenter related async request.

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

let apiInstance = new RubrikRestApi.VmwareVcenterApi();
let id = "id_example"; // String | ID of the request.
apiInstance.getVcenterAsyncRequestStatus(id, (error, data, response) => {
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
 **id** | **String**| ID of the request. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchVcenter

> VcenterSummary patchVcenter(id, vcenterPatch)

Update the SLA Domain for a vCenter Server

Update the SLA Domain that is configured for a vCenter Server.

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

let apiInstance = new RubrikRestApi.VmwareVcenterApi();
let id = "id_example"; // String | ID of the vCenter Server.
let vcenterPatch = new RubrikRestApi.VcenterPatch(); // VcenterPatch | Object containing updated vCenter Server information.
apiInstance.patchVcenter(id, vcenterPatch, (error, data, response) => {
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
 **id** | **String**| ID of the vCenter Server. | 
 **vcenterPatch** | [**VcenterPatch**](VcenterPatch.md)| Object containing updated vCenter Server information. | 

### Return type

[**VcenterSummary**](VcenterSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queryHotAddProxyVm

> HotAddProxyVmInfoListResponse queryHotAddProxyVm(opts)

Get a list of HotAdd proxy virtual machines

Retrieve summary information for all HotAdd proxy virtual machines.

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

let apiInstance = new RubrikRestApi.VmwareVcenterApi();
let opts = {
  'name': "name_example", // String | Limit the list information to HotAdd proxy virtual machines that match the specified HotAdd proxy virtual machine 'name' value.
  'sortBy': "sortBy_example", // String | Attribute to use to sort the HotAdd proxy virtual machines summary information. Optionally use **_sort_order_** to specify whether to sort in ascending or descending order.
  'sortOrder': "sortOrder_example" // String | Sort order, either ascending or descending.
};
apiInstance.queryHotAddProxyVm(opts, (error, data, response) => {
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
 **name** | **String**| Limit the list information to HotAdd proxy virtual machines that match the specified HotAdd proxy virtual machine &#39;name&#39; value. | [optional] 
 **sortBy** | **String**| Attribute to use to sort the HotAdd proxy virtual machines summary information. Optionally use **_sort_order_** to specify whether to sort in ascending or descending order. | [optional] 
 **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] 

### Return type

[**HotAddProxyVmInfoListResponse**](HotAddProxyVmInfoListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryVcenter

> VcenterSummaryListResponse queryVcenter(opts)

Get list of vCenters

Retrieve information for each managed vCenter, including: ID, managed ID, address, username, SLA ID, and primary cluster ID.

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

let apiInstance = new RubrikRestApi.VmwareVcenterApi();
let opts = {
  'primaryClusterId': "primaryClusterId_example", // String | Limits the information to the Rubrik cluster specified by the value of primary_cluster_id. Use 'local' for the Rubrik cluster that is hosting the current REST API session.
  'snappableStatus': "snappableStatus_example", // String | Determines whether to fetch vCenters with additional privilege checks.
  'ignoreConnectionStatus': true // Boolean | Don't ping vCenters for connection status. The connection_status field in the response is unusable.
};
apiInstance.queryVcenter(opts, (error, data, response) => {
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
 **primaryClusterId** | **String**| Limits the information to the Rubrik cluster specified by the value of primary_cluster_id. Use &#39;local&#39; for the Rubrik cluster that is hosting the current REST API session. | [optional] 
 **snappableStatus** | **String**| Determines whether to fetch vCenters with additional privilege checks. | [optional] 
 **ignoreConnectionStatus** | **Boolean**| Don&#39;t ping vCenters for connection status. The connection_status field in the response is unusable. | [optional] 

### Return type

[**VcenterSummaryListResponse**](VcenterSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setHotAddBandwidth

> setHotAddBandwidth(id, hotAddBandwidthInfo)

Set the ingest and export bandwidth limits for HotAdd with the vCenter

Set the ingest and export bandwidth limits in Mbps when using HotAdd with the vCenter. These limits are shared across all HotAdd proxies for the Center.

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

let apiInstance = new RubrikRestApi.VmwareVcenterApi();
let id = "id_example"; // String | ID of the vCenter server upon which the Rubrik cluster is setting the HotAdd bandwidth limits.
let hotAddBandwidthInfo = new RubrikRestApi.HotAddBandwidthInfo(); // HotAddBandwidthInfo | The ingest and export bandwidth limits for the vCenter.
apiInstance.setHotAddBandwidth(id, hotAddBandwidthInfo, (error, data, response) => {
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
 **id** | **String**| ID of the vCenter server upon which the Rubrik cluster is setting the HotAdd bandwidth limits. | 
 **hotAddBandwidthInfo** | [**HotAddBandwidthInfo**](HotAddBandwidthInfo.md)| The ingest and export bandwidth limits for the vCenter. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## setHotAddNetwork

> setHotAddNetwork(id, hotAddNetworkConfigWithId)

Set the user-configured network for HotAdd backup and recovery

Set the user-configured network for HotAdd backup and recovery operations on VMware on AWS.

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

let apiInstance = new RubrikRestApi.VmwareVcenterApi();
let id = "id_example"; // String | ID of the vCenter server for which the Rubrik cluster is setting the HotAdd network information.
let hotAddNetworkConfigWithId = new RubrikRestApi.HotAddNetworkConfigWithId(); // HotAddNetworkConfigWithId | The information about a static IP address and user-configured vCenter network selected for HotAdd backup and recovery.
apiInstance.setHotAddNetwork(id, hotAddNetworkConfigWithId, (error, data, response) => {
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
 **id** | **String**| ID of the vCenter server for which the Rubrik cluster is setting the HotAdd network information. | 
 **hotAddNetworkConfigWithId** | [**HotAddNetworkConfigWithId**](HotAddNetworkConfigWithId.md)| The information about a static IP address and user-configured vCenter network selected for HotAdd backup and recovery. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## updateVcenter

> VcenterSummary updateVcenter(id, vcenterConfig)

Update vCenter Server

Update the address, username and password of the specified vCenter Server object.

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

let apiInstance = new RubrikRestApi.VmwareVcenterApi();
let id = "id_example"; // String | ID of the vCenter Server.
let vcenterConfig = new RubrikRestApi.VcenterConfig(); // VcenterConfig | Object containing updated vCenter Server information.
apiInstance.updateVcenter(id, vcenterConfig, (error, data, response) => {
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
 **id** | **String**| ID of the vCenter Server. | 
 **vcenterConfig** | [**VcenterConfig**](VcenterConfig.md)| Object containing updated vCenter Server information. | 

### Return type

[**VcenterSummary**](VcenterSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

