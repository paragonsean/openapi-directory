# RecoveryServicesBackupClient.RecoveryPointsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recoveryPointsGetAccessToken**](RecoveryPointsApi.md#recoveryPointsGetAccessToken) | **POST** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupFabrics/{fabricName}/protectionContainers/{containerName}/protectedItems/{protectedItemName}/recoveryPoints/{recoveryPointId}/accessToken | Returns the Access token for communication between BMS and Protection service



## recoveryPointsGetAccessToken

> CrrAccessTokenResource recoveryPointsGetAccessToken(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId)

Returns the Access token for communication between BMS and Protection service

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.RecoveryPointsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let fabricName = "fabricName_example"; // String | Fabric name associated with the container.
let containerName = "containerName_example"; // String | Name of the container.
let protectedItemName = "protectedItemName_example"; // String | Name of the Protected Item.
let recoveryPointId = "recoveryPointId_example"; // String | Recovery Point Id
apiInstance.recoveryPointsGetAccessToken(apiVersion, vaultName, resourceGroupName, subscriptionId, fabricName, containerName, protectedItemName, recoveryPointId, (error, data, response) => {
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
 **containerName** | **String**| Name of the container. | 
 **protectedItemName** | **String**| Name of the Protected Item. | 
 **recoveryPointId** | **String**| Recovery Point Id | 

### Return type

[**CrrAccessTokenResource**](CrrAccessTokenResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

