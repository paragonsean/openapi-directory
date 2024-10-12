# ServiceFabricManagementClient.ClusterCreateOperationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clustersCreate**](ClusterCreateOperationApi.md#clustersCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters/{clusterName} | 



## clustersCreate

> Cluster clustersCreate(resourceGroupName, clusterName, apiVersion, subscriptionId, parameters)



Create cluster resource

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ClusterCreateOperationApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the resource belongs or get created
let clusterName = "clusterName_example"; // String | The name of the cluster resource
let apiVersion = "apiVersion_example"; // String | The version of the ServiceFabric resource provider api
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
let parameters = new ServiceFabricManagementClient.Cluster(); // Cluster | Put Request
apiInstance.clustersCreate(resourceGroupName, clusterName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group to which the resource belongs or get created | 
 **clusterName** | **String**| The name of the cluster resource | 
 **apiVersion** | **String**| The version of the ServiceFabric resource provider api | 
 **subscriptionId** | **String**| The customer subscription identifier | 
 **parameters** | [**Cluster**](Cluster.md)| Put Request | 

### Return type

[**Cluster**](Cluster.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

