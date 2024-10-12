# ConversationApi.ConversationApi

All URIs are relative to *https://api.nexmo.com/v0.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getConversations**](ConversationApi.md#getConversations) | **GET** /conversations | List Conversations



## getConversations

> GetConversations200Response getConversations(opts)

List Conversations

Please note that not all data is available in the list endpoint. Once  you&#39;ve identified the conversation you need to work with, use the  [GET /conversations/:id](#get-conversation) endpoint to fetch all of the conversation details 

### Example

```javascript
import ConversationApi from 'conversation_api';

let apiInstance = new ConversationApi.ConversationApi();
let opts = {
  'pageSize': 10, // Number | The number of results returned per page.   The default value is `10`. The maximum value is `100`.
  'order': "'asc'", // String | Show the most (`desc`) / least (`asc`) recently created entries first
  'cursor': "cursor_example", // String | The cursor to start returning results from.  You are not expected to provide this manually, but to follow the url provided in `_links.next.href` in the response which contains a `cursor` value 
  'dateStart': "dateStart_example", // String | Search for conversations created after this ISO8601 date
  'dateEnd': "dateEnd_example" // String | Search for conversations created before this ISO8601 date
};
apiInstance.getConversations(opts, (error, data, response) => {
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
 **pageSize** | **Number**| The number of results returned per page.   The default value is &#x60;10&#x60;. The maximum value is &#x60;100&#x60;. | [optional] [default to 10]
 **order** | **String**| Show the most (&#x60;desc&#x60;) / least (&#x60;asc&#x60;) recently created entries first | [optional] [default to &#39;asc&#39;]
 **cursor** | **String**| The cursor to start returning results from.  You are not expected to provide this manually, but to follow the url provided in &#x60;_links.next.href&#x60; in the response which contains a &#x60;cursor&#x60; value  | [optional] 
 **dateStart** | **String**| Search for conversations created after this ISO8601 date | [optional] 
 **dateEnd** | **String**| Search for conversations created before this ISO8601 date | [optional] 

### Return type

[**GetConversations200Response**](GetConversations200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

