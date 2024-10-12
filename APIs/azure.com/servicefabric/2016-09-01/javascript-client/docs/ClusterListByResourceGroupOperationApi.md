# ServiceFabricManagementClient.ClusterListByResourceGroupOperationApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clustersListByResourceGroup**](ClusterListByResourceGroupOperationApi.md#clustersListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.ServiceFabric/clusters | 



## clustersListByResourceGroup

> ClusterListResult clustersListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



List cluster resource by resource group

### Example

```javascript
import ServiceFabricManagementClient from 'service_fabric_management_client';
let defaultClient = ServiceFabricManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceFabricManagementClient.ClusterListByResourceGroupOperationApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the resource belongs or get created
let apiVersion = "apiVersion_example"; // String | The version of the ServiceFabric resource provider api
let subscriptionId = "subscriptionId_example"; // String | The customer subscription identifier
apiInstance.clustersListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the ServiceFabric resource provider api | 
 **subscriptionId** | **String**| The customer subscription identifier | 

### Return type

[**ClusterListResult**](ClusterListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

