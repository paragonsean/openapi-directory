# AzureSqlDatabase.ElasticPoolsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**elasticPoolsListMetricDefinitions**](ElasticPoolsApi.md#elasticPoolsListMetricDefinitions) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/elasticPools/{elasticPoolName}/metricDefinitions | 
[**elasticPoolsListMetrics**](ElasticPoolsApi.md#elasticPoolsListMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/elasticPools/{elasticPoolName}/metrics | 



## elasticPoolsListMetricDefinitions

> MetricDefinitionListResult elasticPoolsListMetricDefinitions(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName)



Returns elastic pool metric definitions.

### Example

```javascript
import AzureSqlDatabase from 'azure_sql_database';

let apiInstance = new AzureSqlDatabase.ElasticPoolsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let elasticPoolName = "elasticPoolName_example"; // String | The name of the elastic pool.
apiInstance.elasticPoolsListMetricDefinitions(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName, (error, data, response) => {
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

[**MetricDefinitionListResult**](MetricDefinitionListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## elasticPoolsListMetrics

> MetricListResult elasticPoolsListMetrics(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName, filter)



Returns elastic pool  metrics.

### Example

```javascript
import AzureSqlDatabase from 'azure_sql_database';

let apiInstance = new AzureSqlDatabase.ElasticPoolsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let elasticPoolName = "elasticPoolName_example"; // String | The name of the elastic pool.
let filter = "filter_example"; // String | An OData filter expression that describes a subset of metrics to return.
apiInstance.elasticPoolsListMetrics(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName, filter, (error, data, response) => {
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
 **filter** | **String**| An OData filter expression that describes a subset of metrics to return. | 

### Return type

[**MetricListResult**](MetricListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

