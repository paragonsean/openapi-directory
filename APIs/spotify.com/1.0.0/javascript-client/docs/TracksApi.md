# SpotifyWebApi.TracksApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addTracksToPlaylist_0**](TracksApi.md#addTracksToPlaylist_0) | **POST** /playlists/{playlist_id}/tracks | Add Items to Playlist 
[**checkUsersSavedTracks**](TracksApi.md#checkUsersSavedTracks) | **GET** /me/tracks/contains | Check User&#39;s Saved Tracks 
[**getAnAlbumsTracks_0**](TracksApi.md#getAnAlbumsTracks_0) | **GET** /albums/{id}/tracks | Get Album Tracks 
[**getAnArtistsTopTracks_0**](TracksApi.md#getAnArtistsTopTracks_0) | **GET** /artists/{id}/top-tracks | Get Artist&#39;s Top Tracks 
[**getAudioAnalysis**](TracksApi.md#getAudioAnalysis) | **GET** /audio-analysis/{id} | Get Track&#39;s Audio Analysis 
[**getAudioFeatures**](TracksApi.md#getAudioFeatures) | **GET** /audio-features/{id} | Get Track&#39;s Audio Features 
[**getPlaylistsTracks_0**](TracksApi.md#getPlaylistsTracks_0) | **GET** /playlists/{playlist_id}/tracks | Get Playlist Items 
[**getRecommendations**](TracksApi.md#getRecommendations) | **GET** /recommendations | Get Recommendations 
[**getSeveralAudioFeatures**](TracksApi.md#getSeveralAudioFeatures) | **GET** /audio-features | Get Tracks&#39; Audio Features 
[**getSeveralTracks**](TracksApi.md#getSeveralTracks) | **GET** /tracks | Get Several Tracks 
[**getTrack**](TracksApi.md#getTrack) | **GET** /tracks/{id} | Get Track 
[**getUsersSavedTracks**](TracksApi.md#getUsersSavedTracks) | **GET** /me/tracks | Get User&#39;s Saved Tracks 
[**getUsersTopArtistsAndTracks_0**](TracksApi.md#getUsersTopArtistsAndTracks_0) | **GET** /me/top/{type} | Get User&#39;s Top Items 
[**removeTracksPlaylist_0**](TracksApi.md#removeTracksPlaylist_0) | **DELETE** /playlists/{playlist_id}/tracks | Remove Playlist Items 
[**removeTracksUser**](TracksApi.md#removeTracksUser) | **DELETE** /me/tracks | Remove User&#39;s Saved Tracks 
[**reorderOrReplacePlaylistsTracks_0**](TracksApi.md#reorderOrReplacePlaylistsTracks_0) | **PUT** /playlists/{playlist_id}/tracks | Update Playlist Items 
[**saveTracksUser**](TracksApi.md#saveTracksUser) | **PUT** /me/tracks | Save Tracks for Current User 



## addTracksToPlaylist_0

> ReorderOrReplacePlaylistsTracks200Response addTracksToPlaylist_0(playlistId, opts)

Add Items to Playlist 

Add one or more items to a user&#39;s playlist. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.TracksApi();
let playlistId = "3cEYpjA9oz9GiPac4AsH4n"; // String | 
let opts = {
  'position': 0, // Number | 
  'uris': "spotify:track:4iV5W9uYEdYUVa79Axb7Rh,spotify:track:1301WleyT98MSxVHPZCA6M", // String | 
  'addTracksToPlaylistRequest': new SpotifyWebApi.AddTracksToPlaylistRequest() // AddTracksToPlaylistRequest | 
};
apiInstance.addTracksToPlaylist_0(playlistId, opts, (error, data, response) => {
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


## checkUsersSavedTracks

> [Boolean] checkUsersSavedTracks(ids)

Check User&#39;s Saved Tracks 

Check if one or more tracks is already saved in the current Spotify user&#39;s &#39;Your Music&#39; library. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.TracksApi();
let ids = "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"; // String | 
apiInstance.checkUsersSavedTracks(ids, (error, data, response) => {
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


## getAnAlbumsTracks_0

> PagingSimplifiedTrackObject getAnAlbumsTracks_0(id, opts)

Get Album Tracks 

Get Spotify catalog information about an album’s tracks. Optional parameters can be used to limit the number of tracks returned. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.TracksApi();
let id = "4aawyAB9vmqN3uQ7FjRGTy"; // String | 
let opts = {
  'market': "ES", // String | 
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getAnAlbumsTracks_0(id, opts, (error, data, response) => {
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


## getAnArtistsTopTracks_0

> GetAnArtistsTopTracks200Response getAnArtistsTopTracks_0(id, opts)

Get Artist&#39;s Top Tracks 

Get Spotify catalog information about an artist&#39;s top tracks by country. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.TracksApi();
let id = "0TnOYISbd1XYRBk9myaseg"; // String | 
let opts = {
  'market': "ES" // String | 
};
apiInstance.getAnArtistsTopTracks_0(id, opts, (error, data, response) => {
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

[**GetAnArtistsTopTracks200Response**](GetAnArtistsTopTracks200Response.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAudioAnalysis

> AudioAnalysisObject getAudioAnalysis(id)

Get Track&#39;s Audio Analysis 

Get a low-level audio analysis for a track in the Spotify catalog. The audio analysis describes the track’s structure and musical content, including rhythm, pitch, and timbre. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.TracksApi();
let id = "11dFghVXANMlKmJXsNCbNl"; // String | 
apiInstance.getAudioAnalysis(id, (error, data, response) => {
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

### Return type

[**AudioAnalysisObject**](AudioAnalysisObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAudioFeatures

> AudioFeaturesObject getAudioFeatures(id)

Get Track&#39;s Audio Features 

Get audio feature information for a single track identified by its unique Spotify ID. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.TracksApi();
let id = "11dFghVXANMlKmJXsNCbNl"; // String | 
apiInstance.getAudioFeatures(id, (error, data, response) => {
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

### Return type

[**AudioFeaturesObject**](AudioFeaturesObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPlaylistsTracks_0

> PagingPlaylistTrackObject getPlaylistsTracks_0(playlistId, opts)

Get Playlist Items 

Get full details of the items of a playlist owned by a Spotify user. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.TracksApi();
let playlistId = "3cEYpjA9oz9GiPac4AsH4n"; // String | 
let opts = {
  'market': "ES", // String | 
  'fields': "items(added_by.id,track(name,href,album(name,href)))", // String | 
  'limit': 10, // Number | 
  'offset': 5, // Number | 
  'additionalTypes': "additionalTypes_example" // String | 
};
apiInstance.getPlaylistsTracks_0(playlistId, opts, (error, data, response) => {
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


## getRecommendations

> RecommendationsObject getRecommendations(seedArtists, seedGenres, seedTracks, opts)

Get Recommendations 

Recommendations are generated based on the available information for a given seed entity and matched against similar artists and tracks. If there is sufficient information about the provided seeds, a list of tracks will be returned together with pool size details.  For artists and tracks that are very new or obscure there might not be enough data to generate a list of tracks. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.TracksApi();
let seedArtists = "4NHQUGzhtTLFvgF5SZesLK"; // String | 
let seedGenres = "classical,country"; // String | 
let seedTracks = "0c6xIDDpzE81m2q797ordA"; // String | 
let opts = {
  'limit': 10, // Number | 
  'market': "ES", // String | 
  'minAcousticness': 3.4, // Number | 
  'maxAcousticness': 3.4, // Number | 
  'targetAcousticness': 3.4, // Number | 
  'minDanceability': 3.4, // Number | 
  'maxDanceability': 3.4, // Number | 
  'targetDanceability': 3.4, // Number | 
  'minDurationMs': 56, // Number | 
  'maxDurationMs': 56, // Number | 
  'targetDurationMs': 56, // Number | 
  'minEnergy': 3.4, // Number | 
  'maxEnergy': 3.4, // Number | 
  'targetEnergy': 3.4, // Number | 
  'minInstrumentalness': 3.4, // Number | 
  'maxInstrumentalness': 3.4, // Number | 
  'targetInstrumentalness': 3.4, // Number | 
  'minKey': 56, // Number | 
  'maxKey': 56, // Number | 
  'targetKey': 56, // Number | 
  'minLiveness': 3.4, // Number | 
  'maxLiveness': 3.4, // Number | 
  'targetLiveness': 3.4, // Number | 
  'minLoudness': 3.4, // Number | 
  'maxLoudness': 3.4, // Number | 
  'targetLoudness': 3.4, // Number | 
  'minMode': 56, // Number | 
  'maxMode': 56, // Number | 
  'targetMode': 56, // Number | 
  'minPopularity': 56, // Number | 
  'maxPopularity': 56, // Number | 
  'targetPopularity': 56, // Number | 
  'minSpeechiness': 3.4, // Number | 
  'maxSpeechiness': 3.4, // Number | 
  'targetSpeechiness': 3.4, // Number | 
  'minTempo': 3.4, // Number | 
  'maxTempo': 3.4, // Number | 
  'targetTempo': 3.4, // Number | 
  'minTimeSignature': 56, // Number | 
  'maxTimeSignature': 56, // Number | 
  'targetTimeSignature': 56, // Number | 
  'minValence': 3.4, // Number | 
  'maxValence': 3.4, // Number | 
  'targetValence': 3.4 // Number | 
};
apiInstance.getRecommendations(seedArtists, seedGenres, seedTracks, opts, (error, data, response) => {
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
 **seedArtists** | **String**|  | 
 **seedGenres** | **String**|  | 
 **seedTracks** | **String**|  | 
 **limit** | **Number**|  | [optional] [default to 20]
 **market** | **String**|  | [optional] 
 **minAcousticness** | **Number**|  | [optional] 
 **maxAcousticness** | **Number**|  | [optional] 
 **targetAcousticness** | **Number**|  | [optional] 
 **minDanceability** | **Number**|  | [optional] 
 **maxDanceability** | **Number**|  | [optional] 
 **targetDanceability** | **Number**|  | [optional] 
 **minDurationMs** | **Number**|  | [optional] 
 **maxDurationMs** | **Number**|  | [optional] 
 **targetDurationMs** | **Number**|  | [optional] 
 **minEnergy** | **Number**|  | [optional] 
 **maxEnergy** | **Number**|  | [optional] 
 **targetEnergy** | **Number**|  | [optional] 
 **minInstrumentalness** | **Number**|  | [optional] 
 **maxInstrumentalness** | **Number**|  | [optional] 
 **targetInstrumentalness** | **Number**|  | [optional] 
 **minKey** | **Number**|  | [optional] 
 **maxKey** | **Number**|  | [optional] 
 **targetKey** | **Number**|  | [optional] 
 **minLiveness** | **Number**|  | [optional] 
 **maxLiveness** | **Number**|  | [optional] 
 **targetLiveness** | **Number**|  | [optional] 
 **minLoudness** | **Number**|  | [optional] 
 **maxLoudness** | **Number**|  | [optional] 
 **targetLoudness** | **Number**|  | [optional] 
 **minMode** | **Number**|  | [optional] 
 **maxMode** | **Number**|  | [optional] 
 **targetMode** | **Number**|  | [optional] 
 **minPopularity** | **Number**|  | [optional] 
 **maxPopularity** | **Number**|  | [optional] 
 **targetPopularity** | **Number**|  | [optional] 
 **minSpeechiness** | **Number**|  | [optional] 
 **maxSpeechiness** | **Number**|  | [optional] 
 **targetSpeechiness** | **Number**|  | [optional] 
 **minTempo** | **Number**|  | [optional] 
 **maxTempo** | **Number**|  | [optional] 
 **targetTempo** | **Number**|  | [optional] 
 **minTimeSignature** | **Number**|  | [optional] 
 **maxTimeSignature** | **Number**|  | [optional] 
 **targetTimeSignature** | **Number**|  | [optional] 
 **minValence** | **Number**|  | [optional] 
 **maxValence** | **Number**|  | [optional] 
 **targetValence** | **Number**|  | [optional] 

### Return type

[**RecommendationsObject**](RecommendationsObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSeveralAudioFeatures

> GetSeveralAudioFeatures200Response getSeveralAudioFeatures(ids)

Get Tracks&#39; Audio Features 

Get audio features for multiple tracks based on their Spotify IDs. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.TracksApi();
let ids = "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"; // String | 
apiInstance.getSeveralAudioFeatures(ids, (error, data, response) => {
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

[**GetSeveralAudioFeatures200Response**](GetSeveralAudioFeatures200Response.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSeveralTracks

> GetAnArtistsTopTracks200Response getSeveralTracks(ids, opts)

Get Several Tracks 

Get Spotify catalog information for multiple tracks based on their Spotify IDs. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.TracksApi();
let ids = "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"; // String | 
let opts = {
  'market': "ES" // String | 
};
apiInstance.getSeveralTracks(ids, opts, (error, data, response) => {
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

[**GetAnArtistsTopTracks200Response**](GetAnArtistsTopTracks200Response.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTrack

> TrackObject getTrack(id, opts)

Get Track 

Get Spotify catalog information for a single track identified by its unique Spotify ID. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.TracksApi();
let id = "11dFghVXANMlKmJXsNCbNl"; // String | 
let opts = {
  'market': "ES" // String | 
};
apiInstance.getTrack(id, opts, (error, data, response) => {
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

[**TrackObject**](TrackObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUsersSavedTracks

> PagingSavedTrackObject getUsersSavedTracks(opts)

Get User&#39;s Saved Tracks 

Get a list of the songs saved in the current Spotify user&#39;s &#39;Your Music&#39; library. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.TracksApi();
let opts = {
  'market': "ES", // String | 
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getUsersSavedTracks(opts, (error, data, response) => {
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


## getUsersTopArtistsAndTracks_0

> GetUsersTopArtistsAndTracks200Response getUsersTopArtistsAndTracks_0(type, opts)

Get User&#39;s Top Items 

Get the current user&#39;s top artists or tracks based on calculated affinity. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.TracksApi();
let type = "type_example"; // String | 
let opts = {
  'timeRange': "medium_term", // String | 
  'limit': 10, // Number | 
  'offset': 5 // Number | 
};
apiInstance.getUsersTopArtistsAndTracks_0(type, opts, (error, data, response) => {
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


## removeTracksPlaylist_0

> ReorderOrReplacePlaylistsTracks200Response removeTracksPlaylist_0(playlistId, opts)

Remove Playlist Items 

Remove one or more items from a user&#39;s playlist. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.TracksApi();
let playlistId = "3cEYpjA9oz9GiPac4AsH4n"; // String | 
let opts = {
  'removeTracksPlaylistRequest': new SpotifyWebApi.RemoveTracksPlaylistRequest() // RemoveTracksPlaylistRequest | 
};
apiInstance.removeTracksPlaylist_0(playlistId, opts, (error, data, response) => {
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


## removeTracksUser

> removeTracksUser(ids, opts)

Remove User&#39;s Saved Tracks 

Remove one or more tracks from the current user&#39;s &#39;Your Music&#39; library. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.TracksApi();
let ids = "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"; // String | 
let opts = {
  'saveAlbumsUserRequest': new SpotifyWebApi.SaveAlbumsUserRequest() // SaveAlbumsUserRequest | 
};
apiInstance.removeTracksUser(ids, opts, (error, data, response) => {
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


## reorderOrReplacePlaylistsTracks_0

> ReorderOrReplacePlaylistsTracks200Response reorderOrReplacePlaylistsTracks_0(playlistId, opts)

Update Playlist Items 

Either reorder or replace items in a playlist depending on the request&#39;s parameters. To reorder items, include &#x60;range_start&#x60;, &#x60;insert_before&#x60;, &#x60;range_length&#x60; and &#x60;snapshot_id&#x60; in the request&#39;s body. To replace items, include &#x60;uris&#x60; as either a query parameter or in the request&#39;s body. Replacing items in a playlist will overwrite its existing items. This operation can be used for replacing or clearing items in a playlist. &lt;br/&gt; **Note**: Replace and reorder are mutually exclusive operations which share the same endpoint, but have different parameters. These operations can&#39;t be applied together in a single request. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.TracksApi();
let playlistId = "3cEYpjA9oz9GiPac4AsH4n"; // String | 
let opts = {
  'uris': "uris_example", // String | 
  'reorderOrReplacePlaylistsTracksRequest': new SpotifyWebApi.ReorderOrReplacePlaylistsTracksRequest() // ReorderOrReplacePlaylistsTracksRequest | 
};
apiInstance.reorderOrReplacePlaylistsTracks_0(playlistId, opts, (error, data, response) => {
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


## saveTracksUser

> saveTracksUser(ids, opts)

Save Tracks for Current User 

Save one or more tracks to the current user&#39;s &#39;Your Music&#39; library. 

### Example

```javascript
import SpotifyWebApi from 'spotify_web_api';
let defaultClient = SpotifyWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApi.TracksApi();
let ids = "7ouMYWpwJ422jRcDASZB7P,4VqPOruhp5EdPBeR92t6lQ,2takcwOaAZWiXQijPHIx7B"; // String | 
let opts = {
  'saveTracksUserRequest': new SpotifyWebApi.SaveTracksUserRequest() // SaveTracksUserRequest | 
};
apiInstance.saveTracksUser(ids, opts, (error, data, response) => {
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

