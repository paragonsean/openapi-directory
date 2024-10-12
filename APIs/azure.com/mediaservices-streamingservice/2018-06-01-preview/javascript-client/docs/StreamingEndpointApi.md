# AzureMediaServices.StreamingEndpointApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**streamingEndpointsUpdate**](StreamingEndpointApi.md#streamingEndpointsUpdate) | **PATCH** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Media/mediaservices/{accountName}/streamingEndpoints/{streamingEndpointName} | Update StreamingEndpoint



## streamingEndpointsUpdate

> StreamingEndpoint streamingEndpointsUpdate(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion, parameters)

Update StreamingEndpoint

Updates a existing StreamingEndpoint.

### Example

```javascript
import AzureMediaServices from 'azure_media_services';

let apiInstance = new AzureMediaServices.StreamingEndpointApi();
let subscriptionId = "subscriptionId_example"; // String | The unique identifier for a Microsoft Azure subscription.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group within the Azure subscription.
let accountName = "accountName_example"; // String | The Media Services account name.
let streamingEndpointName = "streamingEndpointName_example"; // String | The name of the StreamingEndpoint.
let apiVersion = "apiVersion_example"; // String | The Version of the API to be used with the client request.
let parameters = new AzureMediaServices.StreamingEndpoint(); // StreamingEndpoint | StreamingEndpoint properties needed for creation.
apiInstance.streamingEndpointsUpdate(subscriptionId, resourceGroupName, accountName, streamingEndpointName, apiVersion, parameters, (error, data, response) => {
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

### Return type

[**StreamingEndpoint**](StreamingEndpoint.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

