# VocaDbWeb.TagApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiTagsByNameNameGet**](TagApiApi.md#apiTagsByNameNameGet) | **GET** /api/tags/byName/{name} | 
[**apiTagsCategoryNamesGet**](TagApiApi.md#apiTagsCategoryNamesGet) | **GET** /api/tags/categoryNames | 
[**apiTagsCommentsCommentIdDelete**](TagApiApi.md#apiTagsCommentsCommentIdDelete) | **DELETE** /api/tags/comments/{commentId} | 
[**apiTagsCommentsCommentIdPost**](TagApiApi.md#apiTagsCommentsCommentIdPost) | **POST** /api/tags/comments/{commentId} | 
[**apiTagsGet**](TagApiApi.md#apiTagsGet) | **GET** /api/tags | 
[**apiTagsIdDelete**](TagApiApi.md#apiTagsIdDelete) | **DELETE** /api/tags/{id} | 
[**apiTagsIdGet**](TagApiApi.md#apiTagsIdGet) | **GET** /api/tags/{id} | 
[**apiTagsNamesGet**](TagApiApi.md#apiTagsNamesGet) | **GET** /api/tags/names | 
[**apiTagsPost**](TagApiApi.md#apiTagsPost) | **POST** /api/tags | 
[**apiTagsTagIdChildrenGet**](TagApiApi.md#apiTagsTagIdChildrenGet) | **GET** /api/tags/{tagId}/children | 
[**apiTagsTagIdCommentsGet**](TagApiApi.md#apiTagsTagIdCommentsGet) | **GET** /api/tags/{tagId}/comments | 
[**apiTagsTagIdCommentsPost**](TagApiApi.md#apiTagsTagIdCommentsPost) | **POST** /api/tags/{tagId}/comments | 
[**apiTagsTagIdReportsPost**](TagApiApi.md#apiTagsTagIdReportsPost) | **POST** /api/tags/{tagId}/reports | 
[**apiTagsTopGet**](TagApiApi.md#apiTagsTopGet) | **GET** /api/tags/top | 



## apiTagsByNameNameGet

> TagForApiContract apiTagsByNameNameGet(name, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.TagApiApi();
let name = "name_example"; // String | 
let opts = {
  'fields': new VocaDbWeb.TagOptionalFields(), // TagOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiTagsByNameNameGet(name, opts, (error, data, response) => {
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
 **name** | **String**|  | 
 **fields** | [**TagOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**TagForApiContract**](TagForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiTagsCategoryNamesGet

> [String] apiTagsCategoryNamesGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.TagApiApi();
let opts = {
  'query': "''", // String | 
  'nameMatchMode': new VocaDbWeb.NameMatchMode() // NameMatchMode | 
};
apiInstance.apiTagsCategoryNamesGet(opts, (error, data, response) => {
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
 **query** | **String**|  | [optional] [default to &#39;&#39;]
 **nameMatchMode** | [**NameMatchMode**](.md)|  | [optional] 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiTagsCommentsCommentIdDelete

> apiTagsCommentsCommentIdDelete(commentId)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.TagApiApi();
let commentId = 56; // Number | 
apiInstance.apiTagsCommentsCommentIdDelete(commentId, (error, data, response) => {
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


## apiTagsCommentsCommentIdPost

> apiTagsCommentsCommentIdPost(commentId, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.TagApiApi();
let commentId = 56; // Number | 
let opts = {
  'commentForApiContract': new VocaDbWeb.CommentForApiContract() // CommentForApiContract | 
};
apiInstance.apiTagsCommentsCommentIdPost(commentId, opts, (error, data, response) => {
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


## apiTagsGet

> TagForApiContractPartialFindResult apiTagsGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.TagApiApi();
let opts = {
  'query': "''", // String | 
  'allowChildren': true, // Boolean | 
  'categoryName': "''", // String | 
  'start': 0, // Number | 
  'maxResults': 10, // Number | 
  'getTotalCount': false, // Boolean | 
  'nameMatchMode': new VocaDbWeb.NameMatchMode(), // NameMatchMode | 
  'sort': new VocaDbWeb.TagSortRule(), // TagSortRule | 
  'preferAccurateMatches': false, // Boolean | 
  'fields': new VocaDbWeb.TagOptionalFields(), // TagOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference(), // ContentLanguagePreference | 
  'target': new VocaDbWeb.TagTargetTypes() // TagTargetTypes | 
};
apiInstance.apiTagsGet(opts, (error, data, response) => {
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
 **query** | **String**|  | [optional] [default to &#39;&#39;]
 **allowChildren** | **Boolean**|  | [optional] [default to true]
 **categoryName** | **String**|  | [optional] [default to &#39;&#39;]
 **start** | **Number**|  | [optional] [default to 0]
 **maxResults** | **Number**|  | [optional] [default to 10]
 **getTotalCount** | **Boolean**|  | [optional] [default to false]
 **nameMatchMode** | [**NameMatchMode**](.md)|  | [optional] 
 **sort** | [**TagSortRule**](.md)|  | [optional] 
 **preferAccurateMatches** | **Boolean**|  | [optional] [default to false]
 **fields** | [**TagOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 
 **target** | [**TagTargetTypes**](.md)|  | [optional] 

### Return type

[**TagForApiContractPartialFindResult**](TagForApiContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiTagsIdDelete

> apiTagsIdDelete(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.TagApiApi();
let id = 56; // Number | 
let opts = {
  'notes': "''", // String | 
  'hardDelete': false // Boolean | 
};
apiInstance.apiTagsIdDelete(id, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **notes** | **String**|  | [optional] [default to &#39;&#39;]
 **hardDelete** | **Boolean**|  | [optional] [default to false]

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTagsIdGet

> TagForApiContract apiTagsIdGet(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.TagApiApi();
let id = 56; // Number | 
let opts = {
  'fields': new VocaDbWeb.TagOptionalFields(), // TagOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiTagsIdGet(id, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **fields** | [**TagOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**TagForApiContract**](TagForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiTagsNamesGet

> [String] apiTagsNamesGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.TagApiApi();
let opts = {
  'query': "''", // String | 
  'allowAliases': true, // Boolean | 
  'maxResults': 10 // Number | 
};
apiInstance.apiTagsNamesGet(opts, (error, data, response) => {
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
 **query** | **String**|  | [optional] [default to &#39;&#39;]
 **allowAliases** | **Boolean**|  | [optional] [default to true]
 **maxResults** | **Number**|  | [optional] [default to 10]

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiTagsPost

> TagBaseContract apiTagsPost(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.TagApiApi();
let opts = {
  'name': "name_example" // String | 
};
apiInstance.apiTagsPost(opts, (error, data, response) => {
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
 **name** | **String**|  | [optional] 

### Return type

[**TagBaseContract**](TagBaseContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiTagsTagIdChildrenGet

> [TagForApiContract] apiTagsTagIdChildrenGet(tagId, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.TagApiApi();
let tagId = 56; // Number | 
let opts = {
  'fields': new VocaDbWeb.TagOptionalFields(), // TagOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiTagsTagIdChildrenGet(tagId, opts, (error, data, response) => {
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
 **tagId** | **Number**|  | 
 **fields** | [**TagOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**[TagForApiContract]**](TagForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiTagsTagIdCommentsGet

> CommentForApiContractPartialFindResult apiTagsTagIdCommentsGet(tagId)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.TagApiApi();
let tagId = 56; // Number | 
apiInstance.apiTagsTagIdCommentsGet(tagId, (error, data, response) => {
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
 **tagId** | **Number**|  | 

### Return type

[**CommentForApiContractPartialFindResult**](CommentForApiContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiTagsTagIdCommentsPost

> CommentForApiContract apiTagsTagIdCommentsPost(tagId, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.TagApiApi();
let tagId = 56; // Number | 
let opts = {
  'commentForApiContract': new VocaDbWeb.CommentForApiContract() // CommentForApiContract | 
};
apiInstance.apiTagsTagIdCommentsPost(tagId, opts, (error, data, response) => {
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
 **tagId** | **Number**|  | 
 **commentForApiContract** | [**CommentForApiContract**](CommentForApiContract.md)|  | [optional] 

### Return type

[**CommentForApiContract**](CommentForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## apiTagsTagIdReportsPost

> apiTagsTagIdReportsPost(tagId, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.TagApiApi();
let tagId = 56; // Number | 
let opts = {
  'reportType': new VocaDbWeb.TagReportType(), // TagReportType | 
  'notes': "notes_example", // String | 
  'versionNumber': 56 // Number | 
};
apiInstance.apiTagsTagIdReportsPost(tagId, opts, (error, data, response) => {
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
 **tagId** | **Number**|  | 
 **reportType** | [**TagReportType**](.md)|  | [optional] 
 **notes** | **String**|  | [optional] 
 **versionNumber** | **Number**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiTagsTopGet

> [TagBaseContract] apiTagsTopGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.TagApiApi();
let opts = {
  'categoryName': "categoryName_example", // String | 
  'entryType': new VocaDbWeb.EntryType(), // EntryType | 
  'maxResults': 15, // Number | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiTagsTopGet(opts, (error, data, response) => {
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
 **categoryName** | **String**|  | [optional] 
 **entryType** | [**EntryType**](.md)|  | [optional] 
 **maxResults** | **Number**|  | [optional] [default to 15]
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**[TagBaseContract]**](TagBaseContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

