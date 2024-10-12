# Vimeo.AlbumsCustomAlbumThumbnailsApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAlbumCustomThumb**](AlbumsCustomAlbumThumbnailsApi.md#createAlbumCustomThumb) | **POST** /users/{user_id}/albums/{album_id}/custom_thumbnails | Add a custom uploaded thumbnail
[**deleteAlbumCustomThumbnail**](AlbumsCustomAlbumThumbnailsApi.md#deleteAlbumCustomThumbnail) | **DELETE** /users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id} | Remove a custom uploaded album thumbnail
[**getAlbumCustomThumbnail**](AlbumsCustomAlbumThumbnailsApi.md#getAlbumCustomThumbnail) | **GET** /users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id} | Get a specific custom uploaded album thumbnail
[**getAlbumCustomThumbs**](AlbumsCustomAlbumThumbnailsApi.md#getAlbumCustomThumbs) | **GET** /users/{user_id}/albums/{album_id}/custom_thumbnails | Get all the custom upload thumbnails of an album
[**replaceAlbumCustomThumb**](AlbumsCustomAlbumThumbnailsApi.md#replaceAlbumCustomThumb) | **PATCH** /users/{user_id}/albums/{album_id}/custom_thumbnails/{thumbnail_id} | Replace a custom uploaded album thumbnail



## createAlbumCustomThumb

> Picture createAlbumCustomThumb(albumId, userId)

Add a custom uploaded thumbnail

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.AlbumsCustomAlbumThumbnailsApi();
let albumId = 3706071; // Number | The ID of the album.
let userId = 152184; // Number | The ID of the user.
apiInstance.createAlbumCustomThumb(albumId, userId, (error, data, response) => {
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
 **albumId** | **Number**| The ID of the album. | 
 **userId** | **Number**| The ID of the user. | 

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.picture+json


## deleteAlbumCustomThumbnail

> deleteAlbumCustomThumbnail(albumId, thumbnailId, userId)

Remove a custom uploaded album thumbnail

This method removes a custom uploaded thumbnail from the specified album.

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.AlbumsCustomAlbumThumbnailsApi();
let albumId = 3706071; // Number | The ID of the album.
let thumbnailId = 12345; // Number | The ID of the custom thumbnail.
let userId = 152184; // Number | The ID of the user.
apiInstance.deleteAlbumCustomThumbnail(albumId, thumbnailId, userId, (error, data, response) => {
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
 **albumId** | **Number**| The ID of the album. | 
 **thumbnailId** | **Number**| The ID of the custom thumbnail. | 
 **userId** | **Number**| The ID of the user. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.picture+json


## getAlbumCustomThumbnail

> Picture getAlbumCustomThumbnail(albumId, thumbnailId, userId)

Get a specific custom uploaded album thumbnail

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.AlbumsCustomAlbumThumbnailsApi();
let albumId = 3706071; // Number | The ID of the album.
let thumbnailId = 12345; // Number | The ID of the custom thumbnail.
let userId = 152184; // Number | The ID of the user.
apiInstance.getAlbumCustomThumbnail(albumId, thumbnailId, userId, (error, data, response) => {
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
 **albumId** | **Number**| The ID of the album. | 
 **thumbnailId** | **Number**| The ID of the custom thumbnail. | 
 **userId** | **Number**| The ID of the user. | 

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.picture+json


## getAlbumCustomThumbs

> [Picture] getAlbumCustomThumbs(albumId, userId, opts)

Get all the custom upload thumbnails of an album

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.AlbumsCustomAlbumThumbnailsApi();
let albumId = 3706071; // Number | The ID of the album.
let userId = 152184; // Number | The ID of the user.
let opts = {
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10 // Number | The number of items to show on each page of results, up to a maximum of 100.
};
apiInstance.getAlbumCustomThumbs(albumId, userId, opts, (error, data, response) => {
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
 **albumId** | **Number**| The ID of the album. | 
 **userId** | **Number**| The ID of the user. | 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 

### Return type

[**[Picture]**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.picture+json


## replaceAlbumCustomThumb

> Picture replaceAlbumCustomThumb(albumId, thumbnailId, userId, opts)

Replace a custom uploaded album thumbnail

### Example

```javascript
import Vimeo from 'vimeo';
let defaultClient = Vimeo.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Vimeo.AlbumsCustomAlbumThumbnailsApi();
let albumId = 3706071; // Number | The ID of the album.
let thumbnailId = 12345; // Number | The ID of the custom thumbnail.
let userId = 152184; // Number | The ID of the user.
let opts = {
  'replaceAlbumCustomThumbRequest': new Vimeo.ReplaceAlbumCustomThumbRequest() // ReplaceAlbumCustomThumbRequest | 
};
apiInstance.replaceAlbumCustomThumb(albumId, thumbnailId, userId, opts, (error, data, response) => {
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
 **albumId** | **Number**| The ID of the album. | 
 **thumbnailId** | **Number**| The ID of the custom thumbnail. | 
 **userId** | **Number**| The ID of the user. | 
 **replaceAlbumCustomThumbRequest** | [**ReplaceAlbumCustomThumbRequest**](ReplaceAlbumCustomThumbRequest.md)|  | [optional] 

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.picture+json
- **Accept**: application/vnd.vimeo.picture+json

