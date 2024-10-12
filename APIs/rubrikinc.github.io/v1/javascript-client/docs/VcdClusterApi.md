# RubrikRestApi.VcdClusterApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createVcdClusterV1**](VcdClusterApi.md#createVcdClusterV1) | **POST** /vcd/cluster | Add a vCD Cluster
[**deleteVcdClusterV1**](VcdClusterApi.md#deleteVcdClusterV1) | **DELETE** /vcd/cluster/{id} | Remove vCD Cluster
[**getVcdClusterAsyncRequestStatusV1**](VcdClusterApi.md#getVcdClusterAsyncRequestStatusV1) | **GET** /vcd/cluster/request/{id} | Get vCD Cluster job status
[**getVcdClusterV1**](VcdClusterApi.md#getVcdClusterV1) | **GET** /vcd/cluster/{id} | Get vCD Cluster details
[**queryVcdClusterV1**](VcdClusterApi.md#queryVcdClusterV1) | **GET** /vcd/cluster | Get summary for all vCD Clusters
[**queryVcdVimServerV1**](VcdClusterApi.md#queryVcdVimServerV1) | **GET** /vcd/cluster/{id}/vimserver | Get VimServers of a vCD Cluster
[**refreshVcdClusterV1**](VcdClusterApi.md#refreshVcdClusterV1) | **POST** /vcd/cluster/{id}/refresh | Refresh a vCD Cluster
[**updateVcdClusterV1**](VcdClusterApi.md#updateVcdClusterV1) | **PATCH** /vcd/cluster/{id} | Change vCD Cluster object



## createVcdClusterV1

> AsyncRequestStatus createVcdClusterV1(vcdClusterConfig)

Add a vCD Cluster

Create a vCD Cluster object by providing the address of the vCD Cluster and the credentials for an account on the vCD Cluster that has administrator privileges. This request initiates an asynchronous job to connect with the vCD Cluster and retrieve the required metadata.

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

let apiInstance = new RubrikRestApi.VcdClusterApi();
let vcdClusterConfig = new RubrikRestApi.VcdClusterConfig(); // VcdClusterConfig | IP address and account credentials of the vCD Cluster, and ID of the managing Rubrik cluster.
apiInstance.createVcdClusterV1(vcdClusterConfig, (error, data, response) => {
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
 **vcdClusterConfig** | [**VcdClusterConfig**](VcdClusterConfig.md)| IP address and account credentials of the vCD Cluster, and ID of the managing Rubrik cluster. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteVcdClusterV1

> AsyncRequestStatus deleteVcdClusterV1(id)

Remove vCD Cluster

Start an asynchronous job to remove a vCD Cluster object.

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

let apiInstance = new RubrikRestApi.VcdClusterApi();
let id = "id_example"; // String | ID assigned to a vCD Cluster object.
apiInstance.deleteVcdClusterV1(id, (error, data, response) => {
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
 **id** | **String**| ID assigned to a vCD Cluster object. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVcdClusterAsyncRequestStatusV1

> AsyncRequestStatus getVcdClusterAsyncRequestStatusV1(id)

Get vCD Cluster job status

Retrieve the details of a specified asynchronous job for a vCD Cluster.

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

let apiInstance = new RubrikRestApi.VcdClusterApi();
let id = "id_example"; // String | ID assigned to an asynchronous job.
apiInstance.getVcdClusterAsyncRequestStatusV1(id, (error, data, response) => {
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
 **id** | **String**| ID assigned to an asynchronous job. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVcdClusterV1

> VcdClusterDetail getVcdClusterV1(id)

Get vCD Cluster details

Retrieve detailed information for a vCD Cluster object.

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

let apiInstance = new RubrikRestApi.VcdClusterApi();
let id = "id_example"; // String | ID assigned to a vCD Cluster object.
apiInstance.getVcdClusterV1(id, (error, data, response) => {
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
 **id** | **String**| ID assigned to a vCD Cluster object. | 

### Return type

[**VcdClusterDetail**](VcdClusterDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryVcdClusterV1

> VcdClusterSummaryListResponse queryVcdClusterV1(opts)

Get summary for all vCD Clusters

Retrieve summary information for all vCD cluster objects.

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

let apiInstance = new RubrikRestApi.VcdClusterApi();
let opts = {
  'name': "name_example", // String | Search for a vCD Cluster object by name.
  'status': "status_example", // String | Filter the results using the status value of the vCD Cluster objects.
  'sortBy': "sortBy_example", // String | Attribute to sort the results on.
  'sortOrder': "'asc'" // String | Order for sorting the results, either ascending or descending.
};
apiInstance.queryVcdClusterV1(opts, (error, data, response) => {
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
 **name** | **String**| Search for a vCD Cluster object by name. | [optional] 
 **status** | **String**| Filter the results using the status value of the vCD Cluster objects. | [optional] 
 **sortBy** | **String**| Attribute to sort the results on. | [optional] 
 **sortOrder** | **String**| Order for sorting the results, either ascending or descending. | [optional] [default to &#39;asc&#39;]

### Return type

[**VcdClusterSummaryListResponse**](VcdClusterSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryVcdVimServerV1

> VimserverSummaryListResponse queryVcdVimServerV1(id, opts)

Get VimServers of a vCD Cluster

Retrieves the VimServer representation of the vCenter Servers that are attached to a specified vCD Cluster object.

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

let apiInstance = new RubrikRestApi.VcdClusterApi();
let id = "id_example"; // String | ID assigned to a vCD Cluster object.
let opts = {
  'sortBy': "sortBy_example", // String | Attribute to sort the results on.
  'sortOrder': "'asc'" // String | Order for sorting the results, either ascending or descending.
};
apiInstance.queryVcdVimServerV1(id, opts, (error, data, response) => {
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
 **id** | **String**| ID assigned to a vCD Cluster object. | 
 **sortBy** | **String**| Attribute to sort the results on. | [optional] 
 **sortOrder** | **String**| Order for sorting the results, either ascending or descending. | [optional] [default to &#39;asc&#39;]

### Return type

[**VimserverSummaryListResponse**](VimserverSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## refreshVcdClusterV1

> AsyncRequestStatus refreshVcdClusterV1(id)

Refresh a vCD Cluster

Start an asynchronous job to refresh the metadata for a specified vCD Cluster object.

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

let apiInstance = new RubrikRestApi.VcdClusterApi();
let id = "id_example"; // String | ID assigned to a vCD Cluster object.
apiInstance.refreshVcdClusterV1(id, (error, data, response) => {
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
 **id** | **String**| ID assigned to a vCD Cluster object. | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateVcdClusterV1

> VcdClusterDetail updateVcdClusterV1(id, vcdClusterPatch)

Change vCD Cluster object

Modify the hostname and credentials of a specified vCD Cluster object.

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

let apiInstance = new RubrikRestApi.VcdClusterApi();
let id = "id_example"; // String | ID assigned to a vCD Cluster object.
let vcdClusterPatch = new RubrikRestApi.VcdClusterPatch(); // VcdClusterPatch | Updated hostname and credentials for a specified vCD Cluster object.
apiInstance.updateVcdClusterV1(id, vcdClusterPatch, (error, data, response) => {
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
 **id** | **String**| ID assigned to a vCD Cluster object. | 
 **vcdClusterPatch** | [**VcdClusterPatch**](VcdClusterPatch.md)| Updated hostname and credentials for a specified vCD Cluster object. | 

### Return type

[**VcdClusterDetail**](VcdClusterDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

