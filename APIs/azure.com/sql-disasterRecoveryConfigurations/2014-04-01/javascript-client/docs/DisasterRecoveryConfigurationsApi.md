# AzureSqlDatabaseDisasterRecoveryConfigurations.DisasterRecoveryConfigurationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disasterRecoveryConfigurationsCreateOrUpdate**](DisasterRecoveryConfigurationsApi.md#disasterRecoveryConfigurationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/disasterRecoveryConfiguration/{disasterRecoveryConfigurationName} | 
[**disasterRecoveryConfigurationsDelete**](DisasterRecoveryConfigurationsApi.md#disasterRecoveryConfigurationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/disasterRecoveryConfiguration/{disasterRecoveryConfigurationName} | 
[**disasterRecoveryConfigurationsFailover**](DisasterRecoveryConfigurationsApi.md#disasterRecoveryConfigurationsFailover) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/disasterRecoveryConfiguration/{disasterRecoveryConfigurationName}/failover | 
[**disasterRecoveryConfigurationsFailoverAllowDataLoss**](DisasterRecoveryConfigurationsApi.md#disasterRecoveryConfigurationsFailoverAllowDataLoss) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/disasterRecoveryConfiguration/{disasterRecoveryConfigurationName}/forceFailoverAllowDataLoss | 
[**disasterRecoveryConfigurationsGet**](DisasterRecoveryConfigurationsApi.md#disasterRecoveryConfigurationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/disasterRecoveryConfiguration/{disasterRecoveryConfigurationName} | 
[**disasterRecoveryConfigurationsList**](DisasterRecoveryConfigurationsApi.md#disasterRecoveryConfigurationsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/disasterRecoveryConfiguration | 



## disasterRecoveryConfigurationsCreateOrUpdate

> DisasterRecoveryConfiguration disasterRecoveryConfigurationsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, disasterRecoveryConfigurationName)



Creates or updates a disaster recovery configuration.

### Example

```javascript
import AzureSqlDatabaseDisasterRecoveryConfigurations from 'azure_sql_database_disaster_recovery_configurations';

let apiInstance = new AzureSqlDatabaseDisasterRecoveryConfigurations.DisasterRecoveryConfigurationsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let disasterRecoveryConfigurationName = "disasterRecoveryConfigurationName_example"; // String | The name of the disaster recovery configuration to be created/updated.
apiInstance.disasterRecoveryConfigurationsCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, serverName, disasterRecoveryConfigurationName, (error, data, response) => {
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
 **disasterRecoveryConfigurationName** | **String**| The name of the disaster recovery configuration to be created/updated. | 

### Return type

[**DisasterRecoveryConfiguration**](DisasterRecoveryConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disasterRecoveryConfigurationsDelete

> disasterRecoveryConfigurationsDelete(apiVersion, subscriptionId, resourceGroupName, serverName, disasterRecoveryConfigurationName)



Deletes a disaster recovery configuration.

### Example

```javascript
import AzureSqlDatabaseDisasterRecoveryConfigurations from 'azure_sql_database_disaster_recovery_configurations';

let apiInstance = new AzureSqlDatabaseDisasterRecoveryConfigurations.DisasterRecoveryConfigurationsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let disasterRecoveryConfigurationName = "disasterRecoveryConfigurationName_example"; // String | The name of the disaster recovery configuration to be deleted.
apiInstance.disasterRecoveryConfigurationsDelete(apiVersion, subscriptionId, resourceGroupName, serverName, disasterRecoveryConfigurationName, (error, data, response) => {
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
 **disasterRecoveryConfigurationName** | **String**| The name of the disaster recovery configuration to be deleted. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## disasterRecoveryConfigurationsFailover

> disasterRecoveryConfigurationsFailover(apiVersion, subscriptionId, resourceGroupName, serverName, disasterRecoveryConfigurationName)



Fails over from the current primary server to this server.

### Example

```javascript
import AzureSqlDatabaseDisasterRecoveryConfigurations from 'azure_sql_database_disaster_recovery_configurations';

let apiInstance = new AzureSqlDatabaseDisasterRecoveryConfigurations.DisasterRecoveryConfigurationsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let disasterRecoveryConfigurationName = "disasterRecoveryConfigurationName_example"; // String | The name of the disaster recovery configuration to failover.
apiInstance.disasterRecoveryConfigurationsFailover(apiVersion, subscriptionId, resourceGroupName, serverName, disasterRecoveryConfigurationName, (error, data, response) => {
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
 **disasterRecoveryConfigurationName** | **String**| The name of the disaster recovery configuration to failover. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## disasterRecoveryConfigurationsFailoverAllowDataLoss

> disasterRecoveryConfigurationsFailoverAllowDataLoss(apiVersion, subscriptionId, resourceGroupName, serverName, disasterRecoveryConfigurationName)



Fails over from the current primary server to this server. This operation might result in data loss.

### Example

```javascript
import AzureSqlDatabaseDisasterRecoveryConfigurations from 'azure_sql_database_disaster_recovery_configurations';

let apiInstance = new AzureSqlDatabaseDisasterRecoveryConfigurations.DisasterRecoveryConfigurationsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let disasterRecoveryConfigurationName = "disasterRecoveryConfigurationName_example"; // String | The name of the disaster recovery configuration to failover forcefully.
apiInstance.disasterRecoveryConfigurationsFailoverAllowDataLoss(apiVersion, subscriptionId, resourceGroupName, serverName, disasterRecoveryConfigurationName, (error, data, response) => {
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
 **disasterRecoveryConfigurationName** | **String**| The name of the disaster recovery configuration to failover forcefully. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## disasterRecoveryConfigurationsGet

> DisasterRecoveryConfiguration disasterRecoveryConfigurationsGet(apiVersion, subscriptionId, resourceGroupName, serverName, disasterRecoveryConfigurationName)



Gets a disaster recovery configuration.

### Example

```javascript
import AzureSqlDatabaseDisasterRecoveryConfigurations from 'azure_sql_database_disaster_recovery_configurations';

let apiInstance = new AzureSqlDatabaseDisasterRecoveryConfigurations.DisasterRecoveryConfigurationsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let disasterRecoveryConfigurationName = "disasterRecoveryConfigurationName_example"; // String | The name of the disaster recovery configuration.
apiInstance.disasterRecoveryConfigurationsGet(apiVersion, subscriptionId, resourceGroupName, serverName, disasterRecoveryConfigurationName, (error, data, response) => {
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
 **disasterRecoveryConfigurationName** | **String**| The name of the disaster recovery configuration. | 

### Return type

[**DisasterRecoveryConfiguration**](DisasterRecoveryConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disasterRecoveryConfigurationsList

> DisasterRecoveryConfigurationListResult disasterRecoveryConfigurationsList(apiVersion, subscriptionId, resourceGroupName, serverName)



Lists a server&#39;s disaster recovery configuration.

### Example

```javascript
import AzureSqlDatabaseDisasterRecoveryConfigurations from 'azure_sql_database_disaster_recovery_configurations';

let apiInstance = new AzureSqlDatabaseDisasterRecoveryConfigurations.DisasterRecoveryConfigurationsApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
apiInstance.disasterRecoveryConfigurationsList(apiVersion, subscriptionId, resourceGroupName, serverName, (error, data, response) => {
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

[**DisasterRecoveryConfigurationListResult**](DisasterRecoveryConfigurationListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

