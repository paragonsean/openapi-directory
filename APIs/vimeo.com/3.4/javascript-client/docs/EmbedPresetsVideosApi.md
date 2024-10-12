# Vimeo.EmbedPresetsVideosApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addVideoEmbedPreset**](EmbedPresetsVideosApi.md#addVideoEmbedPreset) | **PUT** /videos/{video_id}/presets/{preset_id} | Add an embed preset to a video
[**createVideoCustomLogo**](EmbedPresetsVideosApi.md#createVideoCustomLogo) | **POST** /videos/{video_id}/timelinethumbnails | Add a new custom logo to a video
[**deleteVideoEmbedPreset**](EmbedPresetsVideosApi.md#deleteVideoEmbedPreset) | **DELETE** /videos/{video_id}/presets/{preset_id} | Remove an embed preset from a video
[**getEmbedPresetVideos**](EmbedPresetsVideosApi.md#getEmbedPresetVideos) | **GET** /users/{user_id}/presets/{preset_id}/videos | Get all the videos that have been added to an embed preset
[**getEmbedPresetVideosAlt1**](EmbedPresetsVideosApi.md#getEmbedPresetVideosAlt1) | **GET** /me/presets/{preset_id}/videos | Get all the videos that have been added to an embed preset
[**getVideoCustomLogo**](EmbedPresetsVideosApi.md#getVideoCustomLogo) | **GET** /videos/{video_id}/timelinethumbnails/{thumbnail_id} | Get a custom video logo
[**getVideoEmbedPreset**](EmbedPresetsVideosApi.md#getVideoEmbedPreset) | **GET** /videos/{video_id}/presets/{preset_id} | Check if an embed preset has been added to a video



## addVideoEmbedPreset

> addVideoEmbedPreset(presetId, videoId)

Add an embed preset to a video

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

let apiInstance = new Vimeo.EmbedPresetsVideosApi();
let presetId = 12345; // Number | The ID of the preset.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.addVideoEmbedPreset(presetId, videoId, (error, data, response) => {
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
 **presetId** | **Number**| The ID of the preset. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## createVideoCustomLogo

> Picture createVideoCustomLogo(videoId)

Add a new custom logo to a video

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

let apiInstance = new Vimeo.EmbedPresetsVideosApi();
let videoId = 258684937; // Number | The ID of the video.
apiInstance.createVideoCustomLogo(videoId, (error, data, response) => {
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

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.picture+json


## deleteVideoEmbedPreset

> deleteVideoEmbedPreset(presetId, videoId)

Remove an embed preset from a video

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

let apiInstance = new Vimeo.EmbedPresetsVideosApi();
let presetId = 12345; // Number | The ID of the preset.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.deleteVideoEmbedPreset(presetId, videoId, (error, data, response) => {
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
 **presetId** | **Number**| The ID of the preset. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmbedPresetVideos

> [Video] getEmbedPresetVideos(presetId, userId, opts)

Get all the videos that have been added to an embed preset

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

let apiInstance = new Vimeo.EmbedPresetsVideosApi();
let presetId = 12345; // Number | The ID of the preset.
let userId = 152184; // Number | The ID of the user.
let opts = {
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10 // Number | The number of items to show on each page of results, up to a maximum of 100.
};
apiInstance.getEmbedPresetVideos(presetId, userId, opts, (error, data, response) => {
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
 **presetId** | **Number**| The ID of the preset. | 
 **userId** | **Number**| The ID of the user. | 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 

### Return type

[**[Video]**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.video+json


## getEmbedPresetVideosAlt1

> [Video] getEmbedPresetVideosAlt1(presetId, opts)

Get all the videos that have been added to an embed preset

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

let apiInstance = new Vimeo.EmbedPresetsVideosApi();
let presetId = 12345; // Number | The ID of the preset.
let opts = {
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10 // Number | The number of items to show on each page of results, up to a maximum of 100.
};
apiInstance.getEmbedPresetVideosAlt1(presetId, opts, (error, data, response) => {
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
 **presetId** | **Number**| The ID of the preset. | 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 

### Return type

[**[Video]**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.video+json


## getVideoCustomLogo

> Picture getVideoCustomLogo(thumbnailId, videoId)

Get a custom video logo

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

let apiInstance = new Vimeo.EmbedPresetsVideosApi();
let thumbnailId = 12345; // Number | The ID of the picture.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.getVideoCustomLogo(thumbnailId, videoId, (error, data, response) => {
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
 **thumbnailId** | **Number**| The ID of the picture. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

[**Picture**](Picture.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.picture+json


## getVideoEmbedPreset

> getVideoEmbedPreset(presetId, videoId)

Check if an embed preset has been added to a video

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

let apiInstance = new Vimeo.EmbedPresetsVideosApi();
let presetId = 12345; // Number | The ID of the preset.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.getVideoEmbedPreset(presetId, videoId, (error, data, response) => {
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
 **presetId** | **Number**| The ID of the preset. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

