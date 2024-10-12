# MusixmatchApi.TrackApi

All URIs are relative to *https://api.musixmatch.com/ws/1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**albumTracksGetGet**](TrackApi.md#albumTracksGetGet) | **GET** /album.tracks.get | 
[**chartTracksGetGet**](TrackApi.md#chartTracksGetGet) | **GET** /chart.tracks.get | 
[**matcherTrackGetGet**](TrackApi.md#matcherTrackGetGet) | **GET** /matcher.track.get | 
[**trackGetGet**](TrackApi.md#trackGetGet) | **GET** /track.get | 
[**trackSearchGet**](TrackApi.md#trackSearchGet) | **GET** /track.search | 



## albumTracksGetGet

> AlbumTracksGetGet200Response albumTracksGetGet(albumId, opts)



### Example

```javascript
import MusixmatchApi from 'musixmatch_api';
let defaultClient = MusixmatchApi.ApiClient.instance;
// Configure API key authorization: key
let key = defaultClient.authentications['key'];
key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//key.apiKeyPrefix = 'Token';

let apiInstance = new MusixmatchApi.TrackApi();
let albumId = "albumId_example"; // String | The musiXmatch album id
let opts = {
  'format': "'json'", // String | output format: json, jsonp, xml.
  'callback': "callback_example", // String | jsonp callback
  'fHasLyrics': "fHasLyrics_example", // String | When set, filter only contents with lyrics
  'page': 3.4, // Number | Define the page number for paginated results
  'pageSize': 3.4 // Number | Define the page size for paginated results.Range is 1 to 100.
};
apiInstance.albumTracksGetGet(albumId, opts, (error, data, response) => {
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
 **albumId** | **String**| The musiXmatch album id | 
 **format** | **String**| output format: json, jsonp, xml. | [optional] [default to &#39;json&#39;]
 **callback** | **String**| jsonp callback | [optional] 
 **fHasLyrics** | **String**| When set, filter only contents with lyrics | [optional] 
 **page** | **Number**| Define the page number for paginated results | [optional] 
 **pageSize** | **Number**| Define the page size for paginated results.Range is 1 to 100. | [optional] 

### Return type

[**AlbumTracksGetGet200Response**](AlbumTracksGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chartTracksGetGet

> ChartTracksGetGet200Response chartTracksGetGet(opts)



### Example

```javascript
import MusixmatchApi from 'musixmatch_api';
let defaultClient = MusixmatchApi.ApiClient.instance;
// Configure API key authorization: key
let key = defaultClient.authentications['key'];
key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//key.apiKeyPrefix = 'Token';

let apiInstance = new MusixmatchApi.TrackApi();
let opts = {
  'format': "'json'", // String | output format: json, jsonp, xml.
  'callback': "callback_example", // String | jsonp callback
  'page': 3.4, // Number | Define the page number for paginated results
  'pageSize': 3.4, // Number | Define the page size for paginated results.Range is 1 to 100.
  'country': "'us'", // String | A valid ISO 3166 country code
  'fHasLyrics': "fHasLyrics_example" // String | When set, filter only contents with lyrics
};
apiInstance.chartTracksGetGet(opts, (error, data, response) => {
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
 **format** | **String**| output format: json, jsonp, xml. | [optional] [default to &#39;json&#39;]
 **callback** | **String**| jsonp callback | [optional] 
 **page** | **Number**| Define the page number for paginated results | [optional] 
 **pageSize** | **Number**| Define the page size for paginated results.Range is 1 to 100. | [optional] 
 **country** | **String**| A valid ISO 3166 country code | [optional] [default to &#39;us&#39;]
 **fHasLyrics** | **String**| When set, filter only contents with lyrics | [optional] 

### Return type

[**ChartTracksGetGet200Response**](ChartTracksGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## matcherTrackGetGet

> MatcherTrackGetGet200Response matcherTrackGetGet(opts)



### Example

```javascript
import MusixmatchApi from 'musixmatch_api';
let defaultClient = MusixmatchApi.ApiClient.instance;
// Configure API key authorization: key
let key = defaultClient.authentications['key'];
key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//key.apiKeyPrefix = 'Token';

let apiInstance = new MusixmatchApi.TrackApi();
let opts = {
  'format': "'json'", // String | output format: json, jsonp, xml.
  'callback': "callback_example", // String | jsonp callback
  'qArtist': "qArtist_example", // String | The song artist
  'qTrack': "qTrack_example", // String | The song title
  'fHasLyrics': 3.4, // Number | When set, filter only contents with lyrics
  'fHasSubtitle': 3.4 // Number | When set, filter only contents with subtitles
};
apiInstance.matcherTrackGetGet(opts, (error, data, response) => {
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
 **format** | **String**| output format: json, jsonp, xml. | [optional] [default to &#39;json&#39;]
 **callback** | **String**| jsonp callback | [optional] 
 **qArtist** | **String**| The song artist | [optional] 
 **qTrack** | **String**| The song title | [optional] 
 **fHasLyrics** | **Number**| When set, filter only contents with lyrics | [optional] 
 **fHasSubtitle** | **Number**| When set, filter only contents with subtitles | [optional] 

### Return type

[**MatcherTrackGetGet200Response**](MatcherTrackGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trackGetGet

> MatcherTrackGetGet200Response trackGetGet(trackId, opts)



### Example

```javascript
import MusixmatchApi from 'musixmatch_api';
let defaultClient = MusixmatchApi.ApiClient.instance;
// Configure API key authorization: key
let key = defaultClient.authentications['key'];
key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//key.apiKeyPrefix = 'Token';

let apiInstance = new MusixmatchApi.TrackApi();
let trackId = "trackId_example"; // String | The musiXmatch track id
let opts = {
  'format': "'json'", // String | output format: json, jsonp, xml.
  'callback': "callback_example" // String | jsonp callback
};
apiInstance.trackGetGet(trackId, opts, (error, data, response) => {
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
 **trackId** | **String**| The musiXmatch track id | 
 **format** | **String**| output format: json, jsonp, xml. | [optional] [default to &#39;json&#39;]
 **callback** | **String**| jsonp callback | [optional] 

### Return type

[**MatcherTrackGetGet200Response**](MatcherTrackGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## trackSearchGet

> ChartTracksGetGet200Response trackSearchGet(opts)



### Example

```javascript
import MusixmatchApi from 'musixmatch_api';
let defaultClient = MusixmatchApi.ApiClient.instance;
// Configure API key authorization: key
let key = defaultClient.authentications['key'];
key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//key.apiKeyPrefix = 'Token';

let apiInstance = new MusixmatchApi.TrackApi();
let opts = {
  'format': "'json'", // String | output format: json, jsonp, xml.
  'callback': "callback_example", // String | jsonp callback
  'qTrack': "qTrack_example", // String | The song title
  'qArtist': "qArtist_example", // String | The song artist
  'qLyrics': "qLyrics_example", // String | Any word in the lyrics
  'fArtistId': 3.4, // Number | When set, filter by this artist id
  'fMusicGenreId': 3.4, // Number | When set, filter by this music category id
  'fLyricsLanguage': 3.4, // Number | Filter by the lyrics language (en,it,..)
  'fHasLyrics': 3.4, // Number | When set, filter only contents with lyrics
  'sArtistRating': "sArtistRating_example", // String | Sort by our popularity index for artists (asc|desc)
  'sTrackRating': "sTrackRating_example", // String | Sort by our popularity index for tracks (asc|desc)
  'quorumFactor': 1.0, // Number | Search only a part of the given query string.Allowed range is (0.1 – 0.9)
  'pageSize': 3.4, // Number | Define the page size for paginated results.Range is 1 to 100.
  'page': 3.4 // Number | Define the page number for paginated results
};
apiInstance.trackSearchGet(opts, (error, data, response) => {
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
 **format** | **String**| output format: json, jsonp, xml. | [optional] [default to &#39;json&#39;]
 **callback** | **String**| jsonp callback | [optional] 
 **qTrack** | **String**| The song title | [optional] 
 **qArtist** | **String**| The song artist | [optional] 
 **qLyrics** | **String**| Any word in the lyrics | [optional] 
 **fArtistId** | **Number**| When set, filter by this artist id | [optional] 
 **fMusicGenreId** | **Number**| When set, filter by this music category id | [optional] 
 **fLyricsLanguage** | **Number**| Filter by the lyrics language (en,it,..) | [optional] 
 **fHasLyrics** | **Number**| When set, filter only contents with lyrics | [optional] 
 **sArtistRating** | **String**| Sort by our popularity index for artists (asc|desc) | [optional] 
 **sTrackRating** | **String**| Sort by our popularity index for tracks (asc|desc) | [optional] 
 **quorumFactor** | **Number**| Search only a part of the given query string.Allowed range is (0.1 – 0.9) | [optional] [default to 1.0]
 **pageSize** | **Number**| Define the page size for paginated results.Range is 1 to 100. | [optional] 
 **page** | **Number**| Define the page number for paginated results | [optional] 

### Return type

[**ChartTracksGetGet200Response**](ChartTracksGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

