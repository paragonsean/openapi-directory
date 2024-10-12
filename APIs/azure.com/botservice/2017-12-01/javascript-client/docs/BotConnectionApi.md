# AzureBotService.BotConnectionApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**botConnectionCreate**](BotConnectionApi.md#botConnectionCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/Connections/{connectionName} | 
[**botConnectionDelete**](BotConnectionApi.md#botConnectionDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/Connections/{connectionName} | 
[**botConnectionGet**](BotConnectionApi.md#botConnectionGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/Connections/{connectionName} | 
[**botConnectionListByBotService**](BotConnectionApi.md#botConnectionListByBotService) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/connections | 
[**botConnectionListWithSecrets**](BotConnectionApi.md#botConnectionListWithSecrets) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/Connections/{connectionName}/listWithSecrets | 
[**botConnectionUpdate**](BotConnectionApi.md#botConnectionUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/Connections/{connectionName} | 



## botConnectionCreate

> ConnectionSetting botConnectionCreate(resourceGroupName, resourceName, connectionName, apiVersion, subscriptionId, parameters)



Register a new Auth Connection for a Bot Service

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.BotConnectionApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
let resourceName = "resourceName_example"; // String | The name of the Bot resource.
let connectionName = "connectionName_example"; // String | The name of the Bot Service Connection Setting resource
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-12-01
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let parameters = new AzureBotService.ConnectionSetting(); // ConnectionSetting | The parameters to provide for creating the Connection Setting.
apiInstance.botConnectionCreate(resourceGroupName, resourceName, connectionName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | 
 **resourceName** | **String**| The name of the Bot resource. | 
 **connectionName** | **String**| The name of the Bot Service Connection Setting resource | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-12-01 | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **parameters** | [**ConnectionSetting**](ConnectionSetting.md)| The parameters to provide for creating the Connection Setting. | 

### Return type

[**ConnectionSetting**](ConnectionSetting.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## botConnectionDelete

> botConnectionDelete(resourceGroupName, resourceName, connectionName, apiVersion, subscriptionId)



Deletes a Connection Setting registration for a Bot Service

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.BotConnectionApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
let resourceName = "resourceName_example"; // String | The name of the Bot resource.
let connectionName = "connectionName_example"; // String | The name of the Bot Service Connection Setting resource
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-12-01
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
apiInstance.botConnectionDelete(resourceGroupName, resourceName, connectionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | 
 **resourceName** | **String**| The name of the Bot resource. | 
 **connectionName** | **String**| The name of the Bot Service Connection Setting resource | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-12-01 | 
 **subscriptionId** | **String**| Azure Subscription ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## botConnectionGet

> ConnectionSetting botConnectionGet(resourceGroupName, resourceName, connectionName, apiVersion, subscriptionId)



Get a Connection Setting registration for a Bot Service

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.BotConnectionApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
let resourceName = "resourceName_example"; // String | The name of the Bot resource.
let connectionName = "connectionName_example"; // String | The name of the Bot Service Connection Setting resource
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-12-01
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
apiInstance.botConnectionGet(resourceGroupName, resourceName, connectionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | 
 **resourceName** | **String**| The name of the Bot resource. | 
 **connectionName** | **String**| The name of the Bot Service Connection Setting resource | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-12-01 | 
 **subscriptionId** | **String**| Azure Subscription ID. | 

### Return type

[**ConnectionSetting**](ConnectionSetting.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## botConnectionListByBotService

> ConnectionSettingResponseList botConnectionListByBotService(resourceGroupName, resourceName, subscriptionId, apiVersion)



Returns all the Connection Settings registered to a particular BotService resource

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.BotConnectionApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
let resourceName = "resourceName_example"; // String | The name of the Bot resource.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-12-01
apiInstance.botConnectionListByBotService(resourceGroupName, resourceName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | 
 **resourceName** | **String**| The name of the Bot resource. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-12-01 | 

### Return type

[**ConnectionSettingResponseList**](ConnectionSettingResponseList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## botConnectionListWithSecrets

> ConnectionSetting botConnectionListWithSecrets(resourceGroupName, resourceName, connectionName, apiVersion, subscriptionId)



Get a Connection Setting registration for a Bot Service

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.BotConnectionApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
let resourceName = "resourceName_example"; // String | The name of the Bot resource.
let connectionName = "connectionName_example"; // String | The name of the Bot Service Connection Setting resource
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-12-01
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
apiInstance.botConnectionListWithSecrets(resourceGroupName, resourceName, connectionName, apiVersion, subscriptionId, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | 
 **resourceName** | **String**| The name of the Bot resource. | 
 **connectionName** | **String**| The name of the Bot Service Connection Setting resource | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-12-01 | 
 **subscriptionId** | **String**| Azure Subscription ID. | 

### Return type

[**ConnectionSetting**](ConnectionSetting.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## botConnectionUpdate

> ConnectionSetting botConnectionUpdate(resourceGroupName, resourceName, connectionName, apiVersion, subscriptionId, parameters)



Updates a Connection Setting registration for a Bot Service

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.BotConnectionApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
let resourceName = "resourceName_example"; // String | The name of the Bot resource.
let connectionName = "connectionName_example"; // String | The name of the Bot Service Connection Setting resource
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-12-01
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let parameters = new AzureBotService.ConnectionSetting(); // ConnectionSetting | The parameters to provide for updating the Connection Setting.
apiInstance.botConnectionUpdate(resourceGroupName, resourceName, connectionName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the Bot resource group in the user subscription. | 
 **resourceName** | **String**| The name of the Bot resource. | 
 **connectionName** | **String**| The name of the Bot Service Connection Setting resource | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-12-01 | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **parameters** | [**ConnectionSetting**](ConnectionSetting.md)| The parameters to provide for updating the Connection Setting. | 

### Return type

[**ConnectionSetting**](ConnectionSetting.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

