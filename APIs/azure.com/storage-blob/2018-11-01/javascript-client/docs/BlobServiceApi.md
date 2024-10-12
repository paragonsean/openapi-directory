# StorageManagementClient.BlobServiceApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blobServicesGetServiceProperties**](BlobServiceApi.md#blobServicesGetServiceProperties) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/{BlobServicesName} | 
[**blobServicesSetServiceProperties**](BlobServiceApi.md#blobServicesSetServiceProperties) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/{BlobServicesName} | 



## blobServicesGetServiceProperties

> BlobServiceProperties blobServicesGetServiceProperties(resourceGroupName, accountName, apiVersion, subscriptionId, blobServicesName)



Gets the properties of a storage account’s Blob service, including properties for Storage Analytics and CORS (Cross-Origin Resource Sharing) rules.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.BlobServiceApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let blobServicesName = "blobServicesName_example"; // String | The name of the blob Service within the specified storage account. Blob Service Name must be 'default'
apiInstance.blobServicesGetServiceProperties(resourceGroupName, accountName, apiVersion, subscriptionId, blobServicesName, (error, data, response) => {
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
 **blobServicesName** | **String**| The name of the blob Service within the specified storage account. Blob Service Name must be &#39;default&#39; | 

### Return type

[**BlobServiceProperties**](BlobServiceProperties.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blobServicesSetServiceProperties

> BlobServiceProperties blobServicesSetServiceProperties(resourceGroupName, accountName, apiVersion, subscriptionId, blobServicesName, parameters)



Sets the properties of a storage account’s Blob service, including properties for Storage Analytics and CORS (Cross-Origin Resource Sharing) rules. 

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.BlobServiceApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let blobServicesName = "blobServicesName_example"; // String | The name of the blob Service within the specified storage account. Blob Service Name must be 'default'
let parameters = new StorageManagementClient.BlobServiceProperties(); // BlobServiceProperties | The properties of a storage account’s Blob service, including properties for Storage Analytics and CORS (Cross-Origin Resource Sharing) rules.
apiInstance.blobServicesSetServiceProperties(resourceGroupName, accountName, apiVersion, subscriptionId, blobServicesName, parameters, (error, data, response) => {
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
 **blobServicesName** | **String**| The name of the blob Service within the specified storage account. Blob Service Name must be &#39;default&#39; | 
 **parameters** | [**BlobServiceProperties**](BlobServiceProperties.md)| The properties of a storage account’s Blob service, including properties for Storage Analytics and CORS (Cross-Origin Resource Sharing) rules. | 

### Return type

[**BlobServiceProperties**](BlobServiceProperties.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

