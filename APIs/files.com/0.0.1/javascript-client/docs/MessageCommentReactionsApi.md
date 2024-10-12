# FilesComApi.MessageCommentReactionsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteMessageCommentReactionsId**](MessageCommentReactionsApi.md#deleteMessageCommentReactionsId) | **DELETE** /message_comment_reactions/{id} | Delete Message Comment Reaction
[**getMessageCommentReactions**](MessageCommentReactionsApi.md#getMessageCommentReactions) | **GET** /message_comment_reactions | List Message Comment Reactions
[**getMessageCommentReactionsId**](MessageCommentReactionsApi.md#getMessageCommentReactionsId) | **GET** /message_comment_reactions/{id} | Show Message Comment Reaction
[**postMessageCommentReactions**](MessageCommentReactionsApi.md#postMessageCommentReactions) | **POST** /message_comment_reactions | Create Message Comment Reaction



## deleteMessageCommentReactionsId

> deleteMessageCommentReactionsId(id)

Delete Message Comment Reaction

Delete Message Comment Reaction

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.MessageCommentReactionsApi();
let id = 56; // Number | Message Comment Reaction ID.
apiInstance.deleteMessageCommentReactionsId(id, (error, data, response) => {
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
 **id** | **Number**| Message Comment Reaction ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getMessageCommentReactions

> [MessageCommentReactionEntity] getMessageCommentReactions(messageCommentId, opts)

List Message Comment Reactions

List Message Comment Reactions

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.MessageCommentReactionsApi();
let messageCommentId = 56; // Number | Message comment to return reactions for.
let opts = {
  'userId': 56, // Number | User ID.  Provide a value of `0` to operate the current session's user.
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56 // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
};
apiInstance.getMessageCommentReactions(messageCommentId, opts, (error, data, response) => {
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
 **messageCommentId** | **Number**| Message comment to return reactions for. | 
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 

### Return type

[**[MessageCommentReactionEntity]**](MessageCommentReactionEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMessageCommentReactionsId

> MessageCommentReactionEntity getMessageCommentReactionsId(id)

Show Message Comment Reaction

Show Message Comment Reaction

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.MessageCommentReactionsApi();
let id = 56; // Number | Message Comment Reaction ID.
apiInstance.getMessageCommentReactionsId(id, (error, data, response) => {
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
 **id** | **Number**| Message Comment Reaction ID. | 

### Return type

[**MessageCommentReactionEntity**](MessageCommentReactionEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postMessageCommentReactions

> MessageCommentReactionEntity postMessageCommentReactions(emoji, opts)

Create Message Comment Reaction

Create Message Comment Reaction

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.MessageCommentReactionsApi();
let emoji = "emoji_example"; // String | Emoji to react with.
let opts = {
  'userId': 56 // Number | User ID.  Provide a value of `0` to operate the current session's user.
};
apiInstance.postMessageCommentReactions(emoji, opts, (error, data, response) => {
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

[**MessageCommentReactionEntity**](MessageCommentReactionEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

