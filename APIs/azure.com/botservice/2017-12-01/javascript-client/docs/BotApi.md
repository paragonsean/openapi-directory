# AzureBotService.BotApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**botsCreate**](BotApi.md#botsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName} | 
[**botsDelete**](BotApi.md#botsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName} | 
[**botsGet**](BotApi.md#botsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName} | 
[**botsGetCheckNameAvailability**](BotApi.md#botsGetCheckNameAvailability) | **GET** /providers/Microsoft.BotService/botServices/checkNameAvailability | 
[**botsList**](BotApi.md#botsList) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.BotService/botServices | 
[**botsListByResourceGroup**](BotApi.md#botsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices | 
[**botsUpdate**](BotApi.md#botsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/botServices/{resourceName} | 



## botsCreate

> Bot botsCreate(resourceGroupName, resourceName, apiVersion, subscriptionId, parameters)



Creates a Bot Service. Bot Service is a resource group wide resource type.

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.BotApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
let resourceName = "resourceName_example"; // String | The name of the Bot resource.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-12-01
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let parameters = new AzureBotService.Bot(); // Bot | The parameters to provide for the created bot.
apiInstance.botsCreate(resourceGroupName, resourceName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-12-01 | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **parameters** | [**Bot**](Bot.md)| The parameters to provide for the created bot. | 

### Return type

[**Bot**](Bot.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## botsDelete

> botsDelete(resourceGroupName, resourceName, apiVersion, subscriptionId)



Deletes a Bot Service from the resource group. 

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.BotApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
let resourceName = "resourceName_example"; // String | The name of the Bot resource.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-12-01
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
apiInstance.botsDelete(resourceGroupName, resourceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-12-01 | 
 **subscriptionId** | **String**| Azure Subscription ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## botsGet

> Bot botsGet(resourceGroupName, resourceName, apiVersion, subscriptionId)



Returns a BotService specified by the parameters.

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.BotApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
let resourceName = "resourceName_example"; // String | The name of the Bot resource.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-12-01
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
apiInstance.botsGet(resourceGroupName, resourceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-12-01 | 
 **subscriptionId** | **String**| Azure Subscription ID. | 

### Return type

[**Bot**](Bot.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## botsGetCheckNameAvailability

> CheckNameAvailabilityResponseBody botsGetCheckNameAvailability(apiVersion, parameters)



Check whether a bot name is available.

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.BotApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-12-01
let parameters = new AzureBotService.CheckNameAvailabilityRequestBody(); // CheckNameAvailabilityRequestBody | The request body parameters to provide for the check name availability request
apiInstance.botsGetCheckNameAvailability(apiVersion, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-12-01 | 
 **parameters** | [**CheckNameAvailabilityRequestBody**](CheckNameAvailabilityRequestBody.md)| The request body parameters to provide for the check name availability request | 

### Return type

[**CheckNameAvailabilityResponseBody**](CheckNameAvailabilityResponseBody.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## botsList

> BotResponseList botsList(apiVersion, subscriptionId)



Returns all the resources of a particular type belonging to a subscription.

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.BotApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-12-01
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
apiInstance.botsList(apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-12-01 | 
 **subscriptionId** | **String**| Azure Subscription ID. | 

### Return type

[**BotResponseList**](BotResponseList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## botsListByResourceGroup

> BotResponseList botsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)



Returns all the resources of a particular type belonging to a resource group

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.BotApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-12-01
apiInstance.botsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-12-01 | 

### Return type

[**BotResponseList**](BotResponseList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## botsUpdate

> Bot botsUpdate(resourceGroupName, resourceName, apiVersion, subscriptionId, parameters)



Updates a Bot Service

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.BotApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
let resourceName = "resourceName_example"; // String | The name of the Bot resource.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request. Current version is 2017-12-01
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let parameters = new AzureBotService.Bot(); // Bot | The parameters to provide for the created bot.
apiInstance.botsUpdate(resourceGroupName, resourceName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. Current version is 2017-12-01 | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **parameters** | [**Bot**](Bot.md)| The parameters to provide for the created bot. | 

### Return type

[**Bot**](Bot.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

