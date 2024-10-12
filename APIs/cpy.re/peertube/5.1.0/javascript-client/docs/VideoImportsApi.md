# PeerTube.VideoImportsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1VideosImportsIdCancelPost**](VideoImportsApi.md#apiV1VideosImportsIdCancelPost) | **POST** /api/v1/videos/imports/{id}/cancel | Cancel video import
[**apiV1VideosImportsIdDelete**](VideoImportsApi.md#apiV1VideosImportsIdDelete) | **DELETE** /api/v1/videos/imports/{id} | Delete video import
[**importVideo**](VideoImportsApi.md#importVideo) | **POST** /api/v1/videos/imports | Import a video



## apiV1VideosImportsIdCancelPost

> apiV1VideosImportsIdCancelPost(id)

Cancel video import

Cancel a pending video import

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoImportsApi();
let id = 56; // Number | Entity id
apiInstance.apiV1VideosImportsIdCancelPost(id, (error, data, response) => {
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
 **id** | **Number**| Entity id | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV1VideosImportsIdDelete

> apiV1VideosImportsIdDelete(id)

Delete video import

Delete ended video import

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoImportsApi();
let id = 56; // Number | Entity id
apiInstance.apiV1VideosImportsIdDelete(id, (error, data, response) => {
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
 **id** | **Number**| Entity id | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## importVideo

> VideoUploadResponse importVideo(channelId, name, opts)

Import a video

Import a torrent or magnetURI or HTTP resource (if enabled by the instance administrator)

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoImportsApi();
let channelId = 56; // Number | Channel id that will contain this video
let name = "name_example"; // String | Video name
let opts = {
  'targetUrl': null, // String | remote URL where to find the import's source video
  'magnetUri': null, // String | magnet URI allowing to resolve the import's source video
  'torrentfile': null, // File | Torrent file containing only the video file
  'category': 56, // Number | category id of the video (see [/videos/categories](#operation/getCategories))
  'commentsEnabled': true, // Boolean | Enable or disable comments for this video
  'description': "description_example", // String | Video description
  'downloadEnabled': true, // Boolean | Enable or disable downloading for this video
  'language': "language_example", // String | language id of the video (see [/videos/languages](#operation/getLanguages))
  'licence': 56, // Number | licence id of the video (see [/videos/licences](#operation/getLicences))
  'nsfw': true, // Boolean | Whether or not this video contains sensitive content
  'originallyPublishedAt': new Date("2013-10-20T19:20:30+01:00"), // Date | Date when the content was originally published
  'previewfile': "/path/to/file", // File | Video preview file
  'privacy': new PeerTube.VideoPrivacySet(), // VideoPrivacySet | 
  'scheduleUpdate': new PeerTube.VideoScheduledUpdate(), // VideoScheduledUpdate | 
  'support': "support_example", // String | A text tell the audience how to support the video creator
  'tags': ["null"], // [String] | Video tags (maximum 5 tags each between 2 and 30 characters)
  'thumbnailfile': "/path/to/file", // File | Video thumbnail file
  'waitTranscoding': true // Boolean | Whether or not we wait transcoding before publish the video
};
apiInstance.importVideo(channelId, name, opts, (error, data, response) => {
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
 **channelId** | **Number**| Channel id that will contain this video | 
 **name** | **String**| Video name | 
 **targetUrl** | [**String**](String.md)| remote URL where to find the import&#39;s source video | [optional] 
 **magnetUri** | [**String**](String.md)| magnet URI allowing to resolve the import&#39;s source video | [optional] 
 **torrentfile** | [**File**](File.md)| Torrent file containing only the video file | [optional] 
 **category** | **Number**| category id of the video (see [/videos/categories](#operation/getCategories)) | [optional] 
 **commentsEnabled** | **Boolean**| Enable or disable comments for this video | [optional] 
 **description** | **String**| Video description | [optional] 
 **downloadEnabled** | **Boolean**| Enable or disable downloading for this video | [optional] 
 **language** | **String**| language id of the video (see [/videos/languages](#operation/getLanguages)) | [optional] 
 **licence** | **Number**| licence id of the video (see [/videos/licences](#operation/getLicences)) | [optional] 
 **nsfw** | **Boolean**| Whether or not this video contains sensitive content | [optional] 
 **originallyPublishedAt** | **Date**| Date when the content was originally published | [optional] 
 **previewfile** | **File**| Video preview file | [optional] 
 **privacy** | [**VideoPrivacySet**](VideoPrivacySet.md)|  | [optional] 
 **scheduleUpdate** | [**VideoScheduledUpdate**](VideoScheduledUpdate.md)|  | [optional] 
 **support** | **String**| A text tell the audience how to support the video creator | [optional] 
 **tags** | [**[String]**](String.md)| Video tags (maximum 5 tags each between 2 and 30 characters) | [optional] 
 **thumbnailfile** | **File**| Video thumbnail file | [optional] 
 **waitTranscoding** | **Boolean**| Whether or not we wait transcoding before publish the video | [optional] 

### Return type

[**VideoUploadResponse**](VideoUploadResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

