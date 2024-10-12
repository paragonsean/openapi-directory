# AzureMonitorPrivateLinkScopes.PrivateEndpointConnectionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**privateEndpointConnectionsCreateOrUpdate**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/privateLinkScopes/{scopeName}/privateEndpointConnections/{privateEndpointConnectionName} | 
[**privateEndpointConnectionsDelete**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/privateLinkScopes/{scopeName}/privateEndpointConnections/{privateEndpointConnectionName} | 
[**privateEndpointConnectionsGet**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/privateLinkScopes/{scopeName}/privateEndpointConnections/{privateEndpointConnectionName} | 
[**privateEndpointConnectionsListByPrivateLinkScope**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsListByPrivateLinkScope) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Insights/privateLinkScopes/{scopeName}/privateEndpointConnections | 



## privateEndpointConnectionsCreateOrUpdate

> PrivateEndpointConnection privateEndpointConnectionsCreateOrUpdate(subscriptionId, resourceGroupName, apiVersion, scopeName, privateEndpointConnectionName, parameters)



Approve or reject a private endpoint connection with a given name.

### Example

```javascript
import AzureMonitorPrivateLinkScopes from 'azure_monitor_private_link_scopes';
let defaultClient = AzureMonitorPrivateLinkScopes.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMonitorPrivateLinkScopes.PrivateEndpointConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let scopeName = "scopeName_example"; // String | Name of the Azure Monitor PrivateLinkScope that will contain the datasource
let privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | The name of the private endpoint connection.
let parameters = new AzureMonitorPrivateLinkScopes.PrivateEndpointConnection(); // PrivateEndpointConnection | 
apiInstance.privateEndpointConnectionsCreateOrUpdate(subscriptionId, resourceGroupName, apiVersion, scopeName, privateEndpointConnectionName, parameters, (error, data, response) => {
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
 **privateEndpointConnectionName** | **String**| The name of the private endpoint connection. | 
 **parameters** | [**PrivateEndpointConnection**](PrivateEndpointConnection.md)|  | 

### Return type

[**PrivateEndpointConnection**](PrivateEndpointConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateEndpointConnectionsDelete

> privateEndpointConnectionsDelete(subscriptionId, resourceGroupName, apiVersion, scopeName, privateEndpointConnectionName)



Deletes a private endpoint connection with a given name.

### Example

```javascript
import AzureMonitorPrivateLinkScopes from 'azure_monitor_private_link_scopes';
let defaultClient = AzureMonitorPrivateLinkScopes.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMonitorPrivateLinkScopes.PrivateEndpointConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let scopeName = "scopeName_example"; // String | Name of the Azure Monitor PrivateLinkScope that will contain the datasource
let privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | The name of the private endpoint connection.
apiInstance.privateEndpointConnectionsDelete(subscriptionId, resourceGroupName, apiVersion, scopeName, privateEndpointConnectionName, (error, data, response) => {
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
 **privateEndpointConnectionName** | **String**| The name of the private endpoint connection. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## privateEndpointConnectionsGet

> PrivateEndpointConnection privateEndpointConnectionsGet(subscriptionId, resourceGroupName, apiVersion, scopeName, privateEndpointConnectionName)



Gets a private endpoint connection.

### Example

```javascript
import AzureMonitorPrivateLinkScopes from 'azure_monitor_private_link_scopes';
let defaultClient = AzureMonitorPrivateLinkScopes.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMonitorPrivateLinkScopes.PrivateEndpointConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let scopeName = "scopeName_example"; // String | Name of the Azure Monitor PrivateLinkScope that will contain the datasource
let privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | The name of the private endpoint connection.
apiInstance.privateEndpointConnectionsGet(subscriptionId, resourceGroupName, apiVersion, scopeName, privateEndpointConnectionName, (error, data, response) => {
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
 **privateEndpointConnectionName** | **String**| The name of the private endpoint connection. | 

### Return type

[**PrivateEndpointConnection**](PrivateEndpointConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateEndpointConnectionsListByPrivateLinkScope

> PrivateEndpointConnectionListResult privateEndpointConnectionsListByPrivateLinkScope(subscriptionId, resourceGroupName, apiVersion, scopeName)



Gets all private endpoint connections on a private link scope.

### Example

```javascript
import AzureMonitorPrivateLinkScopes from 'azure_monitor_private_link_scopes';
let defaultClient = AzureMonitorPrivateLinkScopes.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AzureMonitorPrivateLinkScopes.PrivateEndpointConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let scopeName = "scopeName_example"; // String | Name of the Azure Monitor PrivateLinkScope that will contain the datasource
apiInstance.privateEndpointConnectionsListByPrivateLinkScope(subscriptionId, resourceGroupName, apiVersion, scopeName, (error, data, response) => {
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

[**PrivateEndpointConnectionListResult**](PrivateEndpointConnectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

