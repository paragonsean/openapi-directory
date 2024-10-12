# MySqlManagementClient.WaitStatisticsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**waitStatisticsGet**](WaitStatisticsApi.md#waitStatisticsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/servers/{serverName}/waitStatistics/{waitStatisticsId} | 
[**waitStatisticsListByServer**](WaitStatisticsApi.md#waitStatisticsListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMySQL/servers/{serverName}/waitStatistics | 



## waitStatisticsGet

> WaitStatistic waitStatisticsGet(apiVersion, subscriptionId, resourceGroupName, serverName, waitStatisticsId)



Retrieve wait statistics for specified identifier.

### Example

```javascript
import MySqlManagementClient from 'my_sql_management_client';
let defaultClient = MySqlManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MySqlManagementClient.WaitStatisticsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let waitStatisticsId = "waitStatisticsId_example"; // String | The Wait Statistic identifier.
apiInstance.waitStatisticsGet(apiVersion, subscriptionId, resourceGroupName, serverName, waitStatisticsId, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the request. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **waitStatisticsId** | **String**| The Wait Statistic identifier. | 

### Return type

[**WaitStatistic**](WaitStatistic.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## waitStatisticsListByServer

> WaitStatisticsResultList waitStatisticsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName, parameters)



Retrieve wait statistics for specified aggregation window.

### Example

```javascript
import MySqlManagementClient from 'my_sql_management_client';
let defaultClient = MySqlManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MySqlManagementClient.WaitStatisticsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let parameters = new MySqlManagementClient.WaitStatisticsInput(); // WaitStatisticsInput | The required parameters for retrieving wait statistics.
apiInstance.waitStatisticsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the request. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **parameters** | [**WaitStatisticsInput**](WaitStatisticsInput.md)| The required parameters for retrieving wait statistics. | 

### Return type

[**WaitStatisticsResultList**](WaitStatisticsResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

