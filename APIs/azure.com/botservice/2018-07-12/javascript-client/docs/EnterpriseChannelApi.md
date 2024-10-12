# AzureBotService.EnterpriseChannelApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enterpriseChannelsCheckNameAvailability**](EnterpriseChannelApi.md#enterpriseChannelsCheckNameAvailability) | **POST** /providers/Microsoft.BotService/checkEnterpriseChannelNameAvailability | 
[**enterpriseChannelsCreate**](EnterpriseChannelApi.md#enterpriseChannelsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/enterpriseChannels/{resourceName} | 
[**enterpriseChannelsDelete**](EnterpriseChannelApi.md#enterpriseChannelsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/enterpriseChannels/{resourceName} | 
[**enterpriseChannelsGet**](EnterpriseChannelApi.md#enterpriseChannelsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/enterpriseChannels/{resourceName} | 
[**enterpriseChannelsListByResourceGroup**](EnterpriseChannelApi.md#enterpriseChannelsListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/enterpriseChannels | 
[**enterpriseChannelsUpdate**](EnterpriseChannelApi.md#enterpriseChannelsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.BotService/enterpriseChannels/{resourceName} | 



## enterpriseChannelsCheckNameAvailability

> EnterpriseChannelCheckNameAvailabilityResponse enterpriseChannelsCheckNameAvailability(apiVersion, parameters)



Check whether an Enterprise Channel name is available.

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.EnterpriseChannelApi();
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let parameters = new AzureBotService.EnterpriseChannelCheckNameAvailabilityRequest(); // EnterpriseChannelCheckNameAvailabilityRequest | The parameters to provide for the Enterprise Channel check name availability request.
apiInstance.enterpriseChannelsCheckNameAvailability(apiVersion, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **parameters** | [**EnterpriseChannelCheckNameAvailabilityRequest**](EnterpriseChannelCheckNameAvailabilityRequest.md)| The parameters to provide for the Enterprise Channel check name availability request. | 

### Return type

[**EnterpriseChannelCheckNameAvailabilityResponse**](EnterpriseChannelCheckNameAvailabilityResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enterpriseChannelsCreate

> EnterpriseChannel enterpriseChannelsCreate(resourceGroupName, resourceName, apiVersion, subscriptionId, parameters)



Creates an Enterprise Channel.

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.EnterpriseChannelApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
let resourceName = "resourceName_example"; // String | The name of the Bot resource.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let parameters = new AzureBotService.EnterpriseChannel(); // EnterpriseChannel | The parameters to provide for the new Enterprise Channel.
apiInstance.enterpriseChannelsCreate(resourceGroupName, resourceName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **parameters** | [**EnterpriseChannel**](EnterpriseChannel.md)| The parameters to provide for the new Enterprise Channel. | 

### Return type

[**EnterpriseChannel**](EnterpriseChannel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enterpriseChannelsDelete

> enterpriseChannelsDelete(resourceGroupName, resourceName, apiVersion, subscriptionId)



Deletes an Enterprise Channel from the resource group

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.EnterpriseChannelApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
let resourceName = "resourceName_example"; // String | The name of the Bot resource.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
apiInstance.enterpriseChannelsDelete(resourceGroupName, resourceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseChannelsGet

> EnterpriseChannel enterpriseChannelsGet(resourceGroupName, resourceName, apiVersion, subscriptionId)



Returns an Enterprise Channel specified by the parameters.

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.EnterpriseChannelApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
let resourceName = "resourceName_example"; // String | The name of the Bot resource.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
apiInstance.enterpriseChannelsGet(resourceGroupName, resourceName, apiVersion, subscriptionId, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 

### Return type

[**EnterpriseChannel**](EnterpriseChannel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseChannelsListByResourceGroup

> EnterpriseChannelResponseList enterpriseChannelsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion)



Returns all the resources of a particular type belonging to a resource group.

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.EnterpriseChannelApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
apiInstance.enterpriseChannelsListByResourceGroup(resourceGroupName, subscriptionId, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 

### Return type

[**EnterpriseChannelResponseList**](EnterpriseChannelResponseList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enterpriseChannelsUpdate

> EnterpriseChannel enterpriseChannelsUpdate(resourceGroupName, resourceName, apiVersion, subscriptionId, parameters)



Updates an Enterprise Channel.

### Example

```javascript
import AzureBotService from 'azure_bot_service';

let apiInstance = new AzureBotService.EnterpriseChannelApi();
let resourceGroupName = "resourceGroupName_example"; // String | The name of the Bot resource group in the user subscription.
let resourceName = "resourceName_example"; // String | The name of the Bot resource.
let apiVersion = "apiVersion_example"; // String | Version of the API to be used with the client request.
let subscriptionId = "subscriptionId_example"; // String | Azure Subscription ID.
let parameters = new AzureBotService.EnterpriseChannel(); // EnterpriseChannel | The parameters to provide to update the Enterprise Channel.
apiInstance.enterpriseChannelsUpdate(resourceGroupName, resourceName, apiVersion, subscriptionId, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| Version of the API to be used with the client request. | 
 **subscriptionId** | **String**| Azure Subscription ID. | 
 **parameters** | [**EnterpriseChannel**](EnterpriseChannel.md)| The parameters to provide to update the Enterprise Channel. | 

### Return type

[**EnterpriseChannel**](EnterpriseChannel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

