# AzureMediaServices.StreamingEndpointsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**streamingEndpointsCreate**](StreamingEndpointsApi.md#streamingEndpointsCreate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/streamingEndpoints/{streamingEndpointName} | Create StreamingEndpoint
[**streamingEndpointsDelete**](StreamingEndpointsApi.md#streamingEndpointsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/streamingEndpoints/{streamingEndpointName} | Delete StreamingEndpoint
[**streamingEndpointsGet**](StreamingEndpointsApi.md#streamingEndpointsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/streamingEndpoints/{streamingEndpointName} | Get StreamingEndpoint
[**streamingEndpointsList**](StreamingEndpointsApi.md#streamingEndpointsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/streamingEndpoints | List StreamingEndpoints
[**streamingEndpointsScale**](StreamingEndpointsApi.md#streamingEndpointsScale) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/streamingEndpoints/{streamingEndpointName}/scale | Scale StreamingEndpoint
[**streamingEndpointsStart**](StreamingEndpointsApi.md#streamingEndpointsStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/streamingEndpoints/{streamingEndpointName}/start | Start StreamingEndpoint
[**streamingEndpointsStop**](StreamingEndpointsApi.md#streamingEndpointsStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/streamingEndpoints/{streamingEndpointName}/stop | Stop StreamingEndpoint



## streamingEndpointsCreate

> StreamingEndpoint streamingEndpointsCreate(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion, parameters, opts)

Create StreamingEndpoint

Creates a StreamingEndpoint.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.StreamingEndpointsApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let streamingEndpointName = "streamingEndpointName_example"; // String | The name of the StreamingEndpoint.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.StreamingEndpoint(); // StreamingEndpoint | StreamingEndpoint properties needed for creation.
let opts = {
  'autoStart': true // Boolean | The flag indicates if auto start the Live Event.
};
apiInstance.streamingEndpointsCreate(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion, parameters, opts, (error, data, response) => {
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
 **streamingEndpointName** | **String**| The name of the StreamingEndpoint. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 
 **parameters** | [**StreamingEndpoint**](StreamingEndpoint.md)| StreamingEndpoint properties needed for creation. | 
 **autoStart** | **Boolean**| The flag indicates if auto start the Live Event. | [optional] 

### Return type

[**StreamingEndpoint**](StreamingEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## streamingEndpointsDelete

> streamingEndpointsDelete(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion)

Delete StreamingEndpoint

Deletes a StreamingEndpoint.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.StreamingEndpointsApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let streamingEndpointName = "streamingEndpointName_example"; // String | The name of the StreamingEndpoint.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.streamingEndpointsDelete(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion, (error, data, response) => {
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
 **streamingEndpointName** | **String**| The name of the StreamingEndpoint. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## streamingEndpointsGet

> StreamingEndpoint streamingEndpointsGet(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion)

Get StreamingEndpoint

Gets a StreamingEndpoint.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.StreamingEndpointsApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let streamingEndpointName = "streamingEndpointName_example"; // String | The name of the StreamingEndpoint.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.streamingEndpointsGet(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion, (error, data, response) => {
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
 **streamingEndpointName** | **String**| The name of the StreamingEndpoint. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

[**StreamingEndpoint**](StreamingEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## streamingEndpointsList

> StreamingEndpointListResult streamingEndpointsList(subscriptionId, resourceGroupName, accountName, apiVersion)

List StreamingEndpoints

Lists the StreamingEndpoints in the account.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.StreamingEndpointsApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.streamingEndpointsList(subscriptionId, resourceGroupName, accountName, apiVersion, (error, data, response) => {
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

[**StreamingEndpointListResult**](StreamingEndpointListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## streamingEndpointsScale

> streamingEndpointsScale(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion, parameters)

Scale StreamingEndpoint

Scales an existing StreamingEndpoint.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.StreamingEndpointsApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let streamingEndpointName = "streamingEndpointName_example"; // String | The name of the StreamingEndpoint.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.StreamingEntityScaleUnit(); // StreamingEntityScaleUnit | StreamingEndpoint scale parameters
apiInstance.streamingEndpointsScale(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion, parameters, (error, data, response) => {
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
 **streamingEndpointName** | **String**| The name of the StreamingEndpoint. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 
 **parameters** | [**StreamingEntityScaleUnit**](StreamingEntityScaleUnit.md)| StreamingEndpoint scale parameters | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## streamingEndpointsStart

> streamingEndpointsStart(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion)

Start StreamingEndpoint

Starts an existing StreamingEndpoint.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.StreamingEndpointsApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let streamingEndpointName = "streamingEndpointName_example"; // String | The name of the StreamingEndpoint.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.streamingEndpointsStart(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion, (error, data, response) => {
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
 **streamingEndpointName** | **String**| The name of the StreamingEndpoint. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## streamingEndpointsStop

> streamingEndpointsStop(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion)

Stop StreamingEndpoint

Stops an existing StreamingEndpoint.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.StreamingEndpointsApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let streamingEndpointName = "streamingEndpointName_example"; // String | The name of the StreamingEndpoint.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.streamingEndpointsStop(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion, (error, data, response) => {
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
 **streamingEndpointName** | **String**| The name of the StreamingEndpoint. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

