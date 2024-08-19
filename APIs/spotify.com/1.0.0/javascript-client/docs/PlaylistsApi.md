# SpotifyWebApi.PlaylistsApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addTracksToPlaylist**](PlaylistsApi.md#addTracksToPlaylist) | **POST** /playlists/{playlist_id}/tracks | Add Items to Playlist 
[**changePlaylistDetails**](PlaylistsApi.md#changePlaylistDetails) | **PUT** /playlists/{playlist_id} | Change Playlist Details 
[**checkIfUserFollowsPlaylist_0**](PlaylistsApi.md#checkIfUserFollowsPlaylist_0) | **GET** /playlists/{playlist_id}/followers/contains | Check if Users Follow Playlist 
[**createPlaylist**](PlaylistsApi.md#createPlaylist) | **POST** /users/{user_id}/playlists | Create Playlist 
[**followPlaylist_0**](PlaylistsApi.md#followPlaylist_0) | **PUT** /playlists/{playlist_id}/followers | Follow Playlist 
[**getACategoriesPlaylists**](PlaylistsApi.md#getACategoriesPlaylists) | **GET** /browse/categories/{category_id}/playlists | Get Category&#39;s Playlists 
[**getAListOfCurrentUsersPlaylists**](PlaylistsApi.md#getAListOfCurrentUsersPlaylists) | **GET** /me/playlists | Get Current User&#39;s Playlists 
[**getFeaturedPlaylists**](PlaylistsApi.md#getFeaturedPlaylists) | **GET** /browse/featured-playlists | Get Featured Playlists 
[**getListUsersPlaylists**](PlaylistsApi.md#getListUsersPlaylists) | **GET** /users/{user_id}/playlists | Get User&#39;s Playlists 
[**getPlaylist**](PlaylistsApi.md#getPlaylist) | **GET** /playlists/{playlist_id} | Get Playlist 
[**getPlaylistCover**](PlaylistsApi.md#getPlaylistCover) | **GET** /playlists/{playlist_id}/images | Get Playlist Cover Image 
[**getPlaylistsTracks**](PlaylistsApi.md#getPlaylistsTracks) | **GET** /playlists/{playlist_id}/tracks | Get Playlist Items 
[**removeTracksPlaylist**](PlaylistsApi.md#removeTracksPlaylist) | **DELETE** /playlists/{playlist_id}/tracks | Remove Playlist Items 
[**reorderOrReplacePlaylistsTracks**](PlaylistsApi.md#reorderOrReplacePlaylistsTracks) | **PUT** /playlists/{playlist_id}/tracks | Update Playlist Items 
[**unfollowPlaylist_0**](PlaylistsApi.md#unfollowPlaylist_0) | **DELETE** /playlists/{playlist_id}/followers | Unfollow Playlist 
[**uploadCustomPlaylistCover**](PlaylistsApi.md#uploadCustomPlaylistCover) | **PUT** /playlists/{playlist_id}/images | Add Custom Playlist Cover Image 



## addTracksToPlaylist

> ReorderOrReplacePlaylistsTracks200Response addTracksToPlaylist(playlistId, opts)

Add Items to Playlist 

Add one or more items to a user&#39;s playlist. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.PlaylistsApi();
let playlistId = "3cEYpjA9oz9GiPac4AsH4n"; // String | 
let opts = {
  'position': 0, // Number | 
  'uris': "spotify:track:4iV5W9uYEdYUVa79Axb7Rh,spotify:track:1301WleyT98MSxVHPZCA6M", // String | 
  'addTracksToPlaylistRequest': new SpotifyWebApi.AddTracksToPlaylistRequest() // AddTracksToPlaylistRequest | 
};
apiInstance.addTracksToPlaylist(playlistId, opts, (error, data, response) => {
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
 **playlistId** | **String**|  | 
 **position** | **Number**|  | [optional] 
 **uris** | **String**|  | [optional] 
 **addTracksToPlaylistRequest** | [**AddTracksToPlaylistRequest**](AddTracksToPlaylistRequest.md)|  | [optional] 

### Return type

[**ReorderOrReplacePlaylistsTracks200Response**](ReorderOrReplacePlaylistsTracks200Response.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## changePlaylistDetails

> changePlaylistDetails(playlistId, opts)

Change Playlist Details 

Change a playlist&#39;s name and public/private state. (The user must, of course, own the playlist.) 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.PlaylistsApi();
let playlistId = "3cEYpjA9oz9GiPac4AsH4n"; // String | 
let opts = {
  'changePlaylistDetailsRequest': new SpotifyWebApi.ChangePlaylistDetailsRequest() // ChangePlaylistDetailsRequest | 
};
apiInstance.changePlaylistDetails(playlistId, opts, (error, data, response) => {
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
 **playlistId** | **String**|  | 
 **changePlaylistDetailsRequest** | [**ChangePlaylistDetailsRequest**](ChangePlaylistDetailsRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## checkIfUserFollowsPlaylist_0

> [Boolean] checkIfUserFollowsPlaylist_0(playlistId, ids)

Check if Users Follow Playlist 

Check to see if one or more Spotify users are following a specified playlist. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.PlaylistsApi();
let playlistId = "3cEYpjA9oz9GiPac4AsH4n"; // String | 
let ids = "jmperezperez,thelinmichael,wizzler"; // String | 
apiInstance.checkIfUserFollowsPlaylist_0(playlistId, ids, (error, data, response) => {
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
 **playlistId** | **String**|  | 
 **ids** | **String**|  | 

### Return type

**[Boolean]**

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createPlaylist

> PlaylistObject createPlaylist(userId, opts)

Create Playlist 

Create a playlist for a Spotify user. (The playlist will be empty until you [add tracks](/documentation/web-api/reference/add-tracks-to-playlist).) 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.PlaylistsApi();
let userId = "smedjan"; // String | 
let opts = {
  'createPlaylistRequest': new SpotifyWebApi.CreatePlaylistRequest() // CreatePlaylistRequest | 
};
apiInstance.createPlaylist(userId, opts, (error, data, response) => {
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
 **userId** | **String**|  | 
 **createPlaylistRequest** | [**CreatePlaylistRequest**](CreatePlaylistRequest.md)|  | [optional] 

### Return type

[**PlaylistObject**](PlaylistObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## followPlaylist_0

> followPlaylist_0(playlistId, opts)

Follow Playlist 

Add the current user as a follower of a playlist. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.PlaylistsApi();
let playlistId = "3cEYpjA9oz9GiPac4AsH4n"; // String | 
let opts = {
  'followPlaylistRequest': new SpotifyWebApi.FollowPlaylistRequest() // FollowPlaylistRequest | 
};
apiInstance.followPlaylist_0(playlistId, opts, (error, data, response) => {
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
 **playlistId** | **String**|  | 
 **followPlaylistRequest** | [**FollowPlaylistRequest**](FollowPlaylistRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getACategoriesPlaylists

> PagingFeaturedPlaylistObject getACategoriesPlaylists(categoryId, opts)

Get Category&#39;s Playlists 

Get a list of Spotify playlists tagged with a particular category. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.PlaylistsApi();
let categoryId = "dinner"; // String | 
let opts = {
  'country': "SE", // String | 
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getACategoriesPlaylists(categoryId, opts, (error, data, response) => {
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
 **categoryId** | **String**|  | 
 **country** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 20]
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**PagingFeaturedPlaylistObject**](PagingFeaturedPlaylistObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAListOfCurrentUsersPlaylists

> PagingPlaylistObject getAListOfCurrentUsersPlaylists(opts)

Get Current User&#39;s Playlists 

Get a list of the playlists owned or followed by the current Spotify user. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.PlaylistsApi();
let opts = {
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getAListOfCurrentUsersPlaylists(opts, (error, data, response) => {
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
 **limit** | **Number**|  | [optional] [default to 20]
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**PagingPlaylistObject**](PagingPlaylistObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFeaturedPlaylists

> PagingFeaturedPlaylistObject getFeaturedPlaylists(opts)

Get Featured Playlists 

Get a list of Spotify featured playlists (shown, for example, on a Spotify player&#39;s &#39;Browse&#39; tab). 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.PlaylistsApi();
let opts = {
  'country': "SE", // String | 
  'locale': "sv_SE", // String | 
  'timestamp': "2014-10-23T09:00:00", // String | 
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getFeaturedPlaylists(opts, (error, data, response) => {
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
 **country** | **String**|  | [optional] 
 **locale** | **String**|  | [optional] 
 **timestamp** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 20]
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**PagingFeaturedPlaylistObject**](PagingFeaturedPlaylistObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getListUsersPlaylists

> PagingPlaylistObject getListUsersPlaylists(userId, opts)

Get User&#39;s Playlists 

Get a list of the playlists owned or followed by a Spotify user. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.PlaylistsApi();
let userId = "smedjan"; // String | 
let opts = {
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getListUsersPlaylists(userId, opts, (error, data, response) => {
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
 **userId** | **String**|  | 
 **limit** | **Number**|  | [optional] [default to 20]
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**PagingPlaylistObject**](PagingPlaylistObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPlaylist

> PlaylistObject getPlaylist(playlistId, opts)

Get Playlist 

Get a playlist owned by a Spotify user. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.PlaylistsApi();
let playlistId = "3cEYpjA9oz9GiPac4AsH4n"; // String | 
let opts = {
  'market': "ES", // String | 
  'fields': "items(added_by.id,track(name,href,album(name,href)))", // String | 
  'additionalTypes': "additionalTypes_example" // String | 
};
apiInstance.getPlaylist(playlistId, opts, (error, data, response) => {
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
 **playlistId** | **String**|  | 
 **market** | **String**|  | [optional] 
 **fields** | **String**|  | [optional] 
 **additionalTypes** | **String**|  | [optional] 

### Return type

[**PlaylistObject**](PlaylistObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPlaylistCover

> [ImageObject] getPlaylistCover(playlistId)

Get Playlist Cover Image 

Get the current image associated with a specific playlist. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.PlaylistsApi();
let playlistId = "3cEYpjA9oz9GiPac4AsH4n"; // String | 
apiInstance.getPlaylistCover(playlistId, (error, data, response) => {
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
 **playlistId** | **String**|  | 

### Return type

[**[ImageObject]**](ImageObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPlaylistsTracks

> PagingPlaylistTrackObject getPlaylistsTracks(playlistId, opts)

Get Playlist Items 

Get full details of the items of a playlist owned by a Spotify user. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.PlaylistsApi();
let playlistId = "3cEYpjA9oz9GiPac4AsH4n"; // String | 
let opts = {
  'market': "ES", // String | 
  'fields': "items(added_by.id,track(name,href,album(name,href)))", // String | 
  'limit': 10, // Number | 
  'offset': 5, // Number | 
  'additionalTypes': "additionalTypes_example" // String | 
};
apiInstance.getPlaylistsTracks(playlistId, opts, (error, data, response) => {
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
 **playlistId** | **String**|  | 
 **market** | **String**|  | [optional] 
 **fields** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 20]
 **offset** | **Number**|  | [optional] [default to 0]
 **additionalTypes** | **String**|  | [optional] 

### Return type

[**PagingPlaylistTrackObject**](PagingPlaylistTrackObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeTracksPlaylist

> ReorderOrReplacePlaylistsTracks200Response removeTracksPlaylist(playlistId, opts)

Remove Playlist Items 

Remove one or more items from a user&#39;s playlist. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.PlaylistsApi();
let playlistId = "3cEYpjA9oz9GiPac4AsH4n"; // String | 
let opts = {
  'removeTracksPlaylistRequest': new SpotifyWebApi.RemoveTracksPlaylistRequest() // RemoveTracksPlaylistRequest | 
};
apiInstance.removeTracksPlaylist(playlistId, opts, (error, data, response) => {
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
 **playlistId** | **String**|  | 
 **removeTracksPlaylistRequest** | [**RemoveTracksPlaylistRequest**](RemoveTracksPlaylistRequest.md)|  | [optional] 

### Return type

[**ReorderOrReplacePlaylistsTracks200Response**](ReorderOrReplacePlaylistsTracks200Response.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reorderOrReplacePlaylistsTracks

> ReorderOrReplacePlaylistsTracks200Response reorderOrReplacePlaylistsTracks(playlistId, opts)

Update Playlist Items 

Either reorder or replace items in a playlist depending on the request&#39;s parameters. To reorder items, include &#x60;range_start&#x60;, &#x60;insert_before&#x60;, &#x60;range_length&#x60; and &#x60;snapshot_id&#x60; in the request&#39;s body. To replace items, include &#x60;uris&#x60; as either a query parameter or in the request&#39;s body. Replacing items in a playlist will overwrite its existing items. This operation can be used for replacing or clearing items in a playlist. &lt;br/&gt; **Note**: Replace and reorder are mutually exclusive operations which share the same endpoint, but have different parameters. These operations can&#39;t be applied together in a single request. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.PlaylistsApi();
let playlistId = "3cEYpjA9oz9GiPac4AsH4n"; // String | 
let opts = {
  'uris': "uris_example", // String | 
  'reorderOrReplacePlaylistsTracksRequest': new SpotifyWebApi.ReorderOrReplacePlaylistsTracksRequest() // ReorderOrReplacePlaylistsTracksRequest | 
};
apiInstance.reorderOrReplacePlaylistsTracks(playlistId, opts, (error, data, response) => {
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
 **playlistId** | **String**|  | 
 **uris** | **String**|  | [optional] 
 **reorderOrReplacePlaylistsTracksRequest** | [**ReorderOrReplacePlaylistsTracksRequest**](ReorderOrReplacePlaylistsTracksRequest.md)|  | [optional] 

### Return type

[**ReorderOrReplacePlaylistsTracks200Response**](ReorderOrReplacePlaylistsTracks200Response.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## unfollowPlaylist_0

> unfollowPlaylist_0(playlistId)

Unfollow Playlist 

Remove the current user as a follower of a playlist. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.PlaylistsApi();
let playlistId = "3cEYpjA9oz9GiPac4AsH4n"; // String | 
apiInstance.unfollowPlaylist_0(playlistId, (error, data, response) => {
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
 **playlistId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## uploadCustomPlaylistCover

> uploadCustomPlaylistCover(playlistId, opts)

Add Custom Playlist Cover Image 

Replace the image used to represent a specific playlist. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.PlaylistsApi();
let playlistId = "3cEYpjA9oz9GiPac4AsH4n"; // String | 
let opts = {
  'body': null // Blob | 
};
apiInstance.uploadCustomPlaylistCover(playlistId, opts, (error, data, response) => {
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
 **playlistId** | **String**|  | 
 **body** | **Blob**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: image/jpeg
- **Accept**: application/json

