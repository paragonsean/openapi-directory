# FilesComApi.FileCommentReactionsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteFileCommentReactionsId**](FileCommentReactionsApi.md#deleteFileCommentReactionsId) | **DELETE** /file_comment_reactions/{id} | Delete File Comment Reaction
[**postFileCommentReactions**](FileCommentReactionsApi.md#postFileCommentReactions) | **POST** /file_comment_reactions | Create File Comment Reaction



## deleteFileCommentReactionsId

> deleteFileCommentReactionsId(id)

Delete File Comment Reaction

Delete File Comment Reaction

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.FileCommentReactionsApi();
let id = 56; // Number | File Comment Reaction ID.
apiInstance.deleteFileCommentReactionsId(id, (error, data, response) => {
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
 **id** | **Number**| File Comment Reaction ID. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postFileCommentReactions

> FileCommentReactionEntity postFileCommentReactions(emoji, fileCommentId, opts)

Create File Comment Reaction

Create File Comment Reaction

### Example

```javascript
import FilesComApi from 'files_com_api';

let apiInstance = new FilesComApi.FileCommentReactionsApi();
let emoji = "emoji_example"; // String | Emoji to react with.
let fileCommentId = 56; // Number | ID of file comment to attach reaction to.
let opts = {
  'userId': 56 // Number | User ID.  Provide a value of `0` to operate the current session's user.
};
apiInstance.postFileCommentReactions(emoji, fileCommentId, opts, (error, data, response) => {
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
 **fileCommentId** | **Number**| ID of file comment to attach reaction to. | 
 **userId** | **Number**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] 

### Return type

[**FileCommentReactionEntity**](FileCommentReactionEntity.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

