# VocaDbWeb.DiscussionApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiDiscussionsCommentsCommentIdDelete**](DiscussionApiApi.md#apiDiscussionsCommentsCommentIdDelete) | **DELETE** /api/discussions/comments/{commentId} | 
[**apiDiscussionsCommentsCommentIdPost**](DiscussionApiApi.md#apiDiscussionsCommentsCommentIdPost) | **POST** /api/discussions/comments/{commentId} | 
[**apiDiscussionsFoldersFolderIdTopicsGet**](DiscussionApiApi.md#apiDiscussionsFoldersFolderIdTopicsGet) | **GET** /api/discussions/folders/{folderId}/topics | 
[**apiDiscussionsFoldersFolderIdTopicsPost**](DiscussionApiApi.md#apiDiscussionsFoldersFolderIdTopicsPost) | **POST** /api/discussions/folders/{folderId}/topics | 
[**apiDiscussionsFoldersGet**](DiscussionApiApi.md#apiDiscussionsFoldersGet) | **GET** /api/discussions/folders | 
[**apiDiscussionsFoldersPost**](DiscussionApiApi.md#apiDiscussionsFoldersPost) | **POST** /api/discussions/folders | 
[**apiDiscussionsTopicsGet**](DiscussionApiApi.md#apiDiscussionsTopicsGet) | **GET** /api/discussions/topics | 
[**apiDiscussionsTopicsTopicIdCommentsPost**](DiscussionApiApi.md#apiDiscussionsTopicsTopicIdCommentsPost) | **POST** /api/discussions/topics/{topicId}/comments | 
[**apiDiscussionsTopicsTopicIdDelete**](DiscussionApiApi.md#apiDiscussionsTopicsTopicIdDelete) | **DELETE** /api/discussions/topics/{topicId} | 
[**apiDiscussionsTopicsTopicIdGet**](DiscussionApiApi.md#apiDiscussionsTopicsTopicIdGet) | **GET** /api/discussions/topics/{topicId} | 
[**apiDiscussionsTopicsTopicIdPost**](DiscussionApiApi.md#apiDiscussionsTopicsTopicIdPost) | **POST** /api/discussions/topics/{topicId} | 



## apiDiscussionsCommentsCommentIdDelete

> apiDiscussionsCommentsCommentIdDelete(commentId)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.DiscussionApiApi();
let commentId = 56; // Number | 
apiInstance.apiDiscussionsCommentsCommentIdDelete(commentId, (error, data, response) => {
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
 **commentId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiDiscussionsCommentsCommentIdPost

> apiDiscussionsCommentsCommentIdPost(commentId, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.DiscussionApiApi();
let commentId = 56; // Number | 
let opts = {
  'commentForApiContract': new VocaDbWeb.CommentForApiContract() // CommentForApiContract | 
};
apiInstance.apiDiscussionsCommentsCommentIdPost(commentId, opts, (error, data, response) => {
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
 **commentId** | **Number**|  | 
 **commentForApiContract** | [**CommentForApiContract**](CommentForApiContract.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: Not defined


## apiDiscussionsFoldersFolderIdTopicsGet

> [DiscussionTopicContract] apiDiscussionsFoldersFolderIdTopicsGet(folderId, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.DiscussionApiApi();
let folderId = 56; // Number | 
let opts = {
  'fields': new VocaDbWeb.DiscussionTopicOptionalFields() // DiscussionTopicOptionalFields | 
};
apiInstance.apiDiscussionsFoldersFolderIdTopicsGet(folderId, opts, (error, data, response) => {
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
 **folderId** | **Number**|  | 
 **fields** | [**DiscussionTopicOptionalFields**](.md)|  | [optional] 

### Return type

[**[DiscussionTopicContract]**](DiscussionTopicContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiDiscussionsFoldersFolderIdTopicsPost

> DiscussionTopicContract apiDiscussionsFoldersFolderIdTopicsPost(folderId, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.DiscussionApiApi();
let folderId = 56; // Number | 
let opts = {
  'discussionTopicContract': new VocaDbWeb.DiscussionTopicContract() // DiscussionTopicContract | 
};
apiInstance.apiDiscussionsFoldersFolderIdTopicsPost(folderId, opts, (error, data, response) => {
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
 **folderId** | **Number**|  | 
 **discussionTopicContract** | [**DiscussionTopicContract**](DiscussionTopicContract.md)|  | [optional] 

### Return type

[**DiscussionTopicContract**](DiscussionTopicContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## apiDiscussionsFoldersGet

> [DiscussionFolderContract] apiDiscussionsFoldersGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.DiscussionApiApi();
let opts = {
  'fields': new VocaDbWeb.DiscussionFolderOptionalFields() // DiscussionFolderOptionalFields | 
};
apiInstance.apiDiscussionsFoldersGet(opts, (error, data, response) => {
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
 **fields** | [**DiscussionFolderOptionalFields**](.md)|  | [optional] 

### Return type

[**[DiscussionFolderContract]**](DiscussionFolderContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiDiscussionsFoldersPost

> DiscussionFolderContract apiDiscussionsFoldersPost(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.DiscussionApiApi();
let opts = {
  'discussionFolderContract': new VocaDbWeb.DiscussionFolderContract() // DiscussionFolderContract | 
};
apiInstance.apiDiscussionsFoldersPost(opts, (error, data, response) => {
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
 **discussionFolderContract** | [**DiscussionFolderContract**](DiscussionFolderContract.md)|  | [optional] 

### Return type

[**DiscussionFolderContract**](DiscussionFolderContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## apiDiscussionsTopicsGet

> DiscussionTopicContractPartialFindResult apiDiscussionsTopicsGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.DiscussionApiApi();
let opts = {
  'folderId': 56, // Number | 
  'start': 0, // Number | 
  'maxResults': 10, // Number | 
  'getTotalCount': false, // Boolean | 
  'sort': new VocaDbWeb.DiscussionTopicSortRule(), // DiscussionTopicSortRule | 
  'fields': new VocaDbWeb.DiscussionTopicOptionalFields() // DiscussionTopicOptionalFields | 
};
apiInstance.apiDiscussionsTopicsGet(opts, (error, data, response) => {
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
 **folderId** | **Number**|  | [optional] 
 **start** | **Number**|  | [optional] [default to 0]
 **maxResults** | **Number**|  | [optional] [default to 10]
 **getTotalCount** | **Boolean**|  | [optional] [default to false]
 **sort** | [**DiscussionTopicSortRule**](.md)|  | [optional] 
 **fields** | [**DiscussionTopicOptionalFields**](.md)|  | [optional] 

### Return type

[**DiscussionTopicContractPartialFindResult**](DiscussionTopicContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiDiscussionsTopicsTopicIdCommentsPost

> CommentForApiContract apiDiscussionsTopicsTopicIdCommentsPost(topicId, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.DiscussionApiApi();
let topicId = 56; // Number | 
let opts = {
  'commentForApiContract': new VocaDbWeb.CommentForApiContract() // CommentForApiContract | 
};
apiInstance.apiDiscussionsTopicsTopicIdCommentsPost(topicId, opts, (error, data, response) => {
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
 **topicId** | **Number**|  | 
 **commentForApiContract** | [**CommentForApiContract**](CommentForApiContract.md)|  | [optional] 

### Return type

[**CommentForApiContract**](CommentForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## apiDiscussionsTopicsTopicIdDelete

> apiDiscussionsTopicsTopicIdDelete(topicId)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.DiscussionApiApi();
let topicId = 56; // Number | 
apiInstance.apiDiscussionsTopicsTopicIdDelete(topicId, (error, data, response) => {
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
 **topicId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiDiscussionsTopicsTopicIdGet

> DiscussionTopicContract apiDiscussionsTopicsTopicIdGet(topicId, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.DiscussionApiApi();
let topicId = 56; // Number | 
let opts = {
  'fields': new VocaDbWeb.DiscussionTopicOptionalFields() // DiscussionTopicOptionalFields | 
};
apiInstance.apiDiscussionsTopicsTopicIdGet(topicId, opts, (error, data, response) => {
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
 **topicId** | **Number**|  | 
 **fields** | [**DiscussionTopicOptionalFields**](.md)|  | [optional] 

### Return type

[**DiscussionTopicContract**](DiscussionTopicContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiDiscussionsTopicsTopicIdPost

> apiDiscussionsTopicsTopicIdPost(topicId, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.DiscussionApiApi();
let topicId = 56; // Number | 
let opts = {
  'discussionTopicContract': new VocaDbWeb.DiscussionTopicContract() // DiscussionTopicContract | 
};
apiInstance.apiDiscussionsTopicsTopicIdPost(topicId, opts, (error, data, response) => {
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
 **topicId** | **Number**|  | 
 **discussionTopicContract** | [**DiscussionTopicContract**](DiscussionTopicContract.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: Not defined

