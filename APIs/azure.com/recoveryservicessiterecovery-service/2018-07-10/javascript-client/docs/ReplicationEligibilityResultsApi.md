# SiteRecoveryManagementClient.ReplicationEligibilityResultsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**replicationEligibilityResultsGet**](ReplicationEligibilityResultsApi.md#replicationEligibilityResultsGet) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{virtualMachineName}/providers/Microsoft.RecoveryServices/replicationEligibilityResults/default | Gets the validation errors in case the VM is unsuitable for protection.
[**replicationEligibilityResultsList**](ReplicationEligibilityResultsApi.md#replicationEligibilityResultsList) | **GET** /Subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{virtualMachineName}/providers/Microsoft.RecoveryServices/replicationEligibilityResults | Gets the validation errors in case the VM is unsuitable for protection.



## replicationEligibilityResultsGet

> ReplicationEligibilityResults replicationEligibilityResultsGet(apiVersion, resourceGroupName, subscriptionId, virtualMachineName)

Gets the validation errors in case the VM is unsuitable for protection.

Validates whether a given VM can be protected or not in which case returns list of errors.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationEligibilityResultsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let virtualMachineName = "virtualMachineName_example"; // String | Virtual Machine name.
apiInstance.replicationEligibilityResultsGet(apiVersion, resourceGroupName, subscriptionId, virtualMachineName, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **virtualMachineName** | **String**| Virtual Machine name. | 

### Return type

[**ReplicationEligibilityResults**](ReplicationEligibilityResults.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replicationEligibilityResultsList

> ReplicationEligibilityResultsCollection replicationEligibilityResultsList(apiVersion, resourceGroupName, subscriptionId, virtualMachineName)

Gets the validation errors in case the VM is unsuitable for protection.

Validates whether a given VM can be protected or not in which case returns list of errors.

### Example

```javascript
import SiteRecoveryManagementClient from 'site_recovery_management_client';
let defaultClient = SiteRecoveryManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SiteRecoveryManagementClient.ReplicationEligibilityResultsApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group where the recovery services vault is present.
let subscriptionId = "subscriptionId_example"; // String | The subscription Id.
let virtualMachineName = "virtualMachineName_example"; // String | Virtual Machine name.
apiInstance.replicationEligibilityResultsList(apiVersion, resourceGroupName, subscriptionId, virtualMachineName, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group where the recovery services vault is present. | 
 **subscriptionId** | **String**| The subscription Id. | 
 **virtualMachineName** | **String**| Virtual Machine name. | 

### Return type

[**ReplicationEligibilityResultsCollection**](ReplicationEligibilityResultsCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

