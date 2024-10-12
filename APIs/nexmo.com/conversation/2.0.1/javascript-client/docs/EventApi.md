# ConversationApi.EventApi

All URIs are relative to *https://api.nexmo.com/v0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createEvent**](EventApi.md#createEvent) | **POST** /conversations/{conversation_id}/events | Create an event
[**deleteEvent**](EventApi.md#deleteEvent) | **DELETE** /conversations/{conversation_id}/events/{event_id} | Delete an event
[**getEvent**](EventApi.md#getEvent) | **GET** /conversations/{conversation_id}/events/{event_id} | Retrieve an event
[**getEvents**](EventApi.md#getEvents) | **GET** /conversations/{conversation_id}/events | List events



## createEvent

> CreateEvent201Response createEvent(conversationId, opts)

Create an event

### Example

```javascript
import ConversationApi from 'conversation_api';
let defaultClient = ConversationApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ConversationApi.EventApi();
let conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
let opts = {
  'createEventRequest': new ConversationApi.CreateEventRequest() // CreateEventRequest | 
};
apiInstance.createEvent(conversationId, opts, (error, data, response) => {
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
 **conversationId** | **String**| Conversation ID | 
 **createEventRequest** | [**CreateEventRequest**](CreateEventRequest.md)|  | [optional] 

### Return type

[**CreateEvent201Response**](CreateEvent201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteEvent

> Object deleteEvent(conversationId, eventId)

Delete an event

### Example

```javascript
import ConversationApi from 'conversation_api';
let defaultClient = ConversationApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ConversationApi.EventApi();
let conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
let eventId = "eventId_example"; // String | Event ID
apiInstance.deleteEvent(conversationId, eventId, (error, data, response) => {
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
 **conversationId** | **String**| Conversation ID | 
 **eventId** | **String**| Event ID | 

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEvent

> EventRetrieved getEvent(conversationId, eventId)

Retrieve an event

### Example

```javascript
import ConversationApi from 'conversation_api';
let defaultClient = ConversationApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ConversationApi.EventApi();
let conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
let eventId = "eventId_example"; // String | Event ID
apiInstance.getEvent(conversationId, eventId, (error, data, response) => {
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
 **conversationId** | **String**| Conversation ID | 
 **eventId** | **String**| Event ID | 

### Return type

[**EventRetrieved**](EventRetrieved.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEvents

> [EventRetrieved] getEvents(conversationId)

List events

This endpoint is **DEPRECATED**. Please use [/v0.2/events](/api/conversation.v2#get-events).

### Example

```javascript
import ConversationApi from 'conversation_api';
let defaultClient = ConversationApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ConversationApi.EventApi();
let conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
apiInstance.getEvents(conversationId, (error, data, response) => {
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
 **conversationId** | **String**| Conversation ID | 

### Return type

[**[EventRetrieved]**](EventRetrieved.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

