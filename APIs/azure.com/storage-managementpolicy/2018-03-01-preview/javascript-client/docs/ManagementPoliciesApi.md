# StorageManagementClient.ManagementPoliciesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**managementPoliciesCreateOrUpdate**](ManagementPoliciesApi.md#managementPoliciesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/managementPolicies/{managementPolicyName} | 
[**managementPoliciesDelete**](ManagementPoliciesApi.md#managementPoliciesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/managementPolicies/{managementPolicyName} | 
[**managementPoliciesGet**](ManagementPoliciesApi.md#managementPoliciesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/managementPolicies/{managementPolicyName} | 



## managementPoliciesCreateOrUpdate

> StorageAccountManagementPolicies managementPoliciesCreateOrUpdate(resourceGroupName, accountName, apiVersion, subscriptionId, managementPolicyName, properties)



Sets the data policy rules associated with the specified storage account.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.ManagementPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let managementPolicyName = "managementPolicyName_example"; // String | The name of the Storage Account Management Policy. It should always be 'default'
let properties = new StorageManagementClient.ManagementPoliciesRulesSetParameter(); // ManagementPoliciesRulesSetParameter | The data policy rules to set to a storage account.
apiInstance.managementPoliciesCreateOrUpdate(resourceGroupName, accountName, apiVersion, subscriptionId, managementPolicyName, properties, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **accountName** | **String**| The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **managementPolicyName** | **String**| The name of the Storage Account Management Policy. It should always be &#39;default&#39; | 
 **properties** | [**ManagementPoliciesRulesSetParameter**](ManagementPoliciesRulesSetParameter.md)| The data policy rules to set to a storage account. | 

### Return type

[**StorageAccountManagementPolicies**](StorageAccountManagementPolicies.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## managementPoliciesDelete

> managementPoliciesDelete(resourceGroupName, accountName, apiVersion, subscriptionId, managementPolicyName)



Deletes the data policy rules associated with the specified storage account.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.ManagementPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let managementPolicyName = "managementPolicyName_example"; // String | The name of the Storage Account Management Policy. It should always be 'default'
apiInstance.managementPoliciesDelete(resourceGroupName, accountName, apiVersion, subscriptionId, managementPolicyName, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **accountName** | **String**| The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **managementPolicyName** | **String**| The name of the Storage Account Management Policy. It should always be &#39;default&#39; | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## managementPoliciesGet

> StorageAccountManagementPolicies managementPoliciesGet(resourceGroupName, accountName, apiVersion, subscriptionId, managementPolicyName)



Gets the data policy rules associated with the specified storage account.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.ManagementPoliciesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let managementPolicyName = "managementPolicyName_example"; // String | The name of the Storage Account Management Policy. It should always be 'default'
apiInstance.managementPoliciesGet(resourceGroupName, accountName, apiVersion, subscriptionId, managementPolicyName, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group within the user&#39;s subscription. The name is case insensitive. | 
 **accountName** | **String**| The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **managementPolicyName** | **String**| The name of the Storage Account Management Policy. It should always be &#39;default&#39; | 

### Return type

[**StorageAccountManagementPolicies**](StorageAccountManagementPolicies.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

