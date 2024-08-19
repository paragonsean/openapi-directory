# SpotifyWebApiWithFixesAndImprovementsFromSonallux.AlbumsApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkUsersSavedAlbums**](AlbumsApi.md#checkUsersSavedAlbums) | **GET** /me/albums/contains | Check User&#39;s Saved Albums 
[**getAnAlbum**](AlbumsApi.md#getAnAlbum) | **GET** /albums/{id} | Get Album 
[**getAnAlbumsTracks**](AlbumsApi.md#getAnAlbumsTracks) | **GET** /albums/{id}/tracks | Get Album Tracks 
[**getAnArtistsAlbums_0**](AlbumsApi.md#getAnArtistsAlbums_0) | **GET** /artists/{id}/albums | Get Artist&#39;s Albums 
[**getMultipleAlbums**](AlbumsApi.md#getMultipleAlbums) | **GET** /albums | Get Several Albums 
[**getNewReleases**](AlbumsApi.md#getNewReleases) | **GET** /browse/new-releases | Get New Releases 
[**getUsersSavedAlbums**](AlbumsApi.md#getUsersSavedAlbums) | **GET** /me/albums | Get User&#39;s Saved Albums 
[**removeAlbumsUser**](AlbumsApi.md#removeAlbumsUser) | **DELETE** /me/albums | Remove Users&#39; Saved Albums 
[**saveAlbumsUser**](AlbumsApi.md#saveAlbumsUser) | **PUT** /me/albums | Save Albums for Current User 



## checkUsersSavedAlbums

> [Boolean] checkUsersSavedAlbums(ids)

Check User&#39;s Saved Albums 

Check if one or more albums is already saved in the current Spotify user&#39;s &#39;Your Music&#39; library. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.AlbumsApi();
let ids = "382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc"; // String | 
apiInstance.checkUsersSavedAlbums(ids, (error, data, response) => {
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


## getAnAlbum

> AlbumObject getAnAlbum(id, opts)

Get Album 

Get Spotify catalog information for a single album. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.AlbumsApi();
let id = "4aawyAB9vmqN3uQ7FjRGTy"; // String | 
let opts = {
  'market': "ES" // String | 
};
apiInstance.getAnAlbum(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **market** | **String**|  | [optional] 

### Return type

[**AlbumObject**](AlbumObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAnAlbumsTracks

> PagingSimplifiedTrackObject getAnAlbumsTracks(id, opts)

Get Album Tracks 

Get Spotify catalog information about an album’s tracks. Optional parameters can be used to limit the number of tracks returned. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.AlbumsApi();
let id = "4aawyAB9vmqN3uQ7FjRGTy"; // String | 
let opts = {
  'market': "ES", // String | 
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getAnAlbumsTracks(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **market** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 20]
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**PagingSimplifiedTrackObject**](PagingSimplifiedTrackObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAnArtistsAlbums_0

> PagingSimplifiedAlbumObject getAnArtistsAlbums_0(id, opts)

Get Artist&#39;s Albums 

Get Spotify catalog information about an artist&#39;s albums. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.AlbumsApi();
let id = "0TnOYISbd1XYRBk9myaseg"; // String | 
let opts = {
  'includeGroups': "single,appears_on", // String | 
  'market': "ES", // String | 
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getAnArtistsAlbums_0(id, opts, (error, data, response) => {
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
 **id** | **String**|  | 
 **includeGroups** | **String**|  | [optional] 
 **market** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 20]
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**PagingSimplifiedAlbumObject**](PagingSimplifiedAlbumObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMultipleAlbums

> GetMultipleAlbums200Response getMultipleAlbums(ids, opts)

Get Several Albums 

Get Spotify catalog information for multiple albums identified by their Spotify IDs. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.AlbumsApi();
let ids = "382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc"; // String | 
let opts = {
  'market': "ES" // String | 
};
apiInstance.getMultipleAlbums(ids, opts, (error, data, response) => {
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
 **market** | **String**|  | [optional] 

### Return type

[**GetMultipleAlbums200Response**](GetMultipleAlbums200Response.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNewReleases

> GetNewReleases200Response getNewReleases(opts)

Get New Releases 

Get a list of new album releases featured in Spotify (shown, for example, on a Spotify player’s “Browse” tab). 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.AlbumsApi();
let opts = {
  'country': "SE", // String | 
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getNewReleases(opts, (error, data, response) => {
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
 **limit** | **Number**|  | [optional] [default to 20]
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**GetNewReleases200Response**](GetNewReleases200Response.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsersSavedAlbums

> PagingSavedAlbumObject getUsersSavedAlbums(opts)

Get User&#39;s Saved Albums 

Get a list of the albums saved in the current Spotify user&#39;s &#39;Your Music&#39; library. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.AlbumsApi();
let opts = {
  'limit': 10, // Number | 
  'offset': 5, // Number | 
  'market': "ES" // String | 
};
apiInstance.getUsersSavedAlbums(opts, (error, data, response) => {
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


## removeAlbumsUser

> removeAlbumsUser(ids, opts)

Remove Users&#39; Saved Albums 

Remove one or more albums from the current user&#39;s &#39;Your Music&#39; library. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.AlbumsApi();
let ids = "382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc"; // String | 
let opts = {
  'saveAlbumsUserRequest': new SpotifyWebApiWithFixesAndImprovementsFromSonallux.SaveAlbumsUserRequest() // SaveAlbumsUserRequest | 
};
apiInstance.removeAlbumsUser(ids, opts, (error, data, response) => {
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


## saveAlbumsUser

> saveAlbumsUser(ids, opts)

Save Albums for Current User 

Save one or more albums to the current user&#39;s &#39;Your Music&#39; library. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.AlbumsApi();
let ids = "382ObEPsp2rxGrnsizN5TX,1A2GTWGtFfWp7KSQTwWOyo,2noRn2Aes5aoNVsU6iWThc"; // String | 
let opts = {
  'saveAlbumsUserRequest': new SpotifyWebApiWithFixesAndImprovementsFromSonallux.SaveAlbumsUserRequest() // SaveAlbumsUserRequest | 
};
apiInstance.saveAlbumsUser(ids, opts, (error, data, response) => {
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

