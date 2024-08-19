# AzureMediaServices.LiveEventsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**liveEventsCreate**](LiveEventsApi.md#liveEventsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName} | Create Live Event
[**liveEventsDelete**](LiveEventsApi.md#liveEventsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName} | Delete Live Event
[**liveEventsGet**](LiveEventsApi.md#liveEventsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName} | Get Live Event
[**liveEventsList**](LiveEventsApi.md#liveEventsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents | List Live Events
[**liveEventsReset**](LiveEventsApi.md#liveEventsReset) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName}/reset | Reset Live Event
[**liveEventsStart**](LiveEventsApi.md#liveEventsStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName}/start | Start Live Event
[**liveEventsStop**](LiveEventsApi.md#liveEventsStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName}/stop | Stop Live Event
[**liveEventsUpdate**](LiveEventsApi.md#liveEventsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/liveEvents/{liveEventName} | 



## liveEventsCreate

> LiveEvent liveEventsCreate(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion, parameters, opts)

Create Live Event

Creates a Live Event.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.LiveEventsApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let liveEventName = "liveEventName_example"; // String | The name of the Live Event.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.LiveEvent(); // LiveEvent | Live Event properties needed for creation.
let opts = {
  'autoStart': true // Boolean | The flag indicates if the resource should be automatically started on creation.
};
apiInstance.liveEventsCreate(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion, parameters, opts, (error, data, response) => {
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
 **parameters** | [**LiveEvent**](LiveEvent.md)| Live Event properties needed for creation. | 
 **autoStart** | **Boolean**| The flag indicates if the resource should be automatically started on creation. | [optional] 

### Return type

[**LiveEvent**](LiveEvent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## liveEventsDelete

> liveEventsDelete(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion)

Delete Live Event

Deletes a Live Event.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.LiveEventsApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let liveEventName = "liveEventName_example"; // String | The name of the Live Event.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.liveEventsDelete(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## liveEventsGet

> LiveEvent liveEventsGet(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion)

Get Live Event

Gets a Live Event.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.LiveEventsApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let liveEventName = "liveEventName_example"; // String | The name of the Live Event.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.liveEventsGet(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion, (error, data, response) => {
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

[**LiveEvent**](LiveEvent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## liveEventsList

> LiveEventListResult liveEventsList(subscriptionId, resourceGroupName, accountName, apiVersion)

List Live Events

Lists the Live Events in the account.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.LiveEventsApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.liveEventsList(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

[**LiveEventListResult**](LiveEventListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## liveEventsReset

> liveEventsReset(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion)

Reset Live Event

Resets an existing Live Event.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.LiveEventsApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let liveEventName = "liveEventName_example"; // String | The name of the Live Event.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.liveEventsReset(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## liveEventsStart

> liveEventsStart(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion)

Start Live Event

Starts an existing Live Event.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.LiveEventsApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let liveEventName = "liveEventName_example"; // String | The name of the Live Event.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.liveEventsStart(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## liveEventsStop

> liveEventsStop(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion, parameters)

Stop Live Event

Stops an existing Live Event.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.LiveEventsApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let liveEventName = "liveEventName_example"; // String | The name of the Live Event.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.LiveEventActionInput(); // LiveEventActionInput | LiveEvent stop parameters
apiInstance.liveEventsStop(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion, parameters, (error, data, response) => {
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
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 
 **parameters** | [**LiveEventActionInput**](LiveEventActionInput.md)| LiveEvent stop parameters | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## liveEventsUpdate

> LiveEvent liveEventsUpdate(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion, parameters)



Updates a existing Live Event.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.LiveEventsApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let liveEventName = "liveEventName_example"; // String | The name of the Live Event.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.LiveEvent(); // LiveEvent | Live Event properties needed for creation.
apiInstance.liveEventsUpdate(subscriptionId, resourceGroupName, accountName, liveEventName, apiVersion, parameters, (error, data, response) => {
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
 **parameters** | [**LiveEvent**](LiveEvent.md)| Live Event properties needed for creation. | 

### Return type

[**LiveEvent**](LiveEvent.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

