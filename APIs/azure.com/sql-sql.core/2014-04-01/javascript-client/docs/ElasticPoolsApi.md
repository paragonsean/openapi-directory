# AzureSqlDatabase.ElasticPoolsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**elasticPoolActivitiesListByElasticPool**](ElasticPoolsApi.md#elasticPoolActivitiesListByElasticPool) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/elasticPools/{elasticPoolName}/elasticPoolActivity | 
[**elasticPoolDatabaseActivitiesListByElasticPool**](ElasticPoolsApi.md#elasticPoolDatabaseActivitiesListByElasticPool) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/elasticPools/{elasticPoolName}/elasticPoolDatabaseActivity | 



## elasticPoolActivitiesListByElasticPool

> ElasticPoolActivityListResult elasticPoolActivitiesListByElasticPool(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName)



Returns elastic pool activities.

### Example

```javascript
import AzureSqlDatabase from 'azure_sql_database';

let apiInstance = new AzureSqlDatabase.ElasticPoolsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let elasticPoolName = "elasticPoolName_example"; // String | The name of the elastic pool for which to get the current activity.
apiInstance.elasticPoolActivitiesListByElasticPool(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName, (error, data, response) => {
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
 **elasticPoolName** | **String**| The name of the elastic pool for which to get the current activity. | 

### Return type

[**ElasticPoolActivityListResult**](ElasticPoolActivityListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## elasticPoolDatabaseActivitiesListByElasticPool

> ElasticPoolDatabaseActivityListResult elasticPoolDatabaseActivitiesListByElasticPool(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName)



Returns activity on databases inside of an elastic pool.

### Example

```javascript
import AzureSqlDatabase from 'azure_sql_database';

let apiInstance = new AzureSqlDatabase.ElasticPoolsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let elasticPoolName = "elasticPoolName_example"; // String | The name of the elastic pool.
apiInstance.elasticPoolDatabaseActivitiesListByElasticPool(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName, (error, data, response) => {
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
 **elasticPoolName** | **String**| The name of the elastic pool. | 

### Return type

[**ElasticPoolDatabaseActivityListResult**](ElasticPoolDatabaseActivityListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

