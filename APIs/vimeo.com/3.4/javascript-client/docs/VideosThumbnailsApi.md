# Vimeo.VideosThumbnailsApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createVideoThumbnail**](VideosThumbnailsApi.md#createVideoThumbnail) | **POST** /videos/{video_id}/pictures | Add a video thumbnail
[**createVideoThumbnailAlt1**](VideosThumbnailsApi.md#createVideoThumbnailAlt1) | **POST** /channels/{channel_id}/videos/{video_id}/pictures | Add a video thumbnail
[**deleteVideoThumbnail**](VideosThumbnailsApi.md#deleteVideoThumbnail) | **DELETE** /videos/{video_id}/pictures/{picture_id} | Delete a video thumbnail
[**editVideoThumbnail**](VideosThumbnailsApi.md#editVideoThumbnail) | **PATCH** /videos/{video_id}/pictures/{picture_id} | Edit a video thumbnail
[**getVideoThumbnail**](VideosThumbnailsApi.md#getVideoThumbnail) | **GET** /videos/{video_id}/pictures/{picture_id} | Get a video thumbnail
[**getVideoThumbnails**](VideosThumbnailsApi.md#getVideoThumbnails) | **GET** /videos/{video_id}/pictures | Get all the thumbnails of a video
[**getVideoThumbnailsAlt1**](VideosThumbnailsApi.md#getVideoThumbnailsAlt1) | **GET** /channels/{channel_id}/videos/{video_id}/pictures | Get all the thumbnails of a video



## createVideoThumbnail

> Picture createVideoThumbnail(videoId, opts)

Add a video thumbnail

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

let apiInstance = new Vimeo.VideosThumbnailsApi();
let videoId = 258684937; // Number | The ID of the video.
let opts = {
  'createVideoThumbnailAlt1Request': new Vimeo.CreateVideoThumbnailAlt1Request() // CreateVideoThumbnailAlt1Request | 
};
apiInstance.createVideoThumbnail(videoId, opts, (error, data, response) => {
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
 **videoId** | **Number**| The ID of the video. | 
 **createVideoThumbnailAlt1Request** | [**CreateVideoThumbnailAlt1Request**](CreateVideoThumbnailAlt1Request.md)|  | [optional] 

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.picture+json
- **Accept**: application/vnd.vimeo.picture+json


## createVideoThumbnailAlt1

> Picture createVideoThumbnailAlt1(channelId, videoId, opts)

Add a video thumbnail

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

let apiInstance = new Vimeo.VideosThumbnailsApi();
let channelId = 927; // Number | The ID of the channel.
let videoId = 258684937; // Number | The ID of the video.
let opts = {
  'createVideoThumbnailAlt1Request': new Vimeo.CreateVideoThumbnailAlt1Request() // CreateVideoThumbnailAlt1Request | 
};
apiInstance.createVideoThumbnailAlt1(channelId, videoId, opts, (error, data, response) => {
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
 **channelId** | **Number**| The ID of the channel. | 
 **videoId** | **Number**| The ID of the video. | 
 **createVideoThumbnailAlt1Request** | [**CreateVideoThumbnailAlt1Request**](CreateVideoThumbnailAlt1Request.md)|  | [optional] 

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.picture+json
- **Accept**: application/vnd.vimeo.picture+json


## deleteVideoThumbnail

> deleteVideoThumbnail(pictureId, videoId)

Delete a video thumbnail

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

let apiInstance = new Vimeo.VideosThumbnailsApi();
let pictureId = 12345; // Number | The ID of the picture.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.deleteVideoThumbnail(pictureId, videoId, (error, data, response) => {
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
 **pictureId** | **Number**| The ID of the picture. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## editVideoThumbnail

> Picture editVideoThumbnail(pictureId, videoId, opts)

Edit a video thumbnail

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

let apiInstance = new Vimeo.VideosThumbnailsApi();
let pictureId = 12345; // Number | The ID of the picture.
let videoId = 258684937; // Number | The ID of the video.
let opts = {
  'editVideoThumbnailRequest': new Vimeo.EditVideoThumbnailRequest() // EditVideoThumbnailRequest | 
};
apiInstance.editVideoThumbnail(pictureId, videoId, opts, (error, data, response) => {
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
 **pictureId** | **Number**| The ID of the picture. | 
 **videoId** | **Number**| The ID of the video. | 
 **editVideoThumbnailRequest** | [**EditVideoThumbnailRequest**](EditVideoThumbnailRequest.md)|  | [optional] 

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.picture+json
- **Accept**: application/vnd.vimeo.picture+json


## getVideoThumbnail

> Picture getVideoThumbnail(pictureId, videoId)

Get a video thumbnail

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

let apiInstance = new Vimeo.VideosThumbnailsApi();
let pictureId = 12345; // Number | The ID of the picture.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.getVideoThumbnail(pictureId, videoId, (error, data, response) => {
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
 **pictureId** | **Number**| The ID of the picture. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.picture+json


## getVideoThumbnails

> [Picture] getVideoThumbnails(videoId, opts)

Get all the thumbnails of a video

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

let apiInstance = new Vimeo.VideosThumbnailsApi();
let videoId = 258684937; // Number | The ID of the video.
let opts = {
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10 // Number | The number of items to show on each page of results, up to a maximum of 100.
};
apiInstance.getVideoThumbnails(videoId, opts, (error, data, response) => {
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
 **videoId** | **Number**| The ID of the video. | 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 

### Return type

[**[Picture]**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.picture+json


## getVideoThumbnailsAlt1

> [Picture] getVideoThumbnailsAlt1(channelId, videoId, opts)

Get all the thumbnails of a video

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

let apiInstance = new Vimeo.VideosThumbnailsApi();
let channelId = 927; // Number | The ID of the channel.
let videoId = 258684937; // Number | The ID of the video.
let opts = {
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10 // Number | The number of items to show on each page of results, up to a maximum of 100.
};
apiInstance.getVideoThumbnailsAlt1(channelId, videoId, opts, (error, data, response) => {
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
 **channelId** | **Number**| The ID of the channel. | 
 **videoId** | **Number**| The ID of the video. | 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 

### Return type

[**[Picture]**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.picture+json

