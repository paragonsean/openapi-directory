# VocaDbWeb.CommentApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiCommentsEntryTypeCommentsCommentIdDelete**](CommentApiApi.md#apiCommentsEntryTypeCommentsCommentIdDelete) | **DELETE** /api/comments/{entryType}-comments/{commentId} | 
[**apiCommentsEntryTypeCommentsCommentIdPost**](CommentApiApi.md#apiCommentsEntryTypeCommentsCommentIdPost) | **POST** /api/comments/{entryType}-comments/{commentId} | 
[**apiCommentsEntryTypeCommentsGet**](CommentApiApi.md#apiCommentsEntryTypeCommentsGet) | **GET** /api/comments/{entryType}-comments | 
[**apiCommentsEntryTypeCommentsPost**](CommentApiApi.md#apiCommentsEntryTypeCommentsPost) | **POST** /api/comments/{entryType}-comments | 
[**apiCommentsGet**](CommentApiApi.md#apiCommentsGet) | **GET** /api/comments | 



## apiCommentsEntryTypeCommentsCommentIdDelete

> apiCommentsEntryTypeCommentsCommentIdDelete(entryType, commentId)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.CommentApiApi();
let entryType = new VocaDbWeb.EntryType(); // EntryType | 
let commentId = 56; // Number | 
apiInstance.apiCommentsEntryTypeCommentsCommentIdDelete(entryType, commentId, (error, data, response) => {
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
 **entryType** | [**EntryType**](.md)|  | 
 **commentId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiCommentsEntryTypeCommentsCommentIdPost

> apiCommentsEntryTypeCommentsCommentIdPost(entryType, commentId, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.CommentApiApi();
let entryType = new VocaDbWeb.EntryType(); // EntryType | 
let commentId = 56; // Number | 
let opts = {
  'commentForApiContract': new VocaDbWeb.CommentForApiContract() // CommentForApiContract | 
};
apiInstance.apiCommentsEntryTypeCommentsCommentIdPost(entryType, commentId, opts, (error, data, response) => {
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
 **entryType** | [**EntryType**](.md)|  | 
 **commentId** | **Number**|  | 
 **commentForApiContract** | [**CommentForApiContract**](CommentForApiContract.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: Not defined


## apiCommentsEntryTypeCommentsGet

> CommentForApiContractPartialFindResult apiCommentsEntryTypeCommentsGet(entryType, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.CommentApiApi();
let entryType = new VocaDbWeb.EntryType(); // EntryType | 
let opts = {
  'entryId': 56 // Number | 
};
apiInstance.apiCommentsEntryTypeCommentsGet(entryType, opts, (error, data, response) => {
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
 **entryType** | [**EntryType**](.md)|  | 
 **entryId** | **Number**|  | [optional] 

### Return type

[**CommentForApiContractPartialFindResult**](CommentForApiContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiCommentsEntryTypeCommentsPost

> CommentForApiContract apiCommentsEntryTypeCommentsPost(entryType, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.CommentApiApi();
let entryType = new VocaDbWeb.EntryType(); // EntryType | 
let opts = {
  'commentForApiContract': new VocaDbWeb.CommentForApiContract() // CommentForApiContract | 
};
apiInstance.apiCommentsEntryTypeCommentsPost(entryType, opts, (error, data, response) => {
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
 **entryType** | [**EntryType**](.md)|  | 
 **commentForApiContract** | [**CommentForApiContract**](CommentForApiContract.md)|  | [optional] 

### Return type

[**CommentForApiContract**](CommentForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## apiCommentsGet

> CommentForApiContractPartialFindResult apiCommentsGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.CommentApiApi();
let opts = {
  'before': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'since': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'userId': 56, // Number | 
  'entryType': new VocaDbWeb.EntryType(), // EntryType | 
  'maxResults': 50, // Number | 
  'getTotalCount': false, // Boolean | 
  'fields': new VocaDbWeb.CommentOptionalFields(), // CommentOptionalFields | 
  'entryFields': new VocaDbWeb.EntryOptionalFields(), // EntryOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference(), // ContentLanguagePreference | 
  'sortRule': new VocaDbWeb.CommentSortRule() // CommentSortRule | 
};
apiInstance.apiCommentsGet(opts, (error, data, response) => {
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
 **before** | **Date**|  | [optional] 
 **since** | **Date**|  | [optional] 
 **userId** | **Number**|  | [optional] 
 **entryType** | [**EntryType**](.md)|  | [optional] 
 **maxResults** | **Number**|  | [optional] [default to 50]
 **getTotalCount** | **Boolean**|  | [optional] [default to false]
 **fields** | [**CommentOptionalFields**](.md)|  | [optional] 
 **entryFields** | [**EntryOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 
 **sortRule** | [**CommentSortRule**](.md)|  | [optional] 

### Return type

[**CommentForApiContractPartialFindResult**](CommentForApiContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

