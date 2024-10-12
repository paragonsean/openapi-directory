# CosmosDb.PrivateEndpointConnectionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**privateEndpointConnectionsCreateOrUpdate**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/privateEndpointConnections/{privateEndpointConnectionName} | 
[**privateEndpointConnectionsDelete**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/privateEndpointConnections/{privateEndpointConnectionName} | 
[**privateEndpointConnectionsGet**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/privateEndpointConnections/{privateEndpointConnectionName} | 
[**privateEndpointConnectionsListByDatabaseAccount**](PrivateEndpointConnectionsApi.md#privateEndpointConnectionsListByDatabaseAccount) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DocumentDB/databaseAccounts/{accountName}/privateEndpointConnections | 



## privateEndpointConnectionsCreateOrUpdate

> PrivateEndpointConnection privateEndpointConnectionsCreateOrUpdate(subscriptionId, resourceGroupName, apiVersion, accountName, privateEndpointConnectionName, parameters)



Approve or reject a private endpoint connection with a given name.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.PrivateEndpointConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | The name of the private endpoint connection.
let parameters = new CosmosDb.PrivateEndpointConnection(); // PrivateEndpointConnection | 
apiInstance.privateEndpointConnectionsCreateOrUpdate(subscriptionId, resourceGroupName, apiVersion, accountName, privateEndpointConnectionName, parameters, (error, data, response) => {
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
 **accountName** | **String**| Cosmos DB database account name. | 
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

> privateEndpointConnectionsDelete(subscriptionId, resourceGroupName, apiVersion, accountName, privateEndpointConnectionName)



Deletes a private endpoint connection with a given name.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.PrivateEndpointConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | The name of the private endpoint connection.
apiInstance.privateEndpointConnectionsDelete(subscriptionId, resourceGroupName, apiVersion, accountName, privateEndpointConnectionName, (error, data, response) => {
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
 **accountName** | **String**| Cosmos DB database account name. | 
 **privateEndpointConnectionName** | **String**| The name of the private endpoint connection. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateEndpointConnectionsGet

> PrivateEndpointConnection privateEndpointConnectionsGet(subscriptionId, resourceGroupName, apiVersion, accountName, privateEndpointConnectionName)



Gets a private endpoint connection.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.PrivateEndpointConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
let privateEndpointConnectionName = "privateEndpointConnectionName_example"; // String | The name of the private endpoint connection.
apiInstance.privateEndpointConnectionsGet(subscriptionId, resourceGroupName, apiVersion, accountName, privateEndpointConnectionName, (error, data, response) => {
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
 **accountName** | **String**| Cosmos DB database account name. | 
 **privateEndpointConnectionName** | **String**| The name of the private endpoint connection. | 

### Return type

[**PrivateEndpointConnection**](PrivateEndpointConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## privateEndpointConnectionsListByDatabaseAccount

> PrivateEndpointConnectionListResult privateEndpointConnectionsListByDatabaseAccount(subscriptionId, resourceGroupName, apiVersion, accountName)



List all private endpoint connections on a Cosmos DB account.

### Example

```javascript
import CosmosDb from 'cosmos_db';
let defaultClient = CosmosDb.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new CosmosDb.PrivateEndpointConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | The ID of the target subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group. The name is case insensitive.
let apiVersion = "apiVersion_example"; // String | The API version to use for this operation.
let accountName = "accountName_example"; // String | Cosmos DB database account name.
apiInstance.privateEndpointConnectionsListByDatabaseAccount(subscriptionId, resourceGroupName, apiVersion, accountName, (error, data, response) => {
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
 **accountName** | **String**| Cosmos DB database account name. | 

### Return type

[**PrivateEndpointConnectionListResult**](PrivateEndpointConnectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

