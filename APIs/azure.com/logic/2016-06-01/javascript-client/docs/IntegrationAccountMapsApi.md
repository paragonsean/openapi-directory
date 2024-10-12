# LogicManagementClient.IntegrationAccountMapsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mapsCreateOrUpdate**](IntegrationAccountMapsApi.md#mapsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps/{mapName} | 
[**mapsDelete**](IntegrationAccountMapsApi.md#mapsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps/{mapName} | 
[**mapsGet**](IntegrationAccountMapsApi.md#mapsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps/{mapName} | 
[**mapsListByIntegrationAccounts**](IntegrationAccountMapsApi.md#mapsListByIntegrationAccounts) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps | 
[**mapsListContentCallbackUrl**](IntegrationAccountMapsApi.md#mapsListContentCallbackUrl) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps/{mapName}/listContentCallbackUrl | 



## mapsCreateOrUpdate

> IntegrationAccountMap mapsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, mapName, apiVersion, map)



Creates or updates an integration account map.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountMapsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let mapName = "mapName_example"; // String | The integration account map name.
let apiVersion = "apiVersion_example"; // String | The API version.
let map = new LogicManagementClient.IntegrationAccountMap(); // IntegrationAccountMap | The integration account map.
apiInstance.mapsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, mapName, apiVersion, map, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **integrationAccountName** | **String**| The integration account name. | 
 **mapName** | **String**| The integration account map name. | 
 **apiVersion** | **String**| The API version. | 
 **map** | [**IntegrationAccountMap**](IntegrationAccountMap.md)| The integration account map. | 

### Return type

[**IntegrationAccountMap**](IntegrationAccountMap.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mapsDelete

> mapsDelete(subscriptionId, resourceGroupName, integrationAccountName, mapName, apiVersion)



Deletes an integration account map.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountMapsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let mapName = "mapName_example"; // String | The integration account map name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.mapsDelete(subscriptionId, resourceGroupName, integrationAccountName, mapName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **integrationAccountName** | **String**| The integration account name. | 
 **mapName** | **String**| The integration account map name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## mapsGet

> IntegrationAccountMap mapsGet(subscriptionId, resourceGroupName, integrationAccountName, mapName, apiVersion)



Gets an integration account map.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountMapsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let mapName = "mapName_example"; // String | The integration account map name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.mapsGet(subscriptionId, resourceGroupName, integrationAccountName, mapName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **integrationAccountName** | **String**| The integration account name. | 
 **mapName** | **String**| The integration account map name. | 
 **apiVersion** | **String**| The API version. | 

### Return type

[**IntegrationAccountMap**](IntegrationAccountMap.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mapsListByIntegrationAccounts

> IntegrationAccountMapListResult mapsListByIntegrationAccounts(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, opts)



Gets a list of integration account maps.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountMapsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'top': 56, // Number | The number of items to be included in the result.
  'filter': "filter_example" // String | The filter to apply on the operation. Options for filters include: MapType.
};
apiInstance.mapsListByIntegrationAccounts(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **integrationAccountName** | **String**| The integration account name. | 
 **apiVersion** | **String**| The API version. | 
 **top** | **Number**| The number of items to be included in the result. | [optional] 
 **filter** | **String**| The filter to apply on the operation. Options for filters include: MapType. | [optional] 

### Return type

[**IntegrationAccountMapListResult**](IntegrationAccountMapListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mapsListContentCallbackUrl

> WorkflowTriggerCallbackUrl mapsListContentCallbackUrl(subscriptionId, resourceGroupName, integrationAccountName, mapName, apiVersion, listContentCallbackUrl)



Get the content callback url.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';
let defaultClient = LogicManagementClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new LogicManagementClient.IntegrationAccountMapsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let mapName = "mapName_example"; // String | The integration account map name.
let apiVersion = "apiVersion_example"; // String | The API version.
let listContentCallbackUrl = new LogicManagementClient.GetCallbackUrlParameters(); // GetCallbackUrlParameters | 
apiInstance.mapsListContentCallbackUrl(subscriptionId, resourceGroupName, integrationAccountName, mapName, apiVersion, listContentCallbackUrl, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription id. | 
 **resourceGroupName** | **String**| The resource group name. | 
 **integrationAccountName** | **String**| The integration account name. | 
 **mapName** | **String**| The integration account map name. | 
 **apiVersion** | **String**| The API version. | 
 **listContentCallbackUrl** | [**GetCallbackUrlParameters**](GetCallbackUrlParameters.md)|  | 

### Return type

[**WorkflowTriggerCallbackUrl**](WorkflowTriggerCallbackUrl.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

