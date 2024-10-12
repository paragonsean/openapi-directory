# ConversationApi.EventApi

All URIs are relative to *https://api.nexmo.com/v0.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEvents**](EventApi.md#getEvents) | **GET** /conversations/{conversation_id}/events | List Events



## getEvents

> GetEvents200Response getEvents(conversationId, opts)

List Events

### Example

```javascript
import ConversationApi from 'conversation_api';

let apiInstance = new ConversationApi.EventApi();
let conversationId = "CON-afe887d8-d587-4280-9aae-dfa4c9227d5e"; // String | The ID of the conversation
let opts = {
  'pageSize': 10, // Number | The number of results returned per page.   The default value is `10`. The maximum value is `100`.
  'order': "'asc'", // String | Show the most (`desc`) / least (`asc`) recently created entries first
  'cursor': "cursor_example", // String | The cursor to start returning results from.  You are not expected to provide this manually, but to follow the url provided in `_links.next.href` in the response which contains a `cursor` value 
  'startId': "13", // String | The ID to start returning events at
  'endId': "19", // String | The ID to end returning events at
  'eventType': "text" // String | The type of event to search for. Does not currently support custom events
};
apiInstance.getEvents(conversationId, opts, (error, data, response) => {
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
 **conversationId** | **String**| The ID of the conversation | 
 **pageSize** | **Number**| The number of results returned per page.   The default value is &#x60;10&#x60;. The maximum value is &#x60;100&#x60;. | [optional] [default to 10]
 **order** | **String**| Show the most (&#x60;desc&#x60;) / least (&#x60;asc&#x60;) recently created entries first | [optional] [default to &#39;asc&#39;]
 **cursor** | **String**| The cursor to start returning results from.  You are not expected to provide this manually, but to follow the url provided in &#x60;_links.next.href&#x60; in the response which contains a &#x60;cursor&#x60; value  | [optional] 
 **startId** | **String**| The ID to start returning events at | [optional] 
 **endId** | **String**| The ID to end returning events at | [optional] 
 **eventType** | **String**| The type of event to search for. Does not currently support custom events | [optional] 

### Return type

[**GetEvents200Response**](GetEvents200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

