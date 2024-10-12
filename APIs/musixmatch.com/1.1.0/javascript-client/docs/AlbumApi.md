# MusixmatchApi.AlbumApi

All URIs are relative to *https://api.musixmatch.com/ws/1.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**albumGetGet**](AlbumApi.md#albumGetGet) | **GET** /album.get | 
[**artistAlbumsGetGet**](AlbumApi.md#artistAlbumsGetGet) | **GET** /artist.albums.get | 



## albumGetGet

> AlbumGetGet200Response albumGetGet(albumId, opts)



### Example

```javascript
import MusixmatchApi from 'musixmatch_api';
let defaultClient = MusixmatchApi.ApiClient.instance;
// Configure API key authorization: key
let key = defaultClient.authentications['key'];
key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//key.apiKeyPrefix = 'Token';

let apiInstance = new MusixmatchApi.AlbumApi();
let albumId = "albumId_example"; // String | The musiXmatch album id
let opts = {
  'format': "'json'", // String | output format: json, jsonp, xml.
  'callback': "callback_example" // String | jsonp callback
};
apiInstance.albumGetGet(albumId, opts, (error, data, response) => {
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

### Return type

[**AlbumGetGet200Response**](AlbumGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## artistAlbumsGetGet

> ArtistAlbumsGetGet200Response artistAlbumsGetGet(artistId, opts)



### Example

```javascript
import MusixmatchApi from 'musixmatch_api';
let defaultClient = MusixmatchApi.ApiClient.instance;
// Configure API key authorization: key
let key = defaultClient.authentications['key'];
key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//key.apiKeyPrefix = 'Token';

let apiInstance = new MusixmatchApi.AlbumApi();
let artistId = "artistId_example"; // String | The musiXmatch artist id
let opts = {
  'format': "'json'", // String | output format: json, jsonp, xml.
  'callback': "callback_example", // String | jsonp callback
  'sReleaseDate': "sReleaseDate_example", // String | Sort by release date (asc|desc)
  'gAlbumName': "gAlbumName_example", // String | Group by Album Name
  'pageSize': 3.4, // Number | Define the page size for paginated results.Range is 1 to 100.
  'page': 3.4 // Number | Define the page number for paginated results
};
apiInstance.artistAlbumsGetGet(artistId, opts, (error, data, response) => {
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
 **artistId** | **String**| The musiXmatch artist id | 
 **format** | **String**| output format: json, jsonp, xml. | [optional] [default to &#39;json&#39;]
 **callback** | **String**| jsonp callback | [optional] 
 **sReleaseDate** | **String**| Sort by release date (asc|desc) | [optional] 
 **gAlbumName** | **String**| Group by Album Name | [optional] 
 **pageSize** | **Number**| Define the page size for paginated results.Range is 1 to 100. | [optional] 
 **page** | **Number**| Define the page number for paginated results | [optional] 

### Return type

[**ArtistAlbumsGetGet200Response**](ArtistAlbumsGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

