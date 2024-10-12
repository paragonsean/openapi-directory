# FilesComApi.MessageCommentsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteMessageCommentsId**](MessageCommentsApi.md#deleteMessageCommentsId) | **DELETE** /message_comments/{id} | Delete Message Comment
[**getMessageComments**](MessageCommentsApi.md#getMessageComments) | **GET** /message_comments | List Message Comments
[**getMessageCommentsId**](MessageCommentsApi.md#getMessageCommentsId) | **GET** /message_comments/{id} | Show Message Comment
[**patchMessageCommentsId**](MessageCommentsApi.md#patchMessageCommentsId) | **PATCH** /message_comments/{id} | Update Message Comment
[**postMessageComments**](MessageCommentsApi.md#postMessageComments) | **POST** /message_comments | Create Message Comment



## deleteMessageCommentsId

> deleteMessageCommentsId(id)

Delete Message Comment

Delete Message Comment

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.MessageCommentsApi();
let id = 56; // Number | Message Comment ID.
apiInstance.deleteMessageCommentsId(id, (error, data, response) => {
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
 **id** | **Number**| Message Comment ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getMessageComments

> [MessageCommentEntity] getMessageComments(messageId, opts)

List Message Comments

List Message Comments

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.MessageCommentsApi();
let messageId = 56; // Number | Message comment to return comments for.
let opts = {
  'userId': 56, // Number | User ID.  Provide a value of `0` to operate the current session's user.
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56 // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
};
apiInstance.getMessageComments(messageId, opts, (error, data, response) => {
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
 **messageId** | **Number**| Message comment to return comments for. | 
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 

### Return type

[**[MessageCommentEntity]**](MessageCommentEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMessageCommentsId

> MessageCommentEntity getMessageCommentsId(id)

Show Message Comment

Show Message Comment

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.MessageCommentsApi();
let id = 56; // Number | Message Comment ID.
apiInstance.getMessageCommentsId(id, (error, data, response) => {
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
 **id** | **Number**| Message Comment ID. | 

### Return type

[**MessageCommentEntity**](MessageCommentEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchMessageCommentsId

> MessageCommentEntity patchMessageCommentsId(id, body)

Update Message Comment

Update Message Comment

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.MessageCommentsApi();
let id = 56; // Number | Message Comment ID.
let body = "body_example"; // String | Comment body.
apiInstance.patchMessageCommentsId(id, body, (error, data, response) => {
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
 **id** | **Number**| Message Comment ID. | 
 **body** | **String**| Comment body. | 

### Return type

[**MessageCommentEntity**](MessageCommentEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postMessageComments

> MessageCommentEntity postMessageComments(body, opts)

Create Message Comment

Create Message Comment

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.MessageCommentsApi();
let body = "body_example"; // String | Comment body.
let opts = {
  'userId': 56 // Number | User ID.  Provide a value of `0` to operate the current session's user.
};
apiInstance.postMessageComments(body, opts, (error, data, response) => {
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
 **body** | **String**| Comment body. | 
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] 

### Return type

[**MessageCommentEntity**](MessageCommentEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

