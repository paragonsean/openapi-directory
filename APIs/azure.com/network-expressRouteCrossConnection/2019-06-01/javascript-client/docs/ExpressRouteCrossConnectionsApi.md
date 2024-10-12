# ExpressRouteCrossConnectionRestApis.ExpressRouteCrossConnectionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expressRouteCrossConnectionsCreateOrUpdate**](ExpressRouteCrossConnectionsApi.md#expressRouteCrossConnectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName} | 
[**expressRouteCrossConnectionsGet**](ExpressRouteCrossConnectionsApi.md#expressRouteCrossConnectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName} | 
[**expressRouteCrossConnectionsList**](ExpressRouteCrossConnectionsApi.md#expressRouteCrossConnectionsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Network/expressRouteCrossConnections | 
[**expressRouteCrossConnectionsListByResourceGroup**](ExpressRouteCrossConnectionsApi.md#expressRouteCrossConnectionsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections | 
[**expressRouteCrossConnectionsUpdateTags**](ExpressRouteCrossConnectionsApi.md#expressRouteCrossConnectionsUpdateTags) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteCrossConnections/{crossConnectionName} | 



## expressRouteCrossConnectionsCreateOrUpdate

> ExpressRouteCrossConnection expressRouteCrossConnectionsCreateOrUpdate(resourceGroupName, crossConnectionName, apiVersion, subscriptionId, parameters)



Update the specified ExpressRouteCrossConnection.

### Example

```javascript
import ExpressRouteCrossConnectionRestApis from 'express_route_cross_connection_rest_apis';
let defaultClient = ExpressRouteCrossConnectionRestApis.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ExpressRouteCrossConnectionRestApis.ExpressRouteCrossConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let crossConnectionName = "crossConnectionName_example"; // String | The name of the ExpressRouteCrossConnection.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let parameters = new ExpressRouteCrossConnectionRestApis.ExpressRouteCrossConnection(); // ExpressRouteCrossConnection | Parameters supplied to the update express route crossConnection operation.
apiInstance.expressRouteCrossConnectionsCreateOrUpdate(resourceGroupName, crossConnectionName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **crossConnectionName** | **String**| The name of the ExpressRouteCrossConnection. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **parameters** | [**ExpressRouteCrossConnection**](ExpressRouteCrossConnection.md)| Parameters supplied to the update express route crossConnection operation. | 

### Return type

[**ExpressRouteCrossConnection**](ExpressRouteCrossConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## expressRouteCrossConnectionsGet

> ExpressRouteCrossConnection expressRouteCrossConnectionsGet(resourceGroupName, crossConnectionName, apiVersion, subscriptionId)



Gets details about the specified ExpressRouteCrossConnection.

### Example

```javascript
import ExpressRouteCrossConnectionRestApis from 'express_route_cross_connection_rest_apis';
let defaultClient = ExpressRouteCrossConnectionRestApis.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ExpressRouteCrossConnectionRestApis.ExpressRouteCrossConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group (peering location of the circuit).
let crossConnectionName = "crossConnectionName_example"; // String | The name of the ExpressRouteCrossConnection (service key of the circuit).
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteCrossConnectionsGet(resourceGroupName, crossConnectionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group (peering location of the circuit). | 
 **crossConnectionName** | **String**| The name of the ExpressRouteCrossConnection (service key of the circuit). | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ExpressRouteCrossConnection**](ExpressRouteCrossConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expressRouteCrossConnectionsList

> ExpressRouteCrossConnectionListResult expressRouteCrossConnectionsList(apiVersion, subscriptionId)



Retrieves all the ExpressRouteCrossConnections in a subscription.

### Example

```javascript
import ExpressRouteCrossConnectionRestApis from 'express_route_cross_connection_rest_apis';
let defaultClient = ExpressRouteCrossConnectionRestApis.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ExpressRouteCrossConnectionRestApis.ExpressRouteCrossConnectionsApi();
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteCrossConnectionsList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ExpressRouteCrossConnectionListResult**](ExpressRouteCrossConnectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expressRouteCrossConnectionsListByResourceGroup

> ExpressRouteCrossConnectionListResult expressRouteCrossConnectionsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId)



Retrieves all the ExpressRouteCrossConnections in a resource group.

### Example

```javascript
import ExpressRouteCrossConnectionRestApis from 'express_route_cross_connection_rest_apis';
let defaultClient = ExpressRouteCrossConnectionRestApis.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ExpressRouteCrossConnectionRestApis.ExpressRouteCrossConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
apiInstance.expressRouteCrossConnectionsListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 

### Return type

[**ExpressRouteCrossConnectionListResult**](ExpressRouteCrossConnectionListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## expressRouteCrossConnectionsUpdateTags

> ExpressRouteCrossConnection expressRouteCrossConnectionsUpdateTags(resourceGroupName, crossConnectionName, apiVersion, subscriptionId, crossConnectionParameters)



Updates an express route cross connection tags.

### Example

```javascript
import ExpressRouteCrossConnectionRestApis from 'express_route_cross_connection_rest_apis';
let defaultClient = ExpressRouteCrossConnectionRestApis.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ExpressRouteCrossConnectionRestApis.ExpressRouteCrossConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group.
let crossConnectionName = "crossConnectionName_example"; // String | The name of the cross connection.
let apiVersion = "apiVersion_example"; // String | Client API version.
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let crossConnectionParameters = new ExpressRouteCrossConnectionRestApis.ExpressRouteCrossConnectionsUpdateTagsRequest(); // ExpressRouteCrossConnectionsUpdateTagsRequest | Parameters supplied to update express route cross connection tags.
apiInstance.expressRouteCrossConnectionsUpdateTags(resourceGroupName, crossConnectionName, apiVersion, subscriptionId, crossConnectionParameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group. | 
 **crossConnectionName** | **String**| The name of the cross connection. | 
 **apiVersion** | **String**| Client API version. | 
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **crossConnectionParameters** | [**ExpressRouteCrossConnectionsUpdateTagsRequest**](ExpressRouteCrossConnectionsUpdateTagsRequest.md)| Parameters supplied to update express route cross connection tags. | 

### Return type

[**ExpressRouteCrossConnection**](ExpressRouteCrossConnection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

