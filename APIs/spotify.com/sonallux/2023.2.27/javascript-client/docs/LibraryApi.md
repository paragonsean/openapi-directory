# SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**changePlaylistDetails_0**](LibraryApi.md#changePlaylistDetails_0) | **PUT** /playlists/{playlist_id} | Change Playlist Details 
[**checkCurrentUserFollows_1**](LibraryApi.md#checkCurrentUserFollows_1) | **GET** /me/following/contains | Check If User Follows Artists or Users 
[**checkUsersSavedAlbums_0**](LibraryApi.md#checkUsersSavedAlbums_0) | **GET** /me/albums/contains | Check User&#39;s Saved Albums 
[**checkUsersSavedAudiobooks_0**](LibraryApi.md#checkUsersSavedAudiobooks_0) | **GET** /me/audiobooks/contains | Check User&#39;s Saved Audiobooks 
[**checkUsersSavedEpisodes_0**](LibraryApi.md#checkUsersSavedEpisodes_0) | **GET** /me/episodes/contains | Check User&#39;s Saved Episodes 
[**checkUsersSavedShows_0**](LibraryApi.md#checkUsersSavedShows_0) | **GET** /me/shows/contains | Check User&#39;s Saved Shows 
[**checkUsersSavedTracks_0**](LibraryApi.md#checkUsersSavedTracks_0) | **GET** /me/tracks/contains | Check User&#39;s Saved Tracks 
[**createPlaylist_0**](LibraryApi.md#createPlaylist_0) | **POST** /users/{user_id}/playlists | Create Playlist 
[**followArtistsUsers_1**](LibraryApi.md#followArtistsUsers_1) | **PUT** /me/following | Follow Artists or Users 
[**getAListOfCurrentUsersPlaylists_0**](LibraryApi.md#getAListOfCurrentUsersPlaylists_0) | **GET** /me/playlists | Get Current User&#39;s Playlists 
[**getFollowed_0**](LibraryApi.md#getFollowed_0) | **GET** /me/following | Get Followed Artists 
[**getUsersSavedAlbums_0**](LibraryApi.md#getUsersSavedAlbums_0) | **GET** /me/albums | Get User&#39;s Saved Albums 
[**getUsersSavedAudiobooks_0**](LibraryApi.md#getUsersSavedAudiobooks_0) | **GET** /me/audiobooks | Get User&#39;s Saved Audiobooks 
[**getUsersSavedEpisodes_0**](LibraryApi.md#getUsersSavedEpisodes_0) | **GET** /me/episodes | Get User&#39;s Saved Episodes 
[**getUsersSavedShows_0**](LibraryApi.md#getUsersSavedShows_0) | **GET** /me/shows | Get User&#39;s Saved Shows 
[**getUsersSavedTracks_0**](LibraryApi.md#getUsersSavedTracks_0) | **GET** /me/tracks | Get User&#39;s Saved Tracks 
[**getUsersTopArtists_1**](LibraryApi.md#getUsersTopArtists_1) | **GET** /me/top/artists | Get User&#39;s Top Artists 
[**getUsersTopTracks_1**](LibraryApi.md#getUsersTopTracks_1) | **GET** /me/top/tracks | Get User&#39;s Top Tracks 
[**removeAlbumsUser_0**](LibraryApi.md#removeAlbumsUser_0) | **DELETE** /me/albums | Remove Users&#39; Saved Albums 
[**removeAudiobooksUser_0**](LibraryApi.md#removeAudiobooksUser_0) | **DELETE** /me/audiobooks | Remove User&#39;s Saved Audiobooks 
[**removeEpisodesUser_0**](LibraryApi.md#removeEpisodesUser_0) | **DELETE** /me/episodes | Remove User&#39;s Saved Episodes 
[**removeShowsUser_0**](LibraryApi.md#removeShowsUser_0) | **DELETE** /me/shows | Remove User&#39;s Saved Shows 
[**removeTracksUser_0**](LibraryApi.md#removeTracksUser_0) | **DELETE** /me/tracks | Remove User&#39;s Saved Tracks 
[**saveAlbumsUser_0**](LibraryApi.md#saveAlbumsUser_0) | **PUT** /me/albums | Save Albums for Current User 
[**saveAudiobooksUser_0**](LibraryApi.md#saveAudiobooksUser_0) | **PUT** /me/audiobooks | Save Audiobooks for Current User 
[**saveEpisodesUser_0**](LibraryApi.md#saveEpisodesUser_0) | **PUT** /me/episodes | Save Episodes for Current User 
[**saveShowsUser_0**](LibraryApi.md#saveShowsUser_0) | **PUT** /me/shows | Save Shows for Current User 
[**saveTracksUser_0**](LibraryApi.md#saveTracksUser_0) | **PUT** /me/tracks | Save Tracks for Current User 
[**unfollowArtistsUsers_1**](LibraryApi.md#unfollowArtistsUsers_1) | **DELETE** /me/following | Unfollow Artists or Users 



## changePlaylistDetails_0

> changePlaylistDetails_0(playlistId, opts)

Change Playlist Details 

Change a playlist&#39;s name and public/private state. (The user must, of course, own the playlist.) 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let playlistId = "3cEYpjA9oz9GiPac4AsH4n"; // String | 
let opts = {
  'changePlaylistDetailsRequest': new SpotifyWebApiWithFixesAndImprovementsFromSonallux.ChangePlaylistDetailsRequest() // ChangePlaylistDetailsRequest | 
};
apiInstance.changePlaylistDetails_0(playlistId, opts, (error, data, response) => {
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


## checkCurrentUserFollows_1

> [Boolean] checkCurrentUserFollows_1(type, ids)

Check If User Follows Artists or Users 

Check to see if the current user is following one or more artists or other Spotify users. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let type = "artist"; // String | 
let ids = "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"; // String | 
apiInstance.checkCurrentUserFollows_1(type, ids, (error, data, response) => {
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
 **type** | **String**|  | 
 **ids** | **String**|  | 

### Return type

**[Boolean]**

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## checkUsersSavedAlbums_0

> [Boolean] checkUsersSavedAlbums_0(ids)

Check User&#39;s Saved Albums 

Check if one or more albums is already saved in the current Spotify user&#39;s &#39;Your Music&#39; library. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let ids = "382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc"; // String | 
apiInstance.checkUsersSavedAlbums_0(ids, (error, data, response) => {
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
 **ids** | **String**|  | 

### Return type

**[Boolean]**

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## checkUsersSavedAudiobooks_0

> [Boolean] checkUsersSavedAudiobooks_0(ids)

Check User&#39;s Saved Audiobooks 

Check if one or more audiobooks are already saved in the current Spotify user&#39;s library. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let ids = "18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe"; // String | 
apiInstance.checkUsersSavedAudiobooks_0(ids, (error, data, response) => {
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
 **ids** | **String**|  | 

### Return type

**[Boolean]**

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## checkUsersSavedEpisodes_0

> [Boolean] checkUsersSavedEpisodes_0(ids)

Check User&#39;s Saved Episodes 

Check if one or more episodes is already saved in the current Spotify user&#39;s &#39;Your Episodes&#39; library.&lt;br/&gt; This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer).. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let ids = "77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf"; // String | 
apiInstance.checkUsersSavedEpisodes_0(ids, (error, data, response) => {
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
 **ids** | **String**|  | 

### Return type

**[Boolean]**

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## checkUsersSavedShows_0

> [Boolean] checkUsersSavedShows_0(ids)

Check User&#39;s Saved Shows 

Check if one or more shows is already saved in the current Spotify user&#39;s library. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let ids = "5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ"; // String | 
apiInstance.checkUsersSavedShows_0(ids, (error, data, response) => {
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
 **ids** | **String**|  | 

### Return type

**[Boolean]**

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## checkUsersSavedTracks_0

> [Boolean] checkUsersSavedTracks_0(ids)

Check User&#39;s Saved Tracks 

Check if one or more tracks is already saved in the current Spotify user&#39;s &#39;Your Music&#39; library. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let ids = "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"; // String | 
apiInstance.checkUsersSavedTracks_0(ids, (error, data, response) => {
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
 **ids** | **String**|  | 

### Return type

**[Boolean]**

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## createPlaylist_0

> PlaylistObject createPlaylist_0(userId, opts)

Create Playlist 

Create a playlist for a Spotify user. (The playlist will be empty until you [add tracks](/documentation/web-api/reference/add-tracks-to-playlist).) 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let userId = "smedjan"; // String | 
let opts = {
  'createPlaylistRequest': new SpotifyWebApiWithFixesAndImprovementsFromSonallux.CreatePlaylistRequest() // CreatePlaylistRequest | 
};
apiInstance.createPlaylist_0(userId, opts, (error, data, response) => {
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


## followArtistsUsers_1

> followArtistsUsers_1(type, ids, opts)

Follow Artists or Users 

Add the current user as a follower of one or more artists or other Spotify users. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let type = "artist"; // String | 
let ids = "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"; // String | 
let opts = {
  'followArtistsUsersRequest': new SpotifyWebApiWithFixesAndImprovementsFromSonallux.FollowArtistsUsersRequest() // FollowArtistsUsersRequest | 
};
apiInstance.followArtistsUsers_1(type, ids, opts, (error, data, response) => {
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
 **type** | **String**|  | 
 **ids** | **String**|  | 
 **followArtistsUsersRequest** | [**FollowArtistsUsersRequest**](FollowArtistsUsersRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAListOfCurrentUsersPlaylists_0

> PagingPlaylistObject getAListOfCurrentUsersPlaylists_0(opts)

Get Current User&#39;s Playlists 

Get a list of the playlists owned or followed by the current Spotify user. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let opts = {
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getAListOfCurrentUsersPlaylists_0(opts, (error, data, response) => {
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


## getFollowed_0

> GetFollowed200Response getFollowed_0(type, opts)

Get Followed Artists 

Get the current user&#39;s followed artists. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let type = "artist"; // String | 
let opts = {
  'after': "0I2XqVXqHScXjHhk6AYYRe", // String | 
  'limit': 10 // Number | 
};
apiInstance.getFollowed_0(type, opts, (error, data, response) => {
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
 **type** | **String**|  | 
 **after** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 20]

### Return type

[**GetFollowed200Response**](GetFollowed200Response.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsersSavedAlbums_0

> PagingSavedAlbumObject getUsersSavedAlbums_0(opts)

Get User&#39;s Saved Albums 

Get a list of the albums saved in the current Spotify user&#39;s &#39;Your Music&#39; library. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let opts = {
  'limit': 10, // Number | 
  'offset': 5, // Number | 
  'market': "ES" // String | 
};
apiInstance.getUsersSavedAlbums_0(opts, (error, data, response) => {
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
 **market** | **String**|  | [optional] 

### Return type

[**PagingSavedAlbumObject**](PagingSavedAlbumObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsersSavedAudiobooks_0

> PagingSavedAudiobookObject getUsersSavedAudiobooks_0(opts)

Get User&#39;s Saved Audiobooks 

Get a list of the audiobooks saved in the current Spotify user&#39;s &#39;Your Music&#39; library. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let opts = {
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getUsersSavedAudiobooks_0(opts, (error, data, response) => {
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

[**PagingSavedAudiobookObject**](PagingSavedAudiobookObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsersSavedEpisodes_0

> PagingSavedEpisodeObject getUsersSavedEpisodes_0(opts)

Get User&#39;s Saved Episodes 

Get a list of the episodes saved in the current Spotify user&#39;s library.&lt;br/&gt; This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer). 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let opts = {
  'market': "ES", // String | 
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getUsersSavedEpisodes_0(opts, (error, data, response) => {
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
 **market** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 20]
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**PagingSavedEpisodeObject**](PagingSavedEpisodeObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsersSavedShows_0

> PagingSavedShowObject getUsersSavedShows_0(opts)

Get User&#39;s Saved Shows 

Get a list of shows saved in the current Spotify user&#39;s library. Optional parameters can be used to limit the number of shows returned. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let opts = {
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getUsersSavedShows_0(opts, (error, data, response) => {
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

[**PagingSavedShowObject**](PagingSavedShowObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsersSavedTracks_0

> PagingSavedTrackObject getUsersSavedTracks_0(opts)

Get User&#39;s Saved Tracks 

Get a list of the songs saved in the current Spotify user&#39;s &#39;Your Music&#39; library. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let opts = {
  'market': "ES", // String | 
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getUsersSavedTracks_0(opts, (error, data, response) => {
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
 **market** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 20]
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**PagingSavedTrackObject**](PagingSavedTrackObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsersTopArtists_1

> PagingArtistObject getUsersTopArtists_1(opts)

Get User&#39;s Top Artists 

Get the current user&#39;s top artists based on calculated affinity. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let opts = {
  'timeRange': "medium_term", // String | 
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getUsersTopArtists_1(opts, (error, data, response) => {
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
 **timeRange** | **String**|  | [optional] [default to &#39;medium_term&#39;]
 **limit** | **Number**|  | [optional] [default to 20]
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**PagingArtistObject**](PagingArtistObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsersTopTracks_1

> PagingTrackObject getUsersTopTracks_1(opts)

Get User&#39;s Top Tracks 

Get the current user&#39;s top tracks based on calculated affinity. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let opts = {
  'timeRange': "medium_term", // String | 
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getUsersTopTracks_1(opts, (error, data, response) => {
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
 **timeRange** | **String**|  | [optional] [default to &#39;medium_term&#39;]
 **limit** | **Number**|  | [optional] [default to 20]
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**PagingTrackObject**](PagingTrackObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeAlbumsUser_0

> removeAlbumsUser_0(ids, opts)

Remove Users&#39; Saved Albums 

Remove one or more albums from the current user&#39;s &#39;Your Music&#39; library. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let ids = "382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc"; // String | 
let opts = {
  'saveAlbumsUserRequest': new SpotifyWebApiWithFixesAndImprovementsFromSonallux.SaveAlbumsUserRequest() // SaveAlbumsUserRequest | 
};
apiInstance.removeAlbumsUser_0(ids, opts, (error, data, response) => {
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
 **ids** | **String**|  | 
 **saveAlbumsUserRequest** | [**SaveAlbumsUserRequest**](SaveAlbumsUserRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeAudiobooksUser_0

> removeAudiobooksUser_0(ids)

Remove User&#39;s Saved Audiobooks 

Remove one or more audiobooks from the Spotify user&#39;s library. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let ids = "18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe"; // String | 
apiInstance.removeAudiobooksUser_0(ids, (error, data, response) => {
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
 **ids** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeEpisodesUser_0

> removeEpisodesUser_0(ids, opts)

Remove User&#39;s Saved Episodes 

Remove one or more episodes from the current user&#39;s library.&lt;br/&gt; This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer). 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let ids = "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"; // String | 
let opts = {
  'removeEpisodesUserRequest': new SpotifyWebApiWithFixesAndImprovementsFromSonallux.RemoveEpisodesUserRequest() // RemoveEpisodesUserRequest | 
};
apiInstance.removeEpisodesUser_0(ids, opts, (error, data, response) => {
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
 **ids** | **String**|  | 
 **removeEpisodesUserRequest** | [**RemoveEpisodesUserRequest**](RemoveEpisodesUserRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeShowsUser_0

> removeShowsUser_0(ids, opts)

Remove User&#39;s Saved Shows 

Delete one or more shows from current Spotify user&#39;s library. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let ids = "5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ"; // String | 
let opts = {
  'market': "ES", // String | 
  'saveShowsUserRequest': new SpotifyWebApiWithFixesAndImprovementsFromSonallux.SaveShowsUserRequest() // SaveShowsUserRequest | 
};
apiInstance.removeShowsUser_0(ids, opts, (error, data, response) => {
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
 **ids** | **String**|  | 
 **market** | **String**|  | [optional] 
 **saveShowsUserRequest** | [**SaveShowsUserRequest**](SaveShowsUserRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeTracksUser_0

> removeTracksUser_0(ids, opts)

Remove User&#39;s Saved Tracks 

Remove one or more tracks from the current user&#39;s &#39;Your Music&#39; library. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let ids = "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"; // String | 
let opts = {
  'saveAlbumsUserRequest': new SpotifyWebApiWithFixesAndImprovementsFromSonallux.SaveAlbumsUserRequest() // SaveAlbumsUserRequest | 
};
apiInstance.removeTracksUser_0(ids, opts, (error, data, response) => {
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
 **ids** | **String**|  | 
 **saveAlbumsUserRequest** | [**SaveAlbumsUserRequest**](SaveAlbumsUserRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## saveAlbumsUser_0

> saveAlbumsUser_0(ids, opts)

Save Albums for Current User 

Save one or more albums to the current user&#39;s &#39;Your Music&#39; library. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let ids = "382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc"; // String | 
let opts = {
  'saveAlbumsUserRequest': new SpotifyWebApiWithFixesAndImprovementsFromSonallux.SaveAlbumsUserRequest() // SaveAlbumsUserRequest | 
};
apiInstance.saveAlbumsUser_0(ids, opts, (error, data, response) => {
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
 **ids** | **String**|  | 
 **saveAlbumsUserRequest** | [**SaveAlbumsUserRequest**](SaveAlbumsUserRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## saveAudiobooksUser_0

> saveAudiobooksUser_0(ids)

Save Audiobooks for Current User 

Save one or more audiobooks to the current Spotify user&#39;s library. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let ids = "18yVqkdbdRvS24c0Ilj2ci,1HGw3J3NxZO1TP1BTtVhpZ,7iHfbu1YPACw6oZPAFJtqe"; // String | 
apiInstance.saveAudiobooksUser_0(ids, (error, data, response) => {
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
 **ids** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## saveEpisodesUser_0

> saveEpisodesUser_0(ids, opts)

Save Episodes for Current User 

Save one or more episodes to the current user&#39;s library.&lt;br/&gt; This API endpoint is in __beta__ and could change without warning. Please share any feedback that you have, or issues that you discover, in our [developer community forum](https://community.spotify.com/t5/Spotify-for-Developers/bd-p/Spotify_Developer). 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let ids = "77o6BIVlYM3msb4MMIL1jH,0Q86acNRm6V9GYx55SXKwf"; // String | 
let opts = {
  'saveEpisodesUserRequest': new SpotifyWebApiWithFixesAndImprovementsFromSonallux.SaveEpisodesUserRequest() // SaveEpisodesUserRequest | 
};
apiInstance.saveEpisodesUser_0(ids, opts, (error, data, response) => {
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
 **ids** | **String**|  | 
 **saveEpisodesUserRequest** | [**SaveEpisodesUserRequest**](SaveEpisodesUserRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## saveShowsUser_0

> saveShowsUser_0(ids, opts)

Save Shows for Current User 

Save one or more shows to current Spotify user&#39;s library. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let ids = "5CfCWKI5pZ28U0uOzXkDHe,5as3aKmN2k11yfDDDSrvaZ"; // String | 
let opts = {
  'saveShowsUserRequest': new SpotifyWebApiWithFixesAndImprovementsFromSonallux.SaveShowsUserRequest() // SaveShowsUserRequest | 
};
apiInstance.saveShowsUser_0(ids, opts, (error, data, response) => {
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
 **ids** | **String**|  | 
 **saveShowsUserRequest** | [**SaveShowsUserRequest**](SaveShowsUserRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## saveTracksUser_0

> saveTracksUser_0(ids, opts)

Save Tracks for Current User 

Save one or more tracks to the current user&#39;s &#39;Your Music&#39; library. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let ids = "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"; // String | 
let opts = {
  'saveTracksUserRequest': new SpotifyWebApiWithFixesAndImprovementsFromSonallux.SaveTracksUserRequest() // SaveTracksUserRequest | 
};
apiInstance.saveTracksUser_0(ids, opts, (error, data, response) => {
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
 **ids** | **String**|  | 
 **saveTracksUserRequest** | [**SaveTracksUserRequest**](SaveTracksUserRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## unfollowArtistsUsers_1

> unfollowArtistsUsers_1(type, ids, opts)

Unfollow Artists or Users 

Remove the current user as a follower of one or more artists or other Spotify users. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.LibraryApi();
let type = "artist"; // String | 
let ids = "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"; // String | 
let opts = {
  'unfollowArtistsUsersRequest': new SpotifyWebApiWithFixesAndImprovementsFromSonallux.UnfollowArtistsUsersRequest() // UnfollowArtistsUsersRequest | 
};
apiInstance.unfollowArtistsUsers_1(type, ids, opts, (error, data, response) => {
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
 **type** | **String**|  | 
 **ids** | **String**|  | 
 **unfollowArtistsUsersRequest** | [**UnfollowArtistsUsersRequest**](UnfollowArtistsUsersRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

