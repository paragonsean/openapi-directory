# PeerTube.VideoUploadApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**importVideo_0**](VideoUploadApi.md#importVideo_0) | **POST** /api/v1/videos/imports | Import a video
[**uploadLegacy_0**](VideoUploadApi.md#uploadLegacy_0) | **POST** /api/v1/videos/upload | Upload a video
[**uploadResumableCancel_0**](VideoUploadApi.md#uploadResumableCancel_0) | **DELETE** /api/v1/videos/upload-resumable | Cancel the resumable upload of a video, deleting any data uploaded so far
[**uploadResumableInit_0**](VideoUploadApi.md#uploadResumableInit_0) | **POST** /api/v1/videos/upload-resumable | Initialize the resumable upload of a video
[**uploadResumable_0**](VideoUploadApi.md#uploadResumable_0) | **PUT** /api/v1/videos/upload-resumable | Send chunk for the resumable upload of a video



## importVideo_0

> VideoUploadResponse importVideo_0(channelId, name, opts)

Import a video

Import a torrent or magnetURI or HTTP resource (if enabled by the instance administrator)

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoUploadApi();
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
apiInstance.importVideo_0(channelId, name, opts, (error, data, response) => {
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


## uploadLegacy_0

> VideoUploadResponse uploadLegacy_0(channelId, name, videofile, opts)

Upload a video

Uses a single request to upload a video.

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoUploadApi();
let channelId = 56; // Number | Channel id that will contain this video
let name = "name_example"; // String | Video name
let videofile = "/path/to/file"; // File | Video file
let opts = {
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
apiInstance.uploadLegacy_0(channelId, name, videofile, opts, (error, data, response) => {
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
 **videofile** | **File**| Video file | 
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


## uploadResumableCancel_0

> uploadResumableCancel_0(uploadId, contentLength)

Cancel the resumable upload of a video, deleting any data uploaded so far

Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to cancel the upload of a video

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoUploadApi();
let uploadId = "uploadId_example"; // String | Created session id to proceed with. If you didn't send chunks in the last 12 hours, it is not valid anymore and the upload session has already been deleted with its data ;-) 
let contentLength = 0; // Number | 
apiInstance.uploadResumableCancel_0(uploadId, contentLength, (error, data, response) => {
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
 **uploadId** | **String**| Created session id to proceed with. If you didn&#39;t send chunks in the last 12 hours, it is not valid anymore and the upload session has already been deleted with its data ;-)  | 
 **contentLength** | **Number**|  | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## uploadResumableInit_0

> uploadResumableInit_0(xUploadContentLength, xUploadContentType, opts)

Initialize the resumable upload of a video

Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to initialize the upload of a video

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoUploadApi();
let xUploadContentLength = 2469036; // Number | Number of bytes that will be uploaded in subsequent requests. Set this value to the size of the file you are uploading.
let xUploadContentType = "video/mp4"; // String | MIME type of the file that you are uploading. Depending on your instance settings, acceptable values might vary.
let opts = {
  'videoUploadRequestResumable': new PeerTube.VideoUploadRequestResumable() // VideoUploadRequestResumable | 
};
apiInstance.uploadResumableInit_0(xUploadContentLength, xUploadContentType, opts, (error, data, response) => {
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
 **xUploadContentLength** | **Number**| Number of bytes that will be uploaded in subsequent requests. Set this value to the size of the file you are uploading. | 
 **xUploadContentType** | **String**| MIME type of the file that you are uploading. Depending on your instance settings, acceptable values might vary. | 
 **videoUploadRequestResumable** | [**VideoUploadRequestResumable**](VideoUploadRequestResumable.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## uploadResumable_0

> VideoUploadResponse uploadResumable_0(uploadId, contentRange, contentLength, opts)

Send chunk for the resumable upload of a video

Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to continue, pause or resume the upload of a video

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoUploadApi();
let uploadId = "uploadId_example"; // String | Created session id to proceed with. If you didn't send chunks in the last hour, it is not valid anymore and you need to initialize a new upload. 
let contentRange = "bytes 0-262143/2469036"; // String | Specifies the bytes in the file that the request is uploading.  For example, a value of `bytes 0-262143/1000000` shows that the request is sending the first 262144 bytes (256 x 1024) in a 2,469,036 byte file. 
let contentLength = 262144; // Number | Size of the chunk that the request is sending.  Remember that larger chunks are more efficient. PeerTube's web client uses chunks varying from 1048576 bytes (~1MB) and increases or reduces size depending on connection health. 
let opts = {
  'body': "/path/to/file" // File | 
};
apiInstance.uploadResumable_0(uploadId, contentRange, contentLength, opts, (error, data, response) => {
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
 **uploadId** | **String**| Created session id to proceed with. If you didn&#39;t send chunks in the last hour, it is not valid anymore and you need to initialize a new upload.  | 
 **contentRange** | **String**| Specifies the bytes in the file that the request is uploading.  For example, a value of &#x60;bytes 0-262143/1000000&#x60; shows that the request is sending the first 262144 bytes (256 x 1024) in a 2,469,036 byte file.  | 
 **contentLength** | **Number**| Size of the chunk that the request is sending.  Remember that larger chunks are more efficient. PeerTube&#39;s web client uses chunks varying from 1048576 bytes (~1MB) and increases or reduces size depending on connection health.  | 
 **body** | **File**|  | [optional] 

### Return type

[**VideoUploadResponse**](VideoUploadResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/octet-stream
- **Accept**: application/json

