# LogicManagementClient.IntegrationAccountMapsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrationAccountMapsCreateOrUpdate**](IntegrationAccountMapsApi.md#integrationAccountMapsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps/{mapName} | 
[**integrationAccountMapsDelete**](IntegrationAccountMapsApi.md#integrationAccountMapsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps/{mapName} | 
[**integrationAccountMapsGet**](IntegrationAccountMapsApi.md#integrationAccountMapsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps/{mapName} | 
[**integrationAccountMapsList**](IntegrationAccountMapsApi.md#integrationAccountMapsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/maps | 



## integrationAccountMapsCreateOrUpdate

> IntegrationAccountMap integrationAccountMapsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, mapName, apiVersion, map)



Creates or updates an integration account map.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';

let apiInstance = new LogicManagementClient.IntegrationAccountMapsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let mapName = "mapName_example"; // String | The integration account map name.
let apiVersion = "apiVersion_example"; // String | The API version.
let map = new LogicManagementClient.IntegrationAccountMap(); // IntegrationAccountMap | The integration account map.
apiInstance.integrationAccountMapsCreateOrUpdate(subscriptionId, resourceGroupName, integrationAccountName, mapName, apiVersion, map, (error, data, response) => {
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

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json


## integrationAccountMapsDelete

> integrationAccountMapsDelete(subscriptionId, resourceGroupName, integrationAccountName, mapName, apiVersion)



Deletes an integration account map.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';

let apiInstance = new LogicManagementClient.IntegrationAccountMapsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let mapName = "mapName_example"; // String | The integration account map name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationAccountMapsDelete(subscriptionId, resourceGroupName, integrationAccountName, mapName, apiVersion, (error, data, response) => {
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## integrationAccountMapsGet

> IntegrationAccountMap integrationAccountMapsGet(subscriptionId, resourceGroupName, integrationAccountName, mapName, apiVersion)



Gets an integration account map.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';

let apiInstance = new LogicManagementClient.IntegrationAccountMapsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let mapName = "mapName_example"; // String | The integration account map name.
let apiVersion = "apiVersion_example"; // String | The API version.
apiInstance.integrationAccountMapsGet(subscriptionId, resourceGroupName, integrationAccountName, mapName, apiVersion, (error, data, response) => {
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## integrationAccountMapsList

> IntegrationAccountMapListResult integrationAccountMapsList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, opts)



Gets a list of integration account maps.

### Example

```javascript
import LogicManagementClient from 'logic_management_client';

let apiInstance = new LogicManagementClient.IntegrationAccountMapsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription id.
let resourceGroupName = "resourceGroupName_example"; // String | The resource group name.
let integrationAccountName = "integrationAccountName_example"; // String | The integration account name.
let apiVersion = "apiVersion_example"; // String | The API version.
let opts = {
  'top': 56, // Number | The number of items to be included in the result.
  'filter': "filter_example" // String | The filter to apply on the operation.
};
apiInstance.integrationAccountMapsList(subscriptionId, resourceGroupName, integrationAccountName, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| The filter to apply on the operation. | [optional] 

### Return type

[**IntegrationAccountMapListResult**](IntegrationAccountMapListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

