# SqlManagementClient.ManagedInstanceAdministratorsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**managedInstanceAdministratorsCreateOrUpdate**](ManagedInstanceAdministratorsApi.md#managedInstanceAdministratorsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/administrators/{administratorName} | 
[**managedInstanceAdministratorsDelete**](ManagedInstanceAdministratorsApi.md#managedInstanceAdministratorsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/administrators/{administratorName} | 
[**managedInstanceAdministratorsGet**](ManagedInstanceAdministratorsApi.md#managedInstanceAdministratorsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/administrators/{administratorName} | 
[**managedInstanceAdministratorsListByInstance**](ManagedInstanceAdministratorsApi.md#managedInstanceAdministratorsListByInstance) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/administrators | 



## managedInstanceAdministratorsCreateOrUpdate

> ManagedInstanceAdministrator managedInstanceAdministratorsCreateOrUpdate(resourceGroupName, managedInstanceName, administratorName, subscriptionId, apiVersion, parameters)



Creates or updates a managed instance administrator.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.ManagedInstanceAdministratorsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
let administratorName = "administratorName_example"; // String | The requested administrator name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new SqlManagementClient.ManagedInstanceAdministrator(); // ManagedInstanceAdministrator | The requested administrator parameters.
apiInstance.managedInstanceAdministratorsCreateOrUpdate(resourceGroupName, managedInstanceName, administratorName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **managedInstanceName** | **String**| The name of the managed instance. | 
 **administratorName** | **String**| The requested administrator name. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**ManagedInstanceAdministrator**](ManagedInstanceAdministrator.md)| The requested administrator parameters. | 

### Return type

[**ManagedInstanceAdministrator**](ManagedInstanceAdministrator.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## managedInstanceAdministratorsDelete

> managedInstanceAdministratorsDelete(resourceGroupName, managedInstanceName, administratorName, subscriptionId, apiVersion)



Deletes a managed instance administrator.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.ManagedInstanceAdministratorsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
let administratorName = "administratorName_example"; // String | The administrator name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.managedInstanceAdministratorsDelete(resourceGroupName, managedInstanceName, administratorName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **managedInstanceName** | **String**| The name of the managed instance. | 
 **administratorName** | **String**| The administrator name. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## managedInstanceAdministratorsGet

> ManagedInstanceAdministrator managedInstanceAdministratorsGet(resourceGroupName, managedInstanceName, administratorName, subscriptionId, apiVersion)



Gets a managed instance administrator.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.ManagedInstanceAdministratorsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
let administratorName = "administratorName_example"; // String | The administrator name.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.managedInstanceAdministratorsGet(resourceGroupName, managedInstanceName, administratorName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **managedInstanceName** | **String**| The name of the managed instance. | 
 **administratorName** | **String**| The administrator name. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**ManagedInstanceAdministrator**](ManagedInstanceAdministrator.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managedInstanceAdministratorsListByInstance

> ManagedInstanceAdministratorListResult managedInstanceAdministratorsListByInstance(resourceGroupName, managedInstanceName, subscriptionId, apiVersion)



Gets a list of managed instance administrators.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.ManagedInstanceAdministratorsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.managedInstanceAdministratorsListByInstance(resourceGroupName, managedInstanceName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal. | 
 **managedInstanceName** | **String**| The name of the managed instance. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**ManagedInstanceAdministratorListResult**](ManagedInstanceAdministratorListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

