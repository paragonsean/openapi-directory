# SpotifyWebApiWithFixesAndImprovementsFromSonallux.PlayerApi

All URIs are relative to *https://api.spotify.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addToQueue**](PlayerApi.md#addToQueue) | **POST** /me/player/queue | Add Item to Playback Queue 
[**getAUsersAvailableDevices**](PlayerApi.md#getAUsersAvailableDevices) | **GET** /me/player/devices | Get Available Devices 
[**getInformationAboutTheUsersCurrentPlayback**](PlayerApi.md#getInformationAboutTheUsersCurrentPlayback) | **GET** /me/player | Get Playback State 
[**getQueue**](PlayerApi.md#getQueue) | **GET** /me/player/queue | Get the User&#39;s Queue 
[**getRecentlyPlayed**](PlayerApi.md#getRecentlyPlayed) | **GET** /me/player/recently-played | Get Recently Played Tracks 
[**getTheUsersCurrentlyPlayingTrack**](PlayerApi.md#getTheUsersCurrentlyPlayingTrack) | **GET** /me/player/currently-playing | Get Currently Playing Track 
[**pauseAUsersPlayback**](PlayerApi.md#pauseAUsersPlayback) | **PUT** /me/player/pause | Pause Playback 
[**seekToPositionInCurrentlyPlayingTrack**](PlayerApi.md#seekToPositionInCurrentlyPlayingTrack) | **PUT** /me/player/seek | Seek To Position 
[**setRepeatModeOnUsersPlayback**](PlayerApi.md#setRepeatModeOnUsersPlayback) | **PUT** /me/player/repeat | Set Repeat Mode 
[**setVolumeForUsersPlayback**](PlayerApi.md#setVolumeForUsersPlayback) | **PUT** /me/player/volume | Set Playback Volume 
[**skipUsersPlaybackToNextTrack**](PlayerApi.md#skipUsersPlaybackToNextTrack) | **POST** /me/player/next | Skip To Next 
[**skipUsersPlaybackToPreviousTrack**](PlayerApi.md#skipUsersPlaybackToPreviousTrack) | **POST** /me/player/previous | Skip To Previous 
[**startAUsersPlayback**](PlayerApi.md#startAUsersPlayback) | **PUT** /me/player/play | Start/Resume Playback 
[**toggleShuffleForUsersPlayback**](PlayerApi.md#toggleShuffleForUsersPlayback) | **PUT** /me/player/shuffle | Toggle Playback Shuffle 
[**transferAUsersPlayback**](PlayerApi.md#transferAUsersPlayback) | **PUT** /me/player | Transfer Playback 



## addToQueue

> addToQueue(uri, opts)

Add Item to Playback Queue 

Add an item to the end of the user&#39;s current playback queue. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.PlayerApi();
let uri = "spotify:track:4iV5W9uYEdYUVa79Axb7Rh"; // String | 
let opts = {
  'deviceId': "0d1841b0976bae2a3a310dd74c0f3df354899bc8" // String | 
};
apiInstance.addToQueue(uri, opts, (error, data, response) => {
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
 **uri** | **String**|  | 
 **deviceId** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAUsersAvailableDevices

> DevicesObject getAUsersAvailableDevices()

Get Available Devices 

Get information about a user’s available devices. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.PlayerApi();
apiInstance.getAUsersAvailableDevices((error, data, response) => {
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

[**DevicesObject**](DevicesObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInformationAboutTheUsersCurrentPlayback

> CurrentlyPlayingContextObject getInformationAboutTheUsersCurrentPlayback(opts)

Get Playback State 

Get information about the user’s current playback state, including track or episode, progress, and active device. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.PlayerApi();
let opts = {
  'market': "ES", // String | 
  'additionalTypes': "additionalTypes_example" // String | 
};
apiInstance.getInformationAboutTheUsersCurrentPlayback(opts, (error, data, response) => {
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
 **additionalTypes** | **String**|  | [optional] 

### Return type

[**CurrentlyPlayingContextObject**](CurrentlyPlayingContextObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getQueue

> QueueObject getQueue()

Get the User&#39;s Queue 

Get the list of objects that make up the user&#39;s queue. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.PlayerApi();
apiInstance.getQueue((error, data, response) => {
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

[**QueueObject**](QueueObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRecentlyPlayed

> CursorPagingPlayHistoryObject getRecentlyPlayed(opts)

Get Recently Played Tracks 

Get tracks from the current user&#39;s recently played tracks. _**Note**: Currently doesn&#39;t support podcast episodes._ 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.PlayerApi();
let opts = {
  'limit': 10, // Number | 
  'after': 1484811043508, // Number | 
  'before': 56 // Number | 
};
apiInstance.getRecentlyPlayed(opts, (error, data, response) => {
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
 **after** | **Number**|  | [optional] 
 **before** | **Number**|  | [optional] 

### Return type

[**CursorPagingPlayHistoryObject**](CursorPagingPlayHistoryObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getTheUsersCurrentlyPlayingTrack

> CurrentlyPlayingObject getTheUsersCurrentlyPlayingTrack(opts)

Get Currently Playing Track 

Get the object currently being played on the user&#39;s Spotify account. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.PlayerApi();
let opts = {
  'market': "ES", // String | 
  'additionalTypes': "additionalTypes_example" // String | 
};
apiInstance.getTheUsersCurrentlyPlayingTrack(opts, (error, data, response) => {
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
 **additionalTypes** | **String**|  | [optional] 

### Return type

[**CurrentlyPlayingObject**](CurrentlyPlayingObject.md)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pauseAUsersPlayback

> pauseAUsersPlayback(opts)

Pause Playback 

Pause playback on the user&#39;s account. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.PlayerApi();
let opts = {
  'deviceId': "0d1841b0976bae2a3a310dd74c0f3df354899bc8" // String | 
};
apiInstance.pauseAUsersPlayback(opts, (error, data, response) => {
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
 **deviceId** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## seekToPositionInCurrentlyPlayingTrack

> seekToPositionInCurrentlyPlayingTrack(positionMs, opts)

Seek To Position 

Seeks to the given position in the user’s currently playing track. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.PlayerApi();
let positionMs = 25000; // Number | 
let opts = {
  'deviceId': "0d1841b0976bae2a3a310dd74c0f3df354899bc8" // String | 
};
apiInstance.seekToPositionInCurrentlyPlayingTrack(positionMs, opts, (error, data, response) => {
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
 **positionMs** | **Number**|  | 
 **deviceId** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setRepeatModeOnUsersPlayback

> setRepeatModeOnUsersPlayback(state, opts)

Set Repeat Mode 

Set the repeat mode for the user&#39;s playback. Options are repeat-track, repeat-context, and off. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.PlayerApi();
let state = "context"; // String | 
let opts = {
  'deviceId': "0d1841b0976bae2a3a310dd74c0f3df354899bc8" // String | 
};
apiInstance.setRepeatModeOnUsersPlayback(state, opts, (error, data, response) => {
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
 **state** | **String**|  | 
 **deviceId** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## setVolumeForUsersPlayback

> setVolumeForUsersPlayback(volumePercent, opts)

Set Playback Volume 

Set the volume for the user’s current playback device. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.PlayerApi();
let volumePercent = 50; // Number | 
let opts = {
  'deviceId': "0d1841b0976bae2a3a310dd74c0f3df354899bc8" // String | 
};
apiInstance.setVolumeForUsersPlayback(volumePercent, opts, (error, data, response) => {
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
 **volumePercent** | **Number**|  | 
 **deviceId** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## skipUsersPlaybackToNextTrack

> skipUsersPlaybackToNextTrack(opts)

Skip To Next 

Skips to next track in the user’s queue. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.PlayerApi();
let opts = {
  'deviceId': "0d1841b0976bae2a3a310dd74c0f3df354899bc8" // String | 
};
apiInstance.skipUsersPlaybackToNextTrack(opts, (error, data, response) => {
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
 **deviceId** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## skipUsersPlaybackToPreviousTrack

> skipUsersPlaybackToPreviousTrack(opts)

Skip To Previous 

Skips to previous track in the user’s queue. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.PlayerApi();
let opts = {
  'deviceId': "0d1841b0976bae2a3a310dd74c0f3df354899bc8" // String | 
};
apiInstance.skipUsersPlaybackToPreviousTrack(opts, (error, data, response) => {
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
 **deviceId** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startAUsersPlayback

> startAUsersPlayback(opts)

Start/Resume Playback 

Start a new context or resume current playback on the user&#39;s active device. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.PlayerApi();
let opts = {
  'deviceId': "0d1841b0976bae2a3a310dd74c0f3df354899bc8", // String | 
  'startAUsersPlaybackRequest': new SpotifyWebApiWithFixesAndImprovementsFromSonallux.StartAUsersPlaybackRequest() // StartAUsersPlaybackRequest | 
};
apiInstance.startAUsersPlayback(opts, (error, data, response) => {
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
 **deviceId** | **String**|  | [optional] 
 **startAUsersPlaybackRequest** | [**StartAUsersPlaybackRequest**](StartAUsersPlaybackRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## toggleShuffleForUsersPlayback

> toggleShuffleForUsersPlayback(state, opts)

Toggle Playback Shuffle 

Toggle shuffle on or off for user’s playback. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.PlayerApi();
let state = true; // Boolean | 
let opts = {
  'deviceId': "0d1841b0976bae2a3a310dd74c0f3df354899bc8" // String | 
};
apiInstance.toggleShuffleForUsersPlayback(state, opts, (error, data, response) => {
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
 **state** | **Boolean**|  | 
 **deviceId** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transferAUsersPlayback

> transferAUsersPlayback(opts)

Transfer Playback 

Transfer playback to a new device and determine if it should start playing. 

### Example

```javascript
import SpotifyWebApiWithFixesAndImprovementsFromSonallux from 'spotify_web_api_with_fixes_and_improvements_from_sonallux';
let defaultClient = SpotifyWebApiWithFixesAndImprovementsFromSonallux.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth_2_0
let oauth_2_0 = defaultClient.authentications['oauth_2_0'];
oauth_2_0.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SpotifyWebApiWithFixesAndImprovementsFromSonallux.PlayerApi();
let opts = {
  'transferAUsersPlaybackRequest': new SpotifyWebApiWithFixesAndImprovementsFromSonallux.TransferAUsersPlaybackRequest() // TransferAUsersPlaybackRequest | 
};
apiInstance.transferAUsersPlayback(opts, (error, data, response) => {
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
 **transferAUsersPlaybackRequest** | [**TransferAUsersPlaybackRequest**](TransferAUsersPlaybackRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[oauth_2_0](../README.md#oauth_2_0)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

