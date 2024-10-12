# RecoveryServicesBackupClient.BackupStatusApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backupStatusGet**](BackupStatusApi.md#backupStatusGet) | **POST** /Subscriptions/{subscriptionId}/providers/Microsoft.RecoveryServices/locations/{azureRegion}/backupStatus | Get the container backup status



## backupStatusGet

> BackupStatusResponse backupStatusGet(apiVersion, azureRegion, subscriptionId, parameters)

Get the container backup status

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.BackupStatusApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let azureRegion = "azureRegion_example"; // String | Azure region to hit Api
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let parameters = new RecoveryServicesBackupClient.BackupStatusRequest(); // BackupStatusRequest | Container Backup Status Request
apiInstance.backupStatusGet(apiVersion, azureRegion, subscriptionId, parameters, (error, data, response) => {
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
 **parameters** | [**BackupStatusRequest**](BackupStatusRequest.md)| Container Backup Status Request | 

### Return type

[**BackupStatusResponse**](BackupStatusResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

