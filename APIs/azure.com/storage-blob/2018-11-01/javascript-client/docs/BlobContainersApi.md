# StorageManagementClient.BlobContainersApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blobContainersClearLegalHold**](BlobContainersApi.md#blobContainersClearLegalHold) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName}/clearLegalHold | 
[**blobContainersCreate**](BlobContainersApi.md#blobContainersCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName} | 
[**blobContainersCreateOrUpdateImmutabilityPolicy**](BlobContainersApi.md#blobContainersCreateOrUpdateImmutabilityPolicy) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName}/immutabilityPolicies/{immutabilityPolicyName} | 
[**blobContainersDelete**](BlobContainersApi.md#blobContainersDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName} | 
[**blobContainersDeleteImmutabilityPolicy**](BlobContainersApi.md#blobContainersDeleteImmutabilityPolicy) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName}/immutabilityPolicies/{immutabilityPolicyName} | 
[**blobContainersExtendImmutabilityPolicy**](BlobContainersApi.md#blobContainersExtendImmutabilityPolicy) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName}/immutabilityPolicies/default/extend | 
[**blobContainersGet**](BlobContainersApi.md#blobContainersGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName} | 
[**blobContainersGetImmutabilityPolicy**](BlobContainersApi.md#blobContainersGetImmutabilityPolicy) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName}/immutabilityPolicies/{immutabilityPolicyName} | 
[**blobContainersLease**](BlobContainersApi.md#blobContainersLease) | **POST** /subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName}/lease | 
[**blobContainersList**](BlobContainersApi.md#blobContainersList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers | 
[**blobContainersLockImmutabilityPolicy**](BlobContainersApi.md#blobContainersLockImmutabilityPolicy) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName}/immutabilityPolicies/default/lock | 
[**blobContainersSetLegalHold**](BlobContainersApi.md#blobContainersSetLegalHold) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName}/setLegalHold | 
[**blobContainersUpdate**](BlobContainersApi.md#blobContainersUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/default/containers/{containerName} | 



## blobContainersClearLegalHold

> LegalHold blobContainersClearLegalHold(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, legalHold)



Clears legal hold tags. Clearing the same or non-existent tag results in an idempotent operation. ClearLegalHold clears out only the specified tags in the request.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.BlobContainersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let legalHold = new StorageManagementClient.LegalHold(); // LegalHold | The LegalHold property that will be clear from a blob container.
apiInstance.blobContainersClearLegalHold(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, legalHold, (error, data, response) => {
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
 **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **legalHold** | [**LegalHold**](LegalHold.md)| The LegalHold property that will be clear from a blob container. | 

### Return type

[**LegalHold**](LegalHold.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## blobContainersCreate

> BlobContainer blobContainersCreate(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, blobContainer)



Creates a new container under the specified account as described by request body. The container resource includes metadata and properties for that container. It does not include a list of the blobs contained by the container. 

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.BlobContainersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let blobContainer = new StorageManagementClient.BlobContainer(); // BlobContainer | Properties of the blob container to create.
apiInstance.blobContainersCreate(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, blobContainer, (error, data, response) => {
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
 **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **blobContainer** | [**BlobContainer**](BlobContainer.md)| Properties of the blob container to create. | 

### Return type

[**BlobContainer**](BlobContainer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## blobContainersCreateOrUpdateImmutabilityPolicy

> ImmutabilityPolicy blobContainersCreateOrUpdateImmutabilityPolicy(resourceGroupName, accountName, containerName, immutabilityPolicyName, apiVersion, subscriptionId, opts)



Creates or updates an unlocked immutability policy. ETag in If-Match is honored if given but not required for this operation.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.BlobContainersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
let immutabilityPolicyName = "immutabilityPolicyName_example"; // String | The name of the blob container immutabilityPolicy within the specified storage account. ImmutabilityPolicy Name must be 'default'
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'ifMatch': "ifMatch_example", // String | The entity state (ETag) version of the immutability policy to update. A value of \"*\" can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied.
  'parameters': new StorageManagementClient.ImmutabilityPolicy() // ImmutabilityPolicy | The ImmutabilityPolicy Properties that will be created or updated to a blob container.
};
apiInstance.blobContainersCreateOrUpdateImmutabilityPolicy(resourceGroupName, accountName, containerName, immutabilityPolicyName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | 
 **immutabilityPolicyName** | **String**| The name of the blob container immutabilityPolicy within the specified storage account. ImmutabilityPolicy Name must be &#39;default&#39; | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **ifMatch** | **String**| The entity state (ETag) version of the immutability policy to update. A value of \&quot;*\&quot; can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied. | [optional] 
 **parameters** | [**ImmutabilityPolicy**](ImmutabilityPolicy.md)| The ImmutabilityPolicy Properties that will be created or updated to a blob container. | [optional] 

### Return type

[**ImmutabilityPolicy**](ImmutabilityPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## blobContainersDelete

> blobContainersDelete(resourceGroupName, accountName, containerName, apiVersion, subscriptionId)



Deletes specified container under its account.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.BlobContainersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.blobContainersDelete(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, (error, data, response) => {
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
 **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## blobContainersDeleteImmutabilityPolicy

> ImmutabilityPolicy blobContainersDeleteImmutabilityPolicy(resourceGroupName, accountName, containerName, immutabilityPolicyName, apiVersion, subscriptionId, ifMatch)



Aborts an unlocked immutability policy. The response of delete has immutabilityPeriodSinceCreationInDays set to 0. ETag in If-Match is required for this operation. Deleting a locked immutability policy is not allowed, only way is to delete the container after deleting all blobs inside the container.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.BlobContainersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
let immutabilityPolicyName = "immutabilityPolicyName_example"; // String | The name of the blob container immutabilityPolicy within the specified storage account. ImmutabilityPolicy Name must be 'default'
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let ifMatch = "ifMatch_example"; // String | The entity state (ETag) version of the immutability policy to update. A value of \"*\" can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied.
apiInstance.blobContainersDeleteImmutabilityPolicy(resourceGroupName, accountName, containerName, immutabilityPolicyName, apiVersion, subscriptionId, ifMatch, (error, data, response) => {
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
 **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | 
 **immutabilityPolicyName** | **String**| The name of the blob container immutabilityPolicy within the specified storage account. ImmutabilityPolicy Name must be &#39;default&#39; | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **ifMatch** | **String**| The entity state (ETag) version of the immutability policy to update. A value of \&quot;*\&quot; can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied. | 

### Return type

[**ImmutabilityPolicy**](ImmutabilityPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blobContainersExtendImmutabilityPolicy

> ImmutabilityPolicy blobContainersExtendImmutabilityPolicy(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, ifMatch, opts)



Extends the immutabilityPeriodSinceCreationInDays of a locked immutabilityPolicy. The only action allowed on a Locked policy will be this action. ETag in If-Match is required for this operation.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.BlobContainersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let ifMatch = "ifMatch_example"; // String | The entity state (ETag) version of the immutability policy to update. A value of \"*\" can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied.
let opts = {
  'parameters': new StorageManagementClient.ImmutabilityPolicy() // ImmutabilityPolicy | The ImmutabilityPolicy Properties that will be extended for a blob container.
};
apiInstance.blobContainersExtendImmutabilityPolicy(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, ifMatch, opts, (error, data, response) => {
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
 **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **ifMatch** | **String**| The entity state (ETag) version of the immutability policy to update. A value of \&quot;*\&quot; can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied. | 
 **parameters** | [**ImmutabilityPolicy**](ImmutabilityPolicy.md)| The ImmutabilityPolicy Properties that will be extended for a blob container. | [optional] 

### Return type

[**ImmutabilityPolicy**](ImmutabilityPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## blobContainersGet

> BlobContainer blobContainersGet(resourceGroupName, accountName, containerName, apiVersion, subscriptionId)



Gets properties of a specified container. 

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.BlobContainersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.blobContainersGet(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, (error, data, response) => {
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
 **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**BlobContainer**](BlobContainer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blobContainersGetImmutabilityPolicy

> ImmutabilityPolicy blobContainersGetImmutabilityPolicy(resourceGroupName, accountName, containerName, immutabilityPolicyName, apiVersion, subscriptionId, opts)



Gets the existing immutability policy along with the corresponding ETag in response headers and body.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.BlobContainersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
let immutabilityPolicyName = "immutabilityPolicyName_example"; // String | The name of the blob container immutabilityPolicy within the specified storage account. ImmutabilityPolicy Name must be 'default'
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'ifMatch': "ifMatch_example" // String | The entity state (ETag) version of the immutability policy to update. A value of \"*\" can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied.
};
apiInstance.blobContainersGetImmutabilityPolicy(resourceGroupName, accountName, containerName, immutabilityPolicyName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | 
 **immutabilityPolicyName** | **String**| The name of the blob container immutabilityPolicy within the specified storage account. ImmutabilityPolicy Name must be &#39;default&#39; | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **ifMatch** | **String**| The entity state (ETag) version of the immutability policy to update. A value of \&quot;*\&quot; can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied. | [optional] 

### Return type

[**ImmutabilityPolicy**](ImmutabilityPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blobContainersLease

> LeaseContainerResponse blobContainersLease(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, opts)



The Lease Container operation establishes and manages a lock on a container for delete operations. The lock duration can be 15 to 60 seconds, or can be infinite.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.BlobContainersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let opts = {
  'parameters': new StorageManagementClient.LeaseContainerRequest() // LeaseContainerRequest | Lease Container request body.
};
apiInstance.blobContainersLease(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, opts, (error, data, response) => {
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
 **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **parameters** | [**LeaseContainerRequest**](LeaseContainerRequest.md)| Lease Container request body. | [optional] 

### Return type

[**LeaseContainerResponse**](LeaseContainerResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## blobContainersList

> ListContainerItems blobContainersList(resourceGroupName, accountName, apiVersion, subscriptionId)



Lists all containers and does not support a prefix like data plane. Also SRP today does not return continuation token.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.BlobContainersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.blobContainersList(resourceGroupName, accountName, apiVersion, subscriptionId, (error, data, response) => {
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

[**ListContainerItems**](ListContainerItems.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blobContainersLockImmutabilityPolicy

> ImmutabilityPolicy blobContainersLockImmutabilityPolicy(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, ifMatch)



Sets the ImmutabilityPolicy to Locked state. The only action allowed on a Locked policy is ExtendImmutabilityPolicy action. ETag in If-Match is required for this operation.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.BlobContainersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let ifMatch = "ifMatch_example"; // String | The entity state (ETag) version of the immutability policy to update. A value of \"*\" can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied.
apiInstance.blobContainersLockImmutabilityPolicy(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, ifMatch, (error, data, response) => {
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
 **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **ifMatch** | **String**| The entity state (ETag) version of the immutability policy to update. A value of \&quot;*\&quot; can be used to apply the operation only if the immutability policy already exists. If omitted, this operation will always be applied. | 

### Return type

[**ImmutabilityPolicy**](ImmutabilityPolicy.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## blobContainersSetLegalHold

> LegalHold blobContainersSetLegalHold(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, legalHold)



Sets legal hold tags. Setting the same tag results in an idempotent operation. SetLegalHold follows an append pattern and does not clear out the existing tags that are not specified in the request.

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.BlobContainersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let legalHold = new StorageManagementClient.LegalHold(); // LegalHold | The LegalHold property that will be set to a blob container.
apiInstance.blobContainersSetLegalHold(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, legalHold, (error, data, response) => {
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
 **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **legalHold** | [**LegalHold**](LegalHold.md)| The LegalHold property that will be set to a blob container. | 

### Return type

[**LegalHold**](LegalHold.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## blobContainersUpdate

> BlobContainer blobContainersUpdate(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, blobContainer)



Updates container properties as specified in request body. Properties not mentioned in the request will be unchanged. Update fails if the specified container doesn&#39;t already exist. 

### Example

```javascript
import StorageManagementClient from 'storage_management_client';
let defaultClient = StorageManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorageManagementClient.BlobContainersApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the user's subscription. The name is case insensitive.
let accountName = "accountName_example"; // String | The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
let containerName = "containerName_example"; // String | The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let blobContainer = new StorageManagementClient.BlobContainer(); // BlobContainer | Properties to update for the blob container.
apiInstance.blobContainersUpdate(resourceGroupName, accountName, containerName, apiVersion, subscriptionId, blobContainer, (error, data, response) => {
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
 **containerName** | **String**| The name of the blob container within the specified storage account. Blob container names must be between 3 and 63 characters in length and use numbers, lower-case letters and dash (-) only. Every dash (-) character must be immediately preceded and followed by a letter or number. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **blobContainer** | [**BlobContainer**](BlobContainer.md)| Properties to update for the blob container. | 

### Return type

[**BlobContainer**](BlobContainer.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

