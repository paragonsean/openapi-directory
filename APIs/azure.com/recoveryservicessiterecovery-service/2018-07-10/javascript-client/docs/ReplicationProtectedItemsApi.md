# SiteRecoveryManagementClient.ReplicationProtectedItemsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**replicationProtectedItemsAddDisks**](ReplicationProtectedItemsApi.md#replicationProtectedItemsAddDisks) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/addDisks | Add disk(s) for protection.
[**replicationProtectedItemsApplyRecoveryPoint**](ReplicationProtectedItemsApi.md#replicationProtectedItemsApplyRecoveryPoint) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/applyRecoveryPoint | Change or apply recovery point.
[**replicationProtectedItemsCreate**](ReplicationProtectedItemsApi.md#replicationProtectedItemsCreate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName} | Enables protection.
[**replicationProtectedItemsDelete**](ReplicationProtectedItemsApi.md#replicationProtectedItemsDelete) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/remove | Disables protection.
[**replicationProtectedItemsFailoverCommit**](ReplicationProtectedItemsApi.md#replicationProtectedItemsFailoverCommit) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/failoverCommit | Execute commit failover
[**replicationProtectedItemsGet**](ReplicationProtectedItemsApi.md#replicationProtectedItemsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName} | Gets the details of a Replication protected item.
[**replicationProtectedItemsList**](ReplicationProtectedItemsApi.md#replicationProtectedItemsList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationProtectedItems | Gets the list of replication protected items.
[**replicationProtectedItemsListByReplicationProtectionContainers**](ReplicationProtectedItemsApi.md#replicationProtectedItemsListByReplicationProtectionContainers) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems | Gets the list of Replication protected items.
[**replicationProtectedItemsPlannedFailover**](ReplicationProtectedItemsApi.md#replicationProtectedItemsPlannedFailover) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/plannedFailover | Execute planned failover
[**replicationProtectedItemsPurge**](ReplicationProtectedItemsApi.md#replicationProtectedItemsPurge) | **DELETE** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName} | Purges protection.
[**replicationProtectedItemsRemoveDisks**](ReplicationProtectedItemsApi.md#replicationProtectedItemsRemoveDisks) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/removeDisks | Removes disk(s).
[**replicationProtectedItemsRepairReplication**](ReplicationProtectedItemsApi.md#replicationProtectedItemsRepairReplication) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/repairReplication | Resynchronize or repair replication.
[**replicationProtectedItemsReprotect**](ReplicationProtectedItemsApi.md#replicationProtectedItemsReprotect) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/reProtect | Execute Reverse Replication\\Reprotect
[**replicationProtectedItemsResolveHealthErrors**](ReplicationProtectedItemsApi.md#replicationProtectedItemsResolveHealthErrors) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/ResolveHealthErrors | Resolve health errors.
[**replicationProtectedItemsTestFailover**](ReplicationProtectedItemsApi.md#replicationProtectedItemsTestFailover) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/testFailover | Execute test failover
[**replicationProtectedItemsTestFailoverCleanup**](ReplicationProtectedItemsApi.md#replicationProtectedItemsTestFailoverCleanup) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/testFailoverCleanup | Execute test failover cleanup.
[**replicationProtectedItemsUnplannedFailover**](ReplicationProtectedItemsApi.md#replicationProtectedItemsUnplannedFailover) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName}/unplannedFailover | Execute unplanned failover
[**replicationProtectedItemsUpdate**](ReplicationProtectedItemsApi.md#replicationProtectedItemsUpdate) | **PATCH** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicatedProtectedItemName} | Updates protection.
[**replicationProtectedItemsUpdateMobilityService**](ReplicationProtectedItemsApi.md#replicationProtectedItemsUpdateMobilityService) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{resourceName}/replicationFabrics/{fabricName}/replicationProtectionContainers/{protectionContainerName}/replicationProtectedItems/{replicationProtectedItemName}/updateMobilityService | Update the mobility service on a protected item.



## replicationProtectedItemsAddDisks

> ReplicationProtectedItem replicationProtectedItemsAddDisks(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, addDisksInput)

Add disk(s) for protection.

Operation to add disks(s) to the replication protected item.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Unique fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
let replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
let addDisksInput = new SiteRecoveryManagementClient.AddDisksInput(); // AddDisksInput | Add disks input.
apiInstance.replicationProtectedItemsAddDisks(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, addDisksInput, (error, data, response) => {
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
 **fabricName** | **String**| Unique fabric name. | 
 **protectionContainerName** | **String**| Protection container name. | 
 **replicatedProtectedItemName** | **String**| Replication protected item name. | 
 **addDisksInput** | [**AddDisksInput**](AddDisksInput.md)| Add disks input. | 

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replicationProtectedItemsApplyRecoveryPoint

> ReplicationProtectedItem replicationProtectedItemsApplyRecoveryPoint(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, applyRecoveryPointInput)

Change or apply recovery point.

The operation to change the recovery point of a failed over replication protected item.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | The ARM fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | The protection container name.
let replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | The replicated protected item's name.
let applyRecoveryPointInput = new SiteRecoveryManagementClient.ApplyRecoveryPointInput(); // ApplyRecoveryPointInput | The ApplyRecoveryPointInput.
apiInstance.replicationProtectedItemsApplyRecoveryPoint(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, applyRecoveryPointInput, (error, data, response) => {
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
 **fabricName** | **String**| The ARM fabric name. | 
 **protectionContainerName** | **String**| The protection container name. | 
 **replicatedProtectedItemName** | **String**| The replicated protected item&#39;s name. | 
 **applyRecoveryPointInput** | [**ApplyRecoveryPointInput**](ApplyRecoveryPointInput.md)| The ApplyRecoveryPointInput. | 

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replicationProtectedItemsCreate

> ReplicationProtectedItem replicationProtectedItemsCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, input)

Enables protection.

The operation to create an ASR replication protected item (Enable replication).

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Name of the fabric.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
let replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | A name for the replication protected item.
let input = new SiteRecoveryManagementClient.EnableProtectionInput(); // EnableProtectionInput | Enable Protection Input.
apiInstance.replicationProtectedItemsCreate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, input, (error, data, response) => {
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
 **fabricName** | **String**| Name of the fabric. | 
 **protectionContainerName** | **String**| Protection container name. | 
 **replicatedProtectedItemName** | **String**| A name for the replication protected item. | 
 **input** | [**EnableProtectionInput**](EnableProtectionInput.md)| Enable Protection Input. | 

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replicationProtectedItemsDelete

> replicationProtectedItemsDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, disableProtectionInput)

Disables protection.

The operation to disable replication on a replication protected item. This will also remove the item.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
let replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
let disableProtectionInput = new SiteRecoveryManagementClient.DisableProtectionInput(); // DisableProtectionInput | Disable protection input.
apiInstance.replicationProtectedItemsDelete(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, disableProtectionInput, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **fabricName** | **String**| Fabric name. | 
 **protectionContainerName** | **String**| Protection container name. | 
 **replicatedProtectedItemName** | **String**| Replication protected item name. | 
 **disableProtectionInput** | [**DisableProtectionInput**](DisableProtectionInput.md)| Disable protection input. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## replicationProtectedItemsFailoverCommit

> ReplicationProtectedItem replicationProtectedItemsFailoverCommit(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName)

Execute commit failover

Operation to commit the failover of the replication protected item.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Unique fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
let replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
apiInstance.replicationProtectedItemsFailoverCommit(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, (error, data, response) => {
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
 **fabricName** | **String**| Unique fabric name. | 
 **protectionContainerName** | **String**| Protection container name. | 
 **replicatedProtectedItemName** | **String**| Replication protected item name. | 

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationProtectedItemsGet

> ReplicationProtectedItem replicationProtectedItemsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName)

Gets the details of a Replication protected item.

Gets the details of an ASR replication protected item.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric unique name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
let replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
apiInstance.replicationProtectedItemsGet(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, (error, data, response) => {
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
 **fabricName** | **String**| Fabric unique name. | 
 **protectionContainerName** | **String**| Protection container name. | 
 **replicatedProtectedItemName** | **String**| Replication protected item name. | 

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationProtectedItemsList

> ReplicationProtectedItemCollection replicationProtectedItemsList(apiVersion, resourceName, resourceGroupName, subscriptionId, opts)

Gets the list of replication protected items.

Gets the list of ASR replication protected items in the vault.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let opts = {
  'skipToken': "skipToken_example", // String | The pagination token. Possible values: \"FabricId\" or \"FabricId_CloudId\" or null
  'filter': "filter_example" // String | OData filter options.
};
apiInstance.replicationProtectedItemsList(apiVersion, resourceName, resourceGroupName, subscriptionId, opts, (error, data, response) => {
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
 **skipToken** | **String**| The pagination token. Possible values: \&quot;FabricId\&quot; or \&quot;FabricId_CloudId\&quot; or null | [optional] 
 **filter** | **String**| OData filter options. | [optional] 

### Return type

[**ReplicationProtectedItemCollection**](ReplicationProtectedItemCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationProtectedItemsListByReplicationProtectionContainers

> ReplicationProtectedItemCollection replicationProtectedItemsListByReplicationProtectionContainers(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName)

Gets the list of Replication protected items.

Gets the list of ASR replication protected items in the protection container.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
apiInstance.replicationProtectedItemsListByReplicationProtectionContainers(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, (error, data, response) => {
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

[**ReplicationProtectedItemCollection**](ReplicationProtectedItemCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationProtectedItemsPlannedFailover

> ReplicationProtectedItem replicationProtectedItemsPlannedFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, failoverInput)

Execute planned failover

Operation to initiate a planned failover of the replication protected item.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Unique fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
let replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
let failoverInput = new SiteRecoveryManagementClient.PlannedFailoverInput(); // PlannedFailoverInput | Disable protection input.
apiInstance.replicationProtectedItemsPlannedFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, failoverInput, (error, data, response) => {
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
 **fabricName** | **String**| Unique fabric name. | 
 **protectionContainerName** | **String**| Protection container name. | 
 **replicatedProtectedItemName** | **String**| Replication protected item name. | 
 **failoverInput** | [**PlannedFailoverInput**](PlannedFailoverInput.md)| Disable protection input. | 

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replicationProtectedItemsPurge

> replicationProtectedItemsPurge(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName)

Purges protection.

The operation to delete or purge a replication protected item. This operation will force delete the replication protected item. Use the remove operation on replication protected item to perform a clean disable replication for the item.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
let replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
apiInstance.replicationProtectedItemsPurge(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 
 **resourceName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **fabricName** | **String**| Fabric name. | 
 **protectionContainerName** | **String**| Protection container name. | 
 **replicatedProtectedItemName** | **String**| Replication protected item name. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## replicationProtectedItemsRemoveDisks

> ReplicationProtectedItem replicationProtectedItemsRemoveDisks(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, removeDisksInput)

Removes disk(s).

Operation to remove disk(s) from the replication protected item.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Unique fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
let replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
let removeDisksInput = new SiteRecoveryManagementClient.RemoveDisksInput(); // RemoveDisksInput | Remove disks input.
apiInstance.replicationProtectedItemsRemoveDisks(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, removeDisksInput, (error, data, response) => {
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
 **fabricName** | **String**| Unique fabric name. | 
 **protectionContainerName** | **String**| Protection container name. | 
 **replicatedProtectedItemName** | **String**| Replication protected item name. | 
 **removeDisksInput** | [**RemoveDisksInput**](RemoveDisksInput.md)| Remove disks input. | 

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replicationProtectedItemsRepairReplication

> ReplicationProtectedItem replicationProtectedItemsRepairReplication(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName)

Resynchronize or repair replication.

The operation to start resynchronize/repair replication for a replication protected item requiring resynchronization.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | The name of the fabric.
let protectionContainerName = "protectionContainerName_example"; // String | The name of the container.
let replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | The name of the replication protected item.
apiInstance.replicationProtectedItemsRepairReplication(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, (error, data, response) => {
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
 **fabricName** | **String**| The name of the fabric. | 
 **protectionContainerName** | **String**| The name of the container. | 
 **replicatedProtectedItemName** | **String**| The name of the replication protected item. | 

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationProtectedItemsReprotect

> ReplicationProtectedItem replicationProtectedItemsReprotect(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, rrInput)

Execute Reverse Replication\\Reprotect

Operation to reprotect or reverse replicate a failed over replication protected item.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Unique fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
let replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
let rrInput = new SiteRecoveryManagementClient.ReverseReplicationInput(); // ReverseReplicationInput | Disable protection input.
apiInstance.replicationProtectedItemsReprotect(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, rrInput, (error, data, response) => {
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
 **fabricName** | **String**| Unique fabric name. | 
 **protectionContainerName** | **String**| Protection container name. | 
 **replicatedProtectedItemName** | **String**| Replication protected item name. | 
 **rrInput** | [**ReverseReplicationInput**](ReverseReplicationInput.md)| Disable protection input. | 

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replicationProtectedItemsResolveHealthErrors

> ReplicationProtectedItem replicationProtectedItemsResolveHealthErrors(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, resolveHealthInput)

Resolve health errors.

Operation to resolve health issues of the replication protected item.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Unique fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
let replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
let resolveHealthInput = new SiteRecoveryManagementClient.ResolveHealthInput(); // ResolveHealthInput | Health issue input object.
apiInstance.replicationProtectedItemsResolveHealthErrors(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, resolveHealthInput, (error, data, response) => {
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
 **fabricName** | **String**| Unique fabric name. | 
 **protectionContainerName** | **String**| Protection container name. | 
 **replicatedProtectedItemName** | **String**| Replication protected item name. | 
 **resolveHealthInput** | [**ResolveHealthInput**](ResolveHealthInput.md)| Health issue input object. | 

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replicationProtectedItemsTestFailover

> ReplicationProtectedItem replicationProtectedItemsTestFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, failoverInput)

Execute test failover

Operation to perform a test failover of the replication protected item.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Unique fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
let replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
let failoverInput = new SiteRecoveryManagementClient.TestFailoverInput(); // TestFailoverInput | Test failover input.
apiInstance.replicationProtectedItemsTestFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, failoverInput, (error, data, response) => {
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
 **fabricName** | **String**| Unique fabric name. | 
 **protectionContainerName** | **String**| Protection container name. | 
 **replicatedProtectedItemName** | **String**| Replication protected item name. | 
 **failoverInput** | [**TestFailoverInput**](TestFailoverInput.md)| Test failover input. | 

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replicationProtectedItemsTestFailoverCleanup

> ReplicationProtectedItem replicationProtectedItemsTestFailoverCleanup(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, cleanupInput)

Execute test failover cleanup.

Operation to clean up the test failover of a replication protected item.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Unique fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
let replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
let cleanupInput = new SiteRecoveryManagementClient.TestFailoverCleanupInput(); // TestFailoverCleanupInput | Test failover cleanup input.
apiInstance.replicationProtectedItemsTestFailoverCleanup(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, cleanupInput, (error, data, response) => {
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
 **fabricName** | **String**| Unique fabric name. | 
 **protectionContainerName** | **String**| Protection container name. | 
 **replicatedProtectedItemName** | **String**| Replication protected item name. | 
 **cleanupInput** | [**TestFailoverCleanupInput**](TestFailoverCleanupInput.md)| Test failover cleanup input. | 

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replicationProtectedItemsUnplannedFailover

> ReplicationProtectedItem replicationProtectedItemsUnplannedFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, failoverInput)

Execute unplanned failover

Operation to initiate a failover of the replication protected item.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Unique fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
let replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
let failoverInput = new SiteRecoveryManagementClient.UnplannedFailoverInput(); // UnplannedFailoverInput | Disable protection input.
apiInstance.replicationProtectedItemsUnplannedFailover(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, failoverInput, (error, data, response) => {
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
 **fabricName** | **String**| Unique fabric name. | 
 **protectionContainerName** | **String**| Protection container name. | 
 **replicatedProtectedItemName** | **String**| Replication protected item name. | 
 **failoverInput** | [**UnplannedFailoverInput**](UnplannedFailoverInput.md)| Disable protection input. | 

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replicationProtectedItemsUpdate

> ReplicationProtectedItem replicationProtectedItemsUpdate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, updateProtectionInput)

Updates protection.

The operation to update the recovery settings of an ASR replication protected item.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name.
let protectionContainerName = "protectionContainerName_example"; // String | Protection container name.
let replicatedProtectedItemName = "replicatedProtectedItemName_example"; // String | Replication protected item name.
let updateProtectionInput = new SiteRecoveryManagementClient.UpdateReplicationProtectedItemInput(); // UpdateReplicationProtectedItemInput | Update protection input.
apiInstance.replicationProtectedItemsUpdate(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicatedProtectedItemName, updateProtectionInput, (error, data, response) => {
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
 **replicatedProtectedItemName** | **String**| Replication protected item name. | 
 **updateProtectionInput** | [**UpdateReplicationProtectedItemInput**](UpdateReplicationProtectedItemInput.md)| Update protection input. | 

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replicationProtectedItemsUpdateMobilityService

> ReplicationProtectedItem replicationProtectedItemsUpdateMobilityService(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicationProtectedItemName, updateMobilityServiceRequest)

Update the mobility service on a protected item.

The operation to update(push update) the installed mobility service software on a replication protected item to the latest available version.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceName = "resourceName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | The name of the fabric containing the protected item.
let protectionContainerName = "protectionContainerName_example"; // String | The name of the container containing the protected item.
let replicationProtectedItemName = "replicationProtectedItemName_example"; // String | The name of the protected item on which the agent is to be updated.
let updateMobilityServiceRequest = new SiteRecoveryManagementClient.UpdateMobilityServiceRequest(); // UpdateMobilityServiceRequest | Request to update the mobility service on the protected item.
apiInstance.replicationProtectedItemsUpdateMobilityService(apiVersion, resourceName, resourceGroupName, subscriptionId, fabricName, protectionContainerName, replicationProtectedItemName, updateMobilityServiceRequest, (error, data, response) => {
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
 **fabricName** | **String**| The name of the fabric containing the protected item. | 
 **protectionContainerName** | **String**| The name of the container containing the protected item. | 
 **replicationProtectedItemName** | **String**| The name of the protected item on which the agent is to be updated. | 
 **updateMobilityServiceRequest** | [**UpdateMobilityServiceRequest**](UpdateMobilityServiceRequest.md)| Request to update the mobility service on the protected item. | 

### Return type

[**ReplicationProtectedItem**](ReplicationProtectedItem.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

