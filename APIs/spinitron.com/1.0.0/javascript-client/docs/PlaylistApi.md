# SpinitronV2Api.PlaylistApi

All URIs are relative to *https://spinitron.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**playlistsGet**](PlaylistApi.md#playlistsGet) | **GET** /playlists | Returns playlists optionally filtered by {start} and/or {end} datetimes
[**playlistsIdGet**](PlaylistApi.md#playlistsIdGet) | **GET** /playlists/{id} | Get a Playlist by id



## playlistsGet

> PlaylistsGet200Response playlistsGet(opts)

Returns playlists optionally filtered by {start} and/or {end} datetimes

Get Playlists optionally filtered by a datetime range. Only past Playlists will be returned (with allowed tolerance equals 1 hour in future).  Ordered chronologically from newest to oldest. 

### Example

```javascript
import SpinitronV2Api from 'spinitron_v2_api';
let defaultClient = SpinitronV2Api.ApiClient.instance;
// Configure API key authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//accessToken.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: httpBearer
let httpBearer = defaultClient.authentications['httpBearer'];
httpBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpinitronV2Api.PlaylistApi();
let opts = {
  'start': new Date("2013-10-20T19:20:30+01:00"), // Date | The datetime starting from items must be returned. Maximum 1 hour in future. 
  'end': new Date("2013-10-20T19:20:30+01:00"), // Date | The ending datetime. Maximum 1 hour in future. 
  'showId': 56, // Number | Filter by show
  'personaId': 56, // Number | Filter by persona
  'count': 20, // Number | Amount of items to return
  'page': 56, // Number | Offset, used together with count
  'fields': ["null"], // [String] | Allows to select only needed fields
  'expand': ["null"] // [String] | Allows to select extra fields
};
apiInstance.playlistsGet(opts, (error, data, response) => {
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
 **start** | **Date**| The datetime starting from items must be returned. Maximum 1 hour in future.  | [optional] 
 **end** | **Date**| The ending datetime. Maximum 1 hour in future.  | [optional] 
 **showId** | **Number**| Filter by show | [optional] 
 **personaId** | **Number**| Filter by persona | [optional] 
 **count** | **Number**| Amount of items to return | [optional] [default to 20]
 **page** | **Number**| Offset, used together with count | [optional] 
 **fields** | [**[String]**](String.md)| Allows to select only needed fields | [optional] 
 **expand** | [**[String]**](String.md)| Allows to select extra fields | [optional] 

### Return type

[**PlaylistsGet200Response**](PlaylistsGet200Response.md)

### Authorization

[accessToken](../README.md#accessToken), [httpBearer](../README.md#httpBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## playlistsIdGet

> Playlist playlistsIdGet(id, opts)

Get a Playlist by id

The response object represents the playlist specified by {id}.  Status 404 is returned if a playlist with {id} does not exist or if it does but starts in the future (with allowed tolerance equals 1 hour in future). 

### Example

```javascript
import SpinitronV2Api from 'spinitron_v2_api';
let defaultClient = SpinitronV2Api.ApiClient.instance;
// Configure API key authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//accessToken.apiKeyPrefix = 'Token';
// Configure Bearer (JWT) access token for authorization: httpBearer
let httpBearer = defaultClient.authentications['httpBearer'];
httpBearer.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new SpinitronV2Api.PlaylistApi();
let id = 56; // Number | 
let opts = {
  'fields': ["null"], // [String] | Allows to select only needed fields
  'expand': ["null"] // [String] | Allows to select extra fields
};
apiInstance.playlistsIdGet(id, opts, (error, data, response) => {
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
 **fields** | [**[String]**](String.md)| Allows to select only needed fields | [optional] 
 **expand** | [**[String]**](String.md)| Allows to select extra fields | [optional] 

### Return type

[**Playlist**](Playlist.md)

### Authorization

[accessToken](../README.md#accessToken), [httpBearer](../README.md#httpBearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

