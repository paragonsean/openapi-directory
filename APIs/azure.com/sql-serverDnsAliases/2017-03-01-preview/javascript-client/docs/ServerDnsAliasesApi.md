# SqlManagementClient.ServerDnsAliasesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serverDnsAliasesAcquire**](ServerDnsAliasesApi.md#serverDnsAliasesAcquire) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/dnsAliases/{dnsAliasName}/acquire | 
[**serverDnsAliasesCreateOrUpdate**](ServerDnsAliasesApi.md#serverDnsAliasesCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/dnsAliases/{dnsAliasName} | 
[**serverDnsAliasesDelete**](ServerDnsAliasesApi.md#serverDnsAliasesDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/dnsAliases/{dnsAliasName} | 
[**serverDnsAliasesGet**](ServerDnsAliasesApi.md#serverDnsAliasesGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/dnsAliases/{dnsAliasName} | 
[**serverDnsAliasesListByServer**](ServerDnsAliasesApi.md#serverDnsAliasesListByServer) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Sql/servers/{serverName}/dnsAliases | 



## serverDnsAliasesAcquire

> serverDnsAliasesAcquire(resourceGroupName, serverName, dnsAliasName, subscriptionId, apiVersion, parameters)



Acquires server DNS alias from another server.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.ServerDnsAliasesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server that the alias is pointing to.
let dnsAliasName = "dnsAliasName_example"; // String | The name of the server dns alias.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new SqlManagementClient.ServerDnsAliasAcquisition(); // ServerDnsAliasAcquisition | 
apiInstance.serverDnsAliasesAcquire(resourceGroupName, serverName, dnsAliasName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **serverName** | **String**| The name of the server that the alias is pointing to. | 
 **dnsAliasName** | **String**| The name of the server dns alias. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**ServerDnsAliasAcquisition**](ServerDnsAliasAcquisition.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## serverDnsAliasesCreateOrUpdate

> ServerDnsAlias serverDnsAliasesCreateOrUpdate(resourceGroupName, serverName, dnsAliasName, subscriptionId, apiVersion)



Creates a server dns alias.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.ServerDnsAliasesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server that the alias is pointing to.
let dnsAliasName = "dnsAliasName_example"; // String | The name of the server DNS alias.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.serverDnsAliasesCreateOrUpdate(resourceGroupName, serverName, dnsAliasName, subscriptionId, apiVersion, (error, data, response) => {
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
 **serverName** | **String**| The name of the server that the alias is pointing to. | 
 **dnsAliasName** | **String**| The name of the server DNS alias. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**ServerDnsAlias**](ServerDnsAlias.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serverDnsAliasesDelete

> serverDnsAliasesDelete(resourceGroupName, serverName, dnsAliasName, subscriptionId, apiVersion)



Deletes the server DNS alias with the given name.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.ServerDnsAliasesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server that the alias is pointing to.
let dnsAliasName = "dnsAliasName_example"; // String | The name of the server DNS alias.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.serverDnsAliasesDelete(resourceGroupName, serverName, dnsAliasName, subscriptionId, apiVersion, (error, data, response) => {
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
 **serverName** | **String**| The name of the server that the alias is pointing to. | 
 **dnsAliasName** | **String**| The name of the server DNS alias. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## serverDnsAliasesGet

> ServerDnsAlias serverDnsAliasesGet(resourceGroupName, serverName, dnsAliasName, subscriptionId, apiVersion)



Gets a server DNS alias.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.ServerDnsAliasesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server that the alias is pointing to.
let dnsAliasName = "dnsAliasName_example"; // String | The name of the server DNS alias.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.serverDnsAliasesGet(resourceGroupName, serverName, dnsAliasName, subscriptionId, apiVersion, (error, data, response) => {
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
 **serverName** | **String**| The name of the server that the alias is pointing to. | 
 **dnsAliasName** | **String**| The name of the server DNS alias. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**ServerDnsAlias**](ServerDnsAlias.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serverDnsAliasesListByServer

> ServerDnsAliasListResult serverDnsAliasesListByServer(resourceGroupName, serverName, subscriptionId, apiVersion)



Gets a list of server DNS aliases for a server.

### Example

```javascript
import SqlManagementClient from 'sql_management_client';

let apiInstance = new SqlManagementClient.ServerDnsAliasesApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server that the alias is pointing to.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.serverDnsAliasesListByServer(resourceGroupName, serverName, subscriptionId, apiVersion, (error, data, response) => {
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
 **serverName** | **String**| The name of the server that the alias is pointing to. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**ServerDnsAliasListResult**](ServerDnsAliasListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

