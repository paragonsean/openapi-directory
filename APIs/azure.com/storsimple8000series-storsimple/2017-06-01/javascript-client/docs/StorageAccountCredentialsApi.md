# StorSimple8000SeriesManagementClient.StorageAccountCredentialsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storageAccountCredentialsCreateOrUpdate**](StorageAccountCredentialsApi.md#storageAccountCredentialsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/storageAccountCredentials/{storageAccountCredentialName} | 
[**storageAccountCredentialsDelete**](StorageAccountCredentialsApi.md#storageAccountCredentialsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/storageAccountCredentials/{storageAccountCredentialName} | 
[**storageAccountCredentialsGet**](StorageAccountCredentialsApi.md#storageAccountCredentialsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/storageAccountCredentials/{storageAccountCredentialName} | 
[**storageAccountCredentialsListByManager**](StorageAccountCredentialsApi.md#storageAccountCredentialsListByManager) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorSimple/managers/{managerName}/storageAccountCredentials | 



## storageAccountCredentialsCreateOrUpdate

> StorageAccountCredential storageAccountCredentialsCreateOrUpdate(storageAccountCredentialName, subscriptionId, resourceGroupName, managerName, apiVersion, parameters)



Creates or updates the storage account credential.

### Example

```javascript
import StorSimple8000SeriesManagementClient from 'stor_simple8000_series_management_client';
let defaultClient = StorSimple8000SeriesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimple8000SeriesManagementClient.StorageAccountCredentialsApi();
let storageAccountCredentialName = "storageAccountCredentialName_example"; // String | The storage account credential name.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
let parameters = new StorSimple8000SeriesManagementClient.StorageAccountCredential(); // StorageAccountCredential | The storage account credential to be added or updated.
apiInstance.storageAccountCredentialsCreateOrUpdate(storageAccountCredentialName, subscriptionId, resourceGroupName, managerName, apiVersion, parameters, (error, data, response) => {
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
 **storageAccountCredentialName** | **String**| The storage account credential name. | 
 **subscriptionId** | **String**| The subscription id | 
 **resourceGroupName** | **String**| The resource group name | 
 **managerName** | **String**| The manager name | 
 **apiVersion** | **String**| The api version | 
 **parameters** | [**StorageAccountCredential**](StorageAccountCredential.md)| The storage account credential to be added or updated. | 

### Return type

[**StorageAccountCredential**](StorageAccountCredential.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## storageAccountCredentialsDelete

> storageAccountCredentialsDelete(storageAccountCredentialName, subscriptionId, resourceGroupName, managerName, apiVersion)



Deletes the storage account credential.

### Example

```javascript
import StorSimple8000SeriesManagementClient from 'stor_simple8000_series_management_client';
let defaultClient = StorSimple8000SeriesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimple8000SeriesManagementClient.StorageAccountCredentialsApi();
let storageAccountCredentialName = "storageAccountCredentialName_example"; // String | The name of the storage account credential.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.storageAccountCredentialsDelete(storageAccountCredentialName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **storageAccountCredentialName** | **String**| The name of the storage account credential. | 
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
- **Accept**: Not defined


## storageAccountCredentialsGet

> StorageAccountCredential storageAccountCredentialsGet(storageAccountCredentialName, subscriptionId, resourceGroupName, managerName, apiVersion)



Gets the properties of the specified storage account credential name.

### Example

```javascript
import StorSimple8000SeriesManagementClient from 'stor_simple8000_series_management_client';
let defaultClient = StorSimple8000SeriesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimple8000SeriesManagementClient.StorageAccountCredentialsApi();
let storageAccountCredentialName = "storageAccountCredentialName_example"; // String | The name of storage account credential to be fetched.
let subscriptionId = "subscriptionId_example"; // String | The subscription id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name
let managerName = "managerName_example"; // String | The manager name
let apiVersion = "apiVersion_example"; // String | The api version
apiInstance.storageAccountCredentialsGet(storageAccountCredentialName, subscriptionId, resourceGroupName, managerName, apiVersion, (error, data, response) => {
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
 **storageAccountCredentialName** | **String**| The name of storage account credential to be fetched. | 
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



Gets all the storage account credentials in a manager.

### Example

```javascript
import StorSimple8000SeriesManagementClient from 'stor_simple8000_series_management_client';
let defaultClient = StorSimple8000SeriesManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new StorSimple8000SeriesManagementClient.StorageAccountCredentialsApi();
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

