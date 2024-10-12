# SqlManagementClient.UsagesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**usagesListByInstancePool**](UsagesApi.md#usagesListByInstancePool) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/instancePools/{instancePoolName}/usages | 



## usagesListByInstancePool

> UsageListResult usagesListByInstancePool(resourceGroupName, instancePoolName, subscriptionId, apiVersion, opts)



Gets all instance pool usage metrics

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.UsagesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let instancePoolName = "instancePoolName_example"; // String | The name of the instance pool to be retrieved.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let opts = {
  'expandChildren': true // Boolean | Optional request parameter to include managed instance usages within the instance pool.
};
apiInstance.usagesListByInstancePool(resourceGroupName, instancePoolName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **instancePoolName** | **String**| The name of the instance pool to be retrieved. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **expandChildren** | **Boolean**| Optional request parameter to include managed instance usages within the instance pool. | [optional] 

### Return type

[**UsageListResult**](UsageListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

