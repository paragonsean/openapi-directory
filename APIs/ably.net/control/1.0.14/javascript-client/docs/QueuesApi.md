# ControlApiV1.QueuesApi

All URIs are relative to *https://control.ably.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appsAppIdQueuesGet**](QueuesApi.md#appsAppIdQueuesGet) | **GET** /apps/{app_id}/queues | Lists queues
[**appsAppIdQueuesPost**](QueuesApi.md#appsAppIdQueuesPost) | **POST** /apps/{app_id}/queues | Creates a queue
[**appsAppIdQueuesQueueIdDelete**](QueuesApi.md#appsAppIdQueuesQueueIdDelete) | **DELETE** /apps/{app_id}/queues/{queue_id} | Deletes a queue



## appsAppIdQueuesGet

> [QueueResponse] appsAppIdQueuesGet(appId)

Lists queues

Lists the queues associated with the specified application ID.

### Example

```javascript
import ControlApiV1 from 'control_api_v1';
let defaultClient = ControlApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ControlApiV1.QueuesApi();
let appId = "appId_example"; // String | The application ID.
apiInstance.appsAppIdQueuesGet(appId, (error, data, response) => {
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
 **appId** | **String**| The application ID. | 

### Return type

[**[QueueResponse]**](QueueResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsAppIdQueuesPost

> QueueResponse appsAppIdQueuesPost(appId, opts)

Creates a queue

Creates a queue for the application specified by application ID. The properties for the queue to be created are specified in the request body.

### Example

```javascript
import ControlApiV1 from 'control_api_v1';
let defaultClient = ControlApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ControlApiV1.QueuesApi();
let appId = "appId_example"; // String | The application ID.
let opts = {
  'queue': new ControlApiV1.Queue() // Queue | 
};
apiInstance.appsAppIdQueuesPost(appId, opts, (error, data, response) => {
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
 **appId** | **String**| The application ID. | 
 **queue** | [**Queue**](Queue.md)|  | [optional] 

### Return type

[**QueueResponse**](QueueResponse.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsAppIdQueuesQueueIdDelete

> appsAppIdQueuesQueueIdDelete(appId, queueId)

Deletes a queue

Delete the queue with the specified queue name, from the application with the specified application ID.

### Example

```javascript
import ControlApiV1 from 'control_api_v1';
let defaultClient = ControlApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ControlApiV1.QueuesApi();
let appId = "appId_example"; // String | The application ID.
let queueId = "queueId_example"; // String | The queue ID.
apiInstance.appsAppIdQueuesQueueIdDelete(appId, queueId, (error, data, response) => {
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
 **appId** | **String**| The application ID. | 
 **queueId** | **String**| The queue ID. | 

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

