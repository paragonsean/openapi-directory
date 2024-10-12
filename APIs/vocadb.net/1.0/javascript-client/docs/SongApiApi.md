# VocaDbWeb.SongApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiSongsByPvGet**](SongApiApi.md#apiSongsByPvGet) | **GET** /api/songs/byPv | 
[**apiSongsCommentsCommentIdDelete**](SongApiApi.md#apiSongsCommentsCommentIdDelete) | **DELETE** /api/songs/comments/{commentId} | 
[**apiSongsCommentsCommentIdPost**](SongApiApi.md#apiSongsCommentsCommentIdPost) | **POST** /api/songs/comments/{commentId} | 
[**apiSongsGet**](SongApiApi.md#apiSongsGet) | **GET** /api/songs | 
[**apiSongsHighlightedGet**](SongApiApi.md#apiSongsHighlightedGet) | **GET** /api/songs/highlighted | 
[**apiSongsIdCommentsGet**](SongApiApi.md#apiSongsIdCommentsGet) | **GET** /api/songs/{id}/comments | 
[**apiSongsIdCommentsPost**](SongApiApi.md#apiSongsIdCommentsPost) | **POST** /api/songs/{id}/comments | 
[**apiSongsIdDelete**](SongApiApi.md#apiSongsIdDelete) | **DELETE** /api/songs/{id} | 
[**apiSongsIdDerivedGet**](SongApiApi.md#apiSongsIdDerivedGet) | **GET** /api/songs/{id}/derived | 
[**apiSongsIdGet**](SongApiApi.md#apiSongsIdGet) | **GET** /api/songs/{id} | 
[**apiSongsIdRatingsGet**](SongApiApi.md#apiSongsIdRatingsGet) | **GET** /api/songs/{id}/ratings | 
[**apiSongsIdRatingsPost**](SongApiApi.md#apiSongsIdRatingsPost) | **POST** /api/songs/{id}/ratings | 
[**apiSongsIdRelatedGet**](SongApiApi.md#apiSongsIdRelatedGet) | **GET** /api/songs/{id}/related | 
[**apiSongsLyricsLyricsIdGet**](SongApiApi.md#apiSongsLyricsLyricsIdGet) | **GET** /api/songs/lyrics/{lyricsId} | 
[**apiSongsNamesGet**](SongApiApi.md#apiSongsNamesGet) | **GET** /api/songs/names | 
[**apiSongsTopRatedGet**](SongApiApi.md#apiSongsTopRatedGet) | **GET** /api/songs/top-rated | 



## apiSongsByPvGet

> SongForApiContract apiSongsByPvGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongApiApi();
let opts = {
  'pvService': new VocaDbWeb.PVService(), // PVService | 
  'pvId': "pvId_example", // String | 
  'fields': new VocaDbWeb.SongOptionalFields(), // SongOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiSongsByPvGet(opts, (error, data, response) => {
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
 **pvService** | [**PVService**](.md)|  | [optional] 
 **pvId** | **String**|  | [optional] 
 **fields** | [**SongOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**SongForApiContract**](SongForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiSongsCommentsCommentIdDelete

> apiSongsCommentsCommentIdDelete(commentId)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongApiApi();
let commentId = 56; // Number | 
apiInstance.apiSongsCommentsCommentIdDelete(commentId, (error, data, response) => {
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


## apiSongsCommentsCommentIdPost

> apiSongsCommentsCommentIdPost(commentId, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongApiApi();
let commentId = 56; // Number | 
let opts = {
  'commentForApiContract': new VocaDbWeb.CommentForApiContract() // CommentForApiContract | 
};
apiInstance.apiSongsCommentsCommentIdPost(commentId, opts, (error, data, response) => {
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


## apiSongsGet

> SongForApiContractPartialFindResult apiSongsGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongApiApi();
let opts = {
  'query': "''", // String | 
  'songTypes': "songTypes_example", // String | 
  'afterDate': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'beforeDate': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'tagName': ["null"], // [String] | 
  'tagId': [null], // [Number] | 
  'childTags': false, // Boolean | 
  'unifyTypesAndTags': false, // Boolean | 
  'artistId': [null], // [Number] | 
  'artistParticipationStatus': new VocaDbWeb.ArtistAlbumParticipationStatus(), // ArtistAlbumParticipationStatus | 
  'childVoicebanks': false, // Boolean | 
  'includeMembers': false, // Boolean | 
  'onlyWithPvs': false, // Boolean | 
  'pvServices': new VocaDbWeb.PVServices(), // PVServices | 
  'since': 56, // Number | 
  'minScore': 56, // Number | 
  'userCollectionId': 56, // Number | 
  'releaseEventId': 56, // Number | 
  'parentSongId': 56, // Number | 
  'status': new VocaDbWeb.EntryStatus(), // EntryStatus | 
  'advancedFilters': [new VocaDbWeb.AdvancedSearchFilterParams()], // [AdvancedSearchFilterParams] | 
  'start': 0, // Number | 
  'maxResults': 10, // Number | 
  'getTotalCount': false, // Boolean | 
  'sort': new VocaDbWeb.SongSortRule(), // SongSortRule | 
  'preferAccurateMatches': false, // Boolean | 
  'nameMatchMode': new VocaDbWeb.NameMatchMode(), // NameMatchMode | 
  'fields': new VocaDbWeb.SongOptionalFields(), // SongOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference(), // ContentLanguagePreference | 
  'minMilliBpm': 56, // Number | 
  'maxMilliBpm': 56, // Number | 
  'minLength': 56, // Number | 
  'maxLength': 56 // Number | 
};
apiInstance.apiSongsGet(opts, (error, data, response) => {
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
 **songTypes** | **String**|  | [optional] 
 **afterDate** | **Date**|  | [optional] 
 **beforeDate** | **Date**|  | [optional] 
 **tagName** | [**[String]**](String.md)|  | [optional] 
 **tagId** | [**[Number]**](Number.md)|  | [optional] 
 **childTags** | **Boolean**|  | [optional] [default to false]
 **unifyTypesAndTags** | **Boolean**|  | [optional] [default to false]
 **artistId** | [**[Number]**](Number.md)|  | [optional] 
 **artistParticipationStatus** | [**ArtistAlbumParticipationStatus**](.md)|  | [optional] 
 **childVoicebanks** | **Boolean**|  | [optional] [default to false]
 **includeMembers** | **Boolean**|  | [optional] [default to false]
 **onlyWithPvs** | **Boolean**|  | [optional] [default to false]
 **pvServices** | [**PVServices**](.md)|  | [optional] 
 **since** | **Number**|  | [optional] 
 **minScore** | **Number**|  | [optional] 
 **userCollectionId** | **Number**|  | [optional] 
 **releaseEventId** | **Number**|  | [optional] 
 **parentSongId** | **Number**|  | [optional] 
 **status** | [**EntryStatus**](.md)|  | [optional] 
 **advancedFilters** | [**[AdvancedSearchFilterParams]**](AdvancedSearchFilterParams.md)|  | [optional] 
 **start** | **Number**|  | [optional] [default to 0]
 **maxResults** | **Number**|  | [optional] [default to 10]
 **getTotalCount** | **Boolean**|  | [optional] [default to false]
 **sort** | [**SongSortRule**](.md)|  | [optional] 
 **preferAccurateMatches** | **Boolean**|  | [optional] [default to false]
 **nameMatchMode** | [**NameMatchMode**](.md)|  | [optional] 
 **fields** | [**SongOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 
 **minMilliBpm** | **Number**|  | [optional] 
 **maxMilliBpm** | **Number**|  | [optional] 
 **minLength** | **Number**|  | [optional] 
 **maxLength** | **Number**|  | [optional] 

### Return type

[**SongForApiContractPartialFindResult**](SongForApiContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiSongsHighlightedGet

> [SongForApiContract] apiSongsHighlightedGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongApiApi();
let opts = {
  'languagePreference': new VocaDbWeb.ContentLanguagePreference(), // ContentLanguagePreference | 
  'fields': new VocaDbWeb.SongOptionalFields() // SongOptionalFields | 
};
apiInstance.apiSongsHighlightedGet(opts, (error, data, response) => {
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
 **fields** | [**SongOptionalFields**](.md)|  | [optional] 

### Return type

[**[SongForApiContract]**](SongForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiSongsIdCommentsGet

> [CommentForApiContract] apiSongsIdCommentsGet(id)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongApiApi();
let id = 56; // Number | 
apiInstance.apiSongsIdCommentsGet(id, (error, data, response) => {
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


## apiSongsIdCommentsPost

> CommentForApiContract apiSongsIdCommentsPost(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongApiApi();
let id = 56; // Number | 
let opts = {
  'commentForApiContract': new VocaDbWeb.CommentForApiContract() // CommentForApiContract | 
};
apiInstance.apiSongsIdCommentsPost(id, opts, (error, data, response) => {
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


## apiSongsIdDelete

> apiSongsIdDelete(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongApiApi();
let id = 56; // Number | 
let opts = {
  'notes': "''" // String | 
};
apiInstance.apiSongsIdDelete(id, opts, (error, data, response) => {
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


## apiSongsIdDerivedGet

> [SongForApiContract] apiSongsIdDerivedGet(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongApiApi();
let id = 56; // Number | 
let opts = {
  'fields': new VocaDbWeb.SongOptionalFields(), // SongOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiSongsIdDerivedGet(id, opts, (error, data, response) => {
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

[**[SongForApiContract]**](SongForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiSongsIdGet

> SongForApiContract apiSongsIdGet(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongApiApi();
let id = 56; // Number | 
let opts = {
  'fields': new VocaDbWeb.SongOptionalFields(), // SongOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiSongsIdGet(id, opts, (error, data, response) => {
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

[**SongForApiContract**](SongForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiSongsIdRatingsGet

> [RatedSongForUserForApiContract] apiSongsIdRatingsGet(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongApiApi();
let id = 56; // Number | 
let opts = {
  'userFields': new VocaDbWeb.UserOptionalFields(), // UserOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiSongsIdRatingsGet(id, opts, (error, data, response) => {
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
 **userFields** | [**UserOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**[RatedSongForUserForApiContract]**](RatedSongForUserForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiSongsIdRatingsPost

> apiSongsIdRatingsPost(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongApiApi();
let id = 56; // Number | 
let opts = {
  'songRatingContract': new VocaDbWeb.SongRatingContract() // SongRatingContract | 
};
apiInstance.apiSongsIdRatingsPost(id, opts, (error, data, response) => {
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
 **songRatingContract** | [**SongRatingContract**](SongRatingContract.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: Not defined


## apiSongsIdRelatedGet

> RelatedSongsContract apiSongsIdRelatedGet(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongApiApi();
let id = 56; // Number | 
let opts = {
  'fields': new VocaDbWeb.SongOptionalFields(), // SongOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiSongsIdRelatedGet(id, opts, (error, data, response) => {
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

[**RelatedSongsContract**](RelatedSongsContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiSongsLyricsLyricsIdGet

> LyricsForSongContract apiSongsLyricsLyricsIdGet(lyricsId)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongApiApi();
let lyricsId = 56; // Number | 
apiInstance.apiSongsLyricsLyricsIdGet(lyricsId, (error, data, response) => {
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
 **lyricsId** | **Number**|  | 

### Return type

[**LyricsForSongContract**](LyricsForSongContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiSongsNamesGet

> [String] apiSongsNamesGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongApiApi();
let opts = {
  'query': "''", // String | 
  'nameMatchMode': new VocaDbWeb.NameMatchMode(), // NameMatchMode | 
  'maxResults': 15 // Number | 
};
apiInstance.apiSongsNamesGet(opts, (error, data, response) => {
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


## apiSongsTopRatedGet

> [SongForApiContract] apiSongsTopRatedGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.SongApiApi();
let opts = {
  'durationHours': 56, // Number | 
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'filterBy': new VocaDbWeb.TopSongsDateFilterType(), // TopSongsDateFilterType | 
  'vocalist': new VocaDbWeb.SongVocalistSelection(), // SongVocalistSelection | 
  'maxResults': 25, // Number | 
  'fields': new VocaDbWeb.SongOptionalFields(), // SongOptionalFields | 
  'languagePreference': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiSongsTopRatedGet(opts, (error, data, response) => {
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
 **durationHours** | **Number**|  | [optional] 
 **startDate** | **Date**|  | [optional] 
 **filterBy** | [**TopSongsDateFilterType**](.md)|  | [optional] 
 **vocalist** | [**SongVocalistSelection**](.md)|  | [optional] 
 **maxResults** | **Number**|  | [optional] [default to 25]
 **fields** | [**SongOptionalFields**](.md)|  | [optional] 
 **languagePreference** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**[SongForApiContract]**](SongForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain

