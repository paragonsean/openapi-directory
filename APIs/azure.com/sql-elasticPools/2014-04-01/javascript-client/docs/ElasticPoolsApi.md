# AzureSqlDatabase.ElasticPoolsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**elasticPoolsCreateOrUpdate**](ElasticPoolsApi.md#elasticPoolsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/elasticPools/{elasticPoolName} | 
[**elasticPoolsDelete**](ElasticPoolsApi.md#elasticPoolsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/elasticPools/{elasticPoolName} | 
[**elasticPoolsGet**](ElasticPoolsApi.md#elasticPoolsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/elasticPools/{elasticPoolName} | 
[**elasticPoolsListByServer**](ElasticPoolsApi.md#elasticPoolsListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/elasticPools | 
[**elasticPoolsUpdate**](ElasticPoolsApi.md#elasticPoolsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/elasticPools/{elasticPoolName} | 



## elasticPoolsCreateOrUpdate

> ElasticPool elasticPoolsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName, parameters)



Creates a new elastic pool or updates an existing elastic pool.

### Example

```javascript
import AzureSqlDatabase from 'azure_sql_database';

let apiInstance = new AzureSqlDatabase.ElasticPoolsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let elasticPoolName = "elasticPoolName_example"; // String | The name of the elastic pool to be operated on (updated or created).
let parameters = new AzureSqlDatabase.ElasticPool(); // ElasticPool | The required parameters for creating or updating an elastic pool.
apiInstance.elasticPoolsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName, parameters, (error, data, response) => {
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
 **elasticPoolName** | **String**| The name of the elastic pool to be operated on (updated or created). | 
 **parameters** | [**ElasticPool**](ElasticPool.md)| The required parameters for creating or updating an elastic pool. | 

### Return type

[**ElasticPool**](ElasticPool.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## elasticPoolsDelete

> elasticPoolsDelete(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName)



Deletes the elastic pool.

### Example

```javascript
import AzureSqlDatabase from 'azure_sql_database';

let apiInstance = new AzureSqlDatabase.ElasticPoolsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let elasticPoolName = "elasticPoolName_example"; // String | The name of the elastic pool to be deleted.
apiInstance.elasticPoolsDelete(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for the request. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **serverName** | **String**| The name of the server. | 
 **elasticPoolName** | **String**| The name of the elastic pool to be deleted. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## elasticPoolsGet

> ElasticPool elasticPoolsGet(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName)



Gets an elastic pool.

### Example

```javascript
import AzureSqlDatabase from 'azure_sql_database';

let apiInstance = new AzureSqlDatabase.ElasticPoolsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let elasticPoolName = "elasticPoolName_example"; // String | The name of the elastic pool to be retrieved.
apiInstance.elasticPoolsGet(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName, (error, data, response) => {
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
 **elasticPoolName** | **String**| The name of the elastic pool to be retrieved. | 

### Return type

[**ElasticPool**](ElasticPool.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## elasticPoolsListByServer

> ElasticPoolListResult elasticPoolsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName)



Returns a list of elastic pools in a server.

### Example

```javascript
import AzureSqlDatabase from 'azure_sql_database';

let apiInstance = new AzureSqlDatabase.ElasticPoolsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
apiInstance.elasticPoolsListByServer(apiVersion, subscriptionId, resourceGroupName, serverName, (error, data, response) => {
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

[**ElasticPoolListResult**](ElasticPoolListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## elasticPoolsUpdate

> ElasticPool elasticPoolsUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName, parameters)



Updates an existing elastic pool.

### Example

```javascript
import AzureSqlDatabase from 'azure_sql_database';

let apiInstance = new AzureSqlDatabase.ElasticPoolsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let elasticPoolName = "elasticPoolName_example"; // String | The name of the elastic pool to be updated.
let parameters = new AzureSqlDatabase.ElasticPoolUpdate(); // ElasticPoolUpdate | The required parameters for updating an elastic pool.
apiInstance.elasticPoolsUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, elasticPoolName, parameters, (error, data, response) => {
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
 **elasticPoolName** | **String**| The name of the elastic pool to be updated. | 
 **parameters** | [**ElasticPoolUpdate**](ElasticPoolUpdate.md)| The required parameters for updating an elastic pool. | 

### Return type

[**ElasticPool**](ElasticPool.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

