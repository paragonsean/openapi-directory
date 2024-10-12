# ConversationApi.ConversationApi

All URIs are relative to *https://api.nexmo.com/v0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createConversation**](ConversationApi.md#createConversation) | **POST** /conversations | Create a conversation
[**deleteConversation**](ConversationApi.md#deleteConversation) | **DELETE** /conversations/{conversation_id} | Delete a conversation
[**listConversations**](ConversationApi.md#listConversations) | **GET** /conversations | List conversations
[**recordConversation**](ConversationApi.md#recordConversation) | **PUT** /conversations/{conversation_id}/record | Record a conversation
[**replaceConversation**](ConversationApi.md#replaceConversation) | **PUT** /conversations/{conversation_id} | Update a conversation
[**retrieveConversation**](ConversationApi.md#retrieveConversation) | **GET** /conversations/{conversation_id} | Retrieve a conversation



## createConversation

> CreateConversation200Response createConversation(opts)

Create a conversation

### Example

```javascript
import ConversationApi from 'conversation_api';
let defaultClient = ConversationApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ConversationApi.ConversationApi();
let opts = {
  'createConversationRequest': new ConversationApi.CreateConversationRequest() // CreateConversationRequest | Conversation Request Payload Object
};
apiInstance.createConversation(opts, (error, data, response) => {
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
 **createConversationRequest** | [**CreateConversationRequest**](CreateConversationRequest.md)| Conversation Request Payload Object | [optional] 

### Return type

[**CreateConversation200Response**](CreateConversation200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteConversation

> Object deleteConversation(conversationId)

Delete a conversation

### Example

```javascript
import ConversationApi from 'conversation_api';
let defaultClient = ConversationApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ConversationApi.ConversationApi();
let conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
apiInstance.deleteConversation(conversationId, (error, data, response) => {
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

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listConversations

> ListConversations200Response listConversations(opts)

List conversations

This endpoint is **DEPRECATED**. Please use [/v0.2/conversations](/api/conversation.v2#get-conversations).  List all conversations associated with your application. This endpoint required an admin JWT. To find all conversations for the currently logged in user, see [GET /users/:id/conversations](#getuserConversations)

### Example

```javascript
import ConversationApi from 'conversation_api';
let defaultClient = ConversationApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ConversationApi.ConversationApi();
let opts = {
  'dateStart': "2018-01-01 10:00:00", // String | Return the records that occurred after this point in time.
  'dateEnd': "2018-01-01 12:00:00", // String | Return the records that occurred before this point in time.
  'pageSize': 10, // Number | Return this amount of records in the response
  'recordIndex': 0, // Number | Return calls from this index in the response
  'order': "'asc'" // String | Return the records in ascending or descending order.
};
apiInstance.listConversations(opts, (error, data, response) => {
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
 **dateStart** | **String**| Return the records that occurred after this point in time. | [optional] 
 **dateEnd** | **String**| Return the records that occurred before this point in time. | [optional] 
 **pageSize** | **Number**| Return this amount of records in the response | [optional] [default to 10]
 **recordIndex** | **Number**| Return calls from this index in the response | [optional] [default to 0]
 **order** | **String**| Return the records in ascending or descending order. | [optional] [default to &#39;asc&#39;]

### Return type

[**ListConversations200Response**](ListConversations200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## recordConversation

> recordConversation(conversationId, opts)

Record a conversation

### Example

```javascript
import ConversationApi from 'conversation_api';
let defaultClient = ConversationApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ConversationApi.ConversationApi();
let conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
let opts = {
  'recordConversationRequest': new ConversationApi.RecordConversationRequest() // RecordConversationRequest | Record Conversation Request Payload Object
};
apiInstance.recordConversation(conversationId, opts, (error, data, response) => {
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
 **conversationId** | **String**| Conversation ID | 
 **recordConversationRequest** | [**RecordConversationRequest**](RecordConversationRequest.md)| Record Conversation Request Payload Object | [optional] 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## replaceConversation

> CreateConversation200Response replaceConversation(conversationId, opts)

Update a conversation

### Example

```javascript
import ConversationApi from 'conversation_api';
let defaultClient = ConversationApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ConversationApi.ConversationApi();
let conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
let opts = {
  'createConversationRequest': new ConversationApi.CreateConversationRequest() // CreateConversationRequest | Conversation Request Payload Object
};
apiInstance.replaceConversation(conversationId, opts, (error, data, response) => {
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
 **createConversationRequest** | [**CreateConversationRequest**](CreateConversationRequest.md)| Conversation Request Payload Object | [optional] 

### Return type

[**CreateConversation200Response**](CreateConversation200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## retrieveConversation

> RetrieveConversation200Response retrieveConversation(conversationId)

Retrieve a conversation

### Example

```javascript
import ConversationApi from 'conversation_api';
let defaultClient = ConversationApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ConversationApi.ConversationApi();
let conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
apiInstance.retrieveConversation(conversationId, (error, data, response) => {
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

[**RetrieveConversation200Response**](RetrieveConversation200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

