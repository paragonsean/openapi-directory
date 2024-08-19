# AzureMonitorPrivateLinkScopes.PrivateLinkScopedResourcesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**privateLinkScopedResourcesCreateOrUpdate**](PrivateLinkScopedResourcesApi.md#privateLinkScopedResourcesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/privateLinkScopes/{scopeName}/scopedResources/{name} | 
[**privateLinkScopedResourcesDelete**](PrivateLinkScopedResourcesApi.md#privateLinkScopedResourcesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/privateLinkScopes/{scopeName}/scopedResources/{name} | 
[**privateLinkScopedResourcesGet**](PrivateLinkScopedResourcesApi.md#privateLinkScopedResourcesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/privateLinkScopes/{scopeName}/scopedResources/{name} | 
[**privateLinkScopedResourcesListByPrivateLinkScope**](PrivateLinkScopedResourcesApi.md#privateLinkScopedResourcesListByPrivateLinkScope) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/privateLinkScopes/{scopeName}/scopedResources | 



## privateLinkScopedResourcesCreateOrUpdate

> ScopedResource privateLinkScopedResourcesCreateOrUpdate(subscriptionId, resourceGroupName, apiVersion, scopeName, name, parameters)



Approve or reject a private endpoint connection with a given name.

### Example

```javascript
import AzureMonitorPrivateLinkScopes from 'azure_monitor_private_link_scopes';
let defaultClient = AzureMonitorPrivateLinkScopes.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMonitorPrivateLinkScopes.PrivateLinkScopedResourcesApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let scopeName = "scopeName_example"; // String | Name of the Azure Monitor PrivateLinkScope that will contain the datasource
let name = "name_example"; // String | The name of the scoped resource object.
let parameters = new AzureMonitorPrivateLinkScopes.ScopedResource(); // ScopedResource | 
apiInstance.privateLinkScopedResourcesCreateOrUpdate(subscriptionId, resourceGroupName, apiVersion, scopeName, name, parameters, (error, data, response) => {
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
 **name** | **String**| The name of the scoped resource object. | 
 **parameters** | [**ScopedResource**](ScopedResource.md)|  | 

### Return type

[**ScopedResource**](ScopedResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateLinkScopedResourcesDelete

> privateLinkScopedResourcesDelete(subscriptionId, resourceGroupName, apiVersion, scopeName, name)



Deletes a private endpoint connection with a given name.

### Example

```javascript
import AzureMonitorPrivateLinkScopes from 'azure_monitor_private_link_scopes';
let defaultClient = AzureMonitorPrivateLinkScopes.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMonitorPrivateLinkScopes.PrivateLinkScopedResourcesApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let scopeName = "scopeName_example"; // String | Name of the Azure Monitor PrivateLinkScope that will contain the datasource
let name = "name_example"; // String | The name of the scoped resource object.
apiInstance.privateLinkScopedResourcesDelete(subscriptionId, resourceGroupName, apiVersion, scopeName, name, (error, data, response) => {
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
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **scopeName** | **String**| Name of the Azure Monitor PrivateLinkScope that will contain the datasource | 
 **name** | **String**| The name of the scoped resource object. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## privateLinkScopedResourcesGet

> ScopedResource privateLinkScopedResourcesGet(subscriptionId, resourceGroupName, apiVersion, scopeName, name)



Gets a scoped resource in a private link scope.

### Example

```javascript
import AzureMonitorPrivateLinkScopes from 'azure_monitor_private_link_scopes';
let defaultClient = AzureMonitorPrivateLinkScopes.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMonitorPrivateLinkScopes.PrivateLinkScopedResourcesApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let scopeName = "scopeName_example"; // String | Name of the Azure Monitor PrivateLinkScope that will contain the datasource
let name = "name_example"; // String | The name of the scoped resource object.
apiInstance.privateLinkScopedResourcesGet(subscriptionId, resourceGroupName, apiVersion, scopeName, name, (error, data, response) => {
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
 **name** | **String**| The name of the scoped resource object. | 

### Return type

[**ScopedResource**](ScopedResource.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateLinkScopedResourcesListByPrivateLinkScope

> ScopedResourceListResult privateLinkScopedResourcesListByPrivateLinkScope(subscriptionId, resourceGroupName, apiVersion, scopeName)



Gets all private endpoint connections on a private link scope.

### Example

```javascript
import AzureMonitorPrivateLinkScopes from 'azure_monitor_private_link_scopes';
let defaultClient = AzureMonitorPrivateLinkScopes.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMonitorPrivateLinkScopes.PrivateLinkScopedResourcesApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let scopeName = "scopeName_example"; // String | Name of the Azure Monitor PrivateLinkScope that will contain the datasource
apiInstance.privateLinkScopedResourcesListByPrivateLinkScope(subscriptionId, resourceGroupName, apiVersion, scopeName, (error, data, response) => {
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

[**ScopedResourceListResult**](ScopedResourceListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

