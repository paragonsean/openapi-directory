# SiteRecoveryManagementClient.ReplicationProtectableItemsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**replicationProtectableItemsGet**](ReplicationProtectableItemsApi.md#replicationProtectableItemsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectableItems/{protectableItemName} | Gets the details of a protectable item.
[**replicationProtectableItemsListByReplicationProtectionContainers**](ReplicationProtectableItemsApi.md#replicationProtectableItemsListByReplicationProtectionContainers) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectableItems | Gets the list of protectable items.



## replicationProtectableItemsGet

> ProtectableItem replicationProtectableItemsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, protectableItemName)

Gets the details of a protectable item.

The operation to get the details of a protectable item.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectableItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
let protectableItemName = "protectableItemName_example"; // String | Protectable item name.
apiInstance.replicationProtectableItemsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, protectableItemName, (error, data, response) => {
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
 **protectionContainerName** | **String**| Protection container name. | 
 **protectableItemName** | **String**| Protectable item name. | 

### Return type

[**ProtectableItem**](ProtectableItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationProtectableItemsListByReplicationProtectionContainers

> ProtectableItemCollection replicationProtectableItemsListByReplicationProtectionContainers(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName)

Gets the list of protectable items.

Lists the protectable items in a protection container.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectableItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
apiInstance.replicationProtectableItemsListByReplicationProtectionContainers(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, (error, data, response) => {
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
 **protectionContainerName** | **String**| Protection container name. | 

### Return type

[**ProtectableItemCollection**](ProtectableItemCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

