# VocaDbWeb.AlbumApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiAlbumsCommentsCommentIdDelete**](AlbumApiApi.md#apiAlbumsCommentsCommentIdDelete) | **DELETE** /api/albums/comments/{commentId} | 
[**apiAlbumsCommentsCommentIdPost**](AlbumApiApi.md#apiAlbumsCommentsCommentIdPost) | **POST** /api/albums/comments/{commentId} | 
[**apiAlbumsGet**](AlbumApiApi.md#apiAlbumsGet) | **GET** /api/albums | 
[**apiAlbumsIdCommentsGet**](AlbumApiApi.md#apiAlbumsIdCommentsGet) | **GET** /api/albums/{id}/comments | 
[**apiAlbumsIdCommentsPost**](AlbumApiApi.md#apiAlbumsIdCommentsPost) | **POST** /api/albums/{id}/comments | 
[**apiAlbumsIdDelete**](AlbumApiApi.md#apiAlbumsIdDelete) | **DELETE** /api/albums/{id} | 
[**apiAlbumsIdGet**](AlbumApiApi.md#apiAlbumsIdGet) | **GET** /api/albums/{id} | 
[**apiAlbumsIdReviewsGet**](AlbumApiApi.md#apiAlbumsIdReviewsGet) | **GET** /api/albums/{id}/reviews | 
[**apiAlbumsIdReviewsPost**](AlbumApiApi.md#apiAlbumsIdReviewsPost) | **POST** /api/albums/{id}/reviews | 
[**apiAlbumsIdReviewsReviewIdDelete**](AlbumApiApi.md#apiAlbumsIdReviewsReviewIdDelete) | **DELETE** /api/albums/{id}/reviews/{reviewId} | 
[**apiAlbumsIdTracksFieldsGet**](AlbumApiApi.md#apiAlbumsIdTracksFieldsGet) | **GET** /api/albums/{id}/tracks/fields | 
[**apiAlbumsIdTracksGet**](AlbumApiApi.md#apiAlbumsIdTracksGet) | **GET** /api/albums/{id}/tracks | 
[**apiAlbumsIdUserCollectionsGet**](AlbumApiApi.md#apiAlbumsIdUserCollectionsGet) | **GET** /api/albums/{id}/user-collections | 
[**apiAlbumsNamesGet**](AlbumApiApi.md#apiAlbumsNamesGet) | **GET** /api/albums/names | 
[**apiAlbumsNewGet**](AlbumApiApi.md#apiAlbumsNewGet) | **GET** /api/albums/new | 
[**apiAlbumsTopGet**](AlbumApiApi.md#apiAlbumsTopGet) | **GET** /api/albums/top | 



## apiAlbumsCommentsCommentIdDelete

> apiAlbumsCommentsCommentIdDelete(commentId)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.AlbumApiApi();
let commentId = 56; // Number | 
apiInstance.apiAlbumsCommentsCommentIdDelete(commentId, (error, data, response) => {
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


## apiAlbumsCommentsCommentIdPost

> apiAlbumsCommentsCommentIdPost(commentId, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.AlbumApiApi();
let commentId = 56; // Number | 
let opts = {
  'commentForApiContract': new VocaDbWeb.CommentForApiContract() // CommentForApiContract | 
};
apiInstance.apiAlbumsCommentsCommentIdPost(commentId, opts, (error, data, response) => {
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


## apiAlbumsGet

> AlbumForApiContractPartialFindResult apiAlbumsGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.AlbumApiApi();
let opts = {
  'query': "''", // String | 
  'discTypes': new VocaDbWeb.DiscType(), // DiscType | 
  'tagName': ["null"], // [String] | 
  'tagId': [null], // [Number] | 
  'childTags': false, // Boolean | 
  'artistId': [null], // [Number] | 
  'artistParticipationStatus': new VocaDbWeb.ArtistAlbumParticipationStatus(), // ArtistAlbumParticipationStatus | 
  'childVoicebanks': false, // Boolean | 
  'includeMembers': false, // Boolean | 
  'barcode': "barcode_example", // String | 
  'status': new VocaDbWeb.EntryStatus(), // EntryStatus | 
  'releaseDateAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'releaseDateBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'advancedFilters': [new VocaDbWeb.AdvancedSearchFilterParams()], // [AdvancedSearchFilterParams] | 
  'start': 0, // Number | 
  'maxResults': 10, // Number | 
  'getTotalCount': false, // Boolean | 
  'sort': new VocaDbWeb.AlbumSortRule(), // AlbumSortRule | 
  'preferAccurateMatches': false, // Boolean | 
  'deleted': false, // Boolean | 
  'nameMatchMode': new VocaDbWeb.NameMatchMode(), // NameMatchMode | 
  'fields': new VocaDbWeb.AlbumOptionalFields(), // AlbumOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiAlbumsGet(opts, (error, data, response) => {
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
 **discTypes** | [**DiscType**](.md)|  | [optional] 
 **tagName** | [**[String]**](String.md)|  | [optional] 
 **tagId** | [**[Number]**](Number.md)|  | [optional] 
 **childTags** | **Boolean**|  | [optional] [default to false]
 **artistId** | [**[Number]**](Number.md)|  | [optional] 
 **artistParticipationStatus** | [**ArtistAlbumParticipationStatus**](.md)|  | [optional] 
 **childVoicebanks** | **Boolean**|  | [optional] [default to false]
 **includeMembers** | **Boolean**|  | [optional] [default to false]
 **barcode** | **String**|  | [optional] 
 **status** | [**EntryStatus**](.md)|  | [optional] 
 **releaseDateAfter** | **Date**|  | [optional] 
 **releaseDateBefore** | **Date**|  | [optional] 
 **advancedFilters** | [**[AdvancedSearchFilterParams]**](AdvancedSearchFilterParams.md)|  | [optional] 
 **start** | **Number**|  | [optional] [default to 0]
 **maxResults** | **Number**|  | [optional] [default to 10]
 **getTotalCount** | **Boolean**|  | [optional] [default to false]
 **sort** | [**AlbumSortRule**](.md)|  | [optional] 
 **preferAccurateMatches** | **Boolean**|  | [optional] [default to false]
 **deleted** | **Boolean**|  | [optional] [default to false]
 **nameMatchMode** | [**NameMatchMode**](.md)|  | [optional] 
 **fields** | [**AlbumOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**AlbumForApiContractPartialFindResult**](AlbumForApiContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiAlbumsIdCommentsGet

> [CommentForApiContract] apiAlbumsIdCommentsGet(id)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.AlbumApiApi();
let id = 56; // Number | 
apiInstance.apiAlbumsIdCommentsGet(id, (error, data, response) => {
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


## apiAlbumsIdCommentsPost

> CommentForApiContract apiAlbumsIdCommentsPost(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.AlbumApiApi();
let id = 56; // Number | 
let opts = {
  'commentForApiContract': new VocaDbWeb.CommentForApiContract() // CommentForApiContract | 
};
apiInstance.apiAlbumsIdCommentsPost(id, opts, (error, data, response) => {
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


## apiAlbumsIdDelete

> apiAlbumsIdDelete(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.AlbumApiApi();
let id = 56; // Number | 
let opts = {
  'notes': "''" // String | 
};
apiInstance.apiAlbumsIdDelete(id, opts, (error, data, response) => {
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


## apiAlbumsIdGet

> AlbumForApiContract apiAlbumsIdGet(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.AlbumApiApi();
let id = 56; // Number | 
let opts = {
  'fields': new VocaDbWeb.AlbumOptionalFields(), // AlbumOptionalFields | 
  'songFields': new VocaDbWeb.SongOptionalFields(), // SongOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiAlbumsIdGet(id, opts, (error, data, response) => {
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
 **fields** | [**AlbumOptionalFields**](.md)|  | [optional] 
 **songFields** | [**SongOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**AlbumForApiContract**](AlbumForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiAlbumsIdReviewsGet

> [AlbumReviewContract] apiAlbumsIdReviewsGet(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.AlbumApiApi();
let id = 56; // Number | 
let opts = {
  'languageCode': "languageCode_example" // String | 
};
apiInstance.apiAlbumsIdReviewsGet(id, opts, (error, data, response) => {
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
 **languageCode** | **String**|  | [optional] 

### Return type

[**[AlbumReviewContract]**](AlbumReviewContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiAlbumsIdReviewsPost

> AlbumReviewContract apiAlbumsIdReviewsPost(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.AlbumApiApi();
let id = 56; // Number | 
let opts = {
  'albumReviewContract': new VocaDbWeb.AlbumReviewContract() // AlbumReviewContract | 
};
apiInstance.apiAlbumsIdReviewsPost(id, opts, (error, data, response) => {
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
 **albumReviewContract** | [**AlbumReviewContract**](AlbumReviewContract.md)|  | [optional] 

### Return type

[**AlbumReviewContract**](AlbumReviewContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## apiAlbumsIdReviewsReviewIdDelete

> apiAlbumsIdReviewsReviewIdDelete(reviewId, id)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.AlbumApiApi();
let reviewId = 56; // Number | 
let id = "id_example"; // String | 
apiInstance.apiAlbumsIdReviewsReviewIdDelete(reviewId, id, (error, data, response) => {
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
 **reviewId** | **Number**|  | 
 **id** | **String**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiAlbumsIdTracksFieldsGet

> [{String: String}] apiAlbumsIdTracksFieldsGet(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.AlbumApiApi();
let id = 56; // Number | 
let opts = {
  'field': ["null"], // [String] | 
  'discNumber': 56, // Number | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiAlbumsIdTracksFieldsGet(id, opts, (error, data, response) => {
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
 **field** | [**[String]**](String.md)|  | [optional] 
 **discNumber** | **Number**|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

**[{String: String}]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiAlbumsIdTracksGet

> [SongInAlbumForApiContract] apiAlbumsIdTracksGet(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.AlbumApiApi();
let id = 56; // Number | 
let opts = {
  'fields': new VocaDbWeb.SongOptionalFields(), // SongOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiAlbumsIdTracksGet(id, opts, (error, data, response) => {
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
 **fields** | [**SongOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**[SongInAlbumForApiContract]**](SongInAlbumForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiAlbumsIdUserCollectionsGet

> [AlbumForUserForApiContract] apiAlbumsIdUserCollectionsGet(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.AlbumApiApi();
let id = 56; // Number | 
let opts = {
  'languagePreference': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiAlbumsIdUserCollectionsGet(id, opts, (error, data, response) => {
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
 **languagePreference** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**[AlbumForUserForApiContract]**](AlbumForUserForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiAlbumsNamesGet

> [String] apiAlbumsNamesGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.AlbumApiApi();
let opts = {
  'query': "''", // String | 
  'nameMatchMode': new VocaDbWeb.NameMatchMode(), // NameMatchMode | 
  'maxResults': 15 // Number | 
};
apiInstance.apiAlbumsNamesGet(opts, (error, data, response) => {
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


## apiAlbumsNewGet

> [AlbumForApiContract] apiAlbumsNewGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.AlbumApiApi();
let opts = {
  'languagePreference': new VocaDbWeb.ContentLanguagePreference(), // ContentLanguagePreference | 
  'fields': new VocaDbWeb.AlbumOptionalFields() // AlbumOptionalFields | 
};
apiInstance.apiAlbumsNewGet(opts, (error, data, response) => {
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
 **languagePreference** | [**ContentLanguagePreference**](.md)|  | [optional] 
 **fields** | [**AlbumOptionalFields**](.md)|  | [optional] 

### Return type

[**[AlbumForApiContract]**](AlbumForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiAlbumsTopGet

> [AlbumForApiContract] apiAlbumsTopGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.AlbumApiApi();
let opts = {
  'ignoreIds': [null], // [Number] | 
  'languagePreference': new VocaDbWeb.ContentLanguagePreference(), // ContentLanguagePreference | 
  'fields': new VocaDbWeb.AlbumOptionalFields() // AlbumOptionalFields | 
};
apiInstance.apiAlbumsTopGet(opts, (error, data, response) => {
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
 **ignoreIds** | [**[Number]**](Number.md)|  | [optional] 
 **languagePreference** | [**ContentLanguagePreference**](.md)|  | [optional] 
 **fields** | [**AlbumOptionalFields**](.md)|  | [optional] 

### Return type

[**[AlbumForApiContract]**](AlbumForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

