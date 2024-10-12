# LogicAppsManagementClient.ConnectionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connectionsConfirmConsentCode**](ConnectionsApi.md#connectionsConfirmConsentCode) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName}/confirmConsentCode | Confirms the consent code for a connection
[**connectionsCreateOrUpdate**](ConnectionsApi.md#connectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName} | Replace an existing connection
[**connectionsDelete**](ConnectionsApi.md#connectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName} | Delete an existing connection
[**connectionsGet**](ConnectionsApi.md#connectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName} | Get a connection
[**connectionsList**](ConnectionsApi.md#connectionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections | Get all connections
[**connectionsListConsentLinks**](ConnectionsApi.md#connectionsListConsentLinks) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName}/listConsentLinks | Lists consent links for a connection
[**connectionsUpdate**](ConnectionsApi.md#connectionsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName} | Update an existing connection



## connectionsConfirmConsentCode

> ConfirmConsentCodeDefinition connectionsConfirmConsentCode(subscriptionId, resourceGroupName, connectionName, apiVersion, confirmConsentCode)

Confirms the consent code for a connection

Confirms consent code of a connection

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group
let connectionName = "connectionName_example"; // String | Connection name
let apiVersion = "apiVersion_example"; // String | API Version
let confirmConsentCode = new LogicAppsManagementClient.ConfirmConsentCodeDefinition(); // ConfirmConsentCodeDefinition | The consent code confirmation
apiInstance.connectionsConfirmConsentCode(subscriptionId, resourceGroupName, connectionName, apiVersion, confirmConsentCode, (error, data, response) => {
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
 **connectionName** | **String**| Connection name | 
 **apiVersion** | **String**| API Version | 
 **confirmConsentCode** | [**ConfirmConsentCodeDefinition**](ConfirmConsentCodeDefinition.md)| The consent code confirmation | 

### Return type

[**ConfirmConsentCodeDefinition**](ConfirmConsentCodeDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## connectionsCreateOrUpdate

> ApiConnectionDefinition connectionsCreateOrUpdate(subscriptionId, resourceGroupName, connectionName, apiVersion, connection)

Replace an existing connection

Creates or updates a connection

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group
let connectionName = "connectionName_example"; // String | Connection name
let apiVersion = "apiVersion_example"; // String | API Version
let connection = new LogicAppsManagementClient.ApiConnectionDefinition(); // ApiConnectionDefinition | The connection
apiInstance.connectionsCreateOrUpdate(subscriptionId, resourceGroupName, connectionName, apiVersion, connection, (error, data, response) => {
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
 **connectionName** | **String**| Connection name | 
 **apiVersion** | **String**| API Version | 
 **connection** | [**ApiConnectionDefinition**](ApiConnectionDefinition.md)| The connection | 

### Return type

[**ApiConnectionDefinition**](ApiConnectionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## connectionsDelete

> connectionsDelete(subscriptionId, resourceGroupName, connectionName, apiVersion)

Delete an existing connection

Deletes a connection

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group
let connectionName = "connectionName_example"; // String | Connection name
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.connectionsDelete(subscriptionId, resourceGroupName, connectionName, apiVersion, (error, data, response) => {
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
 **connectionName** | **String**| Connection name | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## connectionsGet

> ApiConnectionDefinition connectionsGet(subscriptionId, resourceGroupName, connectionName, apiVersion)

Get a connection

Get a specific connection

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group
let connectionName = "connectionName_example"; // String | Connection name
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.connectionsGet(subscriptionId, resourceGroupName, connectionName, apiVersion, (error, data, response) => {
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
 **connectionName** | **String**| Connection name | 
 **apiVersion** | **String**| API Version | 

### Return type

[**ApiConnectionDefinition**](ApiConnectionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## connectionsList

> ApiConnectionDefinitionCollection connectionsList(subscriptionId, resourceGroupName, apiVersion, opts)

Get all connections

Gets a list of connections

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'top': 56, // Number | The number of items to be included in the result
  'filter': "filter_example" // String | The filter to apply on the operation
};
apiInstance.connectionsList(subscriptionId, resourceGroupName, apiVersion, opts, (error, data, response) => {
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
 **top** | **Number**| The number of items to be included in the result | [optional] 
 **filter** | **String**| The filter to apply on the operation | [optional] 

### Return type

[**ApiConnectionDefinitionCollection**](ApiConnectionDefinitionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## connectionsListConsentLinks

> ConsentLinkCollection connectionsListConsentLinks(subscriptionId, resourceGroupName, connectionName, apiVersion, listConsentLink)

Lists consent links for a connection

Lists the consent links of a connection

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group
let connectionName = "connectionName_example"; // String | Connection name
let apiVersion = "apiVersion_example"; // String | API Version
let listConsentLink = new LogicAppsManagementClient.ListConsentLinksDefinition(); // ListConsentLinksDefinition | The consent links
apiInstance.connectionsListConsentLinks(subscriptionId, resourceGroupName, connectionName, apiVersion, listConsentLink, (error, data, response) => {
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
 **connectionName** | **String**| Connection name | 
 **apiVersion** | **String**| API Version | 
 **listConsentLink** | [**ListConsentLinksDefinition**](ListConsentLinksDefinition.md)| The consent links | 

### Return type

[**ConsentLinkCollection**](ConsentLinkCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## connectionsUpdate

> ApiConnectionDefinition connectionsUpdate(subscriptionId, resourceGroupName, connectionName, apiVersion, connection)

Update an existing connection

Updates a connection&#39;s tags

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group
let connectionName = "connectionName_example"; // String | Connection name
let apiVersion = "apiVersion_example"; // String | API Version
let connection = new LogicAppsManagementClient.ApiConnectionDefinition(); // ApiConnectionDefinition | The connection
apiInstance.connectionsUpdate(subscriptionId, resourceGroupName, connectionName, apiVersion, connection, (error, data, response) => {
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
 **connectionName** | **String**| Connection name | 
 **apiVersion** | **String**| API Version | 
 **connection** | [**ApiConnectionDefinition**](ApiConnectionDefinition.md)| The connection | 

### Return type

[**ApiConnectionDefinition**](ApiConnectionDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

