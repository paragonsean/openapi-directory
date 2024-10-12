# SpotifyWebApi.UsersApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkCurrentUserFollows**](UsersApi.md#checkCurrentUserFollows) | **GET** /me/following/contains | Check If User Follows Artists or Users 
[**checkIfUserFollowsPlaylist**](UsersApi.md#checkIfUserFollowsPlaylist) | **GET** /playlists/{playlist_id}/followers/contains | Check if Users Follow Playlist 
[**followArtistsUsers**](UsersApi.md#followArtistsUsers) | **PUT** /me/following | Follow Artists or Users 
[**followPlaylist**](UsersApi.md#followPlaylist) | **PUT** /playlists/{playlist_id}/followers | Follow Playlist 
[**getCurrentUsersProfile**](UsersApi.md#getCurrentUsersProfile) | **GET** /me | Get Current User&#39;s Profile 
[**getFollowed**](UsersApi.md#getFollowed) | **GET** /me/following | Get Followed Artists 
[**getListUsersPlaylists_0**](UsersApi.md#getListUsersPlaylists_0) | **GET** /users/{user_id}/playlists | Get User&#39;s Playlists 
[**getUsersProfile**](UsersApi.md#getUsersProfile) | **GET** /users/{user_id} | Get User&#39;s Profile 
[**getUsersTopArtistsAndTracks**](UsersApi.md#getUsersTopArtistsAndTracks) | **GET** /me/top/{type} | Get User&#39;s Top Items 
[**unfollowArtistsUsers**](UsersApi.md#unfollowArtistsUsers) | **DELETE** /me/following | Unfollow Artists or Users 
[**unfollowPlaylist**](UsersApi.md#unfollowPlaylist) | **DELETE** /playlists/{playlist_id}/followers | Unfollow Playlist 



## checkCurrentUserFollows

> [Boolean] checkCurrentUserFollows(type, ids)

Check If User Follows Artists or Users 

Check to see if the current user is following one or more artists or other Spotify users. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.UsersApi();
let type = "artist"; // String | 
let ids = "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"; // String | 
apiInstance.checkCurrentUserFollows(type, ids, (error, data, response) => {
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


## checkIfUserFollowsPlaylist

> [Boolean] checkIfUserFollowsPlaylist(playlistId, ids)

Check if Users Follow Playlist 

Check to see if one or more Spotify users are following a specified playlist. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.UsersApi();
let playlistId = "3cEYpjA9oz9GiPac4AsH4n"; // String | 
let ids = "jmperezperez,thelinmichael,wizzler"; // String | 
apiInstance.checkIfUserFollowsPlaylist(playlistId, ids, (error, data, response) => {
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


## followArtistsUsers

> followArtistsUsers(type, ids, opts)

Follow Artists or Users 

Add the current user as a follower of one or more artists or other Spotify users. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.UsersApi();
let type = "artist"; // String | 
let ids = "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"; // String | 
let opts = {
  'followArtistsUsersRequest': new SpotifyWebApi.FollowArtistsUsersRequest() // FollowArtistsUsersRequest | 
};
apiInstance.followArtistsUsers(type, ids, opts, (error, data, response) => {
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


## followPlaylist

> followPlaylist(playlistId, opts)

Follow Playlist 

Add the current user as a follower of a playlist. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.UsersApi();
let playlistId = "3cEYpjA9oz9GiPac4AsH4n"; // String | 
let opts = {
  'followPlaylistRequest': new SpotifyWebApi.FollowPlaylistRequest() // FollowPlaylistRequest | 
};
apiInstance.followPlaylist(playlistId, opts, (error, data, response) => {
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


## getCurrentUsersProfile

> PrivateUserObject getCurrentUsersProfile()

Get Current User&#39;s Profile 

Get detailed profile information about the current user (including the current user&#39;s username). 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.UsersApi();
apiInstance.getCurrentUsersProfile((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**PrivateUserObject**](PrivateUserObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getFollowed

> GetFollowed200Response getFollowed(type, opts)

Get Followed Artists 

Get the current user&#39;s followed artists. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.UsersApi();
let type = "artist"; // String | 
let opts = {
  'after': "0I2XqVXqHScXjHhk6AYYRe", // String | 
  'limit': 10 // Number | 
};
apiInstance.getFollowed(type, opts, (error, data, response) => {
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


## getListUsersPlaylists_0

> PagingPlaylistObject getListUsersPlaylists_0(userId, opts)

Get User&#39;s Playlists 

Get a list of the playlists owned or followed by a Spotify user. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.UsersApi();
let userId = "smedjan"; // String | 
let opts = {
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getListUsersPlaylists_0(userId, opts, (error, data, response) => {
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


## getUsersProfile

> PublicUserObject getUsersProfile(userId)

Get User&#39;s Profile 

Get public profile information about a Spotify user. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.UsersApi();
let userId = "smedjan"; // String | 
apiInstance.getUsersProfile(userId, (error, data, response) => {
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

### Return type

[**PublicUserObject**](PublicUserObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsersTopArtistsAndTracks

> GetUsersTopArtistsAndTracks200Response getUsersTopArtistsAndTracks(type, opts)

Get User&#39;s Top Items 

Get the current user&#39;s top artists or tracks based on calculated affinity. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.UsersApi();
let type = "type_example"; // String | 
let opts = {
  'timeRange': "medium_term", // String | 
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getUsersTopArtistsAndTracks(type, opts, (error, data, response) => {
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
 **timeRange** | **String**|  | [optional] [default to &#39;medium_term&#39;]
 **limit** | **Number**|  | [optional] [default to 20]
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**GetUsersTopArtistsAndTracks200Response**](GetUsersTopArtistsAndTracks200Response.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## unfollowArtistsUsers

> unfollowArtistsUsers(type, ids, opts)

Unfollow Artists or Users 

Remove the current user as a follower of one or more artists or other Spotify users. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.UsersApi();
let type = "artist"; // String | 
let ids = "2CIMQHirSU0MQqyYHq0eOx,57dN52uHvrHOxijzpIgu3E,1vCWHaC5f2uS3yhpwWbIA6"; // String | 
let opts = {
  'unfollowArtistsUsersRequest': new SpotifyWebApi.UnfollowArtistsUsersRequest() // UnfollowArtistsUsersRequest | 
};
apiInstance.unfollowArtistsUsers(type, ids, opts, (error, data, response) => {
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


## unfollowPlaylist

> unfollowPlaylist(playlistId)

Unfollow Playlist 

Remove the current user as a follower of a playlist. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.UsersApi();
let playlistId = "3cEYpjA9oz9GiPac4AsH4n"; // String | 
apiInstance.unfollowPlaylist(playlistId, (error, data, response) => {
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

