# ServiceFabricManagementClient.ClusterDeleteOperationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clustersDelete**](ClusterDeleteOperationApi.md#clustersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName} | 



## clustersDelete

> clustersDelete(resourceGroupName, clusterName, apiVersion, subscriptionId)



Delete cluster resource

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ClusterDeleteOperationApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the resource belongs or get created
let clusterName = "clusterName_example"; // String | The name of the cluster resource
let apiVersion = "apiVersion_example"; // String | The version of the ServiceFabric resource provider api
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
apiInstance.clustersDelete(resourceGroupName, clusterName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group to which the resource belongs or get created | 
 **clusterName** | **String**| The name of the cluster resource | 
 **apiVersion** | **String**| The version of the ServiceFabric resource provider api | 
 **subscriptionId** | **String**| The customer subscription identifier | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

