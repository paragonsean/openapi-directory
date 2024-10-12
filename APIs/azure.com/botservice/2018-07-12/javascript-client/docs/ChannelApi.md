# AzureBotService.ChannelApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channelsCreate**](ChannelApi.md#channelsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/channels/{channelName} | 
[**channelsDelete**](ChannelApi.md#channelsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/channels/{channelName} | 
[**channelsGet**](ChannelApi.md#channelsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/channels/{channelName} | 
[**channelsListByResourceGroup**](ChannelApi.md#channelsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/channels | 
[**channelsListWithKeys**](ChannelApi.md#channelsListWithKeys) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/channels/{channelName}/listChannelWithKeys | 
[**channelsUpdate**](ChannelApi.md#channelsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName}/channels/{channelName} | 



## channelsCreate

> BotChannel channelsCreate(resourceGroupName, resourceName, channelName, apiVersion, subscriptionId, parameters)



Creates a Channel registration for a Bot Service

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.ChannelApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
let resourceName = "resourceName_example"; // String | The name of the Bot resource.
let channelName = "channelName_example"; // String | The name of the Channel resource.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let parameters = new AzureBotService.BotChannel(); // BotChannel | The parameters to provide for the created bot.
apiInstance.channelsCreate(resourceGroupName, resourceName, channelName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **channelName** | **String**| The name of the Channel resource. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **parameters** | [**BotChannel**](BotChannel.md)| The parameters to provide for the created bot. | 

### Return type

[**BotChannel**](BotChannel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## channelsDelete

> channelsDelete(resourceGroupName, resourceName, channelName, apiVersion, subscriptionId)



Deletes a Channel registration from a Bot Service

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.ChannelApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
let resourceName = "resourceName_example"; // String | The name of the Bot resource.
let channelName = "channelName_example"; // String | The name of the Bot resource.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
apiInstance.channelsDelete(resourceGroupName, resourceName, channelName, apiVersion, subscriptionId, (error, data, response) => {
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
 **channelName** | **String**| The name of the Bot resource. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## channelsGet

> BotChannel channelsGet(resourceGroupName, resourceName, channelName, apiVersion, subscriptionId)



Returns a BotService Channel registration specified by the parameters.

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.ChannelApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
let resourceName = "resourceName_example"; // String | The name of the Bot resource.
let channelName = "channelName_example"; // String | The name of the Bot resource.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
apiInstance.channelsGet(resourceGroupName, resourceName, channelName, apiVersion, subscriptionId, (error, data, response) => {
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
 **channelName** | **String**| The name of the Bot resource. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 

### Return type

[**BotChannel**](BotChannel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## channelsListByResourceGroup

> ChannelResponseList channelsListByResourceGroup(resourceGroupName, resourceName, subscriptionId, apiVersion)



Returns all the Channel registrations of a particular BotService resource

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.ChannelApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
let resourceName = "resourceName_example"; // String | The name of the Bot resource.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.channelsListByResourceGroup(resourceGroupName, resourceName, subscriptionId, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**ChannelResponseList**](ChannelResponseList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## channelsListWithKeys

> BotChannel channelsListWithKeys(resourceGroupName, resourceName, channelName, apiVersion, subscriptionId)



Lists a Channel registration for a Bot Service including secrets

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.ChannelApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
let resourceName = "resourceName_example"; // String | The name of the Bot resource.
let channelName = "channelName_example"; // String | The name of the Channel resource.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
apiInstance.channelsListWithKeys(resourceGroupName, resourceName, channelName, apiVersion, subscriptionId, (error, data, response) => {
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
 **channelName** | **String**| The name of the Channel resource. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 

### Return type

[**BotChannel**](BotChannel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## channelsUpdate

> BotChannel channelsUpdate(resourceGroupName, resourceName, channelName, apiVersion, subscriptionId, parameters)



Updates a Channel registration for a Bot Service

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.ChannelApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
let resourceName = "resourceName_example"; // String | The name of the Bot resource.
let channelName = "channelName_example"; // String | The name of the Channel resource.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let parameters = new AzureBotService.BotChannel(); // BotChannel | The parameters to provide for the created bot.
apiInstance.channelsUpdate(resourceGroupName, resourceName, channelName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **channelName** | **String**| The name of the Channel resource. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **parameters** | [**BotChannel**](BotChannel.md)| The parameters to provide for the created bot. | 

### Return type

[**BotChannel**](BotChannel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

