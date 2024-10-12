# SqlManagementClient.ManagedInstanceOperationsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**managedInstanceOperationsListByManagedInstance**](ManagedInstanceOperationsApi.md#managedInstanceOperationsListByManagedInstance) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/operations | 



## managedInstanceOperationsListByManagedInstance

> ManagedInstanceOperationListResult managedInstanceOperationsListByManagedInstance(resourceGroupName, managedInstanceName, subscriptionId, apiVersion)



Gets a list of operations performed on the managed instance.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.ManagedInstanceOperationsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.managedInstanceOperationsListByManagedInstance(resourceGroupName, managedInstanceName, subscriptionId, apiVersion, (error, data, response) => {
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

[**ManagedInstanceOperationListResult**](ManagedInstanceOperationListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

