# FilesComApi.MessageReactionsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteMessageReactionsId**](MessageReactionsApi.md#deleteMessageReactionsId) | **DELETE** /message_reactions/{id} | Delete Message Reaction
[**getMessageReactions**](MessageReactionsApi.md#getMessageReactions) | **GET** /message_reactions | List Message Reactions
[**getMessageReactionsId**](MessageReactionsApi.md#getMessageReactionsId) | **GET** /message_reactions/{id} | Show Message Reaction
[**postMessageReactions**](MessageReactionsApi.md#postMessageReactions) | **POST** /message_reactions | Create Message Reaction



## deleteMessageReactionsId

> deleteMessageReactionsId(id)

Delete Message Reaction

Delete Message Reaction

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.MessageReactionsApi();
let id = 56; // Number | Message Reaction ID.
apiInstance.deleteMessageReactionsId(id, (error, data, response) => {
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
 **id** | **Number**| Message Reaction ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getMessageReactions

> [MessageReactionEntity] getMessageReactions(messageId, opts)

List Message Reactions

List Message Reactions

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.MessageReactionsApi();
let messageId = 56; // Number | Message to return reactions for.
let opts = {
  'userId': 56, // Number | User ID.  Provide a value of `0` to operate the current session's user.
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56 // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
};
apiInstance.getMessageReactions(messageId, opts, (error, data, response) => {
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
 **messageId** | **Number**| Message to return reactions for. | 
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 

### Return type

[**[MessageReactionEntity]**](MessageReactionEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMessageReactionsId

> MessageReactionEntity getMessageReactionsId(id)

Show Message Reaction

Show Message Reaction

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.MessageReactionsApi();
let id = 56; // Number | Message Reaction ID.
apiInstance.getMessageReactionsId(id, (error, data, response) => {
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
 **id** | **Number**| Message Reaction ID. | 

### Return type

[**MessageReactionEntity**](MessageReactionEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postMessageReactions

> MessageReactionEntity postMessageReactions(emoji, opts)

Create Message Reaction

Create Message Reaction

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.MessageReactionsApi();
let emoji = "emoji_example"; // String | Emoji to react with.
let opts = {
  'userId': 56 // Number | User ID.  Provide a value of `0` to operate the current session's user.
};
apiInstance.postMessageReactions(emoji, opts, (error, data, response) => {
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
 **emoji** | **String**| Emoji to react with. | 
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] 

### Return type

[**MessageReactionEntity**](MessageReactionEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

