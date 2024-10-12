# StorageManagementClient.FileServiceApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fileServicesGetServiceProperties**](FileServiceApi.md#fileServicesGetServiceProperties) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/{FileServicesName} | 
[**fileServicesList**](FileServiceApi.md#fileServicesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices | 
[**fileServicesSetServiceProperties**](FileServiceApi.md#fileServicesSetServiceProperties) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/{FileServicesName} | 



## fileServicesGetServiceProperties

> FileServiceProperties fileServicesGetServiceProperties(resourceGroupName, accountName, apiVersion, subscriptionId, fileServicesName)



Gets the properties of file services in storage accounts, including CORS (Cross-Origin Resource Sharing) rules.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.FileServiceApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let fileServicesName = "fileServicesName_example"; // String | The name of the file Service within the specified storage account. File Service Name must be \"default\"
apiInstance.fileServicesGetServiceProperties(resourceGroupName, accountName, apiVersion, subscriptionId, fileServicesName, (error, data, response) => {
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
 **fileServicesName** | **String**| The name of the file Service within the specified storage account. File Service Name must be \&quot;default\&quot; | 

### Return type

[**FileServiceProperties**](FileServiceProperties.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileServicesList

> FileServiceItems fileServicesList(resourceGroupName, accountName, apiVersion, subscriptionId)



List all file services in storage accounts

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.FileServiceApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.fileServicesList(resourceGroupName, accountName, apiVersion, subscriptionId, (error, data, response) => {
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

### Return type

[**FileServiceItems**](FileServiceItems.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileServicesSetServiceProperties

> FileServiceProperties fileServicesSetServiceProperties(resourceGroupName, accountName, apiVersion, subscriptionId, fileServicesName, parameters)



Sets the properties of file services in storage accounts, including CORS (Cross-Origin Resource Sharing) rules. 

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.FileServiceApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let fileServicesName = "fileServicesName_example"; // String | The name of the file Service within the specified storage account. File Service Name must be \"default\"
let parameters = new StorageManagementClient.FileServiceProperties(); // FileServiceProperties | The properties of file services in storage accounts, including CORS (Cross-Origin Resource Sharing) rules.
apiInstance.fileServicesSetServiceProperties(resourceGroupName, accountName, apiVersion, subscriptionId, fileServicesName, parameters, (error, data, response) => {
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
 **fileServicesName** | **String**| The name of the file Service within the specified storage account. File Service Name must be \&quot;default\&quot; | 
 **parameters** | [**FileServiceProperties**](FileServiceProperties.md)| The properties of file services in storage accounts, including CORS (Cross-Origin Resource Sharing) rules. | 

### Return type

[**FileServiceProperties**](FileServiceProperties.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

