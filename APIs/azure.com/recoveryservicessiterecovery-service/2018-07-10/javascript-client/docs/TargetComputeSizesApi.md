# SiteRecoveryManagementClient.TargetComputeSizesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**targetComputeSizesListByReplicationProtectedItems**](TargetComputeSizesApi.md#targetComputeSizesListByReplicationProtectedItems) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/targetComputeSizes | Gets the list of target compute sizes for the replication protected item.



## targetComputeSizesListByReplicationProtectedItems

> TargetComputeSizeCollection targetComputeSizesListByReplicationProtectedItems(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName)

Gets the list of target compute sizes for the replication protected item.

Lists the available target compute sizes for a replication protected item.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.TargetComputeSizesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | protection container name.
let replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
apiInstance.targetComputeSizesListByReplicationProtectedItems(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **fabricName** | **String**| Fabric name. | 
 **protectionContainerName** | **String**| protection container name. | 
 **replicatedProtectedItemName** | **String**| Replication protected item name. | 

### Return type

[**TargetComputeSizeCollection**](TargetComputeSizeCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

