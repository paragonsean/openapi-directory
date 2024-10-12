# IotHubClient.DELETEApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iotHubResourceDelete**](DELETEApi.md#iotHubResourceDelete) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName} | Delete an IoT hub.
[**iotHubResourceDeleteEventHubConsumerGroup**](DELETEApi.md#iotHubResourceDeleteEventHubConsumerGroup) | **DELETE** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/eventHubEndpoints/{eventHubEndpointName}/ConsumerGroups/{name} | Delete a consumer group from an Event Hub-compatible endpoint in an IoT hub.



## iotHubResourceDelete

> IotHubDescription iotHubResourceDelete(apiVersion, subscriptionId, resourceGroupName, resourceName)

Delete an IoT hub.

Delete an IoT hub.

### Example

```javascript
import IotHubClient from 'iot_hub_client';
let defaultClient = IotHubClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotHubClient.DELETEApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
let resourceName = "resourceName_example"; // String | The name of the IoT hub.
apiInstance.iotHubResourceDelete(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | 
 **resourceName** | **String**| The name of the IoT hub. | 

### Return type

[**IotHubDescription**](IotHubDescription.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## iotHubResourceDeleteEventHubConsumerGroup

> iotHubResourceDeleteEventHubConsumerGroup(apiVersion, subscriptionId, resourceGroupName, resourceName, eventHubEndpointName, name)

Delete a consumer group from an Event Hub-compatible endpoint in an IoT hub.

Delete a consumer group from an Event Hub-compatible endpoint in an IoT hub.

### Example

```javascript
import IotHubClient from 'iot_hub_client';
let defaultClient = IotHubClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new IotHubClient.DELETEApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
let resourceName = "resourceName_example"; // String | The name of the IoT hub.
let eventHubEndpointName = "eventHubEndpointName_example"; // String | The name of the Event Hub-compatible endpoint in the IoT hub.
let name = "name_example"; // String | The name of the consumer group to delete.
apiInstance.iotHubResourceDeleteEventHubConsumerGroup(apiVersion, subscriptionId, resourceGroupName, resourceName, eventHubEndpointName, name, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API. | 
 **subscriptionId** | **String**| The subscription identifier. | 
 **resourceGroupName** | **String**| The name of the resource group that contains the IoT hub. | 
 **resourceName** | **String**| The name of the IoT hub. | 
 **eventHubEndpointName** | **String**| The name of the Event Hub-compatible endpoint in the IoT hub. | 
 **name** | **String**| The name of the consumer group to delete. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

