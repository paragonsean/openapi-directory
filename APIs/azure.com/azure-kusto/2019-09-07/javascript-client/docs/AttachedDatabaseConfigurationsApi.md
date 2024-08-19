# KustoManagementClient.AttachedDatabaseConfigurationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attachedDatabaseConfigurationsCreateOrUpdate**](AttachedDatabaseConfigurationsApi.md#attachedDatabaseConfigurationsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/attachedDatabaseConfigurations/{attachedDatabaseConfigurationName} | 
[**attachedDatabaseConfigurationsDelete**](AttachedDatabaseConfigurationsApi.md#attachedDatabaseConfigurationsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/attachedDatabaseConfigurations/{attachedDatabaseConfigurationName} | 
[**attachedDatabaseConfigurationsGet**](AttachedDatabaseConfigurationsApi.md#attachedDatabaseConfigurationsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/attachedDatabaseConfigurations/{attachedDatabaseConfigurationName} | 
[**attachedDatabaseConfigurationsListByCluster**](AttachedDatabaseConfigurationsApi.md#attachedDatabaseConfigurationsListByCluster) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Kusto/clusters/{clusterName}/attachedDatabaseConfigurations | 



## attachedDatabaseConfigurationsCreateOrUpdate

> AttachedDatabaseConfiguration attachedDatabaseConfigurationsCreateOrUpdate(resourceGroupName, clusterName, attachedDatabaseConfigurationName, subscriptionId, apiVersion, parameters)



Creates or updates an attached database configuration.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.AttachedDatabaseConfigurationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let attachedDatabaseConfigurationName = "attachedDatabaseConfigurationName_example"; // String | The name of the attached database configuration.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
let parameters = new KustoManagementClient.AttachedDatabaseConfiguration(); // AttachedDatabaseConfiguration | The database parameters supplied to the CreateOrUpdate operation.
apiInstance.attachedDatabaseConfigurationsCreateOrUpdate(resourceGroupName, clusterName, attachedDatabaseConfigurationName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | 
 **clusterName** | **String**| The name of the Kusto cluster. | 
 **attachedDatabaseConfigurationName** | **String**| The name of the attached database configuration. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 
 **parameters** | [**AttachedDatabaseConfiguration**](AttachedDatabaseConfiguration.md)| The database parameters supplied to the CreateOrUpdate operation. | 

### Return type

[**AttachedDatabaseConfiguration**](AttachedDatabaseConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## attachedDatabaseConfigurationsDelete

> attachedDatabaseConfigurationsDelete(resourceGroupName, clusterName, attachedDatabaseConfigurationName, subscriptionId, apiVersion)



Deletes the attached database configuration with the given name.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.AttachedDatabaseConfigurationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let attachedDatabaseConfigurationName = "attachedDatabaseConfigurationName_example"; // String | The name of the attached database configuration.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
apiInstance.attachedDatabaseConfigurationsDelete(resourceGroupName, clusterName, attachedDatabaseConfigurationName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | 
 **clusterName** | **String**| The name of the Kusto cluster. | 
 **attachedDatabaseConfigurationName** | **String**| The name of the attached database configuration. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attachedDatabaseConfigurationsGet

> AttachedDatabaseConfiguration attachedDatabaseConfigurationsGet(resourceGroupName, clusterName, attachedDatabaseConfigurationName, subscriptionId, apiVersion)



Returns an attached database configuration.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.AttachedDatabaseConfigurationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let attachedDatabaseConfigurationName = "attachedDatabaseConfigurationName_example"; // String | The name of the attached database configuration.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
apiInstance.attachedDatabaseConfigurationsGet(resourceGroupName, clusterName, attachedDatabaseConfigurationName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | 
 **clusterName** | **String**| The name of the Kusto cluster. | 
 **attachedDatabaseConfigurationName** | **String**| The name of the attached database configuration. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 

### Return type

[**AttachedDatabaseConfiguration**](AttachedDatabaseConfiguration.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## attachedDatabaseConfigurationsListByCluster

> AttachedDatabaseConfigurationListResult attachedDatabaseConfigurationsListByCluster(resourceGroupName, clusterName, subscriptionId, apiVersion)



Returns the list of attached database configurations of the given Kusto cluster.

### Example

```javascript
import KustoManagementClient from 'kusto_management_client';

let apiInstance = new KustoManagementClient.AttachedDatabaseConfigurationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group containing the Kusto cluster.
let clusterName = "clusterName_example"; // String | The name of the Kusto cluster.
let subscriptionId = "subscriptionId_example"; // String | Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API Version.
apiInstance.attachedDatabaseConfigurationsListByCluster(resourceGroupName, clusterName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group containing the Kusto cluster. | 
 **clusterName** | **String**| The name of the Kusto cluster. | 
 **subscriptionId** | **String**| Gets subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API Version. | 

### Return type

[**AttachedDatabaseConfigurationListResult**](AttachedDatabaseConfigurationListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

