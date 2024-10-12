# RecoveryServicesBackupClient.CrrOperationResultsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crrOperationResultsGet**](CrrOperationResultsApi.md#crrOperationResultsGet) | **GET** /Subscriptions/{subscriptionId}/providers/Microsoft.RecoveryServices/locations/{azureRegion}/backupCrrOperationResults/{operationId} | 



## crrOperationResultsGet

> crrOperationResultsGet(apiVersion, azureRegion, subscriptionId, operationId)



### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.CrrOperationResultsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let azureRegion = "azureRegion_example"; // String | Azure region to hit Api
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let operationId = "operationId_example"; // String | 
apiInstance.crrOperationResultsGet(apiVersion, azureRegion, subscriptionId, operationId, (error, data, response) => {
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
 **operationId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

