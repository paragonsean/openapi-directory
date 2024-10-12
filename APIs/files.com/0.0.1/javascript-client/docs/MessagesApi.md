# FilesComApi.MessagesApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteMessagesId**](MessagesApi.md#deleteMessagesId) | **DELETE** /messages/{id} | Delete Message
[**getMessages**](MessagesApi.md#getMessages) | **GET** /messages | List Messages
[**getMessagesId**](MessagesApi.md#getMessagesId) | **GET** /messages/{id} | Show Message
[**patchMessagesId**](MessagesApi.md#patchMessagesId) | **PATCH** /messages/{id} | Update Message
[**postMessages**](MessagesApi.md#postMessages) | **POST** /messages | Create Message



## deleteMessagesId

> deleteMessagesId(id)

Delete Message

Delete Message

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.MessagesApi();
let id = 56; // Number | Message ID.
apiInstance.deleteMessagesId(id, (error, data, response) => {
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
 **id** | **Number**| Message ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getMessages

> [MessageEntity] getMessages(projectId, opts)

List Messages

List Messages

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.MessagesApi();
let projectId = 56; // Number | Project for which to return messages.
let opts = {
  'userId': 56, // Number | User ID.  Provide a value of `0` to operate the current session's user.
  'cursor': "cursor_example", // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
  'perPage': 56 // Number | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
};
apiInstance.getMessages(projectId, opts, (error, data, response) => {
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
 **projectId** | **Number**| Project for which to return messages. | 
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] 
 **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] 
 **perPage** | **Number**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] 

### Return type

[**[MessageEntity]**](MessageEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMessagesId

> MessageEntity getMessagesId(id)

Show Message

Show Message

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.MessagesApi();
let id = 56; // Number | Message ID.
apiInstance.getMessagesId(id, (error, data, response) => {
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
 **id** | **Number**| Message ID. | 

### Return type

[**MessageEntity**](MessageEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## patchMessagesId

> MessageEntity patchMessagesId(id, body, projectId, subject)

Update Message

Update Message

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.MessagesApi();
let id = 56; // Number | Message ID.
let body = "body_example"; // String | Message body.
let projectId = 56; // Number | Project to which the message should be attached.
let subject = "subject_example"; // String | Message subject.
apiInstance.patchMessagesId(id, body, projectId, subject, (error, data, response) => {
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
 **id** | **Number**| Message ID. | 
 **body** | **String**| Message body. | 
 **projectId** | **Number**| Project to which the message should be attached. | 
 **subject** | **String**| Message subject. | 

### Return type

[**MessageEntity**](MessageEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## postMessages

> MessageEntity postMessages(body, projectId, subject, opts)

Create Message

Create Message

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.MessagesApi();
let body = "body_example"; // String | Message body.
let projectId = 56; // Number | Project to which the message should be attached.
let subject = "subject_example"; // String | Message subject.
let opts = {
  'userId': 56 // Number | User ID.  Provide a value of `0` to operate the current session's user.
};
apiInstance.postMessages(body, projectId, subject, opts, (error, data, response) => {
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
 **body** | **String**| Message body. | 
 **projectId** | **Number**| Project to which the message should be attached. | 
 **subject** | **String**| Message subject. | 
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] 

### Return type

[**MessageEntity**](MessageEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

