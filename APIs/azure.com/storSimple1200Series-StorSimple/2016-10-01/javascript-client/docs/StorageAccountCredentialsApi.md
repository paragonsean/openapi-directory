# StorSimpleManagementClient.StorageAccountCredentialsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storageAccountCredentialsCreateOrUpdate**](StorageAccountCredentialsApi.md#storageAccountCredentialsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/storageAccountCredentials/{credentialName} | 
[**storageAccountCredentialsDelete**](StorageAccountCredentialsApi.md#storageAccountCredentialsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/storageAccountCredentials/{credentialName} | 
[**storageAccountCredentialsGet**](StorageAccountCredentialsApi.md#storageAccountCredentialsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/storageAccountCredentials/{credentialName} | 
[**storageAccountCredentialsListByManager**](StorageAccountCredentialsApi.md#storageAccountCredentialsListByManager) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/storageAccountCredentials | 



## storageAccountCredentialsCreateOrUpdate

> StorageAccountCredential storageAccountCredentialsCreateOrUpdate(credentialName, subscriptionId, resourceGroupName, managerName, apiVersion, storageAccount)



Creates or updates the storage account credential

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.StorageAccountCredentialsApi();
let credentialName = "credentialName_example"; // String | The credential name.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
let storageAccount = new StorSimpleManagementClient.StorageAccountCredential(); // StorageAccountCredential | The storage account credential to be added or updated.
apiInstance.storageAccountCredentialsCreateOrUpdate(credentialName, subscriptionId, resourceGroupName, managerName, apiVersion, storageAccount, (error, data, response) => {
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
 **credentialName** | **String**| The credential name. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 
 **storageAccount** | [**StorageAccountCredential**](StorageAccountCredential.md)| The storage account credential to be added or updated. | 

### Return type

[**StorageAccountCredential**](StorageAccountCredential.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storageAccountCredentialsDelete

> storageAccountCredentialsDelete(credentialName, subscriptionId, resourceGroupName, managerName, apiVersion)



Deletes the storage account credential

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.StorageAccountCredentialsApi();
let credentialName = "credentialName_example"; // String | The name of the storage account credential.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.storageAccountCredentialsDelete(credentialName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **credentialName** | **String**| The name of the storage account credential. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageAccountCredentialsGet

> StorageAccountCredential storageAccountCredentialsGet(credentialName, subscriptionId, resourceGroupName, managerName, apiVersion)



Returns the properties of the specified storage account credential name.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.StorageAccountCredentialsApi();
let credentialName = "credentialName_example"; // String | The name of storage account credential to be fetched.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.storageAccountCredentialsGet(credentialName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **credentialName** | **String**| The name of storage account credential to be fetched. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

[**StorageAccountCredential**](StorageAccountCredential.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storageAccountCredentialsListByManager

> StorageAccountCredentialList storageAccountCredentialsListByManager(subscriptionId, resourceGroupName, managerName, apiVersion)



Retrieves all the storage account credentials in a manager.

### Example

```javascript
import StorSimpleManagementClient from 'stor_simple_management_client';
let defaultClient = StorSimpleManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimpleManagementClient.StorageAccountCredentialsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.storageAccountCredentialsListByManager(subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 

### Return type

[**StorageAccountCredentialList**](StorageAccountCredentialList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

