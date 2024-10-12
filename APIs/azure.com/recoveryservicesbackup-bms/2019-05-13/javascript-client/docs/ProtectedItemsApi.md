# RecoveryServicesBackupClient.ProtectedItemsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protectedItemsCreateOrUpdate**](ProtectedItemsApi.md#protectedItemsCreateOrUpdate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName} | 
[**protectedItemsDelete**](ProtectedItemsApi.md#protectedItemsDelete) | **DELETE** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName} | 
[**protectedItemsGet**](ProtectedItemsApi.md#protectedItemsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName} | 



## protectedItemsCreateOrUpdate

> ProtectedItemResource protectedItemsCreateOrUpdate(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, parameters)



Enables backup of an item or to modifies the backup policy information of an already backed up item. This is an  asynchronous operation. To know the status of the operation, call the GetItemOperationResult API.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name associated with the backup item.
let containerName = "containerName_example"; // String | Container name associated with the backup item.
let protectedItemName = "protectedItemName_example"; // String | Item name to be backed up.
let parameters = new RecoveryServicesBackupClient.ProtectedItemResource(); // ProtectedItemResource | resource backed up item
apiInstance.protectedItemsCreateOrUpdate(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, parameters, (error, data, response) => {
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
 **vaultName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **fabricName** | **String**| Fabric name associated with the backup item. | 
 **containerName** | **String**| Container name associated with the backup item. | 
 **protectedItemName** | **String**| Item name to be backed up. | 
 **parameters** | [**ProtectedItemResource**](ProtectedItemResource.md)| resource backed up item | 

### Return type

[**ProtectedItemResource**](ProtectedItemResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## protectedItemsDelete

> protectedItemsDelete(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName)



Used to disable backup of an item within a container. This is an asynchronous operation. To know the status of the  request, call the GetItemOperationResult API.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name associated with the backed up item.
let containerName = "containerName_example"; // String | Container name associated with the backed up item.
let protectedItemName = "protectedItemName_example"; // String | Backed up item to be deleted.
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
 **apiVersion** | **String**| Client Api Version. | 
 **vaultName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **fabricName** | **String**| Fabric name associated with the backed up item. | 
 **containerName** | **String**| Container name associated with the backed up item. | 
 **protectedItemName** | **String**| Backed up item to be deleted. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## protectedItemsGet

> ProtectedItemResource protectedItemsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, opts)



Provides the details of the backed up item. This is an asynchronous operation. To know the status of the operation,  call the GetItemOperationResult API.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectedItemsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name associated with the backed up item.
let containerName = "containerName_example"; // String | Container name associated with the backed up item.
let protectedItemName = "protectedItemName_example"; // String | Backed up item name whose details are to be fetched.
let opts = {
  'filter': "filter_example" // String | OData filter options.
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
 **apiVersion** | **String**| Client Api Version. | 
 **vaultName** | **String**| The name of the recovery services vault. | 
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **fabricName** | **String**| Fabric name associated with the backed up item. | 
 **containerName** | **String**| Container name associated with the backed up item. | 
 **protectedItemName** | **String**| Backed up item name whose details are to be fetched. | 
 **filter** | **String**| OData filter options. | [optional] 

### Return type

[**ProtectedItemResource**](ProtectedItemResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

