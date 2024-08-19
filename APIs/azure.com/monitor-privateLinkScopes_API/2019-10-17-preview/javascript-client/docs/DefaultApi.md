# AzureMonitorPrivateLinkScopes.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**privateLinkScopesCreateOrUpdate**](DefaultApi.md#privateLinkScopesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/privateLinkScopes/{scopeName} | 
[**privateLinkScopesDelete**](DefaultApi.md#privateLinkScopesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/privateLinkScopes/{scopeName} | 
[**privateLinkScopesGet**](DefaultApi.md#privateLinkScopesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/privateLinkScopes/{scopeName} | 
[**privateLinkScopesList**](DefaultApi.md#privateLinkScopesList) | **GET** /subscriptions/{subscriptionId}/providers/microsoft.insights/privateLinkScopes | 
[**privateLinkScopesListByResourceGroup**](DefaultApi.md#privateLinkScopesListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/privateLinkScopes | 
[**privateLinkScopesUpdateTags**](DefaultApi.md#privateLinkScopesUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/microsoft.insights/privateLinkScopes/{scopeName} | 



## privateLinkScopesCreateOrUpdate

> AzureMonitorPrivateLinkScope privateLinkScopesCreateOrUpdate(resourceGroupName, apiVersion, subscriptionId, scopeName, azureMonitorPrivateLinkScopePayload)



Creates (or updates) a Azure Monitor PrivateLinkScope. Note: You cannot specify a different value for InstrumentationKey nor AppId in the Put operation.

### Example

```javascript
import AzureMonitorPrivateLinkScopes from 'azure_monitor_private_link_scopes';
let defaultClient = AzureMonitorPrivateLinkScopes.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMonitorPrivateLinkScopes.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let scopeName = "scopeName_example"; // String | The name of the Azure Monitor PrivateLinkScope resource.
let azureMonitorPrivateLinkScopePayload = new AzureMonitorPrivateLinkScopes.AzureMonitorPrivateLinkScope(); // AzureMonitorPrivateLinkScope | Properties that need to be specified to create or update a Azure Monitor PrivateLinkScope.
apiInstance.privateLinkScopesCreateOrUpdate(resourceGroupName, apiVersion, subscriptionId, scopeName, azureMonitorPrivateLinkScopePayload, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **scopeName** | **String**| The name of the Azure Monitor PrivateLinkScope resource. | 
 **azureMonitorPrivateLinkScopePayload** | [**AzureMonitorPrivateLinkScope**](AzureMonitorPrivateLinkScope.md)| Properties that need to be specified to create or update a Azure Monitor PrivateLinkScope. | 

### Return type

[**AzureMonitorPrivateLinkScope**](AzureMonitorPrivateLinkScope.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateLinkScopesDelete

> privateLinkScopesDelete(resourceGroupName, apiVersion, subscriptionId, scopeName)



Deletes a Azure Monitor PrivateLinkScope.

### Example

```javascript
import AzureMonitorPrivateLinkScopes from 'azure_monitor_private_link_scopes';
let defaultClient = AzureMonitorPrivateLinkScopes.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMonitorPrivateLinkScopes.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let scopeName = "scopeName_example"; // String | The name of the Azure Monitor PrivateLinkScope resource.
apiInstance.privateLinkScopesDelete(resourceGroupName, apiVersion, subscriptionId, scopeName, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **scopeName** | **String**| The name of the Azure Monitor PrivateLinkScope resource. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateLinkScopesGet

> AzureMonitorPrivateLinkScope privateLinkScopesGet(resourceGroupName, apiVersion, subscriptionId, scopeName)



Returns a Azure Monitor PrivateLinkScope.

### Example

```javascript
import AzureMonitorPrivateLinkScopes from 'azure_monitor_private_link_scopes';
let defaultClient = AzureMonitorPrivateLinkScopes.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMonitorPrivateLinkScopes.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let scopeName = "scopeName_example"; // String | The name of the Azure Monitor PrivateLinkScope resource.
apiInstance.privateLinkScopesGet(resourceGroupName, apiVersion, subscriptionId, scopeName, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **scopeName** | **String**| The name of the Azure Monitor PrivateLinkScope resource. | 

### Return type

[**AzureMonitorPrivateLinkScope**](AzureMonitorPrivateLinkScope.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateLinkScopesList

> AzureMonitorPrivateLinkScopeListResult privateLinkScopesList(apiVersion, subscriptionId)



Gets a list of all Azure Monitor PrivateLinkScopes within a subscription.

### Example

```javascript
import AzureMonitorPrivateLinkScopes from 'azure_monitor_private_link_scopes';
let defaultClient = AzureMonitorPrivateLinkScopes.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMonitorPrivateLinkScopes.DefaultApi();
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.privateLinkScopesList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**AzureMonitorPrivateLinkScopeListResult**](AzureMonitorPrivateLinkScopeListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateLinkScopesListByResourceGroup

> AzureMonitorPrivateLinkScopeListResult privateLinkScopesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Gets a list of Azure Monitor PrivateLinkScopes within a resource group.

### Example

```javascript
import AzureMonitorPrivateLinkScopes from 'azure_monitor_private_link_scopes';
let defaultClient = AzureMonitorPrivateLinkScopes.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMonitorPrivateLinkScopes.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
apiInstance.privateLinkScopesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 

### Return type

[**AzureMonitorPrivateLinkScopeListResult**](AzureMonitorPrivateLinkScopeListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateLinkScopesUpdateTags

> AzureMonitorPrivateLinkScope privateLinkScopesUpdateTags(resourceGroupName, apiVersion, subscriptionId, scopeName, privateLinkScopeTags)



Updates an existing PrivateLinkScope&#39;s tags. To update other fields use the CreateOrUpdate method.

### Example

```javascript
import AzureMonitorPrivateLinkScopes from 'azure_monitor_private_link_scopes';
let defaultClient = AzureMonitorPrivateLinkScopes.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMonitorPrivateLinkScopes.DefaultApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let scopeName = "scopeName_example"; // String | The name of the Azure Monitor PrivateLinkScope resource.
let privateLinkScopeTags = new AzureMonitorPrivateLinkScopes.TagsResource(); // TagsResource | Updated tag information to set into the PrivateLinkScope instance.
apiInstance.privateLinkScopesUpdateTags(resourceGroupName, apiVersion, subscriptionId, scopeName, privateLinkScopeTags, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. The name is case insensitive. | 
 **apiVersion** | **String**| The API version to use for this operation. | 
 **subscriptionId** | **String**| The ID of the target subscription. | 
 **scopeName** | **String**| The name of the Azure Monitor PrivateLinkScope resource. | 
 **privateLinkScopeTags** | [**TagsResource**](TagsResource.md)| Updated tag information to set into the PrivateLinkScope instance. | 

### Return type

[**AzureMonitorPrivateLinkScope**](AzureMonitorPrivateLinkScope.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

