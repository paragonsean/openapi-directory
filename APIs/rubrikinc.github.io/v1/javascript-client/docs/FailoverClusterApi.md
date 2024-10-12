# RubrikRestApi.FailoverClusterApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulkDeleteFailoverCluster**](FailoverClusterApi.md#bulkDeleteFailoverCluster) | **DELETE** /failover_cluster/bulk | Delete the provided failover clusters
[**createFailoverCluster**](FailoverClusterApi.md#createFailoverCluster) | **POST** /failover_cluster | Create a failover cluster
[**deleteFailoverCluster**](FailoverClusterApi.md#deleteFailoverCluster) | **DELETE** /failover_cluster/{id} | Delete a failover cluster
[**getFailoverCluster**](FailoverClusterApi.md#getFailoverCluster) | **GET** /failover_cluster/{id} | Get details of a failover cluster
[**queryFailoverCluster**](FailoverClusterApi.md#queryFailoverCluster) | **GET** /failover_cluster | Get a summary of all failover clusters
[**updateFailoverCluster**](FailoverClusterApi.md#updateFailoverCluster) | **PATCH** /failover_cluster/{id} | Update a failover cluster



## bulkDeleteFailoverCluster

> bulkDeleteFailoverCluster(ids, opts)

Delete the provided failover clusters

Delete the provided failover clusters.

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

let apiInstance = new RubrikRestApi.FailoverClusterApi();
let ids = ["null"]; // [String] | The ID of each failover cluster to delete.
let opts = {
  'preserveSnapshots': true // Boolean | Specifies whether to preserve the snapshots of the fileset which belong to a failover cluster application. When this value is 'true,' the snapshots are preserved. The default value is 'true'.
};
apiInstance.bulkDeleteFailoverCluster(ids, opts, (error, data, response) => {
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
 **ids** | [**[String]**](String.md)| The ID of each failover cluster to delete. | 
 **preserveSnapshots** | **Boolean**| Specifies whether to preserve the snapshots of the fileset which belong to a failover cluster application. When this value is &#39;true,&#39; the snapshots are preserved. The default value is &#39;true&#39;. | [optional] 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createFailoverCluster

> FailoverClusterDetail createFailoverCluster(failoverClusterConfig)

Create a failover cluster

Create a failover cluster.

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

let apiInstance = new RubrikRestApi.FailoverClusterApi();
let failoverClusterConfig = new RubrikRestApi.FailoverClusterConfig(); // FailoverClusterConfig | Create configuration parameters for a failover cluster.
apiInstance.createFailoverCluster(failoverClusterConfig, (error, data, response) => {
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
 **failoverClusterConfig** | [**FailoverClusterConfig**](FailoverClusterConfig.md)| Create configuration parameters for a failover cluster. | 

### Return type

[**FailoverClusterDetail**](FailoverClusterDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteFailoverCluster

> deleteFailoverCluster(id, opts)

Delete a failover cluster

Delete a failover cluster.

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

let apiInstance = new RubrikRestApi.FailoverClusterApi();
let id = "id_example"; // String | ID of the failover cluster.
let opts = {
  'preserveSnapshots': true // Boolean | A Boolean that specifies whether to preserve the snapshots of the fileset which belong to a failover cluster application. When this value is 'true,' the snapshots are preserved. The default value is 'true'.
};
apiInstance.deleteFailoverCluster(id, opts, (error, data, response) => {
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
 **id** | **String**| ID of the failover cluster. | 
 **preserveSnapshots** | **Boolean**| A Boolean that specifies whether to preserve the snapshots of the fileset which belong to a failover cluster application. When this value is &#39;true,&#39; the snapshots are preserved. The default value is &#39;true&#39;. | [optional] 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getFailoverCluster

> FailoverClusterDetail getFailoverCluster(id)

Get details of a failover cluster

Get details of a failover cluster.

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

let apiInstance = new RubrikRestApi.FailoverClusterApi();
let id = "id_example"; // String | ID of the failover cluster.
apiInstance.getFailoverCluster(id, (error, data, response) => {
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
 **id** | **String**| ID of the failover cluster. | 

### Return type

[**FailoverClusterDetail**](FailoverClusterDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryFailoverCluster

> FailoverClusterSummaryListResponse queryFailoverCluster(opts)

Get a summary of all failover clusters

Get a summary of all failover clusters.

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

let apiInstance = new RubrikRestApi.FailoverClusterApi();
let opts = {
  'name': "name_example", // String | Filter a response by making an infix comparison of the failover cluster name in the response, with the specified value.
  'operatingSystemType': "operatingSystemType_example", // String | Filter a response based on the operating system type.
  'slaAssignment': "slaAssignment_example", // String | Limit a response to the results that have the specified SLA Domain assignment type.
  'primaryClusterId': "primaryClusterId_example", // String | Limit a response to the results that have the specified primary cluster value.
  'limit': 56, // Number | Limit the summary information to a specified maximum number of matches. Optionally, use with offset to start the count at a specified point. Optionally, use with sort_by to perform sort on given attributes. Include sort_order to determine the ascending or descending direction of the sort.
  'offset': 56, // Number | Starting position in the list of matches. The response includes the specified numbered entry and all higher numbered entries. Use with limit to retrieve the response as smaller groups of entries, for example for paging of results.
  'sortBy': "sortBy_example", // String | Specifies a comma-separated list of attributes to use in sorting the matches. Performs an ASCII sort of the values in the response using each specified attribute, in the order specified.
  'sortOrder': "'asc'" // String | Sort order, either ascending or descending.
};
apiInstance.queryFailoverCluster(opts, (error, data, response) => {
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
 **name** | **String**| Filter a response by making an infix comparison of the failover cluster name in the response, with the specified value. | [optional] 
 **operatingSystemType** | **String**| Filter a response based on the operating system type. | [optional] 
 **slaAssignment** | **String**| Limit a response to the results that have the specified SLA Domain assignment type. | [optional] 
 **primaryClusterId** | **String**| Limit a response to the results that have the specified primary cluster value. | [optional] 
 **limit** | **Number**| Limit the summary information to a specified maximum number of matches. Optionally, use with offset to start the count at a specified point. Optionally, use with sort_by to perform sort on given attributes. Include sort_order to determine the ascending or descending direction of the sort. | [optional] 
 **offset** | **Number**| Starting position in the list of matches. The response includes the specified numbered entry and all higher numbered entries. Use with limit to retrieve the response as smaller groups of entries, for example for paging of results. | [optional] 
 **sortBy** | **String**| Specifies a comma-separated list of attributes to use in sorting the matches. Performs an ASCII sort of the values in the response using each specified attribute, in the order specified. | [optional] 
 **sortOrder** | **String**| Sort order, either ascending or descending. | [optional] [default to &#39;asc&#39;]

### Return type

[**FailoverClusterSummaryListResponse**](FailoverClusterSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateFailoverCluster

> FailoverClusterDetail updateFailoverCluster(id, failoverClusterConfig)

Update a failover cluster

Update failover cluster with specified properties.

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

let apiInstance = new RubrikRestApi.FailoverClusterApi();
let id = "id_example"; // String | ID of failover cluster.
let failoverClusterConfig = new RubrikRestApi.FailoverClusterConfig(); // FailoverClusterConfig | Properties to update.
apiInstance.updateFailoverCluster(id, failoverClusterConfig, (error, data, response) => {
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
 **id** | **String**| ID of failover cluster. | 
 **failoverClusterConfig** | [**FailoverClusterConfig**](FailoverClusterConfig.md)| Properties to update. | 

### Return type

[**FailoverClusterDetail**](FailoverClusterDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

