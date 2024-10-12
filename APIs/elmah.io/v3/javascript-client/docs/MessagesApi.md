# ElmahIoApi.MessagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**messagesCreate**](MessagesApi.md#messagesCreate) | **POST** /v3/messages/{logId} | Create a new message.
[**messagesCreateBulk**](MessagesApi.md#messagesCreateBulk) | **POST** /v3/messages/{logId}/_bulk | Create one or more new messages.
[**messagesDelete**](MessagesApi.md#messagesDelete) | **DELETE** /v3/messages/{logId}/{id} | Delete a message by its ID.
[**messagesDeleteAll**](MessagesApi.md#messagesDeleteAll) | **DELETE** /v3/messages/{logId} | Deletes a list of messages by logid and query.
[**messagesFix**](MessagesApi.md#messagesFix) | **POST** /v3/messages/{logId}/{id}/_fix | Fix a message by its ID.
[**messagesFixAll**](MessagesApi.md#messagesFixAll) | **POST** /v3/messages/{logId}/_fix | Mark a list of messages as fixed by logid and query.
[**messagesGet**](MessagesApi.md#messagesGet) | **GET** /v3/messages/{logId}/{id} | Fetch a message by its ID.
[**messagesGetAll**](MessagesApi.md#messagesGetAll) | **GET** /v3/messages/{logId} | Fetch messages from a log.
[**messagesHide**](MessagesApi.md#messagesHide) | **POST** /v3/messages/{logId}/{id}/_hide | Hide a message by its ID.



## messagesCreate

> CreateMessageResult messagesCreate(logId, opts)

Create a new message.

Required permission: &#x60;messages_write&#x60;

### Example

```javascript
import ElmahIoApi from 'elmah_io_api';
let defaultClient = ElmahIoApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ElmahIoApi.MessagesApi();
let logId = "logId_example"; // String | The ID of the log which should contain the new message.
let opts = {
  'createMessage': new ElmahIoApi.CreateMessage() // CreateMessage | The message object to create.
};
apiInstance.messagesCreate(logId, opts, (error, data, response) => {
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
 **logId** | **String**| The ID of the log which should contain the new message. | 
 **createMessage** | [**CreateMessage**](CreateMessage.md)| The message object to create. | [optional] 

### Return type

[**CreateMessageResult**](CreateMessageResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## messagesCreateBulk

> [CreateBulkMessageResult] messagesCreateBulk(logId, opts)

Create one or more new messages.

Required permission: &#x60;messages_write&#x60;

### Example

```javascript
import ElmahIoApi from 'elmah_io_api';
let defaultClient = ElmahIoApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ElmahIoApi.MessagesApi();
let logId = "logId_example"; // String | The ID of the log which should contain the new messages.
let opts = {
  'createMessage': [new ElmahIoApi.CreateMessage()] // [CreateMessage] | The messages to create.
};
apiInstance.messagesCreateBulk(logId, opts, (error, data, response) => {
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
 **logId** | **String**| The ID of the log which should contain the new messages. | 
 **createMessage** | [**[CreateMessage]**](CreateMessage.md)| The messages to create. | [optional] 

### Return type

[**[CreateBulkMessageResult]**](CreateBulkMessageResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## messagesDelete

> messagesDelete(id, logId)

Delete a message by its ID.

Required permission: &#x60;messages_delete&#x60;

### Example

```javascript
import ElmahIoApi from 'elmah_io_api';
let defaultClient = ElmahIoApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ElmahIoApi.MessagesApi();
let id = "id_example"; // String | The ID of the message to delete.
let logId = "logId_example"; // String | The ID of the log containing the message.
apiInstance.messagesDelete(id, logId, (error, data, response) => {
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
 **id** | **String**| The ID of the message to delete. | 
 **logId** | **String**| The ID of the log containing the message. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## messagesDeleteAll

> messagesDeleteAll(logId, opts)

Deletes a list of messages by logid and query.

Required permission: &#x60;messages_delete&#x60;

### Example

```javascript
import ElmahIoApi from 'elmah_io_api';
let defaultClient = ElmahIoApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ElmahIoApi.MessagesApi();
let logId = "logId_example"; // String | The ID of the log containing the message.
let opts = {
  'search': new ElmahIoApi.Search() // Search | A search object containing query, time filters etc.
};
apiInstance.messagesDeleteAll(logId, opts, (error, data, response) => {
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
 **logId** | **String**| The ID of the log containing the message. | 
 **search** | [**Search**](Search.md)| A search object containing query, time filters etc. | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: Not defined


## messagesFix

> messagesFix(id, logId, opts)

Fix a message by its ID.

Required permission: &#x60;messages_write&#x60;

### Example

```javascript
import ElmahIoApi from 'elmah_io_api';
let defaultClient = ElmahIoApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ElmahIoApi.MessagesApi();
let id = "id_example"; // String | The ID of the message to fix.
let logId = "logId_example"; // String | The ID of the log containing the message.
let opts = {
  'markAllAsFixed': false // Boolean | If set to true, all instances of the log message are set to fixed.
};
apiInstance.messagesFix(id, logId, opts, (error, data, response) => {
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
 **id** | **String**| The ID of the message to fix. | 
 **logId** | **String**| The ID of the log containing the message. | 
 **markAllAsFixed** | **Boolean**| If set to true, all instances of the log message are set to fixed. | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## messagesFixAll

> messagesFixAll(logId, opts)

Mark a list of messages as fixed by logid and query.

Required permission: &#x60;messages_write&#x60;

### Example

```javascript
import ElmahIoApi from 'elmah_io_api';
let defaultClient = ElmahIoApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ElmahIoApi.MessagesApi();
let logId = "logId_example"; // String | The ID of the log containing the messages.
let opts = {
  'search': new ElmahIoApi.Search() // Search | A search object containing query, time filters etc.
};
apiInstance.messagesFixAll(logId, opts, (error, data, response) => {
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
 **logId** | **String**| The ID of the log containing the messages. | 
 **search** | [**Search**](Search.md)| A search object containing query, time filters etc. | [optional] 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: Not defined


## messagesGet

> Message messagesGet(id, logId)

Fetch a message by its ID.

Required permission: &#x60;messages_read&#x60;

### Example

```javascript
import ElmahIoApi from 'elmah_io_api';
let defaultClient = ElmahIoApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ElmahIoApi.MessagesApi();
let id = "id_example"; // String | The ID of the message to fetch.
let logId = "logId_example"; // String | The ID of the log containing the message.
apiInstance.messagesGet(id, logId, (error, data, response) => {
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
 **id** | **String**| The ID of the message to fetch. | 
 **logId** | **String**| The ID of the log containing the message. | 

### Return type

[**Message**](Message.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## messagesGetAll

> MessagesResult messagesGetAll(logId, opts)

Fetch messages from a log.

Required permission: &#x60;messages_read&#x60;

### Example

```javascript
import ElmahIoApi from 'elmah_io_api';
let defaultClient = ElmahIoApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ElmahIoApi.MessagesApi();
let logId = "logId_example"; // String | The ID of the log containing the messages.
let opts = {
  'pageIndex': 0, // Number | The page number of the result.
  'pageSize': 15, // Number | The number of messages to load (max 100) or 15 if not set.
  'query': "query_example", // String | A full-text or Lucene query to limit the messages by.
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | A start date and time to search from (not included).
  'to': new Date("2013-10-20T19:20:30+01:00"), // Date | An end date and time to search to (not included).
  'includeHeaders': false // Boolean | Include headers like server variables and cookies in the result (slower).
};
apiInstance.messagesGetAll(logId, opts, (error, data, response) => {
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
 **logId** | **String**| The ID of the log containing the messages. | 
 **pageIndex** | **Number**| The page number of the result. | [optional] [default to 0]
 **pageSize** | **Number**| The number of messages to load (max 100) or 15 if not set. | [optional] [default to 15]
 **query** | **String**| A full-text or Lucene query to limit the messages by. | [optional] 
 **from** | **Date**| A start date and time to search from (not included). | [optional] 
 **to** | **Date**| An end date and time to search to (not included). | [optional] 
 **includeHeaders** | **Boolean**| Include headers like server variables and cookies in the result (slower). | [optional] [default to false]

### Return type

[**MessagesResult**](MessagesResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## messagesHide

> messagesHide(id, logId)

Hide a message by its ID.

Required permission: &#x60;messages_write&#x60;

### Example

```javascript
import ElmahIoApi from 'elmah_io_api';
let defaultClient = ElmahIoApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';

let apiInstance = new ElmahIoApi.MessagesApi();
let id = "id_example"; // String | The ID of the message to hide.
let logId = "logId_example"; // String | The ID of the log containing the message.
apiInstance.messagesHide(id, logId, (error, data, response) => {
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
 **id** | **String**| The ID of the message to hide. | 
 **logId** | **String**| The ID of the log containing the message. | 

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

