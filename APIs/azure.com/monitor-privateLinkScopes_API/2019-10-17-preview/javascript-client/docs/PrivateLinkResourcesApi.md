# AzureMonitorPrivateLinkScopes.PrivateLinkResourcesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**privateLinkResourcesGet**](PrivateLinkResourcesApi.md#privateLinkResourcesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/privateLinkScopes/{scopeName}/privateLinkResources/{groupName} | 
[**privateLinkResourcesListByPrivateLinkScope**](PrivateLinkResourcesApi.md#privateLinkResourcesListByPrivateLinkScope) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/privateLinkScopes/{scopeName}/privateLinkResources | 



## privateLinkResourcesGet

> PrivateLinkResource privateLinkResourcesGet(subscriptionId, resourceGroupName, apiVersion, scopeName, groupName)



Gets the private link resources that need to be created for a Azure Monitor PrivateLinkScope.

### Example

```javascript
import AzureMonitorPrivateLinkScopes from 'azure_monitor_private_link_scopes';
let defaultClient = AzureMonitorPrivateLinkScopes.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMonitorPrivateLinkScopes.PrivateLinkResourcesApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let scopeName = "scopeName_example"; // String | Name of the Azure Monitor PrivateLinkScope that will contain the datasource
let groupName = "groupName_example"; // String | The name of the private link resource.
apiInstance.privateLinkResourcesGet(subscriptionId, resourceGroupName, apiVersion, scopeName, groupName, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **scopeName** | **String**| Name of the Azure Monitor PrivateLinkScope that will contain the datasource | 
 **groupName** | **String**| The name of the private link resource. | 

### Return type

[**PrivateLinkResource**](PrivateLinkResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateLinkResourcesListByPrivateLinkScope

> PrivateLinkResourceListResult privateLinkResourcesListByPrivateLinkScope(subscriptionId, resourceGroupName, apiVersion, scopeName)



Gets the private link resources that need to be created for a Azure Monitor PrivateLinkScope.

### Example

```javascript
import AzureMonitorPrivateLinkScopes from 'azure_monitor_private_link_scopes';
let defaultClient = AzureMonitorPrivateLinkScopes.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMonitorPrivateLinkScopes.PrivateLinkResourcesApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let scopeName = "scopeName_example"; // String | Name of the Azure Monitor PrivateLinkScope that will contain the datasource
apiInstance.privateLinkResourcesListByPrivateLinkScope(subscriptionId, resourceGroupName, apiVersion, scopeName, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **scopeName** | **String**| Name of the Azure Monitor PrivateLinkScope that will contain the datasource | 

### Return type

[**PrivateLinkResourceListResult**](PrivateLinkResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

