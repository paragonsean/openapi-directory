# RubrikRestApi.VmwareComputeClusterApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAsyncRequestStatusForComputeCluster**](VmwareComputeClusterApi.md#getAsyncRequestStatusForComputeCluster) | **GET** /vmware/compute_cluster/request/{id} | Get asynchronous request details for VMware cluster
[**getComputeCluster**](VmwareComputeClusterApi.md#getComputeCluster) | **GET** /vmware/compute_cluster/{id} | Get details for the compute cluster
[**getIoFilters**](VmwareComputeClusterApi.md#getIoFilters) | **GET** /vmware/compute_cluster/{id}/io_filter | Get the ioFilters on the VMware compute cluster with a specific ID
[**installIoFilter**](VmwareComputeClusterApi.md#installIoFilter) | **POST** /vmware/compute_cluster/{id}/install_io_filter | Install the Rubrik ioFilter to the VMware cluster with a specific ID
[**queryComputeCluster**](VmwareComputeClusterApi.md#queryComputeCluster) | **GET** /vmware/compute_cluster | Get all the clusters belonging to this datacenter
[**uninstallIoFilter**](VmwareComputeClusterApi.md#uninstallIoFilter) | **POST** /vmware/compute_cluster/{id}/uninstall_io_filter | Uninstall the Rubrik ioFilter from the VMware cluster with a specific ID
[**updateComputeCluster**](VmwareComputeClusterApi.md#updateComputeCluster) | **PATCH** /vmware/compute_cluster/{id} | Modify information for a VMware compute cluster
[**upgradeIoFilter**](VmwareComputeClusterApi.md#upgradeIoFilter) | **POST** /vmware/compute_cluster/{id}/upgrade_io_filter | Upgrade the Rubrik ioFilter for the VMware cluster with a specific ID



## getAsyncRequestStatusForComputeCluster

> AsyncRequestStatus getAsyncRequestStatusForComputeCluster(id)

Get asynchronous request details for VMware cluster

Get the details of an asynchronous request that involves a VMware compute cluster.

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

let apiInstance = new RubrikRestApi.VmwareComputeClusterApi();
let id = "id_example"; // String | ID of an asynchronous request.
apiInstance.getAsyncRequestStatusForComputeCluster(id, (error, data, response) => {
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
 **id** | **String**| ID of an asynchronous request. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getComputeCluster

> ComputeClusterDetail getComputeCluster(id)

Get details for the compute cluster

Get details for the compute cluster.

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

let apiInstance = new RubrikRestApi.VmwareComputeClusterApi();
let id = "id_example"; // String | ID of the compute cluster.
apiInstance.getComputeCluster(id, (error, data, response) => {
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
 **id** | **String**| ID of the compute cluster. | 

### Return type

[**ComputeClusterDetail**](ComputeClusterDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getIoFilters

> IoFilterSummaryListResponse getIoFilters(id)

Get the ioFilters on the VMware compute cluster with a specific ID

Get the summary of the ioFilters on the VMware compute cluster with a specific ID.

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

let apiInstance = new RubrikRestApi.VmwareComputeClusterApi();
let id = "id_example"; // String | ID of the VMware compute cluster.
apiInstance.getIoFilters(id, (error, data, response) => {
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
 **id** | **String**| ID of the VMware compute cluster. | 

### Return type

[**IoFilterSummaryListResponse**](IoFilterSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## installIoFilter

> AsyncRequestStatus installIoFilter(id, fullyQualifiedDomainNameInfo)

Install the Rubrik ioFilter to the VMware cluster with a specific ID

Install the latest version of Rubrik ioFilter to the VMware cluster with a specific ID. The cluster must be in maintenance mode to install the ioFilter successfully. The vCenter of the VMware compute cluster must be of version 6.7 and above.

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

let apiInstance = new RubrikRestApi.VmwareComputeClusterApi();
let id = "id_example"; // String | ID of the VMware compute cluster.
let fullyQualifiedDomainNameInfo = new RubrikRestApi.FullyQualifiedDomainNameInfo(); // FullyQualifiedDomainNameInfo | 
apiInstance.installIoFilter(id, fullyQualifiedDomainNameInfo, (error, data, response) => {
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
 **id** | **String**| ID of the VMware compute cluster. | 
 **fullyQualifiedDomainNameInfo** | [**FullyQualifiedDomainNameInfo**](FullyQualifiedDomainNameInfo.md)|  | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## queryComputeCluster

> ComputeClusterSummaryListResponse queryComputeCluster(opts)

Get all the clusters belonging to this datacenter

Get all the clusters belonging to this datacenter.

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

let apiInstance = new RubrikRestApi.VmwareComputeClusterApi();
let opts = {
  'datacenterId': "datacenterId_example", // String | Filter clusters on data center ID.
  'primaryClusterId': "primaryClusterId_example", // String | Filter on a primary cluster ID. Also accepts value 'local'.
  'snappableStatus': "snappableStatus_example" // String | Determines whether to fetch Compute Clusters with additional privilege checks.
};
apiInstance.queryComputeCluster(opts, (error, data, response) => {
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
 **datacenterId** | **String**| Filter clusters on data center ID. | [optional] 
 **primaryClusterId** | **String**| Filter on a primary cluster ID. Also accepts value &#39;local&#39;. | [optional] 
 **snappableStatus** | **String**| Determines whether to fetch Compute Clusters with additional privilege checks. | [optional] 

### Return type

[**ComputeClusterSummaryListResponse**](ComputeClusterSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## uninstallIoFilter

> AsyncRequestStatus uninstallIoFilter(id)

Uninstall the Rubrik ioFilter from the VMware cluster with a specific ID

Uninstall the Rubrik ioFilter from the VMware cluster with a specific ID. The cluster must be in maintenance mode to uninstall the ioFilter successfully. The vCenter of the VMware compute cluster must be of version 6.7 and above.

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

let apiInstance = new RubrikRestApi.VmwareComputeClusterApi();
let id = "id_example"; // String | ID of the VMware compute cluster.
apiInstance.uninstallIoFilter(id, (error, data, response) => {
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
 **id** | **String**| ID of the VMware compute cluster. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateComputeCluster

> ComputeClusterDetail updateComputeCluster(id, computeClusterUpdate)

Modify information for a VMware compute cluster

Update the configuredSlaDomainId for a VMware compute cluster with a specific ID.

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

let apiInstance = new RubrikRestApi.VmwareComputeClusterApi();
let id = "id_example"; // String | ID of the compute cluster.
let computeClusterUpdate = new RubrikRestApi.ComputeClusterUpdate(); // ComputeClusterUpdate | Object with changes for the Compute Cluster information.
apiInstance.updateComputeCluster(id, computeClusterUpdate, (error, data, response) => {
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
 **id** | **String**| ID of the compute cluster. | 
 **computeClusterUpdate** | [**ComputeClusterUpdate**](ComputeClusterUpdate.md)| Object with changes for the Compute Cluster information. | 

### Return type

[**ComputeClusterDetail**](ComputeClusterDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## upgradeIoFilter

> AsyncRequestStatus upgradeIoFilter(id, fullyQualifiedDomainNameInfo)

Upgrade the Rubrik ioFilter for the VMware cluster with a specific ID

Upgrade the Rubrik ioFilter for a VMware cluster with a specific ID. The cluster must be in maintenance mode to upgrade the ioFilter successfully. The vCenter of the VMware compute cluster must be of version 6.7 and above.

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

let apiInstance = new RubrikRestApi.VmwareComputeClusterApi();
let id = "id_example"; // String | ID of the VMware compute cluster.
let fullyQualifiedDomainNameInfo = new RubrikRestApi.FullyQualifiedDomainNameInfo(); // FullyQualifiedDomainNameInfo | 
apiInstance.upgradeIoFilter(id, fullyQualifiedDomainNameInfo, (error, data, response) => {
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
 **id** | **String**| ID of the VMware compute cluster. | 
 **fullyQualifiedDomainNameInfo** | [**FullyQualifiedDomainNameInfo**](FullyQualifiedDomainNameInfo.md)|  | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

