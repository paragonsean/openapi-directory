# RecoveryServicesBackupClient.ProtectionIntentApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protectionIntentCreateOrUpdate**](ProtectionIntentApi.md#protectionIntentCreateOrUpdate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/backupProtectionIntent/{intentObjectName} | 
[**protectionIntentDelete**](ProtectionIntentApi.md#protectionIntentDelete) | **DELETE** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/backupProtectionIntent/{intentObjectName} | 
[**protectionIntentGet**](ProtectionIntentApi.md#protectionIntentGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/backupProtectionIntent/{intentObjectName} | 
[**protectionIntentValidate**](ProtectionIntentApi.md#protectionIntentValidate) | **POST** /Subscriptions/{subscriptionId}/providers/Microsoft.RecoveryServices/locations/{azureRegion}/backupPreValidateProtection | It will validate followings  1. Vault capacity  2. VM is already protected  3. Any VM related configuration passed in properties.



## protectionIntentCreateOrUpdate

> ProtectionIntentResource protectionIntentCreateOrUpdate(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, intentObjectName, parameters)



Create Intent for Enabling backup of an item. This is a synchronous operation.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectionIntentApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name associated with the backup item.
let intentObjectName = "intentObjectName_example"; // String | Intent object name.
let parameters = new RecoveryServicesBackupClient.ProtectionIntentResource(); // ProtectionIntentResource | resource backed up item
apiInstance.protectionIntentCreateOrUpdate(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, intentObjectName, parameters, (error, data, response) => {
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
 **intentObjectName** | **String**| Intent object name. | 
 **parameters** | [**ProtectionIntentResource**](ProtectionIntentResource.md)| resource backed up item | 

### Return type

[**ProtectionIntentResource**](ProtectionIntentResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## protectionIntentDelete

> protectionIntentDelete(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, intentObjectName)



Used to remove intent from an item

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectionIntentApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name associated with the intent.
let intentObjectName = "intentObjectName_example"; // String | Intent to be deleted.
apiInstance.protectionIntentDelete(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, intentObjectName, (error, data, response) => {
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
 **fabricName** | **String**| Fabric name associated with the intent. | 
 **intentObjectName** | **String**| Intent to be deleted. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## protectionIntentGet

> ProtectionIntentResource protectionIntentGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, intentObjectName)



Provides the details of the protection intent up item. This is an asynchronous operation. To know the status of the operation,  call the GetItemOperationResult API.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectionIntentApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name associated with the backed up item.
let intentObjectName = "intentObjectName_example"; // String | Backed up item name whose details are to be fetched.
apiInstance.protectionIntentGet(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, intentObjectName, (error, data, response) => {
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
 **intentObjectName** | **String**| Backed up item name whose details are to be fetched. | 

### Return type

[**ProtectionIntentResource**](ProtectionIntentResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protectionIntentValidate

> PreValidateEnableBackupResponse protectionIntentValidate(apiVersion, azureRegion, subscriptionId, parameters)

It will validate followings  1. Vault capacity  2. VM is already protected  3. Any VM related configuration passed in properties.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectionIntentApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let azureRegion = "azureRegion_example"; // String | Azure region to hit Api
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let parameters = new RecoveryServicesBackupClient.PreValidateEnableBackupRequest(); // PreValidateEnableBackupRequest | Enable backup validation request on Virtual Machine
apiInstance.protectionIntentValidate(apiVersion, azureRegion, subscriptionId, parameters, (error, data, response) => {
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
 **azureRegion** | **String**| Azure region to hit Api | 
 **subscriptionId** | **String**| The subscription Id. | 
 **parameters** | [**PreValidateEnableBackupRequest**](PreValidateEnableBackupRequest.md)| Enable backup validation request on Virtual Machine | 

### Return type

[**PreValidateEnableBackupResponse**](PreValidateEnableBackupResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

