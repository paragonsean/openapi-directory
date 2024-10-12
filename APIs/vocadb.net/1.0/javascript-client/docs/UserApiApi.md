# VocaDbWeb.UserApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiUsersCurrentAlbumCollectionStatusesAlbumIdGet**](UserApiApi.md#apiUsersCurrentAlbumCollectionStatusesAlbumIdGet) | **GET** /api/users/current/album-collection-statuses/{albumId} | 
[**apiUsersCurrentAlbumsAlbumIdPost**](UserApiApi.md#apiUsersCurrentAlbumsAlbumIdPost) | **POST** /api/users/current/albums/{albumId} | 
[**apiUsersCurrentFollowedArtistsArtistIdGet**](UserApiApi.md#apiUsersCurrentFollowedArtistsArtistIdGet) | **GET** /api/users/current/followedArtists/{artistId} | 
[**apiUsersCurrentFollowedTagsTagIdDelete**](UserApiApi.md#apiUsersCurrentFollowedTagsTagIdDelete) | **DELETE** /api/users/current/followedTags/{tagId} | 
[**apiUsersCurrentFollowedTagsTagIdPost**](UserApiApi.md#apiUsersCurrentFollowedTagsTagIdPost) | **POST** /api/users/current/followedTags/{tagId} | 
[**apiUsersCurrentGet**](UserApiApi.md#apiUsersCurrentGet) | **GET** /api/users/current | 
[**apiUsersCurrentRatedSongsSongIdGet**](UserApiApi.md#apiUsersCurrentRatedSongsSongIdGet) | **GET** /api/users/current/ratedSongs/{songId} | 
[**apiUsersCurrentRefreshEntryEditPost**](UserApiApi.md#apiUsersCurrentRefreshEntryEditPost) | **POST** /api/users/current/refreshEntryEdit | 
[**apiUsersCurrentSongTagsSongIdPost**](UserApiApi.md#apiUsersCurrentSongTagsSongIdPost) | **POST** /api/users/current/songTags/{songId} | 
[**apiUsersGet**](UserApiApi.md#apiUsersGet) | **GET** /api/users | 
[**apiUsersIdAlbumCollectionStatusesAlbumIdGet**](UserApiApi.md#apiUsersIdAlbumCollectionStatusesAlbumIdGet) | **GET** /api/users/{id}/album-collection-statuses/{albumId} | 
[**apiUsersIdAlbumsGet**](UserApiApi.md#apiUsersIdAlbumsGet) | **GET** /api/users/{id}/albums | 
[**apiUsersIdEventsGet**](UserApiApi.md#apiUsersIdEventsGet) | **GET** /api/users/{id}/events | 
[**apiUsersIdFollowedArtistsArtistIdGet**](UserApiApi.md#apiUsersIdFollowedArtistsArtistIdGet) | **GET** /api/users/{id}/followedArtists/{artistId} | 
[**apiUsersIdFollowedArtistsGet**](UserApiApi.md#apiUsersIdFollowedArtistsGet) | **GET** /api/users/{id}/followedArtists | 
[**apiUsersIdGet**](UserApiApi.md#apiUsersIdGet) | **GET** /api/users/{id} | 
[**apiUsersIdMessagesDelete**](UserApiApi.md#apiUsersIdMessagesDelete) | **DELETE** /api/users/{id}/messages | 
[**apiUsersIdMessagesGet**](UserApiApi.md#apiUsersIdMessagesGet) | **GET** /api/users/{id}/messages | 
[**apiUsersIdMessagesPost**](UserApiApi.md#apiUsersIdMessagesPost) | **POST** /api/users/{id}/messages | 
[**apiUsersIdProfileCommentsGet**](UserApiApi.md#apiUsersIdProfileCommentsGet) | **GET** /api/users/{id}/profileComments | 
[**apiUsersIdProfileCommentsPost**](UserApiApi.md#apiUsersIdProfileCommentsPost) | **POST** /api/users/{id}/profileComments | 
[**apiUsersIdRatedSongsGet**](UserApiApi.md#apiUsersIdRatedSongsGet) | **GET** /api/users/{id}/ratedSongs | 
[**apiUsersIdRatedSongsSongIdGet**](UserApiApi.md#apiUsersIdRatedSongsSongIdGet) | **GET** /api/users/{id}/ratedSongs/{songId} | 
[**apiUsersIdReportsPost**](UserApiApi.md#apiUsersIdReportsPost) | **POST** /api/users/{id}/reports | 
[**apiUsersIdSettingsSettingNamePost**](UserApiApi.md#apiUsersIdSettingsSettingNamePost) | **POST** /api/users/{id}/settings/{settingName} | 
[**apiUsersIdSongListsGet**](UserApiApi.md#apiUsersIdSongListsGet) | **GET** /api/users/{id}/songLists | 
[**apiUsersMessagesMessageIdGet**](UserApiApi.md#apiUsersMessagesMessageIdGet) | **GET** /api/users/messages/{messageId} | 
[**apiUsersNamesGet**](UserApiApi.md#apiUsersNamesGet) | **GET** /api/users/names | 
[**apiUsersProfileCommentsCommentIdDelete**](UserApiApi.md#apiUsersProfileCommentsCommentIdDelete) | **DELETE** /api/users/profileComments/{commentId} | 
[**apiUsersProfileCommentsCommentIdPost**](UserApiApi.md#apiUsersProfileCommentsCommentIdPost) | **POST** /api/users/profileComments/{commentId} | 



## apiUsersCurrentAlbumCollectionStatusesAlbumIdGet

> AlbumForUserForApiContract apiUsersCurrentAlbumCollectionStatusesAlbumIdGet(albumId)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let albumId = 56; // Number | 
apiInstance.apiUsersCurrentAlbumCollectionStatusesAlbumIdGet(albumId, (error, data, response) => {
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
 **albumId** | **Number**|  | 

### Return type

[**AlbumForUserForApiContract**](AlbumForUserForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiUsersCurrentAlbumsAlbumIdPost

> String apiUsersCurrentAlbumsAlbumIdPost(albumId, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let albumId = 56; // Number | 
let opts = {
  'collectionStatus': new VocaDbWeb.PurchaseStatus(), // PurchaseStatus | 
  'mediaType': new VocaDbWeb.MediaType(), // MediaType | 
  'rating': 56 // Number | 
};
apiInstance.apiUsersCurrentAlbumsAlbumIdPost(albumId, opts, (error, data, response) => {
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
 **albumId** | **Number**|  | 
 **collectionStatus** | [**PurchaseStatus**](.md)|  | [optional] 
 **mediaType** | [**MediaType**](.md)|  | [optional] 
 **rating** | **Number**|  | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiUsersCurrentFollowedArtistsArtistIdGet

> ArtistForUserForApiContract apiUsersCurrentFollowedArtistsArtistIdGet(artistId)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let artistId = 56; // Number | 
apiInstance.apiUsersCurrentFollowedArtistsArtistIdGet(artistId, (error, data, response) => {
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
 **artistId** | **Number**|  | 

### Return type

[**ArtistForUserForApiContract**](ArtistForUserForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiUsersCurrentFollowedTagsTagIdDelete

> apiUsersCurrentFollowedTagsTagIdDelete(tagId)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let tagId = 56; // Number | 
apiInstance.apiUsersCurrentFollowedTagsTagIdDelete(tagId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiUsersCurrentFollowedTagsTagIdPost

> apiUsersCurrentFollowedTagsTagIdPost(tagId)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let tagId = 56; // Number | 
apiInstance.apiUsersCurrentFollowedTagsTagIdPost(tagId, (error, data, response) => {
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

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiUsersCurrentGet

> UserForApiContract apiUsersCurrentGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let opts = {
  'fields': new VocaDbWeb.UserOptionalFields() // UserOptionalFields | 
};
apiInstance.apiUsersCurrentGet(opts, (error, data, response) => {
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
 **fields** | [**UserOptionalFields**](.md)|  | [optional] 

### Return type

[**UserForApiContract**](UserForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiUsersCurrentRatedSongsSongIdGet

> SongVoteRating apiUsersCurrentRatedSongsSongIdGet(songId)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let songId = 56; // Number | 
apiInstance.apiUsersCurrentRatedSongsSongIdGet(songId, (error, data, response) => {
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
 **songId** | **Number**|  | 

### Return type

[**SongVoteRating**](SongVoteRating.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiUsersCurrentRefreshEntryEditPost

> EntryEditDataContract apiUsersCurrentRefreshEntryEditPost(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let opts = {
  'entryType': new VocaDbWeb.EntryType(), // EntryType | 
  'entryId': 56 // Number | 
};
apiInstance.apiUsersCurrentRefreshEntryEditPost(opts, (error, data, response) => {
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
 **entryType** | [**EntryType**](.md)|  | [optional] 
 **entryId** | **Number**|  | [optional] 

### Return type

[**EntryEditDataContract**](EntryEditDataContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiUsersCurrentSongTagsSongIdPost

> apiUsersCurrentSongTagsSongIdPost(songId)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let songId = 56; // Number | 
apiInstance.apiUsersCurrentSongTagsSongIdPost(songId, (error, data, response) => {
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
 **songId** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiUsersGet

> UserForApiContractPartialFindResult apiUsersGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let opts = {
  'query': "''", // String | 
  'groups': new VocaDbWeb.UserGroupId(), // UserGroupId | 
  'joinDateAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'joinDateBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'nameMatchMode': new VocaDbWeb.NameMatchMode(), // NameMatchMode | 
  'start': 0, // Number | 
  'maxResults': 10, // Number | 
  'getTotalCount': false, // Boolean | 
  'sort': new VocaDbWeb.UserSortRule(), // UserSortRule | 
  'includeDisabled': false, // Boolean | 
  'onlyVerified': false, // Boolean | 
  'knowsLanguage': "knowsLanguage_example", // String | 
  'fields': new VocaDbWeb.UserOptionalFields() // UserOptionalFields | 
};
apiInstance.apiUsersGet(opts, (error, data, response) => {
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
 **groups** | [**UserGroupId**](.md)|  | [optional] 
 **joinDateAfter** | **Date**|  | [optional] 
 **joinDateBefore** | **Date**|  | [optional] 
 **nameMatchMode** | [**NameMatchMode**](.md)|  | [optional] 
 **start** | **Number**|  | [optional] [default to 0]
 **maxResults** | **Number**|  | [optional] [default to 10]
 **getTotalCount** | **Boolean**|  | [optional] [default to false]
 **sort** | [**UserSortRule**](.md)|  | [optional] 
 **includeDisabled** | **Boolean**|  | [optional] [default to false]
 **onlyVerified** | **Boolean**|  | [optional] [default to false]
 **knowsLanguage** | **String**|  | [optional] 
 **fields** | [**UserOptionalFields**](.md)|  | [optional] 

### Return type

[**UserForApiContractPartialFindResult**](UserForApiContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiUsersIdAlbumCollectionStatusesAlbumIdGet

> AlbumForUserForApiContract apiUsersIdAlbumCollectionStatusesAlbumIdGet(id, albumId)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let id = 56; // Number | 
let albumId = 56; // Number | 
apiInstance.apiUsersIdAlbumCollectionStatusesAlbumIdGet(id, albumId, (error, data, response) => {
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
 **albumId** | **Number**|  | 

### Return type

[**AlbumForUserForApiContract**](AlbumForUserForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiUsersIdAlbumsGet

> AlbumForUserForApiContractPartialFindResult apiUsersIdAlbumsGet(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let id = 56; // Number | 
let opts = {
  'query': "''", // String | 
  'tagId': 56, // Number | 
  'tag': "tag_example", // String | 
  'artistId': 56, // Number | 
  'purchaseStatuses': new VocaDbWeb.PurchaseStatuses(), // PurchaseStatuses | 
  'releaseEventId': 0, // Number | 
  'albumTypes': new VocaDbWeb.DiscType(), // DiscType | 
  'advancedFilters': [new VocaDbWeb.AdvancedSearchFilterParams()], // [AdvancedSearchFilterParams] | 
  'start': 0, // Number | 
  'maxResults': 10, // Number | 
  'getTotalCount': false, // Boolean | 
  'sort': new VocaDbWeb.AlbumSortRule(), // AlbumSortRule | 
  'nameMatchMode': new VocaDbWeb.NameMatchMode(), // NameMatchMode | 
  'fields': new VocaDbWeb.AlbumOptionalFields(), // AlbumOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference(), // ContentLanguagePreference | 
  'mediaType': new VocaDbWeb.MediaType() // MediaType | 
};
apiInstance.apiUsersIdAlbumsGet(id, opts, (error, data, response) => {
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
 **query** | **String**|  | [optional] [default to &#39;&#39;]
 **tagId** | **Number**|  | [optional] 
 **tag** | **String**|  | [optional] 
 **artistId** | **Number**|  | [optional] 
 **purchaseStatuses** | [**PurchaseStatuses**](.md)|  | [optional] 
 **releaseEventId** | **Number**|  | [optional] [default to 0]
 **albumTypes** | [**DiscType**](.md)|  | [optional] 
 **advancedFilters** | [**[AdvancedSearchFilterParams]**](AdvancedSearchFilterParams.md)|  | [optional] 
 **start** | **Number**|  | [optional] [default to 0]
 **maxResults** | **Number**|  | [optional] [default to 10]
 **getTotalCount** | **Boolean**|  | [optional] [default to false]
 **sort** | [**AlbumSortRule**](.md)|  | [optional] 
 **nameMatchMode** | [**NameMatchMode**](.md)|  | [optional] 
 **fields** | [**AlbumOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 
 **mediaType** | [**MediaType**](.md)|  | [optional] 

### Return type

[**AlbumForUserForApiContractPartialFindResult**](AlbumForUserForApiContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiUsersIdEventsGet

> [ReleaseEventForApiContract] apiUsersIdEventsGet(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let id = 56; // Number | 
let opts = {
  'relationshipType': new VocaDbWeb.UserEventRelationshipType() // UserEventRelationshipType | 
};
apiInstance.apiUsersIdEventsGet(id, opts, (error, data, response) => {
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
 **relationshipType** | [**UserEventRelationshipType**](.md)|  | [optional] 

### Return type

[**[ReleaseEventForApiContract]**](ReleaseEventForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiUsersIdFollowedArtistsArtistIdGet

> ArtistForUserForApiContract apiUsersIdFollowedArtistsArtistIdGet(id, artistId)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let id = 56; // Number | 
let artistId = 56; // Number | 
apiInstance.apiUsersIdFollowedArtistsArtistIdGet(id, artistId, (error, data, response) => {
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
 **artistId** | **Number**|  | 

### Return type

[**ArtistForUserForApiContract**](ArtistForUserForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiUsersIdFollowedArtistsGet

> ArtistForUserForApiContractPartialFindResult apiUsersIdFollowedArtistsGet(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let id = 56; // Number | 
let opts = {
  'query': "''", // String | 
  'tagId': [null], // [Number] | 
  'artistType': new VocaDbWeb.ArtistType(), // ArtistType | 
  'start': 0, // Number | 
  'maxResults': 10, // Number | 
  'getTotalCount': false, // Boolean | 
  'sort': new VocaDbWeb.ArtistSortRule(), // ArtistSortRule | 
  'nameMatchMode': new VocaDbWeb.NameMatchMode(), // NameMatchMode | 
  'fields': new VocaDbWeb.ArtistOptionalFields(), // ArtistOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiUsersIdFollowedArtistsGet(id, opts, (error, data, response) => {
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
 **query** | **String**|  | [optional] [default to &#39;&#39;]
 **tagId** | [**[Number]**](Number.md)|  | [optional] 
 **artistType** | [**ArtistType**](.md)|  | [optional] 
 **start** | **Number**|  | [optional] [default to 0]
 **maxResults** | **Number**|  | [optional] [default to 10]
 **getTotalCount** | **Boolean**|  | [optional] [default to false]
 **sort** | [**ArtistSortRule**](.md)|  | [optional] 
 **nameMatchMode** | [**NameMatchMode**](.md)|  | [optional] 
 **fields** | [**ArtistOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**ArtistForUserForApiContractPartialFindResult**](ArtistForUserForApiContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiUsersIdGet

> UserForApiContract apiUsersIdGet(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let id = 56; // Number | 
let opts = {
  'fields': new VocaDbWeb.UserOptionalFields() // UserOptionalFields | 
};
apiInstance.apiUsersIdGet(id, opts, (error, data, response) => {
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
 **fields** | [**UserOptionalFields**](.md)|  | [optional] 

### Return type

[**UserForApiContract**](UserForApiContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiUsersIdMessagesDelete

> apiUsersIdMessagesDelete(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let id = 56; // Number | 
let opts = {
  'messageId': [null] // [Number] | 
};
apiInstance.apiUsersIdMessagesDelete(id, opts, (error, data, response) => {
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
 **messageId** | [**[Number]**](Number.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiUsersIdMessagesGet

> UserMessageContractPartialFindResult apiUsersIdMessagesGet(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let id = 56; // Number | 
let opts = {
  'inbox': new VocaDbWeb.UserInboxType(), // UserInboxType | 
  'unread': false, // Boolean | 
  'anotherUserId': 56, // Number | 
  'start': 0, // Number | 
  'maxResults': 10, // Number | 
  'getTotalCount': false // Boolean | 
};
apiInstance.apiUsersIdMessagesGet(id, opts, (error, data, response) => {
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
 **inbox** | [**UserInboxType**](.md)|  | [optional] 
 **unread** | **Boolean**|  | [optional] [default to false]
 **anotherUserId** | **Number**|  | [optional] 
 **start** | **Number**|  | [optional] [default to 0]
 **maxResults** | **Number**|  | [optional] [default to 10]
 **getTotalCount** | **Boolean**|  | [optional] [default to false]

### Return type

[**UserMessageContractPartialFindResult**](UserMessageContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiUsersIdMessagesPost

> UserMessageContract apiUsersIdMessagesPost(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let id = 56; // Number | 
let opts = {
  'userMessageContract': new VocaDbWeb.UserMessageContract() // UserMessageContract | 
};
apiInstance.apiUsersIdMessagesPost(id, opts, (error, data, response) => {
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
 **userMessageContract** | [**UserMessageContract**](UserMessageContract.md)|  | [optional] 

### Return type

[**UserMessageContract**](UserMessageContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## apiUsersIdProfileCommentsGet

> CommentForApiContractPartialFindResult apiUsersIdProfileCommentsGet(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let id = 56; // Number | 
let opts = {
  'start': 0, // Number | 
  'maxResults': 10, // Number | 
  'getTotalCount': false // Boolean | 
};
apiInstance.apiUsersIdProfileCommentsGet(id, opts, (error, data, response) => {
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
 **start** | **Number**|  | [optional] [default to 0]
 **maxResults** | **Number**|  | [optional] [default to 10]
 **getTotalCount** | **Boolean**|  | [optional] [default to false]

### Return type

[**CommentForApiContractPartialFindResult**](CommentForApiContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiUsersIdProfileCommentsPost

> CommentForApiContract apiUsersIdProfileCommentsPost(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let id = 56; // Number | 
let opts = {
  'commentForApiContract': new VocaDbWeb.CommentForApiContract() // CommentForApiContract | 
};
apiInstance.apiUsersIdProfileCommentsPost(id, opts, (error, data, response) => {
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


## apiUsersIdRatedSongsGet

> RatedSongForUserForApiContractPartialFindResult apiUsersIdRatedSongsGet(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let id = 56; // Number | 
let opts = {
  'query': "''", // String | 
  'tagName': "tagName_example", // String | 
  'tagId': [null], // [Number] | 
  'artistId': [null], // [Number] | 
  'childVoicebanks': false, // Boolean | 
  'artistGrouping': new VocaDbWeb.LogicalGrouping(), // LogicalGrouping | 
  'rating': new VocaDbWeb.SongVoteRating(), // SongVoteRating | 
  'songListId': 56, // Number | 
  'groupByRating': true, // Boolean | 
  'pvServices': new VocaDbWeb.PVServices(), // PVServices | 
  'advancedFilters': [new VocaDbWeb.AdvancedSearchFilterParams()], // [AdvancedSearchFilterParams] | 
  'start': 0, // Number | 
  'maxResults': 10, // Number | 
  'getTotalCount': false, // Boolean | 
  'sort': new VocaDbWeb.RatedSongForUserSortRule(), // RatedSongForUserSortRule | 
  'nameMatchMode': new VocaDbWeb.NameMatchMode(), // NameMatchMode | 
  'fields': new VocaDbWeb.SongOptionalFields(), // SongOptionalFields | 
  'lang': new VocaDbWeb.ContentLanguagePreference() // ContentLanguagePreference | 
};
apiInstance.apiUsersIdRatedSongsGet(id, opts, (error, data, response) => {
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
 **query** | **String**|  | [optional] [default to &#39;&#39;]
 **tagName** | **String**|  | [optional] 
 **tagId** | [**[Number]**](Number.md)|  | [optional] 
 **artistId** | [**[Number]**](Number.md)|  | [optional] 
 **childVoicebanks** | **Boolean**|  | [optional] [default to false]
 **artistGrouping** | [**LogicalGrouping**](.md)|  | [optional] 
 **rating** | [**SongVoteRating**](.md)|  | [optional] 
 **songListId** | **Number**|  | [optional] 
 **groupByRating** | **Boolean**|  | [optional] [default to true]
 **pvServices** | [**PVServices**](.md)|  | [optional] 
 **advancedFilters** | [**[AdvancedSearchFilterParams]**](AdvancedSearchFilterParams.md)|  | [optional] 
 **start** | **Number**|  | [optional] [default to 0]
 **maxResults** | **Number**|  | [optional] [default to 10]
 **getTotalCount** | **Boolean**|  | [optional] [default to false]
 **sort** | [**RatedSongForUserSortRule**](.md)|  | [optional] 
 **nameMatchMode** | [**NameMatchMode**](.md)|  | [optional] 
 **fields** | [**SongOptionalFields**](.md)|  | [optional] 
 **lang** | [**ContentLanguagePreference**](.md)|  | [optional] 

### Return type

[**RatedSongForUserForApiContractPartialFindResult**](RatedSongForUserForApiContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiUsersIdRatedSongsSongIdGet

> SongVoteRating apiUsersIdRatedSongsSongIdGet(id, songId)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let id = 56; // Number | 
let songId = 56; // Number | 
apiInstance.apiUsersIdRatedSongsSongIdGet(id, songId, (error, data, response) => {
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
 **songId** | **Number**|  | 

### Return type

[**SongVoteRating**](SongVoteRating.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiUsersIdReportsPost

> Boolean apiUsersIdReportsPost(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let id = 56; // Number | 
let opts = {
  'createReportModel': new VocaDbWeb.CreateReportModel() // CreateReportModel | 
};
apiInstance.apiUsersIdReportsPost(id, opts, (error, data, response) => {
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
 **createReportModel** | [**CreateReportModel**](CreateReportModel.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: application/json, text/json, text/plain


## apiUsersIdSettingsSettingNamePost

> apiUsersIdSettingsSettingNamePost(id, settingName, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let id = 56; // Number | 
let settingName = "settingName_example"; // String | 
let opts = {
  'body': "body_example" // String | 
};
apiInstance.apiUsersIdSettingsSettingNamePost(id, settingName, opts, (error, data, response) => {
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
 **settingName** | **String**|  | 
 **body** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
- **Accept**: Not defined


## apiUsersIdSongListsGet

> SongListForApiContractPartialFindResult apiUsersIdSongListsGet(id, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let id = 56; // Number | 
let opts = {
  'query': "''", // String | 
  'tagId': [null], // [Number] | 
  'childTags': false, // Boolean | 
  'nameMatchMode': new VocaDbWeb.NameMatchMode(), // NameMatchMode | 
  'start': 0, // Number | 
  'maxResults': 10, // Number | 
  'getTotalCount': false, // Boolean | 
  'sort': new VocaDbWeb.SongListSortRule(), // SongListSortRule | 
  'fields': new VocaDbWeb.SongListOptionalFields() // SongListOptionalFields | 
};
apiInstance.apiUsersIdSongListsGet(id, opts, (error, data, response) => {
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
 **query** | **String**|  | [optional] [default to &#39;&#39;]
 **tagId** | [**[Number]**](Number.md)|  | [optional] 
 **childTags** | **Boolean**|  | [optional] [default to false]
 **nameMatchMode** | [**NameMatchMode**](.md)|  | [optional] 
 **start** | **Number**|  | [optional] [default to 0]
 **maxResults** | **Number**|  | [optional] [default to 10]
 **getTotalCount** | **Boolean**|  | [optional] [default to false]
 **sort** | [**SongListSortRule**](.md)|  | [optional] 
 **fields** | [**SongListOptionalFields**](.md)|  | [optional] 

### Return type

[**SongListForApiContractPartialFindResult**](SongListForApiContractPartialFindResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiUsersMessagesMessageIdGet

> UserMessageContract apiUsersMessagesMessageIdGet(messageId)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let messageId = 56; // Number | 
apiInstance.apiUsersMessagesMessageIdGet(messageId, (error, data, response) => {
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
 **messageId** | **Number**|  | 

### Return type

[**UserMessageContract**](UserMessageContract.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiUsersNamesGet

> [String] apiUsersNamesGet(opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let opts = {
  'query': "''", // String | 
  'nameMatchMode': new VocaDbWeb.NameMatchMode(), // NameMatchMode | 
  'maxResults': 10, // Number | 
  'includeDisabled': false // Boolean | 
};
apiInstance.apiUsersNamesGet(opts, (error, data, response) => {
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
 **maxResults** | **Number**|  | [optional] [default to 10]
 **includeDisabled** | **Boolean**|  | [optional] [default to false]

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, text/plain


## apiUsersProfileCommentsCommentIdDelete

> apiUsersProfileCommentsCommentIdDelete(commentId)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let commentId = 56; // Number | 
apiInstance.apiUsersProfileCommentsCommentIdDelete(commentId, (error, data, response) => {
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


## apiUsersProfileCommentsCommentIdPost

> apiUsersProfileCommentsCommentIdPost(commentId, opts)



### Example

```javascript
import VocaDbWeb from 'voca_db_web';

let apiInstance = new VocaDbWeb.UserApiApi();
let commentId = 56; // Number | 
let opts = {
  'commentForApiContract': new VocaDbWeb.CommentForApiContract() // CommentForApiContract | 
};
apiInstance.apiUsersProfileCommentsCommentIdPost(commentId, opts, (error, data, response) => {
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

