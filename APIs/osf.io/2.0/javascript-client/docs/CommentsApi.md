# OsfApiv2Documentation.CommentsApi

All URIs are relative to *https://api.test.osf.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commentsDelete**](CommentsApi.md#commentsDelete) | **DELETE** /comments/{comment_id}/ | Delete a comment
[**commentsPut**](CommentsApi.md#commentsPut) | **PUT** /comments/{comment_id}/ | Update a comment
[**commentsRead**](CommentsApi.md#commentsRead) | **GET** /comments/{comment_id}/ | Retrieve a comment



## commentsDelete

> commentsDelete(commentId)

Delete a comment

Deletes a comment. This action can be undone by setting deleted to False in a comment update request. #### Returns If the request is successful, no content is returned.  If the request is unsuccessful, a JSON object with an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CommentsApi();
let commentId = "commentId_example"; // String | The unique identifier of the comment you wish to delete.
apiInstance.commentsDelete(commentId, (error, data, response) => {
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
 **commentId** | **String**| The unique identifier of the comment you wish to delete. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## commentsPut

> commentsPut(commentId, body)

Update a comment

Updates the specified comment by setting the values of the parameters passed. Any parameters not provided will be left unchanged. #### Returns Returns JSON with a &#x60;data&#x60; key containing the new representation of the updated comment, if the request is successful.  If the request is unsuccessful, JSON with an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CommentsApi();
let commentId = "commentId_example"; // String | The unique identifier of the comment you wish to update.
let body = {key: null}; // Object | 
apiInstance.commentsPut(commentId, body, (error, data, response) => {
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
 **commentId** | **String**| The unique identifier of the comment you wish to update. | 
 **body** | **Object**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## commentsRead

> Comment commentsRead(commentId)

Retrieve a comment

Retrieves the details of a comment #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested comment, if the request was successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example

```javascript
import OsfApiv2Documentation from 'osf_apiv2_documentation';

let apiInstance = new OsfApiv2Documentation.CommentsApi();
let commentId = "commentId_example"; // String | The unique identifier of the comment you wish to retrieve.
apiInstance.commentsRead(commentId, (error, data, response) => {
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
 **commentId** | **String**| The unique identifier of the comment you wish to retrieve. | 

### Return type

[**Comment**](Comment.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*, application/json

