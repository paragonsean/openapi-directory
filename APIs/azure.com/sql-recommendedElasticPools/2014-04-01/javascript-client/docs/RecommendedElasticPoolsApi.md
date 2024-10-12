# AzureSqlDatabase.RecommendedElasticPoolsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**recommendedElasticPoolsGet**](RecommendedElasticPoolsApi.md#recommendedElasticPoolsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/recommendedElasticPools/{recommendedElasticPoolName} | 
[**recommendedElasticPoolsListByServer**](RecommendedElasticPoolsApi.md#recommendedElasticPoolsListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/recommendedElasticPools | 
[**recommendedElasticPoolsListMetrics**](RecommendedElasticPoolsApi.md#recommendedElasticPoolsListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/recommendedElasticPools/{recommendedElasticPoolName}/metrics | 



## recommendedElasticPoolsGet

> RecommendedElasticPool recommendedElasticPoolsGet(apiVersion, subscriptionId, resourceGroupName, serverName, recommendedElasticPoolName)



Gets a recommended elastic pool.

### Example

```javascript
import AzureSqlDatabase from 'azure_sql_database';

let apiInstance = new AzureSqlDatabase.RecommendedElasticPoolsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let recommendedElasticPoolName = "recommendedElasticPoolName_example"; // String | The name of the recommended elastic pool to be retrieved.
apiInstance.recommendedElasticPoolsGet(apiVersion, subscriptionId, resourceGroupName, serverName, recommendedElasticPoolName, (error, data, response) => {
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
 **recommendedElasticPoolName** | **String**| The name of the recommended elastic pool to be retrieved. | 

### Return type

[**RecommendedElasticPool**](RecommendedElasticPool.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recommendedElasticPoolsListByServer

> RecommendedElasticPoolListResult recommendedElasticPoolsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName)



Returns recommended elastic pools.

### Example

```javascript
import AzureSqlDatabase from 'azure_sql_database';

let apiInstance = new AzureSqlDatabase.RecommendedElasticPoolsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
apiInstance.recommendedElasticPoolsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName, (error, data, response) => {
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

### Return type

[**RecommendedElasticPoolListResult**](RecommendedElasticPoolListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recommendedElasticPoolsListMetrics

> RecommendedElasticPoolListMetricsResult recommendedElasticPoolsListMetrics(apiVersion, subscriptionId, resourceGroupName, serverName, recommendedElasticPoolName)



Returns recommended elastic pool metrics.

### Example

```javascript
import AzureSqlDatabase from 'azure_sql_database';

let apiInstance = new AzureSqlDatabase.RecommendedElasticPoolsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let recommendedElasticPoolName = "recommendedElasticPoolName_example"; // String | The name of the recommended elastic pool to be retrieved.
apiInstance.recommendedElasticPoolsListMetrics(apiVersion, subscriptionId, resourceGroupName, serverName, recommendedElasticPoolName, (error, data, response) => {
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
 **recommendedElasticPoolName** | **String**| The name of the recommended elastic pool to be retrieved. | 

### Return type

[**RecommendedElasticPoolListMetricsResult**](RecommendedElasticPoolListMetricsResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

