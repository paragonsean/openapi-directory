# AzureMediaServices.DefaultApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mediaGraphsCreateOrUpdate**](DefaultApi.md#mediaGraphsCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/mediaGraphs/{mediaGraphName} | Create or update a Media Graph
[**mediaGraphsDelete**](DefaultApi.md#mediaGraphsDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/mediaGraphs/{mediaGraphName} | Delete a Media Graph
[**mediaGraphsGet**](DefaultApi.md#mediaGraphsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/mediaGraphs/{mediaGraphName} | Get a Media Graph
[**mediaGraphsList**](DefaultApi.md#mediaGraphsList) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/mediaGraphs | List Media Graphs
[**mediaGraphsStart**](DefaultApi.md#mediaGraphsStart) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/mediaGraphs/{mediaGraphName}/start | Start a Media Graph
[**mediaGraphsStop**](DefaultApi.md#mediaGraphsStop) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/mediaGraphs/{mediaGraphName}/stop | Stop a Media Graph
[**operationResultsGet**](DefaultApi.md#operationResultsGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/mediaGraphs/{mediaGraphName}/operationResults/{operationId} | Get the operation result
[**operationsStatusGet**](DefaultApi.md#operationsStatusGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaServices/{accountName}/mediaGraphs/{mediaGraphName}/operationsStatus/{operationId} | Get the operation status



## mediaGraphsCreateOrUpdate

> MediaGraph mediaGraphsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, mediaGraphName, apiVersion, parameters)

Create or update a Media Graph

Create or update a Media Graph in the Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let mediaGraphName = "mediaGraphName_example"; // String | The Media Graph name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.MediaGraph(); // MediaGraph | The request parameters
apiInstance.mediaGraphsCreateOrUpdate(subscriptionId, resourceGroupName, accountName, mediaGraphName, apiVersion, parameters, (error, data, response) => {
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
 **mediaGraphName** | **String**| The Media Graph name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 
 **parameters** | [**MediaGraph**](MediaGraph.md)| The request parameters | 

### Return type

[**MediaGraph**](MediaGraph.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mediaGraphsDelete

> mediaGraphsDelete(subscriptionId, resourceGroupName, accountName, mediaGraphName, apiVersion)

Delete a Media Graph

Deletes a Media Graph in the Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let mediaGraphName = "mediaGraphName_example"; // String | The Media Graph name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.mediaGraphsDelete(subscriptionId, resourceGroupName, accountName, mediaGraphName, apiVersion, (error, data, response) => {
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
 **mediaGraphName** | **String**| The Media Graph name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mediaGraphsGet

> MediaGraph mediaGraphsGet(subscriptionId, resourceGroupName, accountName, mediaGraphName, apiVersion)

Get a Media Graph

Get the details of a Media Graph in the Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let mediaGraphName = "mediaGraphName_example"; // String | The Media Graph name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.mediaGraphsGet(subscriptionId, resourceGroupName, accountName, mediaGraphName, apiVersion, (error, data, response) => {
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
 **mediaGraphName** | **String**| The Media Graph name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

[**MediaGraph**](MediaGraph.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mediaGraphsList

> MediaGraphCollection mediaGraphsList(subscriptionId, resourceGroupName, accountName, apiVersion, opts)

List Media Graphs

Lists Media Graphs in the Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let opts = {
  'top': 56 // Number | Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n.
};
apiInstance.mediaGraphsList(subscriptionId, resourceGroupName, accountName, apiVersion, opts, (error, data, response) => {
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
 **top** | **Number**| Specifies a non-negative integer n that limits the number of items returned from a collection. The service returns the number of available items up to but not greater than the specified value n. | [optional] 

### Return type

[**MediaGraphCollection**](MediaGraphCollection.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mediaGraphsStart

> mediaGraphsStart(subscriptionId, resourceGroupName, accountName, mediaGraphName, apiVersion)

Start a Media Graph

Start a Media Graph in the Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let mediaGraphName = "mediaGraphName_example"; // String | The Media Graph name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.mediaGraphsStart(subscriptionId, resourceGroupName, accountName, mediaGraphName, apiVersion, (error, data, response) => {
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
 **mediaGraphName** | **String**| The Media Graph name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mediaGraphsStop

> mediaGraphsStop(subscriptionId, resourceGroupName, accountName, mediaGraphName, apiVersion)

Stop a Media Graph

Stop a Media Graph in the Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let mediaGraphName = "mediaGraphName_example"; // String | The Media Graph name.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.mediaGraphsStop(subscriptionId, resourceGroupName, accountName, mediaGraphName, apiVersion, (error, data, response) => {
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
 **mediaGraphName** | **String**| The Media Graph name. | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## operationResultsGet

> Object operationResultsGet(subscriptionId, resourceGroupName, accountName, mediaGraphName, operationId, apiVersion)

Get the operation result

Get the operation result of a Media Graph in the Media Services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let mediaGraphName = "mediaGraphName_example"; // String | The Media Graph name.
let operationId = "operationId_example"; // String | The operation ID
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.operationResultsGet(subscriptionId, resourceGroupName, accountName, mediaGraphName, operationId, apiVersion, (error, data, response) => {
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
 **mediaGraphName** | **String**| The Media Graph name. | 
 **operationId** | **String**| The operation ID | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## operationsStatusGet

> MediaGraphOperationStatus operationsStatusGet(subscriptionId, resourceGroupName, accountName, mediaGraphName, operationId, apiVersion)

Get the operation status

Get the operation status of a Media Graph in the media services account

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let mediaGraphName = "mediaGraphName_example"; // String | The Media Graph name.
let operationId = "operationId_example"; // String | The operation ID
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
apiInstance.operationsStatusGet(subscriptionId, resourceGroupName, accountName, mediaGraphName, operationId, apiVersion, (error, data, response) => {
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
 **mediaGraphName** | **String**| The Media Graph name. | 
 **operationId** | **String**| The operation ID | 
 **apiVersion** | **String**| The Version of the API to be used with the client request. | 

### Return type

[**MediaGraphOperationStatus**](MediaGraphOperationStatus.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

