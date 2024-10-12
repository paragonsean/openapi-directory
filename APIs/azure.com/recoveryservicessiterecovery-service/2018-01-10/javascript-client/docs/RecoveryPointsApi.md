# SiteRecoveryManagementClient.RecoveryPointsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recoveryPointsGet**](RecoveryPointsApi.md#recoveryPointsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/recoveryPoints/{recoveryPointName} | Get a recovery point.
[**recoveryPointsListByReplicationProtectedItems**](RecoveryPointsApi.md#recoveryPointsListByReplicationProtectedItems) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/recoveryPoints | Get recovery points for a replication protected item.



## recoveryPointsGet

> RecoveryPoint recoveryPointsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, recoveryPointName)

Get a recovery point.

Get the details of specified recovery point.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.RecoveryPointsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | The fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | The protection container name.
let replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | The replication protected item's name.
let recoveryPointName = "recoveryPointName_example"; // String | The recovery point name.
apiInstance.recoveryPointsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, recoveryPointName, (error, data, response) => {
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
 **fabricName** | **String**| The fabric name. | 
 **protectionContainerName** | **String**| The protection container name. | 
 **replicatedProtectedItemName** | **String**| The replication protected item&#39;s name. | 
 **recoveryPointName** | **String**| The recovery point name. | 

### Return type

[**RecoveryPoint**](RecoveryPoint.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recoveryPointsListByReplicationProtectedItems

> RecoveryPointCollection recoveryPointsListByReplicationProtectedItems(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName)

Get recovery points for a replication protected item.

Lists the available recovery points for a replication protected item.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.RecoveryPointsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | The fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | The protection container name.
let replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | The replication protected item's name.
apiInstance.recoveryPointsListByReplicationProtectedItems(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, (error, data, response) => {
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
 **fabricName** | **String**| The fabric name. | 
 **protectionContainerName** | **String**| The protection container name. | 
 **replicatedProtectedItemName** | **String**| The replication protected item&#39;s name. | 

### Return type

[**RecoveryPointCollection**](RecoveryPointCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

