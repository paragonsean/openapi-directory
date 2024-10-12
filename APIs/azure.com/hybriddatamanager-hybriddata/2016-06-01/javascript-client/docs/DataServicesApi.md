# HybridDataManagementClient.DataServicesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dataServicesGet**](DataServicesApi.md#dataServicesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices/{dataServiceName} | 
[**dataServicesListByDataManager**](DataServicesApi.md#dataServicesListByDataManager) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.HybridData/dataManagers/{dataManagerName}/dataServices | 



## dataServicesGet

> DataService dataServicesGet(dataServiceName, subscriptionId, resourceGroupName, dataManagerName, apiVersion)



Gets the data service that match the data service name given.

### Example

```javascript
import HybridDataManagementClient from 'hybrid_data_management_client';
let defaultClient = HybridDataManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HybridDataManagementClient.DataServicesApi();
let dataServiceName = "dataServiceName_example"; // String | The name of the data service that is being queried.
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
apiInstance.dataServicesGet(dataServiceName, subscriptionId, resourceGroupName, dataManagerName, apiVersion, (error, data, response) => {
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
 **dataServiceName** | **String**| The name of the data service that is being queried. | 
 **subscriptionId** | **String**| The Subscription Id | 
 **resourceGroupName** | **String**| The Resource Group Name | 
 **dataManagerName** | **String**| The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only | 
 **apiVersion** | **String**| The API Version | 

### Return type

[**DataService**](DataService.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dataServicesListByDataManager

> DataServiceList dataServicesListByDataManager(subscriptionId, resourceGroupName, dataManagerName, apiVersion)



This method gets all the data services.

### Example

```javascript
import HybridDataManagementClient from 'hybrid_data_management_client';
let defaultClient = HybridDataManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new HybridDataManagementClient.DataServicesApi();
let subscriptionId = "subscriptionId_example"; // String | The Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The Resource Group Name
let dataManagerName = "dataManagerName_example"; // String | The name of the DataManager Resource within the specified resource group. DataManager names must be between 3 and 24 characters in length and use any alphanumeric and underscore only
let apiVersion = "apiVersion_example"; // String | The API Version
apiInstance.dataServicesListByDataManager(subscriptionId, resourceGroupName, dataManagerName, apiVersion, (error, data, response) => {
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

[**DataServiceList**](DataServiceList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

