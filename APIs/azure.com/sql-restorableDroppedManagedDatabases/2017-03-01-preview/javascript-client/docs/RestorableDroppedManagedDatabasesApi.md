# SqlManagementClient.RestorableDroppedManagedDatabasesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**restorableDroppedManagedDatabasesGet**](RestorableDroppedManagedDatabasesApi.md#restorableDroppedManagedDatabasesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/restorableDroppedDatabases/{restorableDroppedDatabaseId} | 
[**restorableDroppedManagedDatabasesListByInstance**](RestorableDroppedManagedDatabasesApi.md#restorableDroppedManagedDatabasesListByInstance) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/restorableDroppedDatabases | 



## restorableDroppedManagedDatabasesGet

> RestorableDroppedManagedDatabase restorableDroppedManagedDatabasesGet(resourceGroupName, managedInstanceName, restorableDroppedDatabaseId, subscriptionId, apiVersion)



Gets a restorable dropped managed database.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.RestorableDroppedManagedDatabasesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
let restorableDroppedDatabaseId = "restorableDroppedDatabaseId_example"; // String | 
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.restorableDroppedManagedDatabasesGet(resourceGroupName, managedInstanceName, restorableDroppedDatabaseId, subscriptionId, apiVersion, (error, data, response) => {
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
 **restorableDroppedDatabaseId** | **String**|  | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**RestorableDroppedManagedDatabase**](RestorableDroppedManagedDatabase.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## restorableDroppedManagedDatabasesListByInstance

> RestorableDroppedManagedDatabaseListResult restorableDroppedManagedDatabasesListByInstance(resourceGroupName, managedInstanceName, subscriptionId, apiVersion)



Gets a list of restorable dropped managed databases.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.RestorableDroppedManagedDatabasesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.restorableDroppedManagedDatabasesListByInstance(resourceGroupName, managedInstanceName, subscriptionId, apiVersion, (error, data, response) => {
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

[**RestorableDroppedManagedDatabaseListResult**](RestorableDroppedManagedDatabaseListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

