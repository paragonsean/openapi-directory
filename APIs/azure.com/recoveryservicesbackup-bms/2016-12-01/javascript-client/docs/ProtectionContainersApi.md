# RecoveryServicesBackupClient.ProtectionContainersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protectionContainersGet**](ProtectionContainersApi.md#protectionContainersGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName} | 
[**protectionContainersInquire**](ProtectionContainersApi.md#protectionContainersInquire) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/inquire | Inquires all the protectable items under the given container.
[**protectionContainersRefresh**](ProtectionContainersApi.md#protectionContainersRefresh) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/refreshContainers | 
[**protectionContainersRegister**](ProtectionContainersApi.md#protectionContainersRegister) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName} | 
[**protectionContainersUnregister**](ProtectionContainersApi.md#protectionContainersUnregister) | **DELETE** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName} | 



## protectionContainersGet

> ProtectionContainerResource protectionContainersGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName)



Gets details of the specific container registered to your Recovery Services Vault.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectionContainersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Name of the fabric where the container belongs.
let containerName = "containerName_example"; // String | Name of the container whose details need to be fetched.
apiInstance.protectionContainersGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, (error, data, response) => {
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
 **fabricName** | **String**| Name of the fabric where the container belongs. | 
 **containerName** | **String**| Name of the container whose details need to be fetched. | 

### Return type

[**ProtectionContainerResource**](ProtectionContainerResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protectionContainersInquire

> protectionContainersInquire(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, opts)

Inquires all the protectable items under the given container.

This is an async operation and the results should be tracked using location header or Azure-async-url.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectionContainersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric Name associated with the container.
let containerName = "containerName_example"; // String | Name of the container in which inquiry needs to be triggered.
let opts = {
  'filter': "filter_example" // String | OData filter options.
};
apiInstance.protectionContainersInquire(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, opts, (error, data, response) => {
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
 **fabricName** | **String**| Fabric Name associated with the container. | 
 **containerName** | **String**| Name of the container in which inquiry needs to be triggered. | 
 **filter** | **String**| OData filter options. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## protectionContainersRefresh

> protectionContainersRefresh(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, opts)



Discovers all the containers in the subscription that can be backed up to Recovery Services Vault. This is an  asynchronous operation. To know the status of the operation, call GetRefreshOperationResult API.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectionContainersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name associated the container.
let opts = {
  'filter': "filter_example" // String | OData filter options.
};
apiInstance.protectionContainersRefresh(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, opts, (error, data, response) => {
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
 **fabricName** | **String**| Fabric name associated the container. | 
 **filter** | **String**| OData filter options. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## protectionContainersRegister

> ProtectionContainerResource protectionContainersRegister(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, parameters)



Registers the container with Recovery Services vault.  This is an asynchronous operation. To track the operation status, use location header to call get latest status of  the operation.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectionContainersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name associated with the container.
let containerName = "containerName_example"; // String | Name of the container to be registered.
let parameters = new RecoveryServicesBackupClient.ProtectionContainerResource(); // ProtectionContainerResource | Request body for operation
apiInstance.protectionContainersRegister(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, parameters, (error, data, response) => {
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
 **fabricName** | **String**| Fabric name associated with the container. | 
 **containerName** | **String**| Name of the container to be registered. | 
 **parameters** | [**ProtectionContainerResource**](ProtectionContainerResource.md)| Request body for operation | 

### Return type

[**ProtectionContainerResource**](ProtectionContainerResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## protectionContainersUnregister

> protectionContainersUnregister(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName)



Unregisters the given container from your Recovery Services Vault. This is an asynchronous operation. To determine  whether the backend service has finished processing the request, call Get Container Operation Result API.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectionContainersApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Name of the fabric where the container belongs.
let containerName = "containerName_example"; // String | Name of the container which needs to be unregistered from the Recovery Services Vault.
apiInstance.protectionContainersUnregister(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, (error, data, response) => {
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
 **fabricName** | **String**| Name of the fabric where the container belongs. | 
 **containerName** | **String**| Name of the container which needs to be unregistered from the Recovery Services Vault. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

