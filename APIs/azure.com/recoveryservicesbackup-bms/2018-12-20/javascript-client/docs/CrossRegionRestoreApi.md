# RecoveryServicesBackupClient.CrossRegionRestoreApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crossRegionRestoreTrigger**](CrossRegionRestoreApi.md#crossRegionRestoreTrigger) | **POST** /Subscriptions/{subscriptionId}/providers/Microsoft.RecoveryServices/locations/{azureRegion}/backupCrossRegionRestore | Restores the specified backed up data in a different region as compared to where the data is backed up.



## crossRegionRestoreTrigger

> crossRegionRestoreTrigger(apiVersion, azureRegion, subscriptionId, parameters)

Restores the specified backed up data in a different region as compared to where the data is backed up.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.CrossRegionRestoreApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let azureRegion = "azureRegion_example"; // String | Azure region to hit Api
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let parameters = new RecoveryServicesBackupClient.CrossRegionRestoreRequestResource(); // CrossRegionRestoreRequestResource | resource cross region restore request
apiInstance.crossRegionRestoreTrigger(apiVersion, azureRegion, subscriptionId, parameters, (error, data, response) => {
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
 **azureRegion** | **String**| Azure region to hit Api | 
 **subscriptionId** | **String**| The subscription Id. | 
 **parameters** | [**CrossRegionRestoreRequestResource**](CrossRegionRestoreRequestResource.md)| resource cross region restore request | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

