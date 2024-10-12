# Vimeo.AlbumsAlbumVideosApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addVideoToAlbum**](AlbumsAlbumVideosApi.md#addVideoToAlbum) | **PUT** /users/{user_id}/albums/{album_id}/videos/{video_id} | Add a specific video to an album
[**addVideoToAlbumAlt1**](AlbumsAlbumVideosApi.md#addVideoToAlbumAlt1) | **PUT** /me/albums/{album_id}/videos/{video_id} | Add a specific video to an album
[**getAlbumVideo**](AlbumsAlbumVideosApi.md#getAlbumVideo) | **GET** /users/{user_id}/albums/{album_id}/videos/{video_id} | Get a specific video in an album
[**getAlbumVideoAlt1**](AlbumsAlbumVideosApi.md#getAlbumVideoAlt1) | **GET** /me/albums/{album_id}/videos/{video_id} | Get a specific video in an album
[**getAlbumVideos**](AlbumsAlbumVideosApi.md#getAlbumVideos) | **GET** /users/{user_id}/albums/{album_id}/videos | Get all the videos in an album
[**getAlbumVideosAlt1**](AlbumsAlbumVideosApi.md#getAlbumVideosAlt1) | **GET** /me/albums/{album_id}/videos | Get all the videos in an album
[**removeVideoFromAlbum**](AlbumsAlbumVideosApi.md#removeVideoFromAlbum) | **DELETE** /users/{user_id}/albums/{album_id}/videos/{video_id} | Remove a video from an album
[**removeVideoFromAlbumAlt1**](AlbumsAlbumVideosApi.md#removeVideoFromAlbumAlt1) | **DELETE** /me/albums/{album_id}/videos/{video_id} | Remove a video from an album
[**replaceVideosInAlbum**](AlbumsAlbumVideosApi.md#replaceVideosInAlbum) | **PUT** /users/{user_id}/albums/{album_id}/videos | Replace all the videos in an album
[**replaceVideosInAlbumAlt1**](AlbumsAlbumVideosApi.md#replaceVideosInAlbumAlt1) | **PUT** /me/albums/{album_id}/videos | Replace all the videos in an album
[**setVideoAsAlbumThumbnail**](AlbumsAlbumVideosApi.md#setVideoAsAlbumThumbnail) | **POST** /users/{user_id}/albums/{album_id}/videos/{video_id}/set_album_thumbnail | Set a video as the album thumbnail
[**setVideoAsAlbumThumbnailAlt1**](AlbumsAlbumVideosApi.md#setVideoAsAlbumThumbnailAlt1) | **POST** /me/albums/{album_id}/videos/{video_id}/set_album_thumbnail | Set a video as the album thumbnail



## addVideoToAlbum

> addVideoToAlbum(albumId, userId, videoId)

Add a specific video to an album

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

let apiInstance = new Vimeo.AlbumsAlbumVideosApi();
let albumId = 12345; // Number | The ID of the album.
let userId = 152184; // Number | The ID of the user.
let videoId = 196367152; // Number | The ID of the video.
apiInstance.addVideoToAlbum(albumId, userId, videoId, (error, data, response) => {
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
 **userId** | **Number**| The ID of the user. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addVideoToAlbumAlt1

> addVideoToAlbumAlt1(albumId, videoId)

Add a specific video to an album

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

let apiInstance = new Vimeo.AlbumsAlbumVideosApi();
let albumId = 12345; // Number | The ID of the album.
let videoId = 196367152; // Number | The ID of the video.
apiInstance.addVideoToAlbumAlt1(albumId, videoId, (error, data, response) => {
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
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAlbumVideo

> Video getAlbumVideo(albumId, userId, videoId, opts)

Get a specific video in an album

This method gets a single video from an album. You can use this method to determine whether the album contains the specified video.

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

let apiInstance = new Vimeo.AlbumsAlbumVideosApi();
let albumId = 3706071; // Number | The ID of the album.
let userId = 152184; // Number | The ID of the user.
let videoId = 196367152; // Number | The ID of the video.
let opts = {
  'password': "hunter1" // String | The password of the album.
};
apiInstance.getAlbumVideo(albumId, userId, videoId, opts, (error, data, response) => {
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
 **videoId** | **Number**| The ID of the video. | 
 **password** | **String**| The password of the album. | [optional] 

### Return type

[**Video**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.video+json


## getAlbumVideoAlt1

> Video getAlbumVideoAlt1(albumId, videoId, opts)

Get a specific video in an album

This method gets a single video from an album. You can use this method to determine whether the album contains the specified video.

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

let apiInstance = new Vimeo.AlbumsAlbumVideosApi();
let albumId = 3706071; // Number | The ID of the album.
let videoId = 196367152; // Number | The ID of the video.
let opts = {
  'password': "hunter1" // String | The password of the album.
};
apiInstance.getAlbumVideoAlt1(albumId, videoId, opts, (error, data, response) => {
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
 **videoId** | **Number**| The ID of the video. | 
 **password** | **String**| The password of the album. | [optional] 

### Return type

[**Video**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.video+json


## getAlbumVideos

> [Video] getAlbumVideos(albumId, userId, opts)

Get all the videos in an album

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

let apiInstance = new Vimeo.AlbumsAlbumVideosApi();
let albumId = 3706071; // Number | The ID of the album.
let userId = 152184; // Number | The ID of the user.
let opts = {
  'containingUri': "/videos/258684937", // String | The page containing the video URI.
  'direction': "asc", // String | The sort direction of the results.
  'filter': "filter_example", // String | The attribute by which to filter the results.
  'filterEmbeddable': true, // Boolean | Whether to filter the results by embeddable videos (`true`) or non-embeddable videos (`false`). Required only if **filter** is `embeddable`.
  'page': 1, // Number | The page number of the results to show.
  'password': "hunter1", // String | The password of the album.
  'perPage': 10, // Number | The number of items to show on each page of results, up to a maximum of 100.
  'query': "Stop motion", // String | The search query to use to filter the results.
  'sort': "sort_example", // String | The way to sort the results.
  'weakSearch': false // Boolean | Whether to include private videos in the search. Please note that a separate search service provides this functionality. The service performs a partial text search on the video's name.
};
apiInstance.getAlbumVideos(albumId, userId, opts, (error, data, response) => {
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
 **containingUri** | **String**| The page containing the video URI. | [optional] 
 **direction** | **String**| The sort direction of the results. | [optional] 
 **filter** | **String**| The attribute by which to filter the results. | [optional] 
 **filterEmbeddable** | **Boolean**| Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;. | [optional] 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **password** | **String**| The password of the album. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 
 **query** | **String**| The search query to use to filter the results. | [optional] 
 **sort** | **String**| The way to sort the results. | [optional] 
 **weakSearch** | **Boolean**| Whether to include private videos in the search. Please note that a separate search service provides this functionality. The service performs a partial text search on the video&#39;s name. | [optional] 

### Return type

[**[Video]**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.video+json


## getAlbumVideosAlt1

> [Video] getAlbumVideosAlt1(albumId, opts)

Get all the videos in an album

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

let apiInstance = new Vimeo.AlbumsAlbumVideosApi();
let albumId = 3706071; // Number | The ID of the album.
let opts = {
  'containingUri': "/videos/258684937", // String | The page containing the video URI.
  'direction': "asc", // String | The sort direction of the results.
  'filter': "filter_example", // String | The attribute by which to filter the results.
  'filterEmbeddable': true, // Boolean | Whether to filter the results by embeddable videos (`true`) or non-embeddable videos (`false`). Required only if **filter** is `embeddable`.
  'page': 1, // Number | The page number of the results to show.
  'password': "hunter1", // String | The password of the album.
  'perPage': 10, // Number | The number of items to show on each page of results, up to a maximum of 100.
  'query': "Stop motion", // String | The search query to use to filter the results.
  'sort': "sort_example", // String | The way to sort the results.
  'weakSearch': false // Boolean | Whether to include private videos in the search. Please note that a separate search service provides this functionality. The service performs a partial text search on the video's name.
};
apiInstance.getAlbumVideosAlt1(albumId, opts, (error, data, response) => {
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
 **containingUri** | **String**| The page containing the video URI. | [optional] 
 **direction** | **String**| The sort direction of the results. | [optional] 
 **filter** | **String**| The attribute by which to filter the results. | [optional] 
 **filterEmbeddable** | **Boolean**| Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;. | [optional] 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **password** | **String**| The password of the album. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 
 **query** | **String**| The search query to use to filter the results. | [optional] 
 **sort** | **String**| The way to sort the results. | [optional] 
 **weakSearch** | **Boolean**| Whether to include private videos in the search. Please note that a separate search service provides this functionality. The service performs a partial text search on the video&#39;s name. | [optional] 

### Return type

[**[Video]**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.video+json


## removeVideoFromAlbum

> removeVideoFromAlbum(albumId, userId, videoId)

Remove a video from an album

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

let apiInstance = new Vimeo.AlbumsAlbumVideosApi();
let albumId = 12345; // Number | The ID of the album.
let userId = 152184; // Number | The ID of the user.
let videoId = 196367152; // Number | The ID of the video.
apiInstance.removeVideoFromAlbum(albumId, userId, videoId, (error, data, response) => {
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
 **userId** | **Number**| The ID of the user. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## removeVideoFromAlbumAlt1

> removeVideoFromAlbumAlt1(albumId, videoId)

Remove a video from an album

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

let apiInstance = new Vimeo.AlbumsAlbumVideosApi();
let albumId = 12345; // Number | The ID of the album.
let videoId = 196367152; // Number | The ID of the video.
apiInstance.removeVideoFromAlbumAlt1(albumId, videoId, (error, data, response) => {
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
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## replaceVideosInAlbum

> replaceVideosInAlbum(albumId, userId, replaceVideosInAlbumAlt1Request)

Replace all the videos in an album

This method replaces all the existing videos in an album with one or more videos.

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

let apiInstance = new Vimeo.AlbumsAlbumVideosApi();
let albumId = 3706071; // Number | The ID of the album.
let userId = 152184; // Number | The ID of the user.
let replaceVideosInAlbumAlt1Request = new Vimeo.ReplaceVideosInAlbumAlt1Request(); // ReplaceVideosInAlbumAlt1Request | 
apiInstance.replaceVideosInAlbum(albumId, userId, replaceVideosInAlbumAlt1Request, (error, data, response) => {
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
 **userId** | **Number**| The ID of the user. | 
 **replaceVideosInAlbumAlt1Request** | [**ReplaceVideosInAlbumAlt1Request**](ReplaceVideosInAlbumAlt1Request.md)|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## replaceVideosInAlbumAlt1

> replaceVideosInAlbumAlt1(albumId, replaceVideosInAlbumAlt1Request)

Replace all the videos in an album

This method replaces all the existing videos in an album with one or more videos.

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

let apiInstance = new Vimeo.AlbumsAlbumVideosApi();
let albumId = 3706071; // Number | The ID of the album.
let replaceVideosInAlbumAlt1Request = new Vimeo.ReplaceVideosInAlbumAlt1Request(); // ReplaceVideosInAlbumAlt1Request | 
apiInstance.replaceVideosInAlbumAlt1(albumId, replaceVideosInAlbumAlt1Request, (error, data, response) => {
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
 **replaceVideosInAlbumAlt1Request** | [**ReplaceVideosInAlbumAlt1Request**](ReplaceVideosInAlbumAlt1Request.md)|  | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setVideoAsAlbumThumbnail

> Album setVideoAsAlbumThumbnail(albumId, userId, videoId, opts)

Set a video as the album thumbnail

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

let apiInstance = new Vimeo.AlbumsAlbumVideosApi();
let albumId = 12345; // Number | The ID of the album.
let userId = 152184; // Number | The ID of the user.
let videoId = 196367152; // Number | The ID of the video.
let opts = {
  'setVideoAsAlbumThumbnailAlt1Request': new Vimeo.SetVideoAsAlbumThumbnailAlt1Request() // SetVideoAsAlbumThumbnailAlt1Request | 
};
apiInstance.setVideoAsAlbumThumbnail(albumId, userId, videoId, opts, (error, data, response) => {
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
 **videoId** | **Number**| The ID of the video. | 
 **setVideoAsAlbumThumbnailAlt1Request** | [**SetVideoAsAlbumThumbnailAlt1Request**](SetVideoAsAlbumThumbnailAlt1Request.md)|  | [optional] 

### Return type

[**Album**](Album.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setVideoAsAlbumThumbnailAlt1

> Album setVideoAsAlbumThumbnailAlt1(albumId, videoId, opts)

Set a video as the album thumbnail

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

let apiInstance = new Vimeo.AlbumsAlbumVideosApi();
let albumId = 12345; // Number | The ID of the album.
let videoId = 196367152; // Number | The ID of the video.
let opts = {
  'setVideoAsAlbumThumbnailAlt1Request': new Vimeo.SetVideoAsAlbumThumbnailAlt1Request() // SetVideoAsAlbumThumbnailAlt1Request | 
};
apiInstance.setVideoAsAlbumThumbnailAlt1(albumId, videoId, opts, (error, data, response) => {
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
 **videoId** | **Number**| The ID of the video. | 
 **setVideoAsAlbumThumbnailAlt1Request** | [**SetVideoAsAlbumThumbnailAlt1Request**](SetVideoAsAlbumThumbnailAlt1Request.md)|  | [optional] 

### Return type

[**Album**](Album.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

