# ForemApiV1.CommentsApi

All URIs are relative to *https://dev.to/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCommentById**](CommentsApi.md#getCommentById) | **GET** /api/comments/{id} | Comment by id
[**getCommentsByArticleId**](CommentsApi.md#getCommentsByArticleId) | **GET** /api/comments | Comments



## getCommentById

> getCommentById(id)

Comment by id

This endpoint allows the client to retrieve a comment as well as his descendants comments.    It will return the required comment (the root) with its nested descendants as a thread.    See the format specification for further details.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';

let apiInstance = new ForemApiV1.CommentsApi();
let id = 321; // Number | Comment identifier.
apiInstance.getCommentById(id, (error, data, response) => {
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
 **id** | **Number**| Comment identifier. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCommentsByArticleId

> [Comment] getCommentsByArticleId(opts)

Comments

This endpoint allows the client to retrieve all comments belonging to an article or podcast episode as threaded conversations.  It will return the all top level comments with their nested comments as threads. See the format specification for further details.

### Example

```javascript
import ForemApiV1 from 'forem_api_v1';

let apiInstance = new ForemApiV1.CommentsApi();
let opts = {
  'aId': "321", // String | Article identifier.
  'pId': "321" // String | Podcast Episode identifier.
};
apiInstance.getCommentsByArticleId(opts, (error, data, response) => {
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
 **aId** | **String**| Article identifier. | [optional] 
 **pId** | **String**| Podcast Episode identifier. | [optional] 

### Return type

[**[Comment]**](Comment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

