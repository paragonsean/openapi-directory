# HybridDataManagementClient.PublicKeysApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**publicKeysGet**](PublicKeysApi.md#publicKeysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/publicKeys/{publicKeyName} | 
[**publicKeysListByDataManager**](PublicKeysApi.md#publicKeysListByDataManager) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/publicKeys | 



## publicKeysGet

> PublicKey publicKeysGet(publicKeyName, subscriptionId, resourceGroupName, dataManagerName, apiVersion)



This method gets the public keys.

### Example

```javascript
import HybridDataManagementClient from 'hybrid_data_management_client';
let defaultClient = HybridDataManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HybridDataManagementClient.PublicKeysApi();
let publicKeyName = "publicKeyName_example"; // String | Name of the public key.
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
apiInstance.publicKeysGet(publicKeyName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, (error, data, response) => {
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
 **publicKeyName** | **String**| Name of the public key. | 
 **subscriptionId** | **String**| The Subscription Id | 
 **resourceGroupName** | **String**| The Resource Group Name | 
 **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | 
 **apiVersion** | **String**| The API Version | 

### Return type

[**PublicKey**](PublicKey.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## publicKeysListByDataManager

> PublicKeyList publicKeysListByDataManager(subscriptionId, resourceGroupName, dataManagerName, apiVersion)



This method gets the list view of public keys, however it will only have one element.

### Example

```javascript
import HybridDataManagementClient from 'hybrid_data_management_client';
let defaultClient = HybridDataManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HybridDataManagementClient.PublicKeysApi();
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
apiInstance.publicKeysListByDataManager(subscriptionId, resourceGroupName, dataManagerName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Subscription Id | 
 **resourceGroupName** | **String**| The Resource Group Name | 
 **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | 
 **apiVersion** | **String**| The API Version | 

### Return type

[**PublicKeyList**](PublicKeyList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

