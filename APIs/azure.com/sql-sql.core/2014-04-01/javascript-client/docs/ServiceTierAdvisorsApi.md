# AzureSqlDatabase.ServiceTierAdvisorsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serviceTierAdvisorsGet**](ServiceTierAdvisorsApi.md#serviceTierAdvisorsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/serviceTierAdvisors/{serviceTierAdvisorName} | 
[**serviceTierAdvisorsListByDatabase**](ServiceTierAdvisorsApi.md#serviceTierAdvisorsListByDatabase) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/serviceTierAdvisors | 



## serviceTierAdvisorsGet

> ServiceTierAdvisor serviceTierAdvisorsGet(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, serviceTierAdvisorName)



Gets a service tier advisor.

### Example

```javascript
import AzureSqlDatabase from 'azure_sql_database';

let apiInstance = new AzureSqlDatabase.ServiceTierAdvisorsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of database.
let serviceTierAdvisorName = "serviceTierAdvisorName_example"; // String | The name of service tier advisor.
apiInstance.serviceTierAdvisorsGet(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, serviceTierAdvisorName, (error, data, response) => {
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
 **databaseName** | **String**| The name of database. | 
 **serviceTierAdvisorName** | **String**| The name of service tier advisor. | 

### Return type

[**ServiceTierAdvisor**](ServiceTierAdvisor.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceTierAdvisorsListByDatabase

> ServiceTierAdvisorListResult serviceTierAdvisorsListByDatabase(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName)



Returns service tier advisors for specified database.

### Example

```javascript
import AzureSqlDatabase from 'azure_sql_database';

let apiInstance = new AzureSqlDatabase.ServiceTierAdvisorsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let databaseName = "databaseName_example"; // String | The name of database.
apiInstance.serviceTierAdvisorsListByDatabase(apiVersion, subscriptionId, resourceGroupName, serverName, databaseName, (error, data, response) => {
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
 **databaseName** | **String**| The name of database. | 

### Return type

[**ServiceTierAdvisorListResult**](ServiceTierAdvisorListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

