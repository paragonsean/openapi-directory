# DaniWebConnectApi.ConversationsApi

All URIs are relative to *https://www.daniweb.com/connect/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**conversationsIDGet**](ConversationsApi.md#conversationsIDGet) | **GET** /conversations/{ID} | 
[**conversationsIDMessagesGet**](ConversationsApi.md#conversationsIDMessagesGet) | **GET** /conversations/{ID}/messages | 
[**conversationsIDMessagesPost**](ConversationsApi.md#conversationsIDMessagesPost) | **POST** /conversations/{ID}/messages | 
[**conversationsIDSchedulesPost**](ConversationsApi.md#conversationsIDSchedulesPost) | **POST** /conversations/{ID}/schedules | 
[**conversationsIDSearchesPost**](ConversationsApi.md#conversationsIDSearchesPost) | **POST** /conversations/{ID}/searches | 
[**conversationsIDStatusesGet**](ConversationsApi.md#conversationsIDStatusesGet) | **GET** /conversations/{ID}/statuses | 
[**conversationsIDStatusesPatch**](ConversationsApi.md#conversationsIDStatusesPatch) | **PATCH** /conversations/{ID}/statuses | 
[**conversationsSchedulesPost**](ConversationsApi.md#conversationsSchedulesPost) | **POST** /conversations/schedules | 
[**conversationsSearchesPost**](ConversationsApi.md#conversationsSearchesPost) | **POST** /conversations/searches | 
[**conversationsStatusesGet**](ConversationsApi.md#conversationsStatusesGet) | **GET** /conversations/statuses | 



## conversationsIDGet

> EndpointGetConversationsID conversationsIDGet(ID)



Fetch an array of conversations. You can only retrieve conversations with users who exist within the current access token&#39;s bubble.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.ConversationsApi();
let ID = [null]; // [Number] | 
apiInstance.conversationsIDGet(ID, (error, data, response) => {
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
 **ID** | [**[Number]**](Number.md)|  | 

### Return type

[**EndpointGetConversationsID**](EndpointGetConversationsID.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## conversationsIDMessagesGet

> EndpointGetConversationsIDMessages conversationsIDMessagesGet(ID, opts)



Retrieve the last {limit} messages in the conversation, provided the conversations exist within the current access token&#39;s bubble. If a timeout is 0 or greater, the batch is sorted oldest first. Otherwise, if timeout is a negative number, the transcript is paginated and sorted newest first. Specify a timeout for long polling (which delays the server sending back results for up to n seconds or until results are available, whichever comes first), or default to 0 for immediate results. Optionally record your status as online along with sharing the latest message you&#39;ve seen with the other conversation participant. Optionally specify a gt_message_id to retrieve only messages with an ID greater than that specified (such as greater than the latest message ID received in the last poll). Optionally only poll for messages authored by the other person in the conversation, and echo messages authored by you when sending, for a perceived increase in performance. Optionally only retrieve messages that were posted from within the current access token&#39;s bubble. Optionally specify a date formatted as YYYY-MM-DD to retrieve a transcript of messages from a single day. When record_seen is set to true, the new message count for the conversation is reset to zero.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.ConversationsApi();
let ID = 56; // Number | 
let opts = {
  'gtMessageId': 56, // Number | 
  'excludeSelf': false, // Boolean | 
  'date': "date_example", // String | 
  'bubbled': false, // Boolean | 
  'recordSeen': false, // Boolean | 
  'timeout': 0, // Number | 
  'offset': 0, // Number | 
  'limit': 50 // Number | 
};
apiInstance.conversationsIDMessagesGet(ID, opts, (error, data, response) => {
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
 **ID** | **Number**|  | 
 **gtMessageId** | **Number**|  | [optional] 
 **excludeSelf** | **Boolean**|  | [optional] [default to false]
 **date** | **String**|  | [optional] 
 **bubbled** | **Boolean**|  | [optional] [default to false]
 **recordSeen** | **Boolean**|  | [optional] [default to false]
 **timeout** | **Number**|  | [optional] [default to 0]
 **offset** | **Number**|  | [optional] [default to 0]
 **limit** | **Number**|  | [optional] [default to 50]

### Return type

[**EndpointGetConversationsIDMessages**](EndpointGetConversationsIDMessages.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## conversationsIDMessagesPost

> EndpointPostConversationsIDMessages conversationsIDMessagesPost(ID, textRaw, opts)



Post a message to a conversation that is with a user who exists within the current access token&#39;s bubble. Optionally specify whether emoticons should be parsed into smiley images. Optionally specify whether the message should be bubbled within the app. Additionally, optionally attach a single metadata key/value pair to the message upon submission.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.ConversationsApi();
let ID = 56; // Number | 
let textRaw = "textRaw_example"; // String | 
let opts = {
  'bubbled': false, // Boolean | 
  'metadata0Key': "metadata0Key_example", // String | 
  'metadata0Privacy': "metadata0Privacy_example", // String | 
  'metadata0Values': ["null"], // [String] | 
  'metadata1Key': "metadata1Key_example", // String | 
  'metadata1Privacy': "metadata1Privacy_example", // String | 
  'metadata1Values': ["null"], // [String] | 
  'metadata2Key': "metadata2Key_example", // String | 
  'metadata2Privacy': "metadata2Privacy_example", // String | 
  'metadata2Values': ["null"], // [String] | 
  'textEmoticons': false // Boolean | 
};
apiInstance.conversationsIDMessagesPost(ID, textRaw, opts, (error, data, response) => {
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
 **ID** | **Number**|  | 
 **textRaw** | **String**|  | 
 **bubbled** | **Boolean**|  | [optional] [default to false]
 **metadata0Key** | **String**|  | [optional] 
 **metadata0Privacy** | **String**|  | [optional] 
 **metadata0Values** | [**[String]**](String.md)|  | [optional] 
 **metadata1Key** | **String**|  | [optional] 
 **metadata1Privacy** | **String**|  | [optional] 
 **metadata1Values** | [**[String]**](String.md)|  | [optional] 
 **metadata2Key** | **String**|  | [optional] 
 **metadata2Privacy** | **String**|  | [optional] 
 **metadata2Values** | [**[String]**](String.md)|  | [optional] 
 **textEmoticons** | **Boolean**|  | [optional] [default to false]

### Return type

[**EndpointPostConversationsIDMessages**](EndpointPostConversationsIDMessages.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## conversationsIDSchedulesPost

> EndpointPostConversationsIDSchedules conversationsIDSchedulesPost(ID, opts)



Paginated report of information about messages contributed by conversation and date. Only conversations that exist within the current access token&#39;s bubble are considered in the calculations. Optionally roll up all conversations to retrieve one record per date. Optionally specify a date formatted as YYYY-MM-DD to retrieve information just from the single date, along with additional navigational information, which is useful when generating a transcript for a single day and wanting to reference the previous and next days there were messages within the conversation(s).

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.ConversationsApi();
let ID = [null]; // [Number] | 
let opts = {
  'date': "date_example", // String | 
  'limit': 50, // Number | 
  'offset': 0, // Number | 
  'rollUp': false, // Boolean | 
  'sort': "'desc'" // String | 
};
apiInstance.conversationsIDSchedulesPost(ID, opts, (error, data, response) => {
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
 **ID** | [**[Number]**](Number.md)|  | 
 **date** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 50]
 **offset** | **Number**|  | [optional] [default to 0]
 **rollUp** | **Boolean**|  | [optional] [default to false]
 **sort** | **String**|  | [optional] [default to &#39;desc&#39;]

### Return type

[**EndpointPostConversationsIDSchedules**](EndpointPostConversationsIDSchedules.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## conversationsIDSearchesPost

> EndpointPostConversationsIDSearches conversationsIDSearchesPost(ID, query, opts)



Fetch messages authored from within specified conversations that match a query string passed in as a search parameter along with their relevancy score.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.ConversationsApi();
let ID = [null]; // [Number] | 
let query = "query_example"; // String | 
let opts = {
  'date': "date_example", // String | 
  'gtMessageId': 56, // Number | 
  'limit': 50, // Number | 
  'offset': 0 // Number | 
};
apiInstance.conversationsIDSearchesPost(ID, query, opts, (error, data, response) => {
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
 **ID** | [**[Number]**](Number.md)|  | 
 **query** | **String**|  | 
 **date** | **String**|  | [optional] 
 **gtMessageId** | **Number**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 50]
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**EndpointPostConversationsIDSearches**](EndpointPostConversationsIDSearches.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## conversationsIDStatusesGet

> EndpointGetConversationsIDStatuses conversationsIDStatusesGet(ID)



Status information about your current relationship with one or more conversations you participating in, provided the conversations exist within the current access token&#39;s bubble.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.ConversationsApi();
let ID = [null]; // [Number] | 
apiInstance.conversationsIDStatusesGet(ID, (error, data, response) => {
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
 **ID** | [**[Number]**](Number.md)|  | 

### Return type

[**EndpointGetConversationsIDStatuses**](EndpointGetConversationsIDStatuses.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## conversationsIDStatusesPatch

> EndpointPatchConversationsIDStatuses conversationsIDStatusesPatch(ID, archivedStatus)



Archive or unarchive a conversation that is with a user who exists within the same bubble.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.ConversationsApi();
let ID = 56; // Number | 
let archivedStatus = true; // Boolean | 
apiInstance.conversationsIDStatusesPatch(ID, archivedStatus, (error, data, response) => {
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
 **ID** | **Number**|  | 
 **archivedStatus** | **Boolean**|  | 

### Return type

[**EndpointPatchConversationsIDStatuses**](EndpointPatchConversationsIDStatuses.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## conversationsSchedulesPost

> EndpointPostConversationsSchedules conversationsSchedulesPost(opts)



Paginated report of information about messages contributed by conversation and date. Only conversations that exist within the current access token&#39;s bubble are considered in the calculations. Optionally roll up all conversations to retrieve one record per date. Optionally specify a date formatted as YYYY-MM-DD to retrieve information just from the single date, along with additional navigational information, which is useful when generating a transcript for a single day and wanting to reference the previous and next days there were messages.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.ConversationsApi();
let opts = {
  'date': "date_example", // String | 
  'limit': 50, // Number | 
  'offset': 0, // Number | 
  'rollUp': false, // Boolean | 
  'sort': "'desc'" // String | 
};
apiInstance.conversationsSchedulesPost(opts, (error, data, response) => {
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
 **date** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 50]
 **offset** | **Number**|  | [optional] [default to 0]
 **rollUp** | **Boolean**|  | [optional] [default to false]
 **sort** | **String**|  | [optional] [default to &#39;desc&#39;]

### Return type

[**EndpointPostConversationsSchedules**](EndpointPostConversationsSchedules.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## conversationsSearchesPost

> EndpointPostConversationsSearches conversationsSearchesPost(query, opts)



Fetch messages authored from within the current bubble that match a query string passed in as a search parameter along with their relevancy score.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.ConversationsApi();
let query = "query_example"; // String | 
let opts = {
  'date': "date_example", // String | 
  'gtMessageId': 56, // Number | 
  'limit': 50, // Number | 
  'offset': 0 // Number | 
};
apiInstance.conversationsSearchesPost(query, opts, (error, data, response) => {
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
 **query** | **String**|  | 
 **date** | **String**|  | [optional] 
 **gtMessageId** | **Number**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 50]
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**EndpointPostConversationsSearches**](EndpointPostConversationsSearches.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## conversationsStatusesGet

> EndpointGetConversationsStatuses conversationsStatusesGet(opts)



Retrieve conversations that you are participating in with users who exists within the same bubble, along with your current relationship with the conversations. The user_a / user_b properties of the conversation are populated with as much data as is available if the user is not you. If the user is you, only the id field is populated. There is a separate status endpoint to retrieve relationship information for individual conversations. Optionally filter: &#39;new&#39; to only show conversations with messages you haven&#39;t yet seen; &#39;introductions&#39; to only show conversations where users have introduced themselves to you but nothing more; &#39;unreplied&#39; to only show conversations where you have introduced yourself to other users but nothing more; &#39;notifications&#39; to show all conversations where the other user was the last person to message. Optionally only show conversations engaging within the existing access token&#39;s bubble. This report is limited to your ~500-1000 most recently active conversations you&#39;ve engaged in within current the access token&#39;s bubble.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.ConversationsApi();
let opts = {
  'filter': "filter_example", // String | 
  'includeArchived': false, // Boolean | 
  'bubbled': false, // Boolean | 
  'offset': 0, // Number | 
  'limit': 50 // Number | 
};
apiInstance.conversationsStatusesGet(opts, (error, data, response) => {
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
 **filter** | **String**|  | [optional] 
 **includeArchived** | **Boolean**|  | [optional] [default to false]
 **bubbled** | **Boolean**|  | [optional] [default to false]
 **offset** | **Number**|  | [optional] [default to 0]
 **limit** | **Number**|  | [optional] [default to 50]

### Return type

[**EndpointGetConversationsStatuses**](EndpointGetConversationsStatuses.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

