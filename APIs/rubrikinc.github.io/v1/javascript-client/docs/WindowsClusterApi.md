# RubrikRestApi.WindowsClusterApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getWindowsCluster**](WindowsClusterApi.md#getWindowsCluster) | **GET** /windows_cluster/{id} | Get detailed information for a Windows cluster
[**queryWindowsCluster**](WindowsClusterApi.md#queryWindowsCluster) | **GET** /windows_cluster | Get summary information for Windows clusters



## getWindowsCluster

> WindowsClusterDetail getWindowsCluster(id)

Get detailed information for a Windows cluster

Returns a detailed view of a Windows server failover cluster.

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

let apiInstance = new RubrikRestApi.WindowsClusterApi();
let id = "id_example"; // String | ID of the Windows cluster.
apiInstance.getWindowsCluster(id, (error, data, response) => {
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
 **id** | **String**| ID of the Windows cluster. | 

### Return type

[**WindowsClusterDetail**](WindowsClusterDetail.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryWindowsCluster

> WindowsClusterSummaryListResponse queryWindowsCluster(opts)

Get summary information for Windows clusters

Returns a list of summary information for Windows server failover clusters.

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

let apiInstance = new RubrikRestApi.WindowsClusterApi();
let opts = {
  'primaryClusterId': "primaryClusterId_example", // String | Filter by primary_cluster_id. Use **local** for the local cluster.
  'isAgentless': true, // Boolean | Filter by is_agentless flag.
  'snappableStatus': "snappableStatus_example" // String | Determines whether Windows clusters are fetched with additional privilege checks.
};
apiInstance.queryWindowsCluster(opts, (error, data, response) => {
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
 **primaryClusterId** | **String**| Filter by primary_cluster_id. Use **local** for the local cluster. | [optional] 
 **isAgentless** | **Boolean**| Filter by is_agentless flag. | [optional] 
 **snappableStatus** | **String**| Determines whether Windows clusters are fetched with additional privilege checks. | [optional] 

### Return type

[**WindowsClusterSummaryListResponse**](WindowsClusterSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

