# Story.ConversationApi

All URIs are relative to */story*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storyIdMessagesGet**](ConversationApi.md#storyIdMessagesGet) | **GET** /{id}/messages | Conversation: List Conversation Messages
[**storyIdMessagesPost**](ConversationApi.md#storyIdMessagesPost) | **POST** /{id}/messages | Conversation: Send a Message



## storyIdMessagesGet

> [Message] storyIdMessagesGet(id)

Conversation: List Conversation Messages

Get a list of messages that have been send in this story

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.ConversationApi();
let id = "id_example"; // String | the id from the story object
apiInstance.storyIdMessagesGet(id, (error, data, response) => {
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
 **id** | **String**| the id from the story object | 

### Return type

[**[Message]**](Message.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## storyIdMessagesPost

> storyIdMessagesPost(id, body)

Conversation: Send a Message

Add a message to the Story&#39;s conversation

### Example

```javascript
import Story from 'story';

let apiInstance = new Story.ConversationApi();
let id = "id_example"; // String | the id from the story object
let body = "body_example"; // String | The message text
apiInstance.storyIdMessagesPost(id, body, (error, data, response) => {
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
 **id** | **String**| the id from the story object | 
 **body** | **String**| The message text | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

