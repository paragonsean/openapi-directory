# ApiVideo.VideosApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dELETEVideo**](VideosApi.md#dELETEVideo) | **DELETE** /videos/{videoId} | Delete a video
[**gETVideo**](VideosApi.md#gETVideo) | **GET** /videos/{videoId} | Show a video
[**gETVideoStatus**](VideosApi.md#gETVideoStatus) | **GET** /videos/{videoId}/status | Show video status
[**lISTVideos**](VideosApi.md#lISTVideos) | **GET** /videos | List all videos
[**pATCHVideo**](VideosApi.md#pATCHVideo) | **PATCH** /videos/{videoId} | Update a video
[**pATCHVideosVideoIdThumbnail**](VideosApi.md#pATCHVideosVideoIdThumbnail) | **PATCH** /videos/{videoId}/thumbnail | Pick a thumbnail
[**pOSTVideo**](VideosApi.md#pOSTVideo) | **POST** /videos | Create a video
[**pOSTVideosVideoIdSource**](VideosApi.md#pOSTVideosVideoIdSource) | **POST** /videos/{videoId}/source | Upload a video
[**pOSTVideosVideoIdThumbnail**](VideosApi.md#pOSTVideosVideoIdThumbnail) | **POST** /videos/{videoId}/thumbnail | Upload a thumbnail



## dELETEVideo

> dELETEVideo(videoId)

Delete a video

If you do not need a video any longer, you can send a request to delete it. All you need is the videoId. Tutorials using [video deletion](https://api.video/blog/endpoints/video-delete).

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.VideosApi();
let videoId = "vi4k0jvEUuaTdRAEjQ4Jfrgz"; // String | The video ID for the video you want to delete.
apiInstance.dELETEVideo(videoId, (error, data, response) => {
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
 **videoId** | **String**| The video ID for the video you want to delete. | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gETVideo

> Video gETVideo(videoId)

Show a video

This call provides the same JSON information provided on video creation. For private videos, it will generate a unique token url. Use this to retrieve any details you need about a video, or set up a private viewing URL. Tutorials using [video GET](https://api.video/blog/endpoints/video-get).

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.VideosApi();
let videoId = "videoId_example"; // String | The unique identifier for the video you want details about.
apiInstance.gETVideo(videoId, (error, data, response) => {
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
 **videoId** | **String**| The unique identifier for the video you want details about. | 

### Return type

[**Video**](Video.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gETVideoStatus

> Videostatus gETVideoStatus(videoId)

Show video status

This API provides upload status &amp; encoding status to determine when the video is uploaded or ready to playback. Once encoding is completed, the response also lists the available stream qualities. Tutorials using [video status](https://api.video/blog/endpoints/video-status).

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.VideosApi();
let videoId = "vi4k0jvEUuaTdRAEjQ4Jfrgz"; // String | The unique identifier for the video you want the status for.
apiInstance.gETVideoStatus(videoId, (error, data, response) => {
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
 **videoId** | **String**| The unique identifier for the video you want the status for. | 

### Return type

[**Videostatus**](Videostatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## lISTVideos

> VideosListResponse lISTVideos(opts)

List all videos

Requests to this endpoint return a list of your videos (with all their details). With no parameters added to this query, the API returns all videos. You can filter what videos the API returns using the parameters described below.  We have [several tutorials](https://api.video/blog/endpoints/video-list) that demonstrate this endpoint.

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.VideosApi();
let opts = {
  'title': "My Video.mp4", // String | The title of a specific video you want to find. The search will match exactly to what term you provide and return any videos that contain the same term as part of their titles.
  'tags': ["null"], // [String] | A tag is a category you create and apply to videos. You can search for videos with particular tags by listing one or more here. Only videos that have all the tags you list will be returned.
  'metadata': ["null"], // [String] | Videos can be tagged with metadata tags in key:value pairs. You can search for videos with specific key value pairs using this parameter. [Dynamic Metadata](https://api.video/blog/endpoints/dynamic-metadata) allows you to define a key that allows any value pair.
  'description': "New Zealand", // String | If you described a video with a term or sentence, you can add it here to return videos containing this string.
  'liveStreamId': "li400mYKSgQ6xs7taUeSaEKr", // String | If you know the ID for a live stream, you can retrieve the stream by adding the ID for it here.
  'sortBy': "publishedAt", // String | Allowed: publishedAt, title. You can search by the time videos were published at, or by title.
  'sortOrder': "asc", // String | Allowed: asc, desc. asc is ascending and sorts from A to Z. desc is descending and sorts from Z to A.
  'currentPage': 2, // Number | Choose the number of search results to return per page. Minimum value: 1
  'pageSize': 30 // Number | Results per page. Allowed values 1-100, default is 25.
};
apiInstance.lISTVideos(opts, (error, data, response) => {
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
 **title** | **String**| The title of a specific video you want to find. The search will match exactly to what term you provide and return any videos that contain the same term as part of their titles. | [optional] 
 **tags** | [**[String]**](String.md)| A tag is a category you create and apply to videos. You can search for videos with particular tags by listing one or more here. Only videos that have all the tags you list will be returned. | [optional] 
 **metadata** | [**[String]**](String.md)| Videos can be tagged with metadata tags in key:value pairs. You can search for videos with specific key value pairs using this parameter. [Dynamic Metadata](https://api.video/blog/endpoints/dynamic-metadata) allows you to define a key that allows any value pair. | [optional] 
 **description** | **String**| If you described a video with a term or sentence, you can add it here to return videos containing this string. | [optional] 
 **liveStreamId** | **String**| If you know the ID for a live stream, you can retrieve the stream by adding the ID for it here. | [optional] 
 **sortBy** | **String**| Allowed: publishedAt, title. You can search by the time videos were published at, or by title. | [optional] 
 **sortOrder** | **String**| Allowed: asc, desc. asc is ascending and sorts from A to Z. desc is descending and sorts from Z to A. | [optional] 
 **currentPage** | **Number**| Choose the number of search results to return per page. Minimum value: 1 | [optional] [default to 1]
 **pageSize** | **Number**| Results per page. Allowed values 1-100, default is 25. | [optional] [default to 25]

### Return type

[**VideosListResponse**](VideosListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pATCHVideo

> Video pATCHVideo(videoId, opts)

Update a video

Use this endpoint to update the parameters associated with your video. The video you are updating is determined by the video ID you provide in the path. For each parameter you want to update, include the update in the request body. NOTE: If you are updating an array, you must provide the entire array as what you provide here overwrites what is in the system rather than appending to it. Tutorials using [video update](https://api.video/blog/endpoints/video-update).

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.VideosApi();
let videoId = "vi4k0jvEUuaTdRAEjQ4Jfrgz"; // String | The video ID for the video you want to delete.
let opts = {
  'videoUpdatePayload': new ApiVideo.VideoUpdatePayload() // VideoUpdatePayload | 
};
apiInstance.pATCHVideo(videoId, opts, (error, data, response) => {
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
 **videoId** | **String**| The video ID for the video you want to delete. | 
 **videoUpdatePayload** | [**VideoUpdatePayload**](VideoUpdatePayload.md)|  | [optional] 

### Return type

[**Video**](Video.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pATCHVideosVideoIdThumbnail

> Video pATCHVideosVideoIdThumbnail(videoId, opts)

Pick a thumbnail

Pick a thumbnail from the given time code. If you&#39;d like to upload an image for your thumbnail, use the [Upload a Thumbnail](https://docs.api.video/reference#post_videos-videoid-thumbnail) endpoint. There may be a short delay for the thumbnail to update. Tutorials using [Thumbnail picking](https://api.video/blog/endpoints/video-pick-a-thumbnail).

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.VideosApi();
let videoId = "vi4k0jvEUuaTdRAEjQ4Jfrgz"; // String | Unique identifier of the video you want to add a thumbnail to, where you use a section of your video as the thumbnail.
let opts = {
  'videoThumbnailPickPayload': new ApiVideo.VideoThumbnailPickPayload() // VideoThumbnailPickPayload | 
};
apiInstance.pATCHVideosVideoIdThumbnail(videoId, opts, (error, data, response) => {
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
 **videoId** | **String**| Unique identifier of the video you want to add a thumbnail to, where you use a section of your video as the thumbnail. | 
 **videoThumbnailPickPayload** | [**VideoThumbnailPickPayload**](VideoThumbnailPickPayload.md)|  | [optional] 

### Return type

[**Video**](Video.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pOSTVideo

> Video pOSTVideo(opts)

Create a video

To create a video, you create its container&amp;parameters first, before adding the video file (exception - when using an existing HTTP source). * Videos are public by default. [Learn about Private videos](https://api.video/blog/tutorials/tutorial-private-videos) * Up to 6 responsive video streams will be created (from 240p to 4k) * Mp4 encoded versions are created at the highest quality (max 1080p) by default. * Panoramic videos are for videos recorded in 360 degrees.  You can toggle this after your 360 video upload. * Searchable parameters: title, description, tags and metadata   &#x60;&#x60;&#x60;shell $ curl https://ws.api.video/videos \\ -H &#39;Authorization: Bearer {access_token} \\ -d &#39;{\&quot;title\&quot;:\&quot;My video\&quot;,       \&quot;description\&quot;:\&quot;so many details\&quot;,      \&quot;mp4Support\&quot;:true }&#39; &#x60;&#x60;&#x60;    ## add an URL to upload on creation You can also create a video directly from a video hosted on a third-party server by giving its URI in &#x60;source&#x60; parameter: &#x60;&#x60;&#x60;shell $ curl https://ws.api.video/videos \\ -H &#39;Authorization: Bearer {access_token} \\ -d &#39;{\&quot;source\&quot;:\&quot;http://uri/to/video.mp4\&quot;, \&quot;title\&quot;:\&quot;My video\&quot;}&#39; &#x60;&#x60;&#x60;  In this case, the service will respond &#x60;202 Accepted&#x60; and ingest the video asynchronously. ## Track users with Dynamic Metadata Metadata values can be a key:value where the values are predefined, but Dynamic metadata allows you to enter *any* value for a defined key.  To defined a dynamic metadata pair use: &#x60;&#x60;&#x60; \&quot;metadata\&quot;:[{\&quot;dynamicKey\&quot;: \&quot;__dynamicKey__\&quot;}] &#x60;&#x60;&#x60;  The double underscore on both sides of the value allows any variable to be added for a given video session. Added the the url you might have: &#x60;&#x60;&#x60; &lt;iframe type&#x3D;\&quot;text/html\&quot; src&#x3D;\&quot;https://embed.api.video/vod/vi6QvU9dhYCzW3BpPvPsZUa8?metadata[classUserName]&#x3D;Doug\&quot; width&#x3D;\&quot;960\&quot; height&#x3D;\&quot;320\&quot; frameborder&#x3D;\&quot;0\&quot; scrollling&#x3D;\&quot;no\&quot;&gt;&lt;/iframe&gt; &#x60;&#x60;&#x60;   This video session will be tagged as watched by Doug - allowing for in-depth analysis on how each viewer interacts with the videos. ### We have tutorials on: * [Creating and uploading videos](https://api.video/blog/tutorials/video-upload-tutorial) * [Uploading large videos](https://api.video/blog/tutorials/video-upload-tutorial-large-videos)   * [Using tags with videos](https://api.video/blog/tutorials/video-tagging-best-practices) * [Private videos](https://api.video/blog/tutorials/tutorial-private-videos) * [Using Dynamic Metadata](https://api.video/blog/tutorials/dynamic-metadata)  * Full list of [tutorials](https://api.video/blog/endpoints/video-create) that demonstrate this endpoint. 

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.VideosApi();
let opts = {
  'videoCreatePayload': new ApiVideo.VideoCreatePayload() // VideoCreatePayload | video to create
};
apiInstance.pOSTVideo(opts, (error, data, response) => {
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
 **videoCreatePayload** | [**VideoCreatePayload**](VideoCreatePayload.md)| video to create | [optional] 

### Return type

[**Video**](Video.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pOSTVideosVideoIdSource

> Video pOSTVideosVideoIdSource(videoId, file, opts)

Upload a video

To upload a video to the videoId you created. Replace {videoId} with the id you&#39;d like to use, {access_token} with your token, and /path/to/video.mp4 with the path to the video you&#39;d like to upload. You can only upload your video to the videoId once. &#x60;&#x60;&#x60;bash curl https://ws.api.video/videos/{videoId}/source \\   -H &#39;Authorization: Bearer {access_token}&#39; \\   -F file&#x3D;@/path/to/video.mp4    &#x60;&#x60;&#x60; Tutorials using [video upload](https://api.video/blog/endpoints/video-upload).

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.VideosApi();
let videoId = "vi4k0jvEUuaTdRAEjQ4Jfrgz"; // String | Enter the videoId you want to use to upload your video.
let file = "/path/to/file"; // File | The path to the video you would like to upload. The path must be local. If you want to use a video from an online source, you must use the \\\"/videos\\\" endpoint and add the \\\"source\\\" parameter when you create a new video.
let opts = {
  'contentRange': "Content-Range: bytes 200-100/5000" // String | Content-Range represents the range of bytes that will be returned as a result of the request. Byte ranges are inclusive, meaning that bytes 0-999 represents the first 1000 bytes in a file or object.
};
apiInstance.pOSTVideosVideoIdSource(videoId, file, opts, (error, data, response) => {
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
 **videoId** | **String**| Enter the videoId you want to use to upload your video. | 
 **file** | **File**| The path to the video you would like to upload. The path must be local. If you want to use a video from an online source, you must use the \\\&quot;/videos\\\&quot; endpoint and add the \\\&quot;source\\\&quot; parameter when you create a new video. | 
 **contentRange** | **String**| Content-Range represents the range of bytes that will be returned as a result of the request. Byte ranges are inclusive, meaning that bytes 0-999 represents the first 1000 bytes in a file or object. | [optional] 

### Return type

[**Video**](Video.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## pOSTVideosVideoIdThumbnail

> Video pOSTVideosVideoIdThumbnail(videoId, file)

Upload a thumbnail

The thumbnail is the poster that appears in the player window before video playback begins. This endpoint allows you to upload an image for the thumbnail. To select a still frame from the video using a time stamp, use [Pick a Thumbnail](https://docs.api.video/reference#patch_videos-videoid-thumbnail) to pick a time in the video.  Note: There may be a short delay before the new thumbnail is delivered to our CDN. Tutorials using [Thumbnail upload](https://api.video/blog/endpoints/videos-upload-a-thumbnail).

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.VideosApi();
let videoId = "videoId_example"; // String | Unique identifier of the chosen video 
let file = "/path/to/file"; // File | The image to be added as a thumbnail.
apiInstance.pOSTVideosVideoIdThumbnail(videoId, file, (error, data, response) => {
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
 **videoId** | **String**| Unique identifier of the chosen video  | 
 **file** | **File**| The image to be added as a thumbnail. | 

### Return type

[**Video**](Video.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

