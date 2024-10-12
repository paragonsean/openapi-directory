# MariaDbManagementClient.ServerKeysApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serverKeysCreateOrUpdate**](ServerKeysApi.md#serverKeysCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMariaDB/servers/{serverName}/keys/{keyName} | 
[**serverKeysDelete**](ServerKeysApi.md#serverKeysDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMariaDB/servers/{serverName}/keys/{keyName} | 
[**serverKeysGet**](ServerKeysApi.md#serverKeysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMariaDB/servers/{serverName}/keys/{keyName} | 
[**serverKeysListByInstance**](ServerKeysApi.md#serverKeysListByInstance) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DBforMariaDB/servers/{serverName}/keys | 



## serverKeysCreateOrUpdate

> ServerKey serverKeysCreateOrUpdate(resourceGroupName, serverName, keyName, subscriptionId, apiVersion, parameters)



Creates or updates a MariaDB Server key.

### Example

```javascript
import MariaDbManagementClient from 'maria_db_management_client';

let apiInstance = new MariaDbManagementClient.ServerKeysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let keyName = "keyName_example"; // String | The name of the MariaDB Server key to be operated on (updated or created).
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
let parameters = new MariaDbManagementClient.ServerKey(); // ServerKey | The requested MariaDB Server key resource state.
apiInstance.serverKeysCreateOrUpdate(resourceGroupName, serverName, keyName, subscriptionId, apiVersion, parameters, (error, data, response) => {
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
 **serverName** | **String**| The name of the server. | 
 **keyName** | **String**| The name of the MariaDB Server key to be operated on (updated or created). | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 
 **parameters** | [**ServerKey**](ServerKey.md)| The requested MariaDB Server key resource state. | 

### Return type

[**ServerKey**](ServerKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## serverKeysDelete

> serverKeysDelete(resourceGroupName, serverName, keyName, subscriptionId, apiVersion)



Deletes the MariaDB Server key with the given name.

### Example

```javascript
import MariaDbManagementClient from 'maria_db_management_client';

let apiInstance = new MariaDbManagementClient.ServerKeysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let keyName = "keyName_example"; // String | The name of the MariaDB Server key to be deleted.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.serverKeysDelete(resourceGroupName, serverName, keyName, subscriptionId, apiVersion, (error, data, response) => {
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
 **serverName** | **String**| The name of the server. | 
 **keyName** | **String**| The name of the MariaDB Server key to be deleted. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serverKeysGet

> ServerKey serverKeysGet(resourceGroupName, serverName, keyName, subscriptionId, apiVersion)



Gets a MariaDB Server key.

### Example

```javascript
import MariaDbManagementClient from 'maria_db_management_client';

let apiInstance = new MariaDbManagementClient.ServerKeysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let keyName = "keyName_example"; // String | The name of the MariaDB Server key to be retrieved.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.serverKeysGet(resourceGroupName, serverName, keyName, subscriptionId, apiVersion, (error, data, response) => {
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
 **serverName** | **String**| The name of the server. | 
 **keyName** | **String**| The name of the MariaDB Server key to be retrieved. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**ServerKey**](ServerKey.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serverKeysListByInstance

> ServerKeyListResult serverKeysListByInstance(resourceGroupName, serverName, subscriptionId, apiVersion)



Gets a list of  Server keys.

### Example

```javascript
import MariaDbManagementClient from 'maria_db_management_client';

let apiInstance = new MariaDbManagementClient.ServerKeysApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
let serverName = "serverName_example"; // String | The name of the server.
let subscriptionId = "subscriptionId_example"; // String | The subscription ID that identifies an Azure subscription.
let apiVersion = "apiVersion_example"; // String | The API version to use for the request.
apiInstance.serverKeysListByInstance(resourceGroupName, serverName, subscriptionId, apiVersion, (error, data, response) => {
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
 **serverName** | **String**| The name of the server. | 
 **subscriptionId** | **String**| The subscription ID that identifies an Azure subscription. | 
 **apiVersion** | **String**| The API version to use for the request. | 

### Return type

[**ServerKeyListResult**](ServerKeyListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

