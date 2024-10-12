# VocaDbWeb.ArtistApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiArtistsCommentsCommentIdDelete**](ArtistApiApi.md#apiArtistsCommentsCommentIdDelete) | **DELETE** /api/artists/comments/{commentId} | 
[**apiArtistsCommentsCommentIdPost**](ArtistApiApi.md#apiArtistsCommentsCommentIdPost) | **POST** /api/artists/comments/{commentId} | 
[**apiArtistsGet**](ArtistApiApi.md#apiArtistsGet) | **GET** /api/artists | 
[**apiArtistsIdCommentsGet**](ArtistApiApi.md#apiArtistsIdCommentsGet) | **GET** /api/artists/{id}/comments | 
[**apiArtistsIdCommentsPost**](ArtistApiApi.md#apiArtistsIdCommentsPost) | **POST** /api/artists/{id}/comments | 
[**apiArtistsIdDelete**](ArtistApiApi.md#apiArtistsIdDelete) | **DELETE** /api/artists/{id} | 
[**apiArtistsIdGet**](ArtistApiApi.md#apiArtistsIdGet) | **GET** /api/artists/{id} | 
[**apiArtistsNamesGet**](ArtistApiApi.md#apiArtistsNamesGet) | **GET** /api/artists/names | 



## apiArtistsCommentsCommentIdDelete

> apiArtistsCommentsCommentIdDelete(commentId)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.ArtistApiApi();
let commentId = 56; // Number | 
apiInstance.apiArtistsCommentsCommentIdDelete(commentId, (error, data, response) => {
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


## apiArtistsCommentsCommentIdPost

> apiArtistsCommentsCommentIdPost(commentId, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.ArtistApiApi();
let commentId = 56; // Number | 
let opts = {
  'commentForApiContract': new VocaDbWeb.CommentForApiContract() // CommentForApiContract | 
};
apiInstance.apiArtistsCommentsCommentIdPost(commentId, opts, (error, data, response) => {
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


## apiArtistsGet

> ArtistForApiContractPartialFindResult apiArtistsGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.ArtistApiApi();
let opts = {
  'query': "''", // String | 
  'artistTypes': "artistTypes_example", // String | 
  'allowBaseVoicebanks': true, // Boolean | 
  'tagName': ["null"], // [String] | 
  'tagId': [null], // [Number] | 
  'childTags': false, // Boolean | 
  'followedByUserId': 56, // Number | 
  'status': new VocaDbWeb.EntryStatus(), // EntryStatus | 
  'advancedFilters': [new VocaDbWeb.AdvancedSearchFilterParams()], // [AdvancedSearchFilterParams] | 
  'start': 0, // Number | 
  'maxResults': 10, // Number | 
  'getTotalCount': false, // Boolean | 
  'sort': new VocaDbWeb.ArtistSortRule(), // ArtistSortRule | 
  'preferAccurateMatches': false, // Boolean | 
  'nameMatchMode': new VocaDbWeb.NameMatchMode(), // NameMatchMode | 
  'fields': new VocaDbWeb.ArtistOptionalFields(), // ArtistOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiArtistsGet(opts, (error, data, response) => {
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
 **artistTypes** | **String**|  | [optional] 
 **allowBaseVoicebanks** | **Boolean**|  | [optional] [default to true]
 **tagName** | [**[String]**](String.md)|  | [optional] 
 **tagId** | [**[Number]**](Number.md)|  | [optional] 
 **childTags** | **Boolean**|  | [optional] [default to false]
 **followedByUserId** | **Number**|  | [optional] 
 **status** | [**EntryStatus**](.md)|  | [optional] 
 **advancedFilters** | [**[AdvancedSearchFilterParams]**](AdvancedSearchFilterParams.md)|  | [optional] 
 **start** | **Number**|  | [optional] [default to 0]
 **maxResults** | **Number**|  | [optional] [default to 10]
 **getTotalCount** | **Boolean**|  | [optional] [default to false]
 **sort** | [**ArtistSortRule**](.md)|  | [optional] 
 **preferAccurateMatches** | **Boolean**|  | [optional] [default to false]
 **nameMatchMode** | [**NameMatchMode**](.md)|  | [optional] 
 **fields** | [**ArtistOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**ArtistForApiContractPartialFindResult**](ArtistForApiContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiArtistsIdCommentsGet

> [CommentForApiContract] apiArtistsIdCommentsGet(id)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.ArtistApiApi();
let id = 56; // Number | 
apiInstance.apiArtistsIdCommentsGet(id, (error, data, response) => {
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

### Return type

[**[CommentForApiContract]**](CommentForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiArtistsIdCommentsPost

> CommentForApiContract apiArtistsIdCommentsPost(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.ArtistApiApi();
let id = 56; // Number | 
let opts = {
  'commentForApiContract': new VocaDbWeb.CommentForApiContract() // CommentForApiContract | 
};
apiInstance.apiArtistsIdCommentsPost(id, opts, (error, data, response) => {
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
 **commentForApiContract** | [**CommentForApiContract**](CommentForApiContract.md)|  | [optional] 

### Return type

[**CommentForApiContract**](CommentForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## apiArtistsIdDelete

> apiArtistsIdDelete(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.ArtistApiApi();
let id = 56; // Number | 
let opts = {
  'notes': "''" // String | 
};
apiInstance.apiArtistsIdDelete(id, opts, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiArtistsIdGet

> ArtistForApiContract apiArtistsIdGet(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.ArtistApiApi();
let id = 56; // Number | 
let opts = {
  'fields': new VocaDbWeb.ArtistOptionalFields(), // ArtistOptionalFields | 
  'relations': new VocaDbWeb.ArtistRelationsFields(), // ArtistRelationsFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiArtistsIdGet(id, opts, (error, data, response) => {
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
 **fields** | [**ArtistOptionalFields**](.md)|  | [optional] 
 **relations** | [**ArtistRelationsFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**ArtistForApiContract**](ArtistForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiArtistsNamesGet

> [String] apiArtistsNamesGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.ArtistApiApi();
let opts = {
  'query': "''", // String | 
  'nameMatchMode': new VocaDbWeb.NameMatchMode(), // NameMatchMode | 
  'maxResults': 15 // Number | 
};
apiInstance.apiArtistsNamesGet(opts, (error, data, response) => {
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
 **maxResults** | **Number**|  | [optional] [default to 15]

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

