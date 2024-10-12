# IotHubClient.GETApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**iotHubResourceGet**](GETApi.md#iotHubResourceGet) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName} | Get the non-security related metadata of an IoT hub.
[**iotHubResourceGetEventHubConsumerGroup**](GETApi.md#iotHubResourceGetEventHubConsumerGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/eventHubEndpoints/{eventHubEndpointName}/ConsumerGroups/{name} | Get a consumer group from the Event Hub-compatible device-to-cloud endpoint for an IoT hub.
[**iotHubResourceGetJob**](GETApi.md#iotHubResourceGetJob) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/jobs/{jobId} | Get the details of a job from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry.
[**iotHubResourceGetQuotaMetrics**](GETApi.md#iotHubResourceGetQuotaMetrics) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/quotaMetrics | Get the quota metrics for an IoT hub.
[**iotHubResourceGetStats**](GETApi.md#iotHubResourceGetStats) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/IotHubStats | Get the statistics from an IoT hub.
[**iotHubResourceGetValidSkus**](GETApi.md#iotHubResourceGetValidSkus) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/skus | Get the list of valid SKUs for an IoT hub.
[**iotHubResourceListByResourceGroup**](GETApi.md#iotHubResourceListByResourceGroup) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs | Get all the IoT hubs in a resource group.
[**iotHubResourceListBySubscription**](GETApi.md#iotHubResourceListBySubscription) | **GET** /subscriptions/{subscriptionId}/providers/Microsoft.Devices/IotHubs | Get all the IoT hubs in a subscription.
[**iotHubResourceListEventHubConsumerGroups**](GETApi.md#iotHubResourceListEventHubConsumerGroups) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/eventHubEndpoints/{eventHubEndpointName}/ConsumerGroups | Get a list of the consumer groups in the Event Hub-compatible device-to-cloud endpoint in an IoT hub.
[**iotHubResourceListJobs**](GETApi.md#iotHubResourceListJobs) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Devices/IotHubs/{resourceName}/jobs | Get a list of all the jobs in an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry.



## iotHubResourceGet

> IotHubDescription iotHubResourceGet(apiVersion, subscriptionId, resourceGroupName, resourceName)

Get the non-security related metadata of an IoT hub.

Get the non-security related metadata of an IoT hub.

### Example

```javascript
import IotHubClient from 'iot_hub_client';

let apiInstance = new IotHubClient.GETApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
let resourceName = "resourceName_example"; // String | The name of the IoT hub.
apiInstance.iotHubResourceGet(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## iotHubResourceGetEventHubConsumerGroup

> EventHubConsumerGroupInfo iotHubResourceGetEventHubConsumerGroup(apiVersion, subscriptionId, resourceGroupName, resourceName, eventHubEndpointName, name)

Get a consumer group from the Event Hub-compatible device-to-cloud endpoint for an IoT hub.

Get a consumer group from the Event Hub-compatible device-to-cloud endpoint for an IoT hub.

### Example

```javascript
import IotHubClient from 'iot_hub_client';

let apiInstance = new IotHubClient.GETApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
let resourceName = "resourceName_example"; // String | The name of the IoT hub.
let eventHubEndpointName = "eventHubEndpointName_example"; // String | The name of the Event Hub-compatible endpoint in the IoT hub.
let name = "name_example"; // String | The name of the consumer group to retrieve.
apiInstance.iotHubResourceGetEventHubConsumerGroup(apiVersion, subscriptionId, resourceGroupName, resourceName, eventHubEndpointName, name, (error, data, response) => {
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
 **name** | **String**| The name of the consumer group to retrieve. | 

### Return type

[**EventHubConsumerGroupInfo**](EventHubConsumerGroupInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## iotHubResourceGetJob

> JobResponse iotHubResourceGetJob(apiVersion, subscriptionId, resourceGroupName, resourceName, jobId)

Get the details of a job from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry.

Get the details of a job from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry.

### Example

```javascript
import IotHubClient from 'iot_hub_client';

let apiInstance = new IotHubClient.GETApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
let resourceName = "resourceName_example"; // String | The name of the IoT hub.
let jobId = "jobId_example"; // String | The job identifier.
apiInstance.iotHubResourceGetJob(apiVersion, subscriptionId, resourceGroupName, resourceName, jobId, (error, data, response) => {
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
 **jobId** | **String**| The job identifier. | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## iotHubResourceGetQuotaMetrics

> IotHubQuotaMetricInfoListResult iotHubResourceGetQuotaMetrics(apiVersion, subscriptionId, resourceGroupName, resourceName)

Get the quota metrics for an IoT hub.

Get the quota metrics for an IoT hub.

### Example

```javascript
import IotHubClient from 'iot_hub_client';

let apiInstance = new IotHubClient.GETApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
let resourceName = "resourceName_example"; // String | The name of the IoT hub.
apiInstance.iotHubResourceGetQuotaMetrics(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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

[**IotHubQuotaMetricInfoListResult**](IotHubQuotaMetricInfoListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## iotHubResourceGetStats

> RegistryStatistics iotHubResourceGetStats(apiVersion, subscriptionId, resourceGroupName, resourceName)

Get the statistics from an IoT hub.

Get the statistics from an IoT hub.

### Example

```javascript
import IotHubClient from 'iot_hub_client';

let apiInstance = new IotHubClient.GETApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
let resourceName = "resourceName_example"; // String | The name of the IoT hub.
apiInstance.iotHubResourceGetStats(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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

[**RegistryStatistics**](RegistryStatistics.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## iotHubResourceGetValidSkus

> IotHubSkuDescriptionListResult iotHubResourceGetValidSkus(apiVersion, subscriptionId, resourceGroupName, resourceName)

Get the list of valid SKUs for an IoT hub.

Get the list of valid SKUs for an IoT hub.

### Example

```javascript
import IotHubClient from 'iot_hub_client';

let apiInstance = new IotHubClient.GETApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
let resourceName = "resourceName_example"; // String | The name of the IoT hub.
apiInstance.iotHubResourceGetValidSkus(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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

[**IotHubSkuDescriptionListResult**](IotHubSkuDescriptionListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## iotHubResourceListByResourceGroup

> IotHubDescriptionListResult iotHubResourceListByResourceGroup(apiVersion, subscriptionId, resourceGroupName)

Get all the IoT hubs in a resource group.

Get all the IoT hubs in a resource group.

### Example

```javascript
import IotHubClient from 'iot_hub_client';

let apiInstance = new IotHubClient.GETApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hubs.
apiInstance.iotHubResourceListByResourceGroup(apiVersion, subscriptionId, resourceGroupName, (error, data, response) => {
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
 **resourceGroupName** | **String**| The name of the resource group that contains the IoT hubs. | 

### Return type

[**IotHubDescriptionListResult**](IotHubDescriptionListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## iotHubResourceListBySubscription

> IotHubDescriptionListResult iotHubResourceListBySubscription(apiVersion, subscriptionId)

Get all the IoT hubs in a subscription.

Get all the IoT hubs in a subscription.

### Example

```javascript
import IotHubClient from 'iot_hub_client';

let apiInstance = new IotHubClient.GETApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
apiInstance.iotHubResourceListBySubscription(apiVersion, subscriptionId, (error, data, response) => {
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

### Return type

[**IotHubDescriptionListResult**](IotHubDescriptionListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## iotHubResourceListEventHubConsumerGroups

> EventHubConsumerGroupsListResult iotHubResourceListEventHubConsumerGroups(apiVersion, subscriptionId, resourceGroupName, resourceName, eventHubEndpointName)

Get a list of the consumer groups in the Event Hub-compatible device-to-cloud endpoint in an IoT hub.

Get a list of the consumer groups in the Event Hub-compatible device-to-cloud endpoint in an IoT hub.

### Example

```javascript
import IotHubClient from 'iot_hub_client';

let apiInstance = new IotHubClient.GETApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
let resourceName = "resourceName_example"; // String | The name of the IoT hub.
let eventHubEndpointName = "eventHubEndpointName_example"; // String | The name of the Event Hub-compatible endpoint.
apiInstance.iotHubResourceListEventHubConsumerGroups(apiVersion, subscriptionId, resourceGroupName, resourceName, eventHubEndpointName, (error, data, response) => {
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
 **eventHubEndpointName** | **String**| The name of the Event Hub-compatible endpoint. | 

### Return type

[**EventHubConsumerGroupsListResult**](EventHubConsumerGroupsListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## iotHubResourceListJobs

> JobResponseListResult iotHubResourceListJobs(apiVersion, subscriptionId, resourceGroupName, resourceName)

Get a list of all the jobs in an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry.

Get a list of all the jobs in an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry.

### Example

```javascript
import IotHubClient from 'iot_hub_client';

let apiInstance = new IotHubClient.GETApi();
let apiVersion = "apiVersion_example"; // String | The version of the API.
let subscriptionId = "subscriptionId_example"; // String | The subscription identifier.
let resourceGroupName = "resourceGroupName_example"; // String | The name of the resource group that contains the IoT hub.
let resourceName = "resourceName_example"; // String | The name of the IoT hub.
apiInstance.iotHubResourceListJobs(apiVersion, subscriptionId, resourceGroupName, resourceName, (error, data, response) => {
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

[**JobResponseListResult**](JobResponseListResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

