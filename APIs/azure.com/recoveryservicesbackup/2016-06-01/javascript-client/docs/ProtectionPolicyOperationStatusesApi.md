# RecoveryServicesBackupClient.ProtectionPolicyOperationStatusesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protectionPolicyOperationStatusesGet**](ProtectionPolicyOperationStatusesApi.md#protectionPolicyOperationStatusesGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupPolicies/{policyName}/operations/{operationId} | 



## protectionPolicyOperationStatusesGet

> OperationStatus protectionPolicyOperationStatusesGet(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName, operationId)



Provides the status of the asynchronous operations like backup or restore. The status can be: in progress, completed, or failed. You can refer to the Operation Status enumeration for the possible states of an operation. Some operations create jobs. This method returns the list of jobs associated with the operation.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectionPolicyOperationStatusesApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let policyName = "policyName_example"; // String | The backup policy name used in this GET operation.
let operationId = "operationId_example"; // String | The ID associated with this GET operation.
apiInstance.protectionPolicyOperationStatusesGet(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName, operationId, (error, data, response) => {
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
 **policyName** | **String**| The backup policy name used in this GET operation. | 
 **operationId** | **String**| The ID associated with this GET operation. | 

### Return type

[**OperationStatus**](OperationStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

