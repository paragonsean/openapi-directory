# Qakka.QueuesApi

All URIs are relative to *https://apache.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ackMessage**](QueuesApi.md#ackMessage) | **DELETE** /queues/{queueName}/messages/{queueMessageId} | Acknowledge that Queue Message has been processed.
[**createQueue**](QueuesApi.md#createQueue) | **POST** /queues | Create new queue.
[**deleteQueue**](QueuesApi.md#deleteQueue) | **DELETE** /queues/{queueName} | Delete Queue.
[**getListOfQueues**](QueuesApi.md#getListOfQueues) | **GET** /queues | Get list of all Queues.
[**getMessageData**](QueuesApi.md#getMessageData) | **GET** /queues/{queueName}/data/{queueMessageId} | Get data associated with a Queue Message.
[**getNextMessages**](QueuesApi.md#getNextMessages) | **GET** /queues/{queueName}/messages | Get next Queue Messages from a Queue
[**getQueueConfig**](QueuesApi.md#getQueueConfig) | **GET** /queues/{queueName}/config | Get Queue config.
[**sendMessageBinary**](QueuesApi.md#sendMessageBinary) | **POST** /queues/{queueName}/messages | Send Queue Message with a binary data (blob) payload.
[**updateQueueConfig**](QueuesApi.md#updateQueueConfig) | **PUT** /queues/{queueName}/config | Update Queue configuration.



## ackMessage

> ApiResponse ackMessage(queueName, queueMessageId)

Acknowledge that Queue Message has been processed.



### Example

```javascript
import Qakka from 'qakka';

let apiInstance = new Qakka.QueuesApi();
let queueName = "queueName_example"; // String | Name of Queue
let queueMessageId = "queueMessageId_example"; // String | ID of Queue Message to be acknowledged
apiInstance.ackMessage(queueName, queueMessageId, (error, data, response) => {
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
 **queueName** | **String**| Name of Queue | 
 **queueMessageId** | **String**| ID of Queue Message to be acknowledged | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createQueue

> ApiResponse createQueue()

Create new queue.



### Example

```javascript
import Qakka from 'qakka';

let apiInstance = new Qakka.QueuesApi();
apiInstance.createQueue((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteQueue

> ApiResponse deleteQueue(queueName, opts)

Delete Queue.



### Example

```javascript
import Qakka from 'qakka';

let apiInstance = new Qakka.QueuesApi();
let queueName = "queueName_example"; // String | 
let opts = {
  'confirm': false // Boolean | 
};
apiInstance.deleteQueue(queueName, opts, (error, data, response) => {
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
 **queueName** | **String**|  | 
 **confirm** | **Boolean**|  | [optional] [default to false]

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getListOfQueues

> ApiResponse getListOfQueues()

Get list of all Queues.



### Example

```javascript
import Qakka from 'qakka';

let apiInstance = new Qakka.QueuesApi();
apiInstance.getListOfQueues((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMessageData

> ApiResponse getMessageData(queueName, queueMessageId)

Get data associated with a Queue Message.



### Example

```javascript
import Qakka from 'qakka';

let apiInstance = new Qakka.QueuesApi();
let queueName = "queueName_example"; // String | Name of Queue
let queueMessageId = "queueMessageId_example"; // String | ID of Queue Message for which data is to be returned
apiInstance.getMessageData(queueName, queueMessageId, (error, data, response) => {
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
 **queueName** | **String**| Name of Queue | 
 **queueMessageId** | **String**| ID of Queue Message for which data is to be returned | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getNextMessages

> ApiResponse getNextMessages(queueName, opts)

Get next Queue Messages from a Queue



### Example

```javascript
import Qakka from 'qakka';

let apiInstance = new Qakka.QueuesApi();
let queueName = "queueName_example"; // String | Name of Queue
let opts = {
  'count': "'1'" // String | Number of messages to get
};
apiInstance.getNextMessages(queueName, opts, (error, data, response) => {
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
 **queueName** | **String**| Name of Queue | 
 **count** | **String**| Number of messages to get | [optional] [default to &#39;1&#39;]

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getQueueConfig

> ApiResponse getQueueConfig(queueName)

Get Queue config.



### Example

```javascript
import Qakka from 'qakka';

let apiInstance = new Qakka.QueuesApi();
let queueName = "queueName_example"; // String | Name of Queue
apiInstance.getQueueConfig(queueName, (error, data, response) => {
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
 **queueName** | **String**| Name of Queue | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sendMessageBinary

> ApiResponse sendMessageBinary(queueName, contentType, requestBody, opts)

Send Queue Message with a binary data (blob) payload.



### Example

```javascript
import Qakka from 'qakka';

let apiInstance = new Qakka.QueuesApi();
let queueName = "queueName_example"; // String | Name of Queue
let contentType = "contentType_example"; // String | Content type of the data to be sent with Queue Message
let requestBody = [null]; // [Blob] | Data to be send with Queue Message
let opts = {
  'regions': "regions_example", // String | Regions to which message is to be sent
  'delay': "delay_example", // String | 
  'expiration': "expiration_example" // String | 
};
apiInstance.sendMessageBinary(queueName, contentType, requestBody, opts, (error, data, response) => {
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
 **queueName** | **String**| Name of Queue | 
 **contentType** | **String**| Content type of the data to be sent with Queue Message | 
 **requestBody** | [**[Blob]**](Blob.md)| Data to be send with Queue Message | 
 **regions** | **String**| Regions to which message is to be sent | [optional] 
 **delay** | **String**|  | [optional] 
 **expiration** | **String**|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json


## updateQueueConfig

> ApiResponse updateQueueConfig(queueName)

Update Queue configuration.



### Example

```javascript
import Qakka from 'qakka';

let apiInstance = new Qakka.QueuesApi();
let queueName = "queueName_example"; // String | 
apiInstance.updateQueueConfig(queueName, (error, data, response) => {
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
 **queueName** | **String**|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

