# RecoveryServicesBackupClient.ProtectedItemsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protectedItemsCreateOrUpdate**](ProtectedItemsApi.md#protectedItemsCreateOrUpdate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName} | 
[**protectedItemsDelete**](ProtectedItemsApi.md#protectedItemsDelete) | **DELETE** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName} | 
[**protectedItemsGet**](ProtectedItemsApi.md#protectedItemsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName} | 
[**protectedItemsList**](ProtectedItemsApi.md#protectedItemsList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupProtectedItems | 



## protectedItemsCreateOrUpdate

> protectedItemsCreateOrUpdate(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, resourceProtectedItem)



This operation enables an item to be backed up, or modifies the existing backup policy information for an item that has been backed up. This is an asynchronous operation. To learn the status of the operation, call the GetItemOperationResult API.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let fabricName = "fabricName_example"; // String | The fabric name associated with the backup item.
let containerName = "containerName_example"; // String | The container name associated with the backup item.
let protectedItemName = "protectedItemName_example"; // String | The name of the backup item.
let resourceProtectedItem = new RecoveryServicesBackupClient.ProtectedItemResource(); // ProtectedItemResource | The resource backup item.
apiInstance.protectedItemsCreateOrUpdate(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, resourceProtectedItem, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **vaultName** | **String**| The name of the Recovery Services vault. | 
 **resourceGroupName** | **String**| The name of the resource group associated with the Recovery Services vault. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **fabricName** | **String**| The fabric name associated with the backup item. | 
 **containerName** | **String**| The container name associated with the backup item. | 
 **protectedItemName** | **String**| The name of the backup item. | 
 **resourceProtectedItem** | [**ProtectedItemResource**](ProtectedItemResource.md)| The resource backup item. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## protectedItemsDelete

> protectedItemsDelete(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName)



Used to disable the backup job for an item within a container. This is an asynchronous operation. To learn the status of the request, call the GetItemOperationResult API.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let fabricName = "fabricName_example"; // String |  The fabric name associated with the backup item.
let containerName = "containerName_example"; // String | The container name associated with the backup item.
let protectedItemName = "protectedItemName_example"; // String | The backup item to be deleted.
apiInstance.protectedItemsDelete(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **vaultName** | **String**| The name of the Recovery Services vault. | 
 **resourceGroupName** | **String**| The name of the resource group associated with the Recovery Services vault. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **fabricName** | **String**|  The fabric name associated with the backup item. | 
 **containerName** | **String**| The container name associated with the backup item. | 
 **protectedItemName** | **String**| The backup item to be deleted. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## protectedItemsGet

> ProtectedItemResource protectedItemsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, opts)



Provides the details of the backup item. This is an asynchronous operation. To know the status of the operation, call the GetItemOperationResult API.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let fabricName = "fabricName_example"; // String | The fabric name associated with the backup item.
let containerName = "containerName_example"; // String | The container name associated with the backup item.
let protectedItemName = "protectedItemName_example"; // String | The backup item name used in this GET operation.
let opts = {
  'filter': "filter_example" // String | expand eq {extendedInfo}. This filter enables you to choose (or filter) specific items in the list of backup items.
};
apiInstance.protectedItemsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **vaultName** | **String**| The name of the Recovery Services vault. | 
 **resourceGroupName** | **String**| The name of the resource group associated with the Recovery Services vault. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **fabricName** | **String**| The fabric name associated with the backup item. | 
 **containerName** | **String**| The container name associated with the backup item. | 
 **protectedItemName** | **String**| The backup item name used in this GET operation. | 
 **filter** | **String**| expand eq {extendedInfo}. This filter enables you to choose (or filter) specific items in the list of backup items. | [optional] 

### Return type

[**ProtectedItemResource**](ProtectedItemResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protectedItemsList

> ProtectedItemResourceList protectedItemsList(apiVersion, vaultName, resourceGroupName, subscriptionId, opts)



Provides a pageable list of all items in a subscription, that can be protected.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let opts = {
  'filter': "filter_example", // String |  itemType eq { VM , FileFolder , AzureSqlDb , SQLDB , Exchange , Sharepoint , DPMUnknown } and providerType eq { AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql } and policyName eq {policyName} and containerName eq {containername} and backupManagementType eq { AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql }.
  'skipToken': "skipToken_example" // String |  The Skip Token filter.
};
apiInstance.protectedItemsList(apiVersion, vaultName, resourceGroupName, subscriptionId, opts, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **vaultName** | **String**| The name of the Recovery Services vault. | 
 **resourceGroupName** | **String**| The name of the resource group associated with the Recovery Services vault. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **filter** | **String**|  itemType eq { VM , FileFolder , AzureSqlDb , SQLDB , Exchange , Sharepoint , DPMUnknown } and providerType eq { AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql } and policyName eq {policyName} and containerName eq {containername} and backupManagementType eq { AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql }. | [optional] 
 **skipToken** | **String**|  The Skip Token filter. | [optional] 

### Return type

[**ProtectedItemResourceList**](ProtectedItemResourceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

