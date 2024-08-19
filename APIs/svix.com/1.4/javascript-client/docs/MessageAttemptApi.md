# SvixApi.MessageAttemptApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**expungeAttemptContentApiV1AppAppIdMsgMsgIdAttemptAttemptIdContentDelete**](MessageAttemptApi.md#expungeAttemptContentApiV1AppAppIdMsgMsgIdAttemptAttemptIdContentDelete) | **DELETE** /api/v1/app/{app_id}/msg/{msg_id}/attempt/{attempt_id}/content/ | Delete attempt response body
[**getAttemptApiV1AppAppIdMsgMsgIdAttemptAttemptIdGet**](MessageAttemptApi.md#getAttemptApiV1AppAppIdMsgMsgIdAttemptAttemptIdGet) | **GET** /api/v1/app/{app_id}/msg/{msg_id}/attempt/{attempt_id}/ | Get Attempt
[**listAttemptedDestinationsApiV1AppAppIdMsgMsgIdEndpointGet**](MessageAttemptApi.md#listAttemptedDestinationsApiV1AppAppIdMsgMsgIdEndpointGet) | **GET** /api/v1/app/{app_id}/msg/{msg_id}/endpoint/ | List Attempted Destinations
[**listAttemptedMessagesApiV1AppAppIdEndpointEndpointIdMsgGet**](MessageAttemptApi.md#listAttemptedMessagesApiV1AppAppIdEndpointEndpointIdMsgGet) | **GET** /api/v1/app/{app_id}/endpoint/{endpoint_id}/msg/ | List Attempted Messages
[**listAttemptsApiV1AppAppIdMsgMsgIdAttemptGet**](MessageAttemptApi.md#listAttemptsApiV1AppAppIdMsgMsgIdAttemptGet) | **GET** /api/v1/app/{app_id}/msg/{msg_id}/attempt/ | List Attempts
[**listAttemptsByEndpointApiV1AppAppIdAttemptEndpointEndpointIdGet**](MessageAttemptApi.md#listAttemptsByEndpointApiV1AppAppIdAttemptEndpointEndpointIdGet) | **GET** /api/v1/app/{app_id}/attempt/endpoint/{endpoint_id}/ | List Attempts By Endpoint
[**listAttemptsByMsgApiV1AppAppIdAttemptMsgMsgIdGet**](MessageAttemptApi.md#listAttemptsByMsgApiV1AppAppIdAttemptMsgMsgIdGet) | **GET** /api/v1/app/{app_id}/attempt/msg/{msg_id}/ | List Attempts By Msg
[**listAttemptsForEndpointApiV1AppAppIdMsgMsgIdEndpointEndpointIdAttemptGet**](MessageAttemptApi.md#listAttemptsForEndpointApiV1AppAppIdMsgMsgIdEndpointEndpointIdAttemptGet) | **GET** /api/v1/app/{app_id}/msg/{msg_id}/endpoint/{endpoint_id}/attempt/ | List Attempts For Endpoint
[**resendWebhookApiV1AppAppIdMsgMsgIdEndpointEndpointIdResendPost**](MessageAttemptApi.md#resendWebhookApiV1AppAppIdMsgMsgIdEndpointEndpointIdResendPost) | **POST** /api/v1/app/{app_id}/msg/{msg_id}/endpoint/{endpoint_id}/resend/ | Resend Webhook



## expungeAttemptContentApiV1AppAppIdMsgMsgIdAttemptAttemptIdContentDelete

> expungeAttemptContentApiV1AppAppIdMsgMsgIdAttemptAttemptIdContentDelete(attemptId, msgId, appId, opts)

Delete attempt response body

Deletes the given attempt&#39;s response body. Useful when an endpoint accidentally returned sensitive content.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.MessageAttemptApi();
let attemptId = "atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let msgId = "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.expungeAttemptContentApiV1AppAppIdMsgMsgIdAttemptAttemptIdContentDelete(attemptId, msgId, appId, opts, (error, data, response) => {
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
 **attemptId** | **String**|  | 
 **msgId** | **String**|  | 
 **appId** | **String**|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

null (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAttemptApiV1AppAppIdMsgMsgIdAttemptAttemptIdGet

> MessageAttemptOut getAttemptApiV1AppAppIdMsgMsgIdAttemptAttemptIdGet(attemptId, msgId, appId, opts)

Get Attempt

&#x60;msg_id&#x60;: Use a message id or a message &#x60;eventId&#x60;

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.MessageAttemptApi();
let attemptId = "atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let msgId = "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.getAttemptApiV1AppAppIdMsgMsgIdAttemptAttemptIdGet(attemptId, msgId, appId, opts, (error, data, response) => {
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
 **attemptId** | **String**|  | 
 **msgId** | **String**|  | 
 **appId** | **String**|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**MessageAttemptOut**](MessageAttemptOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAttemptedDestinationsApiV1AppAppIdMsgMsgIdEndpointGet

> ListResponseMessageEndpointOut listAttemptedDestinationsApiV1AppAppIdMsgMsgIdEndpointGet(msgId, appId, opts)

List Attempted Destinations

&#x60;msg_id&#x60;: Use a message id or a message &#x60;eventId&#x60;

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.MessageAttemptApi();
let msgId = "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'iterator': "msgep_1srOrx2ZWZBpBUvZwXKQmoEYga2", // String | 
  'limit': 50, // Number | 
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.listAttemptedDestinationsApiV1AppAppIdMsgMsgIdEndpointGet(msgId, appId, opts, (error, data, response) => {
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
 **msgId** | **String**|  | 
 **appId** | **String**|  | 
 **iterator** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 50]
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**ListResponseMessageEndpointOut**](ListResponseMessageEndpointOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAttemptedMessagesApiV1AppAppIdEndpointEndpointIdMsgGet

> ListResponseEndpointMessageOut listAttemptedMessagesApiV1AppAppIdEndpointEndpointIdMsgGet(endpointId, appId, opts)

List Attempted Messages

List messages for a particular endpoint. Additionally includes metadata about the latest message attempt.  The &#x60;before&#x60; parameter lets you filter all items created before a certain date and is ignored if an iterator is passed.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.MessageAttemptApi();
let endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'iterator': "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2", // String | 
  'limit': 50, // Number | 
  'channel': "project_1337", // String | 
  'status': new SvixApi.MessageStatus(), // MessageStatus | 
  'before': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'after': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.listAttemptedMessagesApiV1AppAppIdEndpointEndpointIdMsgGet(endpointId, appId, opts, (error, data, response) => {
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
 **endpointId** | **String**|  | 
 **appId** | **String**|  | 
 **iterator** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 50]
 **channel** | **String**|  | [optional] 
 **status** | [**MessageStatus**](.md)|  | [optional] 
 **before** | **Date**|  | [optional] 
 **after** | **Date**|  | [optional] 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**ListResponseEndpointMessageOut**](ListResponseEndpointMessageOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAttemptsApiV1AppAppIdMsgMsgIdAttemptGet

> ListResponseMessageAttemptOut listAttemptsApiV1AppAppIdMsgMsgIdAttemptGet(appId, msgId, opts)

List Attempts

Deprecated: Please use \&quot;List Attempts by Endpoint\&quot; and \&quot;List Attempts by Msg\&quot; instead.  &#x60;msg_id&#x60;: Use a message id or a message &#x60;eventId&#x60;

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.MessageAttemptApi();
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let msgId = "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'iterator': "atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2", // String | 
  'limit': 50, // Number | 
  'endpointId': "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2", // String | 
  'eventTypes': ["user.signup"], // [String] | 
  'channel': "project_1337", // String | 
  'status': new SvixApi.MessageStatus(), // MessageStatus | 
  'before': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'after': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.listAttemptsApiV1AppAppIdMsgMsgIdAttemptGet(appId, msgId, opts, (error, data, response) => {
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
 **msgId** | **String**|  | 
 **iterator** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 50]
 **endpointId** | **String**|  | [optional] 
 **eventTypes** | [**[String]**](String.md)|  | [optional] 
 **channel** | **String**|  | [optional] 
 **status** | [**MessageStatus**](.md)|  | [optional] 
 **before** | **Date**|  | [optional] 
 **after** | **Date**|  | [optional] 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**ListResponseMessageAttemptOut**](ListResponseMessageAttemptOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAttemptsByEndpointApiV1AppAppIdAttemptEndpointEndpointIdGet

> ListResponseMessageAttemptOut listAttemptsByEndpointApiV1AppAppIdAttemptEndpointEndpointIdGet(appId, endpointId, opts)

List Attempts By Endpoint

List attempts by endpoint id

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.MessageAttemptApi();
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'iterator': "atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2", // String | 
  'limit': 50, // Number | 
  'status': new SvixApi.MessageStatus(), // MessageStatus | 
  'statusCodeClass': new SvixApi.StatusCodeClass(), // StatusCodeClass | 
  'eventTypes': ["user.signup"], // [String] | 
  'channel': "project_1337", // String | 
  'before': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'after': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.listAttemptsByEndpointApiV1AppAppIdAttemptEndpointEndpointIdGet(appId, endpointId, opts, (error, data, response) => {
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
 **endpointId** | **String**|  | 
 **iterator** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 50]
 **status** | [**MessageStatus**](.md)|  | [optional] 
 **statusCodeClass** | [**StatusCodeClass**](.md)|  | [optional] 
 **eventTypes** | [**[String]**](String.md)|  | [optional] 
 **channel** | **String**|  | [optional] 
 **before** | **Date**|  | [optional] 
 **after** | **Date**|  | [optional] 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**ListResponseMessageAttemptOut**](ListResponseMessageAttemptOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAttemptsByMsgApiV1AppAppIdAttemptMsgMsgIdGet

> ListResponseMessageAttemptOut listAttemptsByMsgApiV1AppAppIdAttemptMsgMsgIdGet(appId, msgId, opts)

List Attempts By Msg

List attempts by message id

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.MessageAttemptApi();
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let msgId = "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'endpointId': "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2", // String | 
  'iterator': "atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2", // String | 
  'limit': 50, // Number | 
  'status': new SvixApi.MessageStatus(), // MessageStatus | 
  'statusCodeClass': new SvixApi.StatusCodeClass(), // StatusCodeClass | 
  'eventTypes': ["user.signup"], // [String] | 
  'channel': "project_1337", // String | 
  'before': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'after': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.listAttemptsByMsgApiV1AppAppIdAttemptMsgMsgIdGet(appId, msgId, opts, (error, data, response) => {
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
 **msgId** | **String**|  | 
 **endpointId** | **String**|  | [optional] 
 **iterator** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 50]
 **status** | [**MessageStatus**](.md)|  | [optional] 
 **statusCodeClass** | [**StatusCodeClass**](.md)|  | [optional] 
 **eventTypes** | [**[String]**](String.md)|  | [optional] 
 **channel** | **String**|  | [optional] 
 **before** | **Date**|  | [optional] 
 **after** | **Date**|  | [optional] 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**ListResponseMessageAttemptOut**](ListResponseMessageAttemptOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAttemptsForEndpointApiV1AppAppIdMsgMsgIdEndpointEndpointIdAttemptGet

> ListResponseMessageAttemptEndpointOut listAttemptsForEndpointApiV1AppAppIdMsgMsgIdEndpointEndpointIdAttemptGet(msgId, appId, endpointId, opts)

List Attempts For Endpoint

DEPRECATED: please use list_attempts with endpoint_id as a query parameter instead.  List the message attempts for a particular endpoint.  Returning the endpoint.  The &#x60;before&#x60; parameter lets you filter all items created before a certain date and is ignored if an iterator is passed.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.MessageAttemptApi();
let msgId = "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'iterator': "atmpt_1srOrx2ZWZBpBUvZwXKQmoEYga2", // String | 
  'limit': 50, // Number | 
  'eventTypes': ["user.signup"], // [String] | 
  'channel': "project_1337", // String | 
  'status': new SvixApi.MessageStatus(), // MessageStatus | 
  'before': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'after': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.listAttemptsForEndpointApiV1AppAppIdMsgMsgIdEndpointEndpointIdAttemptGet(msgId, appId, endpointId, opts, (error, data, response) => {
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
 **msgId** | **String**|  | 
 **appId** | **String**|  | 
 **endpointId** | **String**|  | 
 **iterator** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 50]
 **eventTypes** | [**[String]**](String.md)|  | [optional] 
 **channel** | **String**|  | [optional] 
 **status** | [**MessageStatus**](.md)|  | [optional] 
 **before** | **Date**|  | [optional] 
 **after** | **Date**|  | [optional] 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**ListResponseMessageAttemptEndpointOut**](ListResponseMessageAttemptEndpointOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## resendWebhookApiV1AppAppIdMsgMsgIdEndpointEndpointIdResendPost

> resendWebhookApiV1AppAppIdMsgMsgIdEndpointEndpointIdResendPost(endpointId, msgId, appId, opts)

Resend Webhook

Resend a message to the specified endpoint.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.MessageAttemptApi();
let endpointId = "ep_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let msgId = "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.resendWebhookApiV1AppAppIdMsgMsgIdEndpointEndpointIdResendPost(endpointId, msgId, appId, opts, (error, data, response) => {
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
 **endpointId** | **String**|  | 
 **msgId** | **String**|  | 
 **appId** | **String**|  | 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

null (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

