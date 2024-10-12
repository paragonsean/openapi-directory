# RecoveryServicesBackupClient.ProtectionPolicyOperationResultsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protectionPolicyOperationResultsGet**](ProtectionPolicyOperationResultsApi.md#protectionPolicyOperationResultsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupPolicies/{policyName}/operationResults/{operationId} | 



## protectionPolicyOperationResultsGet

> ProtectionPolicyResource protectionPolicyOperationResultsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName, operationId)



Provides the result of an operation.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectionPolicyOperationResultsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let policyName = "policyName_example"; // String | Backup policy name whose operation's result needs to be fetched.
let operationId = "operationId_example"; // String | Operation ID which represents the operation whose result needs to be fetched.
apiInstance.protectionPolicyOperationResultsGet(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName, operationId, (error, data, response) => {
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
 **policyName** | **String**| Backup policy name whose operation&#39;s result needs to be fetched. | 
 **operationId** | **String**| Operation ID which represents the operation whose result needs to be fetched. | 

### Return type

[**ProtectionPolicyResource**](ProtectionPolicyResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

