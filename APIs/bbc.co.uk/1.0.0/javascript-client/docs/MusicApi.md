# RadioMusicServices.MusicApi

All URIs are relative to *https://rms.api.bbc.co.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletePersonalisedMusicFavouritesByTypeById**](MusicApi.md#deletePersonalisedMusicFavouritesByTypeById) | **DELETE** /my/music/favourites/{type}/{id} | Favourite Track or Clip
[**deletePersonalisedMusicFollowsByTypeById**](MusicApi.md#deletePersonalisedMusicFollowsByTypeById) | **DELETE** /my/music/follows/{type}/{id} | Followed Network, Category, Artist, Playlist and Genre
[**getMusicPopularArtistById**](MusicApi.md#getMusicPopularArtistById) | **GET** /music/popular/artists/{id} | Single Artist Popularity
[**getMusicPopularArtists**](MusicApi.md#getMusicPopularArtists) | **GET** /music/popular/artists | Popular Artists
[**getMusicPopularPlaylistById**](MusicApi.md#getMusicPopularPlaylistById) | **GET** /music/popular/playlists/{id} | Single Playlist Popularity
[**getMusicPopularPlaylists**](MusicApi.md#getMusicPopularPlaylists) | **GET** /music/popular/playlists | Popular Playlists
[**getMusicPopularTrackById**](MusicApi.md#getMusicPopularTrackById) | **GET** /music/popular/tracks/{id} | Single Track Popularity
[**getMusicPopularTracks**](MusicApi.md#getMusicPopularTracks) | **GET** /music/popular/tracks | Popular Tracks
[**getPersonalisedMusicFavourites**](MusicApi.md#getPersonalisedMusicFavourites) | **GET** /my/music/favourites | Favourite Tracks or Clips
[**getPersonalisedMusicFavouritesByType**](MusicApi.md#getPersonalisedMusicFavouritesByType) | **GET** /my/music/favourites/{type} | Favourite Tracks or Clips by Type
[**getPersonalisedMusicFavouritesByTypeById**](MusicApi.md#getPersonalisedMusicFavouritesByTypeById) | **GET** /my/music/favourites/{type}/{id} | Favourite Track or Clip
[**getPersonalisedMusicFollows**](MusicApi.md#getPersonalisedMusicFollows) | **GET** /my/music/follows | Followed Networks, Categories, Artists, Playlists and Genres
[**getPersonalisedMusicFollowsByType**](MusicApi.md#getPersonalisedMusicFollowsByType) | **GET** /my/music/follows/{type} | Followed Networks, Categories, Artists, Playlists and Genres by Type
[**getPersonalisedMusicFollowsByTypeById**](MusicApi.md#getPersonalisedMusicFollowsByTypeById) | **GET** /my/music/follows/{type}/{id} | Followed Network, Category, Artist, Playlist and Genre
[**postPersonalisedMusicFavouritesBatch**](MusicApi.md#postPersonalisedMusicFavouritesBatch) | **POST** /my/music/favourites | Favourite Tracks or Clips
[**postPersonalisedMusicFavouritesByTypeById**](MusicApi.md#postPersonalisedMusicFavouritesByTypeById) | **POST** /my/music/favourites/{type}/{id} | Favourite Track or Clip
[**postPersonalisedMusicFollowsBatch**](MusicApi.md#postPersonalisedMusicFollowsBatch) | **POST** /my/music/follows | Followed Networks, Categories, Artists, Playlists and Genres
[**postPersonalisedMusicFollowsByTypeById**](MusicApi.md#postPersonalisedMusicFollowsByTypeById) | **POST** /my/music/follows/{type}/{id} | Followed Network, Category, Artist, Playlist and Genre
[**putPersonalisedMusicFavouritesBatch**](MusicApi.md#putPersonalisedMusicFavouritesBatch) | **PUT** /my/music/favourites | Favourite Tracks or Clips
[**putPersonalisedMusicFavouritesByTypeById**](MusicApi.md#putPersonalisedMusicFavouritesByTypeById) | **PUT** /my/music/favourites/{type}/{id} | Favourite Track or Clip
[**putPersonalisedMusicFollowsBatch**](MusicApi.md#putPersonalisedMusicFollowsBatch) | **PUT** /my/music/follows | Followed Networks, Categories, Artists, Playlists and Genres
[**putPersonalisedMusicFollowsByTypeById**](MusicApi.md#putPersonalisedMusicFollowsByTypeById) | **PUT** /my/music/follows/{type}/{id} | Followed Network, Category, Artist, Playlist and Genre



## deletePersonalisedMusicFavouritesByTypeById

> PersonalisedMusicSuccess deletePersonalisedMusicFavouritesByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id)

Favourite Track or Clip

Delete track or clip from a BBC Music user favourites. 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let type = "type_example"; // String | Supported Music favourite types: Clips or Tracks
let id = "id_example"; // String | Clip PID or Track ID
apiInstance.deletePersonalisedMusicFavouritesByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **type** | **String**| Supported Music favourite types: Clips or Tracks | 
 **id** | **String**| Clip PID or Track ID | 

### Return type

[**PersonalisedMusicSuccess**](PersonalisedMusicSuccess.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePersonalisedMusicFollowsByTypeById

> PersonalisedMusicSuccess deletePersonalisedMusicFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, opts)

Followed Network, Category, Artist, Playlist and Genre

Remove a single network, category, artist, playlist, network, genre or service entity is in a users follows 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let type = "type_example"; // String | Supported Music follows types: Playlists, Services, Genres & Artists
let id = "id_example"; // String | Playlists, Services, Networks, Genres, Categories or Artists ID
let opts = {
  'musicData': true, // Boolean | Omits music data from the response, defaults to true
  'musicContext': "musicContext_example", // String | Specify context to be passed to Music API
  'musicWithinUk': true // Boolean | Specify location to be passed to Music API
};
apiInstance.deletePersonalisedMusicFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, opts, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **type** | **String**| Supported Music follows types: Playlists, Services, Genres &amp; Artists | 
 **id** | **String**| Playlists, Services, Networks, Genres, Categories or Artists ID | 
 **musicData** | **Boolean**| Omits music data from the response, defaults to true | [optional] 
 **musicContext** | **String**| Specify context to be passed to Music API | [optional] 
 **musicWithinUk** | **Boolean**| Specify location to be passed to Music API | [optional] 

### Return type

[**PersonalisedMusicSuccess**](PersonalisedMusicSuccess.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMusicPopularArtistById

> MusicPopularityArtists getMusicPopularArtistById(xAPIKey, id, opts)

Single Artist Popularity

Popularity Artist By Id 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicApi();
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let id = "id_example"; // String | MusicBrainz Id - Used to get single resource score
let opts = {
  'since': "since_example", // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now
  'until': "until_example", // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given 'since' and 'until' date params
  'decomposed': true // Boolean | In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is >= 31 days
};
apiInstance.getMusicPopularArtistById(xAPIKey, id, opts, (error, data, response) => {
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
 **xAPIKey** | **String**| API_KEY | 
 **id** | **String**| MusicBrainz Id - Used to get single resource score | 
 **since** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now | [optional] 
 **until** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given &#39;since&#39; and &#39;until&#39; date params | [optional] 
 **decomposed** | **Boolean**| In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is &gt;&#x3D; 31 days | [optional] 

### Return type

[**MusicPopularityArtists**](MusicPopularityArtists.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMusicPopularArtists

> MusicPopularityArtists getMusicPopularArtists(xAPIKey, opts)

Popular Artists

List of Most Popular artists from BBC Music. 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicApi();
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let opts = {
  'since': "since_example", // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now
  'until': "until_example", // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given 'since' and 'until' date params
  'decomposed': true, // Boolean | In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is >= 31 days
  'offset': 56, // Number | Paginated results offset
  'limit': 56 // Number | Paginated results limit
};
apiInstance.getMusicPopularArtists(xAPIKey, opts, (error, data, response) => {
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
 **xAPIKey** | **String**| API_KEY | 
 **since** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now | [optional] 
 **until** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given &#39;since&#39; and &#39;until&#39; date params | [optional] 
 **decomposed** | **Boolean**| In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is &gt;&#x3D; 31 days | [optional] 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 

### Return type

[**MusicPopularityArtists**](MusicPopularityArtists.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMusicPopularPlaylistById

> MusicPopularityPlaylists getMusicPopularPlaylistById(xAPIKey, id, opts)

Single Playlist Popularity

Popular playlist by Id 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicApi();
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let id = "id_example"; // String | BBC Music Playlist Id - Used to get single resource score
let opts = {
  'since': "since_example", // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now
  'until': "until_example", // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given 'since' and 'until' date params
  'decomposed': true // Boolean | In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is >= 31 days
};
apiInstance.getMusicPopularPlaylistById(xAPIKey, id, opts, (error, data, response) => {
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
 **xAPIKey** | **String**| API_KEY | 
 **id** | **String**| BBC Music Playlist Id - Used to get single resource score | 
 **since** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now | [optional] 
 **until** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given &#39;since&#39; and &#39;until&#39; date params | [optional] 
 **decomposed** | **Boolean**| In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is &gt;&#x3D; 31 days | [optional] 

### Return type

[**MusicPopularityPlaylists**](MusicPopularityPlaylists.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMusicPopularPlaylists

> MusicPopularityPlaylists getMusicPopularPlaylists(xAPIKey, opts)

Popular Playlists

List of Most Popular playlists from BBC Music. 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicApi();
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let opts = {
  'since': "since_example", // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now
  'until': "until_example", // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given 'since' and 'until' date params
  'decomposed': true, // Boolean | In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is >= 31 days
  'offset': 56, // Number | Paginated results offset
  'limit': 56 // Number | Paginated results limit
};
apiInstance.getMusicPopularPlaylists(xAPIKey, opts, (error, data, response) => {
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
 **xAPIKey** | **String**| API_KEY | 
 **since** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now | [optional] 
 **until** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given &#39;since&#39; and &#39;until&#39; date params | [optional] 
 **decomposed** | **Boolean**| In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is &gt;&#x3D; 31 days | [optional] 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 

### Return type

[**MusicPopularityPlaylists**](MusicPopularityPlaylists.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMusicPopularTrackById

> MusicPopularityTracks getMusicPopularTrackById(xAPIKey, id, opts)

Single Track Popularity

Popular Track for BBC Music 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicApi();
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let id = "id_example"; // String | BBC Music Track Id - Used to get single resource score
let opts = {
  'since': "since_example", // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now
  'until': "until_example", // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given 'since' and 'until' date params
  'network': "network_example", // String | Return items with given Network ID
  'programme': "programme_example", // String | Items with given Programme Pid
  'artist': "artist_example", // String | MusicBrainz artist ID
  'decomposed': true // Boolean | In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is >= 31 days
};
apiInstance.getMusicPopularTrackById(xAPIKey, id, opts, (error, data, response) => {
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
 **xAPIKey** | **String**| API_KEY | 
 **id** | **String**| BBC Music Track Id - Used to get single resource score | 
 **since** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now | [optional] 
 **until** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given &#39;since&#39; and &#39;until&#39; date params | [optional] 
 **network** | **String**| Return items with given Network ID | [optional] 
 **programme** | **String**| Items with given Programme Pid | [optional] 
 **artist** | **String**| MusicBrainz artist ID | [optional] 
 **decomposed** | **Boolean**| In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is &gt;&#x3D; 31 days | [optional] 

### Return type

[**MusicPopularityTracks**](MusicPopularityTracks.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMusicPopularTracks

> MusicPopularityTracks getMusicPopularTracks(xAPIKey, opts)

Popular Tracks

List of popular tracks for BBC Music. Filter by time, network, artist, playlist or programme. 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicApi();
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let opts = {
  'since': "since_example", // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now
  'until': "until_example", // String | ISO 8601 Date yyyy-mm-dd.  Returns items between given 'since' and 'until' date params
  'network': "network_example", // String | Return items with given Network ID
  'programme': "programme_example", // String | Items with given Programme Pid
  'artist': "artist_example", // String | MusicBrainz artist ID
  'decomposed': true, // Boolean | In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is >= 31 days
  'offset': 56, // Number | Paginated results offset
  'limit': 56 // Number | Paginated results limit
};
apiInstance.getMusicPopularTracks(xAPIKey, opts, (error, data, response) => {
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
 **xAPIKey** | **String**| API_KEY | 
 **since** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given time period and now | [optional] 
 **until** | **String**| ISO 8601 Date yyyy-mm-dd.  Returns items between given &#39;since&#39; and &#39;until&#39; date params | [optional] 
 **network** | **String**| Return items with given Network ID | [optional] 
 **programme** | **String**| Items with given Programme Pid | [optional] 
 **artist** | **String**| MusicBrainz artist ID | [optional] 
 **decomposed** | **Boolean**| In addition to the overall score, return a list of scores broken down by day N.B Must be used in conjunction with since and/or until and since is &gt;&#x3D; 31 days | [optional] 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 

### Return type

[**MusicPopularityTracks**](MusicPopularityTracks.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPersonalisedMusicFavourites

> PersonalisedMusicResponse getPersonalisedMusicFavourites(authorization, xAuthenticationProvider, xAPIKey, opts)

Favourite Tracks or Clips

List of favourited tracks and clips for a given user for BBC Music. 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let opts = {
  'offset': 56, // Number | Paginated results offset
  'limit': 56, // Number | Paginated results limit
  'action': "action_example", // String | Filters activities based on the type of action
  'musicData': true // Boolean | Omits music data from the response, defaults to true
};
apiInstance.getPersonalisedMusicFavourites(authorization, xAuthenticationProvider, xAPIKey, opts, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 
 **action** | **String**| Filters activities based on the type of action | [optional] 
 **musicData** | **Boolean**| Omits music data from the response, defaults to true | [optional] 

### Return type

[**PersonalisedMusicResponse**](PersonalisedMusicResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPersonalisedMusicFavouritesByType

> PersonalisedMusicResponse getPersonalisedMusicFavouritesByType(authorization, xAuthenticationProvider, xAPIKey, type, opts)

Favourite Tracks or Clips by Type

List of favourited tracks or clips for a given user for BBC Music. 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let type = "type_example"; // String | Supported Music favourite types: Clips or Tracks
let opts = {
  'action': "action_example", // String | Filters activities based on the type of action
  'offset': 56, // Number | Paginated results offset
  'limit': 56 // Number | Paginated results limit
};
apiInstance.getPersonalisedMusicFavouritesByType(authorization, xAuthenticationProvider, xAPIKey, type, opts, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **type** | **String**| Supported Music favourite types: Clips or Tracks | 
 **action** | **String**| Filters activities based on the type of action | [optional] 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 

### Return type

[**PersonalisedMusicResponse**](PersonalisedMusicResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPersonalisedMusicFavouritesByTypeById

> PersonalisedMusicResponse getPersonalisedMusicFavouritesByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id)

Favourite Track or Clip

Check to see if a single track or clip entity is in a users favourites - determines UX of add button. 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let type = "type_example"; // String | Supported Music favourite types: Clips or Tracks
let id = "id_example"; // String | Clip PID or Track ID
apiInstance.getPersonalisedMusicFavouritesByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **type** | **String**| Supported Music favourite types: Clips or Tracks | 
 **id** | **String**| Clip PID or Track ID | 

### Return type

[**PersonalisedMusicResponse**](PersonalisedMusicResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPersonalisedMusicFollows

> PersonalisedMusicResponse getPersonalisedMusicFollows(authorization, xAuthenticationProvider, xAPIKey, opts)

Followed Networks, Categories, Artists, Playlists and Genres

List of followed networks, categories, artists, playlists and genres for a given user for BBC Music. 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let opts = {
  'action': "action_example", // String | Filters activities based on the type of action
  'musicData': true, // Boolean | Omits music data from the response, defaults to true
  'musicContext': "musicContext_example", // String | Specify context to be passed to Music API
  'musicWithinUk': true, // Boolean | Specify location to be passed to Music API
  'offset': 56, // Number | Paginated results offset
  'limit': 56 // Number | Paginated results limit
};
apiInstance.getPersonalisedMusicFollows(authorization, xAuthenticationProvider, xAPIKey, opts, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **action** | **String**| Filters activities based on the type of action | [optional] 
 **musicData** | **Boolean**| Omits music data from the response, defaults to true | [optional] 
 **musicContext** | **String**| Specify context to be passed to Music API | [optional] 
 **musicWithinUk** | **Boolean**| Specify location to be passed to Music API | [optional] 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 

### Return type

[**PersonalisedMusicResponse**](PersonalisedMusicResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPersonalisedMusicFollowsByType

> PersonalisedMusicResponse getPersonalisedMusicFollowsByType(authorization, xAuthenticationProvider, xAPIKey, type, opts)

Followed Networks, Categories, Artists, Playlists and Genres by Type

List of followed networks, categories, artists, playlists, networks, genres, categories or services for a given BBC Music user. 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let type = "type_example"; // String | Supported Music follows types: Playlists, Services, Genres & Artists
let opts = {
  'action': "action_example", // String | Filters activities based on the type of action
  'musicData': true, // Boolean | Omits music data from the response, defaults to true
  'musicContext': "musicContext_example", // String | Specify context to be passed to Music API
  'musicWithinUk': true, // Boolean | Specify location to be passed to Music API
  'offset': 56, // Number | Paginated results offset
  'limit': 56 // Number | Paginated results limit
};
apiInstance.getPersonalisedMusicFollowsByType(authorization, xAuthenticationProvider, xAPIKey, type, opts, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **type** | **String**| Supported Music follows types: Playlists, Services, Genres &amp; Artists | 
 **action** | **String**| Filters activities based on the type of action | [optional] 
 **musicData** | **Boolean**| Omits music data from the response, defaults to true | [optional] 
 **musicContext** | **String**| Specify context to be passed to Music API | [optional] 
 **musicWithinUk** | **Boolean**| Specify location to be passed to Music API | [optional] 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 

### Return type

[**PersonalisedMusicResponse**](PersonalisedMusicResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPersonalisedMusicFollowsByTypeById

> PersonalisedMusicResponse getPersonalisedMusicFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, opts)

Followed Network, Category, Artist, Playlist and Genre

Check to see if a single network, category, artist, playlist, network, genre or service entity is in a users follows - determines UX of add button. 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let type = "type_example"; // String | Supported Music follows types: Playlists, Services, Genres & Artists
let id = "id_example"; // String | Playlists, Services, Networks, Genres, Categories or Artists ID
let opts = {
  'musicData': true, // Boolean | Omits music data from the response, defaults to true
  'musicContext': "musicContext_example", // String | Specify context to be passed to Music API
  'musicWithinUk': true // Boolean | Specify location to be passed to Music API
};
apiInstance.getPersonalisedMusicFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, opts, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **type** | **String**| Supported Music follows types: Playlists, Services, Genres &amp; Artists | 
 **id** | **String**| Playlists, Services, Networks, Genres, Categories or Artists ID | 
 **musicData** | **Boolean**| Omits music data from the response, defaults to true | [optional] 
 **musicContext** | **String**| Specify context to be passed to Music API | [optional] 
 **musicWithinUk** | **Boolean**| Specify location to be passed to Music API | [optional] 

### Return type

[**PersonalisedMusicResponse**](PersonalisedMusicResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postPersonalisedMusicFavouritesBatch

> PersonalisedMusicResponse postPersonalisedMusicFavouritesBatch(authorization, xAuthenticationProvider, xAPIKey, body)

Favourite Tracks or Clips

Add multiple tracks and/or clips to a BBC Music user&#39;s favourites.  N.B. Any HTML tags submitted in metadata will be removed 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let body = [new RadioMusicServices.PersonalisedMusicBatchRequest()]; // [PersonalisedMusicBatchRequest] | Action favourited or unfavourited
apiInstance.postPersonalisedMusicFavouritesBatch(authorization, xAuthenticationProvider, xAPIKey, body, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **body** | [**[PersonalisedMusicBatchRequest]**](PersonalisedMusicBatchRequest.md)| Action favourited or unfavourited | 

### Return type

[**PersonalisedMusicResponse**](PersonalisedMusicResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postPersonalisedMusicFavouritesByTypeById

> PersonalisedMusicResponse postPersonalisedMusicFavouritesByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, body)

Favourite Track or Clip

Add track or clip to a BBC Music user favourites.  N.B. Any HTML tags submitted in metadata will be removed 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let type = "type_example"; // String | Supported Music favourite types: Clips or Tracks
let id = "id_example"; // String | Clip PID or Track ID
let body = new RadioMusicServices.PersonalisedMusicRequest(); // PersonalisedMusicRequest | Action favourited or unfavourited
apiInstance.postPersonalisedMusicFavouritesByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, body, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **type** | **String**| Supported Music favourite types: Clips or Tracks | 
 **id** | **String**| Clip PID or Track ID | 
 **body** | [**PersonalisedMusicRequest**](PersonalisedMusicRequest.md)| Action favourited or unfavourited | 

### Return type

[**PersonalisedMusicResponse**](PersonalisedMusicResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postPersonalisedMusicFollowsBatch

> PersonalisedMusicSuccess postPersonalisedMusicFollowsBatch(authorization, xAuthenticationProvider, xAPIKey, body, opts)

Followed Networks, Categories, Artists, Playlists and Genres

Add networks, categories, artists, playlists, networks, genres or services in a users follows  N.B. Any HTML tags submitted in metadata will be removed 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let body = [new RadioMusicServices.PersonalisedMusicBatchRequest()]; // [PersonalisedMusicBatchRequest] | Action followed or unfollowed
let opts = {
  'action': "action_example", // String | Filters activities based on the type of action
  'musicData': true, // Boolean | Omits music data from the response, defaults to true
  'musicContext': "musicContext_example", // String | Specify context to be passed to Music API
  'musicWithinUk': true // Boolean | Specify location to be passed to Music API
};
apiInstance.postPersonalisedMusicFollowsBatch(authorization, xAuthenticationProvider, xAPIKey, body, opts, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **body** | [**[PersonalisedMusicBatchRequest]**](PersonalisedMusicBatchRequest.md)| Action followed or unfollowed | 
 **action** | **String**| Filters activities based on the type of action | [optional] 
 **musicData** | **Boolean**| Omits music data from the response, defaults to true | [optional] 
 **musicContext** | **String**| Specify context to be passed to Music API | [optional] 
 **musicWithinUk** | **Boolean**| Specify location to be passed to Music API | [optional] 

### Return type

[**PersonalisedMusicSuccess**](PersonalisedMusicSuccess.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postPersonalisedMusicFollowsByTypeById

> PersonalisedMusicSuccess postPersonalisedMusicFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, body, opts)

Followed Network, Category, Artist, Playlist and Genre

Add a single network, category, artist, playlist, network, genre or service entity is in a users follows  N.B. Any HTML tags submitted in metadata will be removed 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let type = "type_example"; // String | Supported Music follows types: Playlists, Services, Genres & Artists
let id = "id_example"; // String | Playlists, Services, Networks, Genres, Categories or Artists ID
let body = new RadioMusicServices.PersonalisedMusicRequest(); // PersonalisedMusicRequest | Action followed or unfollowed
let opts = {
  'musicData': true, // Boolean | Omits music data from the response, defaults to true
  'musicContext': "musicContext_example", // String | Specify context to be passed to Music API
  'musicWithinUk': true // Boolean | Specify location to be passed to Music API
};
apiInstance.postPersonalisedMusicFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, body, opts, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **type** | **String**| Supported Music follows types: Playlists, Services, Genres &amp; Artists | 
 **id** | **String**| Playlists, Services, Networks, Genres, Categories or Artists ID | 
 **body** | [**PersonalisedMusicRequest**](PersonalisedMusicRequest.md)| Action followed or unfollowed | 
 **musicData** | **Boolean**| Omits music data from the response, defaults to true | [optional] 
 **musicContext** | **String**| Specify context to be passed to Music API | [optional] 
 **musicWithinUk** | **Boolean**| Specify location to be passed to Music API | [optional] 

### Return type

[**PersonalisedMusicSuccess**](PersonalisedMusicSuccess.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putPersonalisedMusicFavouritesBatch

> PersonalisedMusicSuccess putPersonalisedMusicFavouritesBatch(authorization, xAuthenticationProvider, xAPIKey, body)

Favourite Tracks or Clips

Update tracks or clips from a BBC Music user favourites.  N.B. Any HTML tags submitted in metadata will be removed 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let body = [new RadioMusicServices.PersonalisedMusicBatchRequest()]; // [PersonalisedMusicBatchRequest] | Action favourited or unfavourited
apiInstance.putPersonalisedMusicFavouritesBatch(authorization, xAuthenticationProvider, xAPIKey, body, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **body** | [**[PersonalisedMusicBatchRequest]**](PersonalisedMusicBatchRequest.md)| Action favourited or unfavourited | 

### Return type

[**PersonalisedMusicSuccess**](PersonalisedMusicSuccess.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putPersonalisedMusicFavouritesByTypeById

> PersonalisedMusicSuccess putPersonalisedMusicFavouritesByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, body)

Favourite Track or Clip

Update tracks or clips from a BBC Music user favourites.  N.B. Any HTML tags submitted in metadata will be removed 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let type = "type_example"; // String | Supported Music favourite types: Clips or Tracks
let id = "id_example"; // String | Clip PID or Track ID
let body = new RadioMusicServices.PersonalisedMusicRequest(); // PersonalisedMusicRequest | Action favourited or unfavourited
apiInstance.putPersonalisedMusicFavouritesByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, body, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **type** | **String**| Supported Music favourite types: Clips or Tracks | 
 **id** | **String**| Clip PID or Track ID | 
 **body** | [**PersonalisedMusicRequest**](PersonalisedMusicRequest.md)| Action favourited or unfavourited | 

### Return type

[**PersonalisedMusicSuccess**](PersonalisedMusicSuccess.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putPersonalisedMusicFollowsBatch

> PersonalisedMusicSuccess putPersonalisedMusicFollowsBatch(authorization, xAuthenticationProvider, xAPIKey, body, opts)

Followed Networks, Categories, Artists, Playlists and Genres

Update networks, categories, artists, playlists, networks, genres or services in a users follows  N.B. Any HTML tags submitted in metadata will be removed 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let body = [new RadioMusicServices.PersonalisedMusicBatchRequest()]; // [PersonalisedMusicBatchRequest] | Action followed or unfollowed
let opts = {
  'action': "action_example", // String | Filters activities based on the type of action
  'musicData': true, // Boolean | Omits music data from the response, defaults to true
  'musicContext': "musicContext_example", // String | Specify context to be passed to Music API
  'musicWithinUk': true // Boolean | Specify location to be passed to Music API
};
apiInstance.putPersonalisedMusicFollowsBatch(authorization, xAuthenticationProvider, xAPIKey, body, opts, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **body** | [**[PersonalisedMusicBatchRequest]**](PersonalisedMusicBatchRequest.md)| Action followed or unfollowed | 
 **action** | **String**| Filters activities based on the type of action | [optional] 
 **musicData** | **Boolean**| Omits music data from the response, defaults to true | [optional] 
 **musicContext** | **String**| Specify context to be passed to Music API | [optional] 
 **musicWithinUk** | **Boolean**| Specify location to be passed to Music API | [optional] 

### Return type

[**PersonalisedMusicSuccess**](PersonalisedMusicSuccess.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putPersonalisedMusicFollowsByTypeById

> PersonalisedMusicSuccess putPersonalisedMusicFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, body, opts)

Followed Network, Category, Artist, Playlist and Genre

Update a single network, category, artist, playlist, network, genre or service entity is in a users follows  N.B. Any HTML tags submitted in metadata will be removed 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.MusicApi();
let authorization = "'Bearer OAUTH_TOKEN'"; // String | Bearer OAUTH_TOKEN
let xAuthenticationProvider = "'idv5'"; // String | Authentication type
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let type = "type_example"; // String | Supported Music follows types: Playlists, Services, Genres & Artists
let id = "id_example"; // String | Playlists, Services, Networks, Genres, Categories or Artists ID
let body = new RadioMusicServices.PersonalisedMusicRequest(); // PersonalisedMusicRequest | Action followed or unfollowed
let opts = {
  'musicData': true, // Boolean | Omits music data from the response, defaults to true
  'musicContext': "musicContext_example", // String | Specify context to be passed to Music API
  'musicWithinUk': true // Boolean | Specify location to be passed to Music API
};
apiInstance.putPersonalisedMusicFollowsByTypeById(authorization, xAuthenticationProvider, xAPIKey, type, id, body, opts, (error, data, response) => {
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
 **authorization** | **String**| Bearer OAUTH_TOKEN | [default to &#39;Bearer OAUTH_TOKEN&#39;]
 **xAuthenticationProvider** | **String**| Authentication type | [default to &#39;idv5&#39;]
 **xAPIKey** | **String**| API_KEY | 
 **type** | **String**| Supported Music follows types: Playlists, Services, Genres &amp; Artists | 
 **id** | **String**| Playlists, Services, Networks, Genres, Categories or Artists ID | 
 **body** | [**PersonalisedMusicRequest**](PersonalisedMusicRequest.md)| Action followed or unfollowed | 
 **musicData** | **Boolean**| Omits music data from the response, defaults to true | [optional] 
 **musicContext** | **String**| Specify context to be passed to Music API | [optional] 
 **musicWithinUk** | **Boolean**| Specify location to be passed to Music API | [optional] 

### Return type

[**PersonalisedMusicSuccess**](PersonalisedMusicSuccess.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

