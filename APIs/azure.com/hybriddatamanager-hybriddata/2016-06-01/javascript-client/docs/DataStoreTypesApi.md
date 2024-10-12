# HybridDataManagementClient.DataStoreTypesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataStoreTypesGet**](DataStoreTypesApi.md#dataStoreTypesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataStoreTypes/{dataStoreTypeName} | 
[**dataStoreTypesListByDataManager**](DataStoreTypesApi.md#dataStoreTypesListByDataManager) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataStoreTypes | 



## dataStoreTypesGet

> DataStoreType dataStoreTypesGet(dataStoreTypeName, subscriptionId, resourceGroupName, dataManagerName, apiVersion)



Gets the data store/repository type given its name.

### Example

```javascript
import HybridDataManagementClient from 'hybrid_data_management_client';
let defaultClient = HybridDataManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HybridDataManagementClient.DataStoreTypesApi();
let dataStoreTypeName = "dataStoreTypeName_example"; // String | The data store/repository type name for which details are needed.
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
apiInstance.dataStoreTypesGet(dataStoreTypeName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, (error, data, response) => {
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
 **dataStoreTypeName** | **String**| The data store/repository type name for which details are needed. | 
 **subscriptionId** | **String**| The Subscription Id | 
 **resourceGroupName** | **String**| The Resource Group Name | 
 **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | 
 **apiVersion** | **String**| The API Version | 

### Return type

[**DataStoreType**](DataStoreType.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dataStoreTypesListByDataManager

> DataStoreTypeList dataStoreTypesListByDataManager(subscriptionId, resourceGroupName, dataManagerName, apiVersion)



Gets all the data store/repository types that the resource supports.

### Example

```javascript
import HybridDataManagementClient from 'hybrid_data_management_client';
let defaultClient = HybridDataManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HybridDataManagementClient.DataStoreTypesApi();
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
apiInstance.dataStoreTypesListByDataManager(subscriptionId, resourceGroupName, dataManagerName, apiVersion, (error, data, response) => {
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

[**DataStoreTypeList**](DataStoreTypeList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

