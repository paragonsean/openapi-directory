# RecoveryServicesBackupClient.BackupCrrJobsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**backupCrrJobsList**](BackupCrrJobsApi.md#backupCrrJobsList) | **POST** /Subscriptions/{subscriptionId}/providers/Microsoft.RecoveryServices/locations/{azureRegion}/backupCrrJobs | Gets the list of CRR jobs from the target region.



## backupCrrJobsList

> JobResourceList backupCrrJobsList(apiVersion, azureRegion, subscriptionId)

Gets the list of CRR jobs from the target region.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.BackupCrrJobsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let azureRegion = "azureRegion_example"; // String | Azure region to hit Api
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
apiInstance.backupCrrJobsList(apiVersion, azureRegion, subscriptionId, (error, data, response) => {
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

### Return type

[**JobResourceList**](JobResourceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

