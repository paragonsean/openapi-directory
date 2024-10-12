# IotHubClient.PUTApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iotHubResourceCreateEventHubConsumerGroup**](PUTApi.md#iotHubResourceCreateEventHubConsumerGroup) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/eventHubEndpoints/{eventHubEndpointName}/ConsumerGroups/{name} | Add a consumer group to an Event Hub-compatible endpoint in an IoT hub.
[**iotHubResourceCreateOrUpdate**](PUTApi.md#iotHubResourceCreateOrUpdate) | **PUT** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName} | Create or update the metadata of an IoT hub.



## iotHubResourceCreateEventHubConsumerGroup

> EventHubConsumerGroupInfo iotHubResourceCreateEventHubConsumerGroup(apiVersion, subscriptionId, resourceGroupName, resourceName, eventHubEndpointName, name)

Add a consumer group to an Event Hub-compatible endpoint in an IoT hub.

Add a consumer group to an Event Hub-compatible endpoint in an IoT hub.

### Example

```javascript
import IotHubClient from 'iot_hub_client';

let apiInstance = new IotHubClient.PUTApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
let resourceName = "resourceName_example"; // String | The name of the IoT hub.
let eventHubEndpointName = "eventHubEndpointName_example"; // String | The name of the Event Hub-compatible endpoint in the IoT hub.
let name = "name_example"; // String | The name of the consumer group to add.
apiInstance.iotHubResourceCreateEventHubConsumerGroup(apiVersion, subscriptionId, resourceGroupName, resourceName, eventHubEndpointName, name, (error, data, response) => {
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
 **eventHubEndpointName** | **String**| The name of the Event Hub-compatible endpoint in the IoT hub. | 
 **name** | **String**| The name of the consumer group to add. | 

### Return type

[**EventHubConsumerGroupInfo**](EventHubConsumerGroupInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## iotHubResourceCreateOrUpdate

> IotHubDescription iotHubResourceCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, iotHubDescription)

Create or update the metadata of an IoT hub.

Create or update the metadata of an Iot hub. The usual pattern to modify a property is to retrieve the IoT hub metadata and security metadata, and then combine them with the modified values in a new body to update the IoT hub.

### Example

```javascript
import IotHubClient from 'iot_hub_client';

let apiInstance = new IotHubClient.PUTApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
let resourceName = "resourceName_example"; // String | The name of the IoT hub to create or update.
let iotHubDescription = new IotHubClient.IotHubDescription(); // IotHubDescription | The IoT hub metadata and security metadata.
apiInstance.iotHubResourceCreateOrUpdate(apiVersion, subscriptionId, resourceGroupName, resourceName, iotHubDescription, (error, data, response) => {
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
 **resourceName** | **String**| The name of the IoT hub to create or update. | 
 **iotHubDescription** | [**IotHubDescription**](IotHubDescription.md)| The IoT hub metadata and security metadata. | 

### Return type

[**IotHubDescription**](IotHubDescription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: application/json, text/json

