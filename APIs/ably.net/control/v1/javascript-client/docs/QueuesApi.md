# ApiV1.QueuesApi

All URIs are relative to *https://control.ably.net/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appsAppIdQueuesGet**](QueuesApi.md#appsAppIdQueuesGet) | **GET** /apps/{app_id}/queues | Lists queues
[**appsAppIdQueuesPost**](QueuesApi.md#appsAppIdQueuesPost) | **POST** /apps/{app_id}/queues | Creates a queue
[**appsAppIdQueuesQueueIdDelete**](QueuesApi.md#appsAppIdQueuesQueueIdDelete) | **DELETE** /apps/{app_id}/queues/{queue_id} | Deletes a queue



## appsAppIdQueuesGet

> [QueueResponse] appsAppIdQueuesGet(appId)

Lists queues

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiV1.QueuesApi();
let appId = "appId_example"; // String | 
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
 **appId** | **String**|  | 

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

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiV1.QueuesApi();
let appId = "appId_example"; // String | 
let opts = {
  'queue': new ApiV1.Queue() // Queue | 
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
 **appId** | **String**|  | 
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

### Example

```javascript
import ApiV1 from 'api_v1';
let defaultClient = ApiV1.ApiClient.instance;
// Configure Bearer access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiV1.QueuesApi();
let appId = "appId_example"; // String | 
let queueId = "queueId_example"; // String | 
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
 **appId** | **String**|  | 
 **queueId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

