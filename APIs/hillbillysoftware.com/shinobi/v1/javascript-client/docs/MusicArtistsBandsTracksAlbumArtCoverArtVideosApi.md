# Shinobiapi.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi

All URIs are relative to *https://api.hillbillysoftware.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**musiVideosGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musiVideosGet) | **GET** /Music/Videos/{AccessToken}/{ArtistID} | Lists all videos available for this Artist / Band
[**musicAlbumArtGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicAlbumArtGet) | **GET** /Music/Albums/Art/{AccessToken}/{AlbumID} | Returns Albumart for passed AlbumID
[**musicAlbumsGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicAlbumsGet) | **GET** /Music/Albums/{AccessToken}/{ArtistID} | Get albums from passed ArtistID
[**musicArtistExtendedGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicArtistExtendedGet) | **GET** /Music/Artist/Extended/{AccessToken}/{Name} | Provides extended information, which includes all known albums and music videos of artist / band
[**musicByMusicBrainzGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicByMusicBrainzGet) | **GET** /Music/Albums/MusicBrainzID/{AccessToken}/{MBID} | Get Artist / Band information on MusicBrainzID
[**musicCDCoversGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicCDCoversGet) | **GET** /Music/Albums/CoverArt/{AccessToken}/{MBID} | Gets CD art for passed MusicBrainzID
[**musicCoverArtByNameGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicCoverArtByNameGet) | **GET** /Music/Artist/Art/Name/{AccessToken}/{Name} | Retrieves artist / band Banner and logo based on artist or bandname
[**musicCoverArtGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicCoverArtGet) | **GET** /Music/Artist/Art/ID/{AccessToken}/{ArtistID} | Retrieves artist / band Banner and logo based on ArtistID
[**musicGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicGet) | **GET** /Music/Artist/{AccessToken}/{Name} | Get information about passed band name or artist
[**musicLyricsBySongGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicLyricsBySongGet) | **GET** /Music/Lyrics/BySong/{AccessToken}/{Song} | Get lyrics on song title
[**musicLyricsGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicLyricsGet) | **GET** /Music/Lyrics/ByName/{AccessToken}/{Name} | Get lyrics for band or artist (record set limited to 25)
[**musicLyricsbyAlbumIDGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicLyricsbyAlbumIDGet) | **GET** /Music/Lyrics/AlbumID/{AccessToken}/{AlbumID} | Returns all lyrics for requested AlbumID
[**musicTracksGet**](MusicArtistsBandsTracksAlbumArtCoverArtVideosApi.md#musicTracksGet) | **GET** /Music/Tracks/{AccessToken}/{AlbumID} | Get all tracks from requested album



## musiVideosGet

> [MusicVideo] musiVideosGet(accessToken, artistID)

Lists all videos available for this Artist / Band

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi();
let accessToken = "accessToken_example"; // String | 
let artistID = "artistID_example"; // String | 
apiInstance.musiVideosGet(accessToken, artistID, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **artistID** | **String**|  | 

### Return type

[**[MusicVideo]**](MusicVideo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## musicAlbumArtGet

> AlbumArt musicAlbumArtGet(accessToken, albumID)

Returns Albumart for passed AlbumID

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi();
let accessToken = "accessToken_example"; // String | 
let albumID = "albumID_example"; // String | 
apiInstance.musicAlbumArtGet(accessToken, albumID, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **albumID** | **String**|  | 

### Return type

[**AlbumArt**](AlbumArt.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## musicAlbumsGet

> [BandAlbums] musicAlbumsGet(accessToken, artistID)

Get albums from passed ArtistID

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi();
let accessToken = "accessToken_example"; // String | 
let artistID = "artistID_example"; // String | ID of artist or band to retrieve albums from
apiInstance.musicAlbumsGet(accessToken, artistID, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **artistID** | **String**| ID of artist or band to retrieve albums from | 

### Return type

[**[BandAlbums]**](BandAlbums.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## musicArtistExtendedGet

> [BandInfoExtended] musicArtistExtendedGet(accessToken, name)

Provides extended information, which includes all known albums and music videos of artist / band

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi();
let accessToken = "accessToken_example"; // String | 
let name = "name_example"; // String | 
apiInstance.musicArtistExtendedGet(accessToken, name, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **name** | **String**|  | 

### Return type

[**[BandInfoExtended]**](BandInfoExtended.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## musicByMusicBrainzGet

> [BandInfo] musicByMusicBrainzGet(accessToken, MBID)

Get Artist / Band information on MusicBrainzID

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi();
let accessToken = "accessToken_example"; // String | 
let MBID = "MBID_example"; // String | MusicBrainzID
apiInstance.musicByMusicBrainzGet(accessToken, MBID, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **MBID** | **String**| MusicBrainzID | 

### Return type

[**[BandInfo]**](BandInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## musicCDCoversGet

> [CDCoverArt] musicCDCoversGet(accessToken, MBID)

Gets CD art for passed MusicBrainzID

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi();
let accessToken = "accessToken_example"; // String | 
let MBID = "MBID_example"; // String | MusicBrainzID
apiInstance.musicCDCoversGet(accessToken, MBID, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **MBID** | **String**| MusicBrainzID | 

### Return type

[**[CDCoverArt]**](CDCoverArt.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## musicCoverArtByNameGet

> ArtistArt musicCoverArtByNameGet(accessToken, name)

Retrieves artist / band Banner and logo based on artist or bandname

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi();
let accessToken = "accessToken_example"; // String | 
let name = "name_example"; // String | Name of artist or band
apiInstance.musicCoverArtByNameGet(accessToken, name, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **name** | **String**| Name of artist or band | 

### Return type

[**ArtistArt**](ArtistArt.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## musicCoverArtGet

> ArtistArt musicCoverArtGet(accessToken, artistID)

Retrieves artist / band Banner and logo based on ArtistID

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi();
let accessToken = "accessToken_example"; // String | 
let artistID = "artistID_example"; // String | ArtistID of artist or band
apiInstance.musicCoverArtGet(accessToken, artistID, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **artistID** | **String**| ArtistID of artist or band | 

### Return type

[**ArtistArt**](ArtistArt.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## musicGet

> [BandInfo] musicGet(accessToken, name)

Get information about passed band name or artist

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi();
let accessToken = "accessToken_example"; // String | 
let name = "name_example"; // String | Name (or part) of band or artist name
apiInstance.musicGet(accessToken, name, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **name** | **String**| Name (or part) of band or artist name | 

### Return type

[**[BandInfo]**](BandInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## musicLyricsBySongGet

> [Lyric] musicLyricsBySongGet(accessToken, song)

Get lyrics on song title

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi();
let accessToken = "accessToken_example"; // String | 
let song = "song_example"; // String | Name or part of song name
apiInstance.musicLyricsBySongGet(accessToken, song, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **song** | **String**| Name or part of song name | 

### Return type

[**[Lyric]**](Lyric.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## musicLyricsGet

> [Lyric] musicLyricsGet(accessToken, name)

Get lyrics for band or artist (record set limited to 25)

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi();
let accessToken = "accessToken_example"; // String | 
let name = "name_example"; // String | Name (or partial) of band or artist (record set limited to 25)
apiInstance.musicLyricsGet(accessToken, name, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **name** | **String**| Name (or partial) of band or artist (record set limited to 25) | 

### Return type

[**[Lyric]**](Lyric.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## musicLyricsbyAlbumIDGet

> [Lyric] musicLyricsbyAlbumIDGet(accessToken, albumID)

Returns all lyrics for requested AlbumID

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi();
let accessToken = "accessToken_example"; // String | 
let albumID = "albumID_example"; // String | 
apiInstance.musicLyricsbyAlbumIDGet(accessToken, albumID, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **albumID** | **String**|  | 

### Return type

[**[Lyric]**](Lyric.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## musicTracksGet

> [AlbumTracks] musicTracksGet(accessToken, albumID)

Get all tracks from requested album

### Example

```javascript
import Shinobiapi from 'shinobiapi';

let apiInstance = new Shinobiapi.MusicArtistsBandsTracksAlbumArtCoverArtVideosApi();
let accessToken = "accessToken_example"; // String | 
let albumID = "albumID_example"; // String | AlbumID (can be retrieved via album endpoint)
apiInstance.musicTracksGet(accessToken, albumID, (error, data, response) => {
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
 **accessToken** | **String**|  | 
 **albumID** | **String**| AlbumID (can be retrieved via album endpoint) | 

### Return type

[**[AlbumTracks]**](AlbumTracks.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

