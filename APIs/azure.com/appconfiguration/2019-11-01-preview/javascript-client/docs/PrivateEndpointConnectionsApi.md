# AppConfigurationManagementClient.PrivateEndpointConnectionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**privateEndpointConnectionsCreateOrUpdate**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/privateEndpointConnections/{privateEndpointConnectionName} | 
[**privateEndpointConnectionsDelete**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/privateEndpointConnections/{privateEndpointConnectionName} | 
[**privateEndpointConnectionsGet**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/privateEndpointConnections/{privateEndpointConnectionName} | 
[**privateEndpointConnectionsListByConfigurationStore**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsListByConfigurationStore) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.AppConfiguration/configurationStores/{configStoreName}/privateEndpointConnections | 



## privateEndpointConnectionsCreateOrUpdate

> PrivateEndpointConnection privateEndpointConnectionsCreateOrUpdate(subscriptionId, resourceGroupName, configStoreName, apiVersion, privateEndpointConnectionName, privateEndpointConnection)



Update the state of the specified private endpoint connection associated with the configuration store.

### Example

```javascript
import AppConfigurationManagementClient from 'app_configuration_management_client';
let defaultClient = AppConfigurationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppConfigurationManagementClient.PrivateEndpointConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let configStoreName = "configStoreName_example"; // String | The name of the configuration store.
let apiVersion = "apiVersion_example"; // String | The client API version.
let privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | Private endpoint connection name
let privateEndpointConnection = new AppConfigurationManagementClient.PrivateEndpointConnection(); // PrivateEndpointConnection | The private endpoint connection properties.
apiInstance.privateEndpointConnectionsCreateOrUpdate(subscriptionId, resourceGroupName, configStoreName, apiVersion, privateEndpointConnectionName, privateEndpointConnection, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | 
 **configStoreName** | **String**| The name of the configuration store. | 
 **apiVersion** | **String**| The client API version. | 
 **privateEndpointConnectionName** | **String**| Private endpoint connection name | 
 **privateEndpointConnection** | [**PrivateEndpointConnection**](PrivateEndpointConnection.md)| The private endpoint connection properties. | 

### Return type

[**PrivateEndpointConnection**](PrivateEndpointConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## privateEndpointConnectionsDelete

> privateEndpointConnectionsDelete(subscriptionId, resourceGroupName, configStoreName, apiVersion, privateEndpointConnectionName)



Deletes a private endpoint connection.

### Example

```javascript
import AppConfigurationManagementClient from 'app_configuration_management_client';
let defaultClient = AppConfigurationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppConfigurationManagementClient.PrivateEndpointConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let configStoreName = "configStoreName_example"; // String | The name of the configuration store.
let apiVersion = "apiVersion_example"; // String | The client API version.
let privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | Private endpoint connection name
apiInstance.privateEndpointConnectionsDelete(subscriptionId, resourceGroupName, configStoreName, apiVersion, privateEndpointConnectionName, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | 
 **configStoreName** | **String**| The name of the configuration store. | 
 **apiVersion** | **String**| The client API version. | 
 **privateEndpointConnectionName** | **String**| Private endpoint connection name | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateEndpointConnectionsGet

> PrivateEndpointConnection privateEndpointConnectionsGet(subscriptionId, resourceGroupName, configStoreName, apiVersion, privateEndpointConnectionName)



Gets the specified private endpoint connection associated with the configuration store.

### Example

```javascript
import AppConfigurationManagementClient from 'app_configuration_management_client';
let defaultClient = AppConfigurationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppConfigurationManagementClient.PrivateEndpointConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let configStoreName = "configStoreName_example"; // String | The name of the configuration store.
let apiVersion = "apiVersion_example"; // String | The client API version.
let privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | Private endpoint connection name
apiInstance.privateEndpointConnectionsGet(subscriptionId, resourceGroupName, configStoreName, apiVersion, privateEndpointConnectionName, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | 
 **configStoreName** | **String**| The name of the configuration store. | 
 **apiVersion** | **String**| The client API version. | 
 **privateEndpointConnectionName** | **String**| Private endpoint connection name | 

### Return type

[**PrivateEndpointConnection**](PrivateEndpointConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateEndpointConnectionsListByConfigurationStore

> PrivateEndpointConnectionListResult privateEndpointConnectionsListByConfigurationStore(subscriptionId, resourceGroupName, configStoreName, apiVersion)



Lists all private endpoint connections for a configuration store.

### Example

```javascript
import AppConfigurationManagementClient from 'app_configuration_management_client';
let defaultClient = AppConfigurationManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AppConfigurationManagementClient.PrivateEndpointConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | The Microsoft Azure subscription ID.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group to which the container registry belongs.
let configStoreName = "configStoreName_example"; // String | The name of the configuration store.
let apiVersion = "apiVersion_example"; // String | The client API version.
apiInstance.privateEndpointConnectionsListByConfigurationStore(subscriptionId, resourceGroupName, configStoreName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The Microsoft Azure subscription ID. | 
 **resourceGroupName** | **String**| The name of the resource group to which the container registry belongs. | 
 **configStoreName** | **String**| The name of the configuration store. | 
 **apiVersion** | **String**| The client API version. | 

### Return type

[**PrivateEndpointConnectionListResult**](PrivateEndpointConnectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

