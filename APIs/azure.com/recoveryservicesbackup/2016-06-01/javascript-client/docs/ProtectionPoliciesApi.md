# RecoveryServicesBackupClient.ProtectionPoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protectionPoliciesCreateOrUpdate**](ProtectionPoliciesApi.md#protectionPoliciesCreateOrUpdate) | **PUT** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupPolicies/{policyName} | 
[**protectionPoliciesDelete**](ProtectionPoliciesApi.md#protectionPoliciesDelete) | **DELETE** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupPolicies/{policyName} | 
[**protectionPoliciesGet**](ProtectionPoliciesApi.md#protectionPoliciesGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupPolicies/{policyName} | 
[**protectionPoliciesList**](ProtectionPoliciesApi.md#protectionPoliciesList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.RecoveryServices/vaults/{vaultName}/backupPolicies | 



## protectionPoliciesCreateOrUpdate

> ProtectionPolicyResource protectionPoliciesCreateOrUpdate(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName, resourceProtectionPolicy)



Creates or modifies a backup policy. This is an asynchronous operation. Use the GetPolicyOperationResult API to Get the operation status.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectionPoliciesApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let policyName = "policyName_example"; // String | The backup policy to be created.
let resourceProtectionPolicy = new RecoveryServicesBackupClient.ProtectionPolicyResource(); // ProtectionPolicyResource | The resource backup policy.
apiInstance.protectionPoliciesCreateOrUpdate(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName, resourceProtectionPolicy, (error, data, response) => {
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
 **policyName** | **String**| The backup policy to be created. | 
 **resourceProtectionPolicy** | [**ProtectionPolicyResource**](ProtectionPolicyResource.md)| The resource backup policy. | 

### Return type

[**ProtectionPolicyResource**](ProtectionPolicyResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## protectionPoliciesDelete

> protectionPoliciesDelete(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName)



Deletes the specified backup policy from your Recovery Services vault. This is an asynchronous operation. Use the GetPolicyOperationResult API to Get the operation status.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectionPoliciesApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let policyName = "policyName_example"; // String | The name of the backup policy to be deleted.
apiInstance.protectionPoliciesDelete(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **vaultName** | **String**| The name of the Recovery Services vault. | 
 **resourceGroupName** | **String**| The name of the resource group associated with the Recovery Services vault. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **policyName** | **String**| The name of the backup policy to be deleted. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## protectionPoliciesGet

> ProtectionPolicyResource protectionPoliciesGet(apiVersion, vaultName, resourceGroupName, subscriptionId, policyName)



Gets the details of the backup policy associated with the Recovery Services vault. This is an asynchronous operation. Use the GetPolicyOperationResult API to Get the operation status.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectionPoliciesApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let policyName = "policyName_example"; // String | The backup policy name used in this GET operation.
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
 **apiVersion** | **String**| Client API version. | 
 **vaultName** | **String**| The name of the Recovery Services vault. | 
 **resourceGroupName** | **String**| The name of the resource group associated with the Recovery Services vault. | 
 **subscriptionId** | **String**| The subscription ID. | 
 **policyName** | **String**| The backup policy name used in this GET operation. | 

### Return type

[**ProtectionPolicyResource**](ProtectionPolicyResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## protectionPoliciesList

> ProtectionPolicyResourceList protectionPoliciesList(apiVersion, vaultName, resourceGroupName, subscriptionId, opts)



Lists the backup policies associated with the Recovery Services vault. The API provides parameters to Get scoped results.

### Example

```javascript
import RecoveryServicesBackupClient from 'recovery_services_backup_client';
let defaultClient = RecoveryServicesBackupClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new RecoveryServicesBackupClient.ProtectionPoliciesApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let vaultName = "vaultName_example"; // String | The name of the Recovery Services vault.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group associated with the Recovery Services vault.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID.
let opts = {
  'filter': "filter_example" // String | The following equation can be used to filter the list of backup policies. backupManagementType eq {AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql}.
};
apiInstance.protectionPoliciesList(apiVersion, vaultName, resourceGroupName, subscriptionId, opts, (error, data, response) => {
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
 **filter** | **String**| The following equation can be used to filter the list of backup policies. backupManagementType eq {AzureIaasVM, MAB, DPM, AzureBackupServer, AzureSql}. | [optional] 

### Return type

[**ProtectionPolicyResourceList**](ProtectionPolicyResourceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

