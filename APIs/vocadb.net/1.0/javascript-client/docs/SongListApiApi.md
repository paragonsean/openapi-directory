# VocaDbWeb.SongListApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiSongListsCommentsCommentIdDelete**](SongListApiApi.md#apiSongListsCommentsCommentIdDelete) | **DELETE** /api/songLists/comments/{commentId} | 
[**apiSongListsCommentsCommentIdPost**](SongListApiApi.md#apiSongListsCommentsCommentIdPost) | **POST** /api/songLists/comments/{commentId} | 
[**apiSongListsFeaturedGet**](SongListApiApi.md#apiSongListsFeaturedGet) | **GET** /api/songLists/featured | 
[**apiSongListsFeaturedNamesGet**](SongListApiApi.md#apiSongListsFeaturedNamesGet) | **GET** /api/songLists/featured/names | 
[**apiSongListsIdDelete**](SongListApiApi.md#apiSongListsIdDelete) | **DELETE** /api/songLists/{id} | 
[**apiSongListsListIdCommentsGet**](SongListApiApi.md#apiSongListsListIdCommentsGet) | **GET** /api/songLists/{listId}/comments | 
[**apiSongListsListIdCommentsPost**](SongListApiApi.md#apiSongListsListIdCommentsPost) | **POST** /api/songLists/{listId}/comments | 
[**apiSongListsListIdSongsGet**](SongListApiApi.md#apiSongListsListIdSongsGet) | **GET** /api/songLists/{listId}/songs | 
[**apiSongListsPost**](SongListApiApi.md#apiSongListsPost) | **POST** /api/songLists | 



## apiSongListsCommentsCommentIdDelete

> apiSongListsCommentsCommentIdDelete(commentId)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongListApiApi();
let commentId = 56; // Number | 
apiInstance.apiSongListsCommentsCommentIdDelete(commentId, (error, data, response) => {
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


## apiSongListsCommentsCommentIdPost

> apiSongListsCommentsCommentIdPost(commentId, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongListApiApi();
let commentId = 56; // Number | 
let opts = {
  'commentForApiContract': new VocaDbWeb.CommentForApiContract() // CommentForApiContract | 
};
apiInstance.apiSongListsCommentsCommentIdPost(commentId, opts, (error, data, response) => {
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


## apiSongListsFeaturedGet

> SongListForApiContractPartialFindResult apiSongListsFeaturedGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongListApiApi();
let opts = {
  'query': "''", // String | 
  'tagId': [null], // [Number] | 
  'childTags': false, // Boolean | 
  'nameMatchMode': new VocaDbWeb.NameMatchMode(), // NameMatchMode | 
  'featuredCategory': new VocaDbWeb.SongListFeaturedCategory(), // SongListFeaturedCategory | 
  'start': 0, // Number | 
  'maxResults': 10, // Number | 
  'getTotalCount': false, // Boolean | 
  'sort': new VocaDbWeb.SongListSortRule(), // SongListSortRule | 
  'fields': new VocaDbWeb.SongListOptionalFields(), // SongListOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiSongListsFeaturedGet(opts, (error, data, response) => {
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
 **tagId** | [**[Number]**](Number.md)|  | [optional] 
 **childTags** | **Boolean**|  | [optional] [default to false]
 **nameMatchMode** | [**NameMatchMode**](.md)|  | [optional] 
 **featuredCategory** | [**SongListFeaturedCategory**](.md)|  | [optional] 
 **start** | **Number**|  | [optional] [default to 0]
 **maxResults** | **Number**|  | [optional] [default to 10]
 **getTotalCount** | **Boolean**|  | [optional] [default to false]
 **sort** | [**SongListSortRule**](.md)|  | [optional] 
 **fields** | [**SongListOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**SongListForApiContractPartialFindResult**](SongListForApiContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiSongListsFeaturedNamesGet

> [String] apiSongListsFeaturedNamesGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongListApiApi();
let opts = {
  'query': "''", // String | 
  'nameMatchMode': new VocaDbWeb.NameMatchMode(), // NameMatchMode | 
  'featuredCategory': new VocaDbWeb.SongListFeaturedCategory(), // SongListFeaturedCategory | 
  'maxResults': 10 // Number | 
};
apiInstance.apiSongListsFeaturedNamesGet(opts, (error, data, response) => {
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
 **featuredCategory** | [**SongListFeaturedCategory**](.md)|  | [optional] 
 **maxResults** | **Number**|  | [optional] [default to 10]

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiSongListsIdDelete

> apiSongListsIdDelete(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongListApiApi();
let id = 56; // Number | 
let opts = {
  'notes': "''", // String | 
  'hardDelete': false // Boolean | 
};
apiInstance.apiSongListsIdDelete(id, opts, (error, data, response) => {
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


## apiSongListsListIdCommentsGet

> CommentForApiContractPartialFindResult apiSongListsListIdCommentsGet(listId)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongListApiApi();
let listId = 56; // Number | 
apiInstance.apiSongListsListIdCommentsGet(listId, (error, data, response) => {
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
 **listId** | **Number**|  | 

### Return type

[**CommentForApiContractPartialFindResult**](CommentForApiContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiSongListsListIdCommentsPost

> CommentForApiContract apiSongListsListIdCommentsPost(listId, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongListApiApi();
let listId = 56; // Number | 
let opts = {
  'commentForApiContract': new VocaDbWeb.CommentForApiContract() // CommentForApiContract | 
};
apiInstance.apiSongListsListIdCommentsPost(listId, opts, (error, data, response) => {
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
 **listId** | **Number**|  | 
 **commentForApiContract** | [**CommentForApiContract**](CommentForApiContract.md)|  | [optional] 

### Return type

[**CommentForApiContract**](CommentForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## apiSongListsListIdSongsGet

> SongInListForApiContractPartialFindResult apiSongListsListIdSongsGet(listId, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongListApiApi();
let listId = 56; // Number | 
let opts = {
  'query': "''", // String | 
  'songTypes': "songTypes_example", // String | 
  'pvServices': new VocaDbWeb.PVServices(), // PVServices | 
  'tagId': [null], // [Number] | 
  'artistId': [null], // [Number] | 
  'childVoicebanks': false, // Boolean | 
  'advancedFilters': [new VocaDbWeb.AdvancedSearchFilterParams()], // [AdvancedSearchFilterParams] | 
  'start': 0, // Number | 
  'maxResults': 10, // Number | 
  'getTotalCount': false, // Boolean | 
  'sort': new VocaDbWeb.SongSortRule(), // SongSortRule | 
  'nameMatchMode': new VocaDbWeb.NameMatchMode(), // NameMatchMode | 
  'fields': new VocaDbWeb.SongOptionalFields(), // SongOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiSongListsListIdSongsGet(listId, opts, (error, data, response) => {
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
 **listId** | **Number**|  | 
 **query** | **String**|  | [optional] [default to &#39;&#39;]
 **songTypes** | **String**|  | [optional] 
 **pvServices** | [**PVServices**](.md)|  | [optional] 
 **tagId** | [**[Number]**](Number.md)|  | [optional] 
 **artistId** | [**[Number]**](Number.md)|  | [optional] 
 **childVoicebanks** | **Boolean**|  | [optional] [default to false]
 **advancedFilters** | [**[AdvancedSearchFilterParams]**](AdvancedSearchFilterParams.md)|  | [optional] 
 **start** | **Number**|  | [optional] [default to 0]
 **maxResults** | **Number**|  | [optional] [default to 10]
 **getTotalCount** | **Boolean**|  | [optional] [default to false]
 **sort** | [**SongSortRule**](.md)|  | [optional] 
 **nameMatchMode** | [**NameMatchMode**](.md)|  | [optional] 
 **fields** | [**SongOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**SongInListForApiContractPartialFindResult**](SongInListForApiContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiSongListsPost

> Number apiSongListsPost(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongListApiApi();
let opts = {
  'songListForEditForApiContract': new VocaDbWeb.SongListForEditForApiContract() // SongListForEditForApiContract | 
};
apiInstance.apiSongListsPost(opts, (error, data, response) => {
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
 **songListForEditForApiContract** | [**SongListForEditForApiContract**](SongListForEditForApiContract.md)|  | [optional] 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain

