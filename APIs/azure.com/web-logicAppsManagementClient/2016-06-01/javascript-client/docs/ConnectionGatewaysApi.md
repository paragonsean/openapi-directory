# LogicAppsManagementClient.ConnectionGatewaysApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connectionGatewayInstallationsGet**](ConnectionGatewaysApi.md#connectionGatewayInstallationsGet) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/locations/{location}/connectionGatewayInstallations/{gatewayId} | Gets an installed gateway that the user is an admin of
[**connectionGatewayInstallationsList**](ConnectionGatewaysApi.md#connectionGatewayInstallationsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/locations/{location}/connectionGatewayInstallations | Gets a list of installed gateways that the user is an admin of
[**connectionGatewaysCreateOrUpdate**](ConnectionGatewaysApi.md#connectionGatewaysCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connectionGateways/{connectionGatewayName} | Replaces a specific gateway
[**connectionGatewaysDelete**](ConnectionGatewaysApi.md#connectionGatewaysDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connectionGateways/{connectionGatewayName} | Deletes a specific gateway
[**connectionGatewaysGet**](ConnectionGatewaysApi.md#connectionGatewaysGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connectionGateways/{connectionGatewayName} | Gets a specific gateway
[**connectionGatewaysList**](ConnectionGatewaysApi.md#connectionGatewaysList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Web/connectionGateways | Lists all of the connection gateways
[**connectionGatewaysListByResourceGroup**](ConnectionGatewaysApi.md#connectionGatewaysListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connectionGateways | Lists all of the connection gateways
[**connectionGatewaysUpdate**](ConnectionGatewaysApi.md#connectionGatewaysUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connectionGateways/{connectionGatewayName} | Updates a specific gateway



## connectionGatewayInstallationsGet

> ConnectionGatewayInstallationDefinition connectionGatewayInstallationsGet(subscriptionId, location, gatewayId, apiVersion)

Gets an installed gateway that the user is an admin of

Get a specific installed gateway that the user is an admin of, in a specific subscription and at a certain location

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ConnectionGatewaysApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let location = "location_example"; // String | The location
let gatewayId = "gatewayId_example"; // String | Gateway ID
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.connectionGatewayInstallationsGet(subscriptionId, location, gatewayId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **location** | **String**| The location | 
 **gatewayId** | **String**| Gateway ID | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ConnectionGatewayInstallationDefinition**](ConnectionGatewayInstallationDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## connectionGatewayInstallationsList

> ConnectionGatewayInstallationDefinitionCollection connectionGatewayInstallationsList(subscriptionId, location, apiVersion)

Gets a list of installed gateways that the user is an admin of

Gets a list of installed gateways that the user is an admin of, in a specific subscription and at a certain location

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ConnectionGatewaysApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let location = "location_example"; // String | The location
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.connectionGatewayInstallationsList(subscriptionId, location, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **location** | **String**| The location | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ConnectionGatewayInstallationDefinitionCollection**](ConnectionGatewayInstallationDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## connectionGatewaysCreateOrUpdate

> ConnectionGatewayDefinition connectionGatewaysCreateOrUpdate(subscriptionId, resourceGroupName, connectionGatewayName, apiVersion, connectionGateway)

Replaces a specific gateway

Creates or updates a specific gateway for under a subscription and in a specific resource group

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ConnectionGatewaysApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group
let connectionGatewayName = "connectionGatewayName_example"; // String | The connection gateway name
let apiVersion = "apiVersion_example"; // String | API Version
let connectionGateway = new LogicAppsManagementClient.ConnectionGatewayDefinition(); // ConnectionGatewayDefinition | The connection gateway
apiInstance.connectionGatewaysCreateOrUpdate(subscriptionId, resourceGroupName, connectionGatewayName, apiVersion, connectionGateway, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **resourceGroupName** | **String**| The resource group | 
 **connectionGatewayName** | **String**| The connection gateway name | 
 **apiVersion** | **String**| API Version | 
 **connectionGateway** | [**ConnectionGatewayDefinition**](ConnectionGatewayDefinition.md)| The connection gateway | 

### Return type

[**ConnectionGatewayDefinition**](ConnectionGatewayDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## connectionGatewaysDelete

> connectionGatewaysDelete(subscriptionId, resourceGroupName, connectionGatewayName, apiVersion)

Deletes a specific gateway

Deletes a specific gateway for under a subscription and in a specific resource group

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ConnectionGatewaysApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group
let connectionGatewayName = "connectionGatewayName_example"; // String | The connection gateway name
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.connectionGatewaysDelete(subscriptionId, resourceGroupName, connectionGatewayName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **resourceGroupName** | **String**| The resource group | 
 **connectionGatewayName** | **String**| The connection gateway name | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## connectionGatewaysGet

> ConnectionGatewayDefinition connectionGatewaysGet(subscriptionId, resourceGroupName, connectionGatewayName, apiVersion)

Gets a specific gateway

Gets a specific gateway under a subscription and in a specific resource group

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ConnectionGatewaysApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group
let connectionGatewayName = "connectionGatewayName_example"; // String | The connection gateway name
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.connectionGatewaysGet(subscriptionId, resourceGroupName, connectionGatewayName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **resourceGroupName** | **String**| The resource group | 
 **connectionGatewayName** | **String**| The connection gateway name | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ConnectionGatewayDefinition**](ConnectionGatewayDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## connectionGatewaysList

> ConnectionGatewayDefinitionCollection connectionGatewaysList(subscriptionId, apiVersion)

Lists all of the connection gateways

Gets a list of gateways under a subscription

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ConnectionGatewaysApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.connectionGatewaysList(subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ConnectionGatewayDefinitionCollection**](ConnectionGatewayDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## connectionGatewaysListByResourceGroup

> ConnectionGatewayDefinitionCollection connectionGatewaysListByResourceGroup(subscriptionId, resourceGroupName, apiVersion)

Lists all of the connection gateways

Gets a list of gateways under a subscription and in a specific resource group

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ConnectionGatewaysApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.connectionGatewaysListByResourceGroup(subscriptionId, resourceGroupName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **resourceGroupName** | **String**| The resource group | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ConnectionGatewayDefinitionCollection**](ConnectionGatewayDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## connectionGatewaysUpdate

> ConnectionGatewayDefinition connectionGatewaysUpdate(subscriptionId, resourceGroupName, connectionGatewayName, apiVersion, connectionGateway)

Updates a specific gateway

Updates a connection gateway&#39;s tags

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ConnectionGatewaysApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group
let connectionGatewayName = "connectionGatewayName_example"; // String | The connection gateway name
let apiVersion = "apiVersion_example"; // String | API Version
let connectionGateway = new LogicAppsManagementClient.ConnectionGatewayDefinition(); // ConnectionGatewayDefinition | The connection gateway
apiInstance.connectionGatewaysUpdate(subscriptionId, resourceGroupName, connectionGatewayName, apiVersion, connectionGateway, (error, data, response) => {
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
 **subscriptionId** | **String**| Subscription Id | 
 **resourceGroupName** | **String**| The resource group | 
 **connectionGatewayName** | **String**| The connection gateway name | 
 **apiVersion** | **String**| API Version | 
 **connectionGateway** | [**ConnectionGatewayDefinition**](ConnectionGatewayDefinition.md)| The connection gateway | 

### Return type

[**ConnectionGatewayDefinition**](ConnectionGatewayDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

