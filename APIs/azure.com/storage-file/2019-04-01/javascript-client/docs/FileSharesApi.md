# StorageManagementClient.FileSharesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fileSharesCreate**](FileSharesApi.md#fileSharesCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName} | 
[**fileSharesDelete**](FileSharesApi.md#fileSharesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName} | 
[**fileSharesGet**](FileSharesApi.md#fileSharesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName} | 
[**fileSharesList**](FileSharesApi.md#fileSharesList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares | 
[**fileSharesUpdate**](FileSharesApi.md#fileSharesUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/fileServices/default/shares/{shareName} | 



## fileSharesCreate

> FileShare fileSharesCreate(resourceGroupName, accountName, shareName, apiVersion, subscriptionId, fileShare)



Creates a new share under the specified account as described by request body. The share resource includes metadata and properties for that share. It does not include a list of the files contained by the share. 

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.FileSharesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let shareName = "shareName_example"; // String | The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let fileShare = new StorageManagementClient.FileShare(); // FileShare | Properties of the file share to create.
apiInstance.fileSharesCreate(resourceGroupName, accountName, shareName, apiVersion, subscriptionId, fileShare, (error, data, response) => {
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
 **shareName** | **String**| The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **fileShare** | [**FileShare**](FileShare.md)| Properties of the file share to create. | 

### Return type

[**FileShare**](FileShare.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## fileSharesDelete

> fileSharesDelete(resourceGroupName, accountName, shareName, apiVersion, subscriptionId)



Deletes specified share under its account.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.FileSharesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let shareName = "shareName_example"; // String | The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.fileSharesDelete(resourceGroupName, accountName, shareName, apiVersion, subscriptionId, (error, data, response) => {
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
 **shareName** | **String**| The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileSharesGet

> FileShare fileSharesGet(resourceGroupName, accountName, shareName, apiVersion, subscriptionId)



Gets properties of a specified share.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.FileSharesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let shareName = "shareName_example"; // String | The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.fileSharesGet(resourceGroupName, accountName, shareName, apiVersion, subscriptionId, (error, data, response) => {
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
 **shareName** | **String**| The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**FileShare**](FileShare.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileSharesList

> FileShareItems fileSharesList(resourceGroupName, accountName, apiVersion, subscriptionId, opts)



Lists all shares.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.FileSharesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'skipToken': "skipToken_example", // String | Optional. Continuation token for the list operation.
  'maxpagesize': "maxpagesize_example", // String | Optional. Specified maximum number of shares that can be included in the list.
  'filter': "filter_example" // String | Optional. When specified, only share names starting with the filter will be listed.
};
apiInstance.fileSharesList(resourceGroupName, accountName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **skipToken** | **String**| Optional. Continuation token for the list operation. | [optional] 
 **maxpagesize** | **String**| Optional. Specified maximum number of shares that can be included in the list. | [optional] 
 **filter** | **String**| Optional. When specified, only share names starting with the filter will be listed. | [optional] 

### Return type

[**FileShareItems**](FileShareItems.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fileSharesUpdate

> FileShare fileSharesUpdate(resourceGroupName, accountName, shareName, apiVersion, subscriptionId, fileShare)



Updates share properties as specified in request body. Properties not mentioned in the request will not be changed. Update fails if the specified share does not already exist. 

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.FileSharesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let shareName = "shareName_example"; // String | The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let fileShare = new StorageManagementClient.FileShare(); // FileShare | Properties to update for the file share.
apiInstance.fileSharesUpdate(resourceGroupName, accountName, shareName, apiVersion, subscriptionId, fileShare, (error, data, response) => {
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
 **shareName** | **String**| The name of the file share within the specified storage account. File share names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **fileShare** | [**FileShare**](FileShare.md)| Properties to update for the file share. | 

### Return type

[**FileShare**](FileShare.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

