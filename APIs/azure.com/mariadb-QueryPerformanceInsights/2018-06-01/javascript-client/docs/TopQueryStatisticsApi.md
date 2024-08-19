# MariaDbManagementClient.TopQueryStatisticsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**topQueryStatisticsGet**](TopQueryStatisticsApi.md#topQueryStatisticsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMariaDB/servers/{serverName}/topQueryStatistics/{queryStatisticId} | 
[**topQueryStatisticsListByServer**](TopQueryStatisticsApi.md#topQueryStatisticsListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMariaDB/servers/{serverName}/topQueryStatistics | 



## topQueryStatisticsGet

> QueryStatistic topQueryStatisticsGet(apiVersion, subscriptionId, resourceGroupName, serverName, queryStatisticId)



Retrieve the query statistic for specified identifier.

### Example

```javascript
import MariaDbManagementClient from 'maria_db_management_client';
let defaultClient = MariaDbManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MariaDbManagementClient.TopQueryStatisticsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let serverName = "serverName_example"; // String | The name of the server.
let queryStatisticId = "queryStatisticId_example"; // String | The Query Statistic identifier.
apiInstance.topQueryStatisticsGet(apiVersion, subscriptionId, resourceGroupName, serverName, queryStatisticId, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **serverName** | **String**| The name of the server. | 
 **queryStatisticId** | **String**| The Query Statistic identifier. | 

### Return type

[**QueryStatistic**](QueryStatistic.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## topQueryStatisticsListByServer

> TopQueryStatisticsResultList topQueryStatisticsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName, parameters)



Retrieve the Query-Store top queries for specified metric and aggregation.

### Example

```javascript
import MariaDbManagementClient from 'maria_db_management_client';
let defaultClient = MariaDbManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MariaDbManagementClient.TopQueryStatisticsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let serverName = "serverName_example"; // String | The name of the server.
let parameters = new MariaDbManagementClient.TopQueryStatisticsInput(); // TopQueryStatisticsInput | The required parameters for retrieving top query statistics.
apiInstance.topQueryStatisticsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **serverName** | **String**| The name of the server. | 
 **parameters** | [**TopQueryStatisticsInput**](TopQueryStatisticsInput.md)| The required parameters for retrieving top query statistics. | 

### Return type

[**TopQueryStatisticsResultList**](TopQueryStatisticsResultList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

