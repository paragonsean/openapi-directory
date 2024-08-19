# SvixApi.MessageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createMessageApiV1AppAppIdMsgPost**](MessageApi.md#createMessageApiV1AppAppIdMsgPost) | **POST** /api/v1/app/{app_id}/msg/ | Create Message
[**expungeMessagePayloadApiV1AppAppIdMsgMsgIdContentDelete**](MessageApi.md#expungeMessagePayloadApiV1AppAppIdMsgMsgIdContentDelete) | **DELETE** /api/v1/app/{app_id}/msg/{msg_id}/content/ | Delete message payload
[**getMessageApiV1AppAppIdMsgMsgIdGet**](MessageApi.md#getMessageApiV1AppAppIdMsgMsgIdGet) | **GET** /api/v1/app/{app_id}/msg/{msg_id}/ | Get Message
[**listMessagesApiV1AppAppIdMsgGet**](MessageApi.md#listMessagesApiV1AppAppIdMsgGet) | **GET** /api/v1/app/{app_id}/msg/ | List Messages



## createMessageApiV1AppAppIdMsgPost

> MessageOut createMessageApiV1AppAppIdMsgPost(appId, messageIn, opts)

Create Message

Creates a new message and dispatches it to all of the application&#39;s endpoints.  The &#x60;eventId&#x60; is an optional custom unique ID. It&#39;s verified to be unique only up to a day, after that no verification will be made. If a message with the same &#x60;eventId&#x60; already exists for any application in your environment, a 409 conflict error will be returned.  The &#x60;eventType&#x60; indicates the type and schema of the event. All messages of a certain &#x60;eventType&#x60; are expected to have the same schema. Endpoints can choose to only listen to specific event types. Messages can also have &#x60;channels&#x60;, which similar to event types let endpoints filter by them. Unlike event types, messages can have multiple channels, and channels don&#39;t imply a specific message content or schema.  The &#x60;payload&#x60; property is the webhook&#39;s body (the actual webhook message). Svix supports payload sizes of up to ~350kb, though it&#39;s generally a good idea to keep webhook payloads small, probably no larger than 40kb.  The optional &#x60;application&#x60; property will be used to create an application if the application referenced in the path does not exist. If it does then this property is ignored.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.MessageApi();
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let messageIn = new SvixApi.MessageIn(); // MessageIn | 
let opts = {
  'withContent': true, // Boolean | 
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.createMessageApiV1AppAppIdMsgPost(appId, messageIn, opts, (error, data, response) => {
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
 **messageIn** | [**MessageIn**](MessageIn.md)|  | 
 **withContent** | **Boolean**|  | [optional] [default to true]
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**MessageOut**](MessageOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## expungeMessagePayloadApiV1AppAppIdMsgMsgIdContentDelete

> expungeMessagePayloadApiV1AppAppIdMsgMsgIdContentDelete(msgId, appId, opts)

Delete message payload

Delete the given message&#39;s payload. Useful in cases when a message was accidentally sent with sensitive content.  The message can&#39;t be replayed or resent once its payload has been deleted or expired.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.MessageApi();
let msgId = "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.expungeMessagePayloadApiV1AppAppIdMsgMsgIdContentDelete(msgId, appId, opts, (error, data, response) => {
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


## getMessageApiV1AppAppIdMsgMsgIdGet

> MessageOut getMessageApiV1AppAppIdMsgMsgIdGet(msgId, appId, opts)

Get Message

Get a message by its ID or eventID.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.MessageApi();
let msgId = "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.getMessageApiV1AppAppIdMsgMsgIdGet(msgId, appId, opts, (error, data, response) => {
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
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**MessageOut**](MessageOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMessagesApiV1AppAppIdMsgGet

> ListResponseMessageOut listMessagesApiV1AppAppIdMsgGet(appId, opts)

List Messages

List all of the application&#39;s messages.  The &#x60;before&#x60; parameter lets you filter all items created before a certain date and is ignored if an iterator is passed. The &#x60;after&#x60; parameter lets you filter all items created after a certain date and is ignored if an iterator is passed. &#x60;before&#x60; and &#x60;after&#x60; cannot be used simultaneously.

### Example

```javascript
import SvixApi from 'svix_api';
let defaultClient = SvixApi.ApiClient.instance;
// Configure Bearer access token for authorization: HTTPBearer
let HTTPBearer = defaultClient.authentications['HTTPBearer'];
HTTPBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SvixApi.MessageApi();
let appId = "app_1srOrx2ZWZBpBUvZwXKQmoEYga2"; // String | 
let opts = {
  'iterator': "msg_1srOrx2ZWZBpBUvZwXKQmoEYga2", // String | 
  'limit': 50, // Number | 
  'eventTypes': ["user.signup"], // [String] | 
  'channel': "project_1337", // String | 
  'before': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'after': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'idempotencyKey': "idempotencyKey_example" // String | The request's idempotency key
};
apiInstance.listMessagesApiV1AppAppIdMsgGet(appId, opts, (error, data, response) => {
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
 **iterator** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 50]
 **eventTypes** | [**[String]**](String.md)|  | [optional] 
 **channel** | **String**|  | [optional] 
 **before** | **Date**|  | [optional] 
 **after** | **Date**|  | [optional] 
 **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] 

### Return type

[**ListResponseMessageOut**](ListResponseMessageOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

