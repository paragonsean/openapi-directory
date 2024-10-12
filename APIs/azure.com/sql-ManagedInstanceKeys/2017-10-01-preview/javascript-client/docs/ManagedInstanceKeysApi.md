# SqlManagementClient.ManagedInstanceKeysApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**managedInstanceKeysCreateOrUpdate**](ManagedInstanceKeysApi.md#managedInstanceKeysCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/keys/{keyName} | 
[**managedInstanceKeysDelete**](ManagedInstanceKeysApi.md#managedInstanceKeysDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/keys/{keyName} | 
[**managedInstanceKeysGet**](ManagedInstanceKeysApi.md#managedInstanceKeysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/keys/{keyName} | 
[**managedInstanceKeysListByInstance**](ManagedInstanceKeysApi.md#managedInstanceKeysListByInstance) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/managedInstances/{managedInstanceName}/keys | 



## managedInstanceKeysCreateOrUpdate

> ManagedInstanceKey managedInstanceKeysCreateOrUpdate(resourceGroupName, managedInstanceName, keyName, subscriptionId, apiVersion, parameters)



Creates or updates a managed instance key.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.ManagedInstanceKeysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
let keyName = "keyName_example"; // String | The name of the managed instance key to be operated on (updated or created).
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new SqlManagementClient.ManagedInstanceKey(); // ManagedInstanceKey | The requested managed instance key resource state.
apiInstance.managedInstanceKeysCreateOrUpdate(resourceGroupName, managedInstanceName, keyName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **keyName** | **String**| The name of the managed instance key to be operated on (updated or created). | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**ManagedInstanceKey**](ManagedInstanceKey.md)| The requested managed instance key resource state. | 

### Return type

[**ManagedInstanceKey**](ManagedInstanceKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## managedInstanceKeysDelete

> managedInstanceKeysDelete(resourceGroupName, managedInstanceName, keyName, subscriptionId, apiVersion)



Deletes the managed instance key with the given name.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.ManagedInstanceKeysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
let keyName = "keyName_example"; // String | The name of the managed instance key to be deleted.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.managedInstanceKeysDelete(resourceGroupName, managedInstanceName, keyName, subscriptionId, apiVersion, (error, data, response) => {
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
 **keyName** | **String**| The name of the managed instance key to be deleted. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## managedInstanceKeysGet

> ManagedInstanceKey managedInstanceKeysGet(resourceGroupName, managedInstanceName, keyName, subscriptionId, apiVersion)



Gets a managed instance key.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.ManagedInstanceKeysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
let keyName = "keyName_example"; // String | The name of the managed instance key to be retrieved.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.managedInstanceKeysGet(resourceGroupName, managedInstanceName, keyName, subscriptionId, apiVersion, (error, data, response) => {
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
 **keyName** | **String**| The name of the managed instance key to be retrieved. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**ManagedInstanceKey**](ManagedInstanceKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## managedInstanceKeysListByInstance

> ManagedInstanceKeyListResult managedInstanceKeysListByInstance(resourceGroupName, managedInstanceName, subscriptionId, apiVersion, opts)



Gets a list of managed instance keys.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.ManagedInstanceKeysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let managedInstanceName = "managedInstanceName_example"; // String | The name of the managed instance.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let opts = {
  'filter': "filter_example" // String | An OData filter expression that filters elements in the collection.
};
apiInstance.managedInstanceKeysListByInstance(resourceGroupName, managedInstanceName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| An OData filter expression that filters elements in the collection. | [optional] 

### Return type

[**ManagedInstanceKeyListResult**](ManagedInstanceKeyListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

