# AzureMediaServices.LiveOutputsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**liveOutputsCreate**](LiveOutputsApi.md#liveOutputsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName}/liveOutputs/{liveOutputName} | Create Live Output
[**liveOutputsDelete**](LiveOutputsApi.md#liveOutputsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName}/liveOutputs/{liveOutputName} | Delete Live Output
[**liveOutputsGet**](LiveOutputsApi.md#liveOutputsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName}/liveOutputs/{liveOutputName} | Get Live Output
[**liveOutputsList**](LiveOutputsApi.md#liveOutputsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName}/liveOutputs | List Live Outputs



## liveOutputsCreate

> LiveOutput liveOutputsCreate(subscriptionId, resourceGroupName, accountName, liveEventName, liveOutputName, apiVersion, parameters)

Create Live Output

Creates a Live Output.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.LiveOutputsApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let liveEventName = "liveEventName_example"; // String | The name of the Live Event.
let liveOutputName = "liveOutputName_example"; // String | The name of the Live Output.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.LiveOutput(); // LiveOutput | Live Output properties needed for creation.
apiInstance.liveOutputsCreate(subscriptionId, resourceGroupName, accountName, liveEventName, liveOutputName, apiVersion, parameters, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **liveEventName** | **String**| The name of the Live Event. | 
 **liveOutputName** | **String**| The name of the Live Output. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 
 **parameters** | [**LiveOutput**](LiveOutput.md)| Live Output properties needed for creation. | 

### Return type

[**LiveOutput**](LiveOutput.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## liveOutputsDelete

> liveOutputsDelete(subscriptionId, resourceGroupName, accountName, liveEventName, liveOutputName, apiVersion)

Delete Live Output

Deletes a Live Output.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.LiveOutputsApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let liveEventName = "liveEventName_example"; // String | The name of the Live Event.
let liveOutputName = "liveOutputName_example"; // String | The name of the Live Output.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.liveOutputsDelete(subscriptionId, resourceGroupName, accountName, liveEventName, liveOutputName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **liveEventName** | **String**| The name of the Live Event. | 
 **liveOutputName** | **String**| The name of the Live Output. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## liveOutputsGet

> LiveOutput liveOutputsGet(subscriptionId, resourceGroupName, accountName, liveEventName, liveOutputName, apiVersion)

Get Live Output

Gets a Live Output.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.LiveOutputsApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let liveEventName = "liveEventName_example"; // String | The name of the Live Event.
let liveOutputName = "liveOutputName_example"; // String | The name of the Live Output.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.liveOutputsGet(subscriptionId, resourceGroupName, accountName, liveEventName, liveOutputName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **liveEventName** | **String**| The name of the Live Event. | 
 **liveOutputName** | **String**| The name of the Live Output. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

[**LiveOutput**](LiveOutput.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## liveOutputsList

> LiveOutputListResult liveOutputsList(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion)

List Live Outputs

Lists the Live Outputs in the Live Event.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.LiveOutputsApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let liveEventName = "liveEventName_example"; // String | The name of the Live Event.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.liveOutputsList(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion, (error, data, response) => {
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
 **subscriptionId** | **String**| The unique identifier for a Microsoft Azure subscription. | 
 **resourceGroupName** | **String**| The name of the resource group within the Azure subscription. | 
 **accountName** | **String**| The Media Services account name. | 
 **liveEventName** | **String**| The name of the Live Event. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

[**LiveOutputListResult**](LiveOutputListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

