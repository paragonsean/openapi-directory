# RecoveryServicesBackupClient.ProtectionPoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protectionPoliciesCreateOrUpdate**](ProtectionPoliciesApi.md#protectionPoliciesCreateOrUpdate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupPolicies/{policyName} | 
[**protectionPoliciesGet**](ProtectionPoliciesApi.md#protectionPoliciesGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupPolicies/{policyName} | 



## protectionPoliciesCreateOrUpdate

> ProtectionPolicyResource protectionPoliciesCreateOrUpdate(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName, parameters)



Creates or modifies a backup policy. This is an asynchronous operation. Status of the operation can be fetched  using GetPolicyOperationResult API.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectionPoliciesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let policyName = "policyName_example"; // String | Backup policy to be created.
let parameters = new RecoveryServicesBackupClient.ProtectionPolicyResource(); // ProtectionPolicyResource | resource backup policy
apiInstance.protectionPoliciesCreateOrUpdate(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName, parameters, (error, data, response) => {
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
 **policyName** | **String**| Backup policy to be created. | 
 **parameters** | [**ProtectionPolicyResource**](ProtectionPolicyResource.md)| resource backup policy | 

### Return type

[**ProtectionPolicyResource**](ProtectionPolicyResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## protectionPoliciesGet

> ProtectionPolicyResource protectionPoliciesGet(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName)



Provides the details of the backup policies associated to Recovery Services Vault. This is an asynchronous  operation. Status of the operation can be fetched using GetPolicyOperationResult API.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectionPoliciesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let vaultName = "vaultName_example"; // String | The name of the recovery services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let policyName = "policyName_example"; // String | Backup policy information to be fetched.
apiInstance.protectionPoliciesGet(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName, (error, data, response) => {
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
 **policyName** | **String**| Backup policy information to be fetched. | 

### Return type

[**ProtectionPolicyResource**](ProtectionPolicyResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

