# LogicAppsManagementClient.ConnectionsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connectionsConfirmConsentCode**](ConnectionsApi.md#connectionsConfirmConsentCode) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName}/confirmConsentCode | 
[**connectionsCreateOrUpdate**](ConnectionsApi.md#connectionsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName} | 
[**connectionsDelete**](ConnectionsApi.md#connectionsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName} | 
[**connectionsGet**](ConnectionsApi.md#connectionsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName} | 
[**connectionsList**](ConnectionsApi.md#connectionsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections | Get Connections
[**connectionsListConnectionKeys**](ConnectionsApi.md#connectionsListConnectionKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName}/listConnectionKeys | 
[**connectionsListConsentLinks**](ConnectionsApi.md#connectionsListConsentLinks) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/connections/{connectionName}/listConsentLinks | 



## connectionsConfirmConsentCode

> Connection connectionsConfirmConsentCode(subscriptionId, resourceGroupName, connectionName, apiVersion, content)



Confirms consent code of a connection.

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let connectionName = "connectionName_example"; // String | The connection name.
let apiVersion = "apiVersion_example"; // String | API Version
let content = new LogicAppsManagementClient.ConfirmConsentCodeInput(); // ConfirmConsentCodeInput | The content.
apiInstance.connectionsConfirmConsentCode(subscriptionId, resourceGroupName, connectionName, apiVersion, content, (error, data, response) => {
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
 **resourceGroupName** | **String**| The resource group name. | 
 **connectionName** | **String**| The connection name. | 
 **apiVersion** | **String**| API Version | 
 **content** | [**ConfirmConsentCodeInput**](ConfirmConsentCodeInput.md)| The content. | 

### Return type

[**Connection**](Connection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## connectionsCreateOrUpdate

> Connection connectionsCreateOrUpdate(subscriptionId, resourceGroupName, connectionName, apiVersion, connection)



Creates or updates a connection.

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let connectionName = "connectionName_example"; // String | The connection name.
let apiVersion = "apiVersion_example"; // String | API Version
let connection = new LogicAppsManagementClient.Connection(); // Connection | The connection.
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
 **resourceGroupName** | **String**| The resource group name. | 
 **connectionName** | **String**| The connection name. | 
 **apiVersion** | **String**| API Version | 
 **connection** | [**Connection**](Connection.md)| The connection. | 

### Return type

[**Connection**](Connection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## connectionsDelete

> connectionsDelete(subscriptionId, resourceGroupName, connectionName, apiVersion)



Deletes a connection.

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let connectionName = "connectionName_example"; // String | The connection name.
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
 **resourceGroupName** | **String**| The resource group name. | 
 **connectionName** | **String**| The connection name. | 
 **apiVersion** | **String**| API Version | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## connectionsGet

> Connection connectionsGet(subscriptionId, resourceGroupName, connectionName, apiVersion)



Gets a connection.

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let connectionName = "connectionName_example"; // String | The connection name.
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
 **resourceGroupName** | **String**| The resource group name. | 
 **connectionName** | **String**| The connection name. | 
 **apiVersion** | **String**| API Version | 

### Return type

[**Connection**](Connection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## connectionsList

> ConnectionCollection connectionsList(resourceGroupName, subscriptionId, apiVersion, opts)

Get Connections

Gets a list of connections.

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ConnectionsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Resource Group Name
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'top': 56, // Number | The number of items to be included in the result.
  'filter': "filter_example" // String | The filter to apply on the operation.
};
apiInstance.connectionsList(resourceGroupName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Resource Group Name | 
 **subscriptionId** | **String**| Subscription Id | 
 **apiVersion** | **String**| API Version | 
 **top** | **Number**| The number of items to be included in the result. | [optional] 
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**ConnectionCollection**](ConnectionCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## connectionsListConnectionKeys

> ConnectionSecrets connectionsListConnectionKeys(subscriptionId, resourceGroupName, connectionName, apiVersion, content)



Lists connection keys.

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let connectionName = "connectionName_example"; // String | The connection name.
let apiVersion = "apiVersion_example"; // String | API Version
let content = new LogicAppsManagementClient.ListConnectionKeysInput(); // ListConnectionKeysInput | The content.
apiInstance.connectionsListConnectionKeys(subscriptionId, resourceGroupName, connectionName, apiVersion, content, (error, data, response) => {
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
 **resourceGroupName** | **String**| The resource group name. | 
 **connectionName** | **String**| The connection name. | 
 **apiVersion** | **String**| API Version | 
 **content** | [**ListConnectionKeysInput**](ListConnectionKeysInput.md)| The content. | 

### Return type

[**ConnectionSecrets**](ConnectionSecrets.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## connectionsListConsentLinks

> ConsentLinkPayload connectionsListConsentLinks(subscriptionId, resourceGroupName, connectionName, apiVersion, content)



Lists consent links of a connection.

### Example

```javascript
import LogicAppsManagementClient from 'logic_apps_management_client';
let defaultClient = LogicAppsManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicAppsManagementClient.ConnectionsApi();
let subscriptionId = "subscriptionId_example"; // String | Subscription Id
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let connectionName = "connectionName_example"; // String | The connection name.
let apiVersion = "apiVersion_example"; // String | API Version
let content = new LogicAppsManagementClient.ConsentLinkInput(); // ConsentLinkInput | The content.
apiInstance.connectionsListConsentLinks(subscriptionId, resourceGroupName, connectionName, apiVersion, content, (error, data, response) => {
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
 **resourceGroupName** | **String**| The resource group name. | 
 **connectionName** | **String**| The connection name. | 
 **apiVersion** | **String**| API Version | 
 **content** | [**ConsentLinkInput**](ConsentLinkInput.md)| The content. | 

### Return type

[**ConsentLinkPayload**](ConsentLinkPayload.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

