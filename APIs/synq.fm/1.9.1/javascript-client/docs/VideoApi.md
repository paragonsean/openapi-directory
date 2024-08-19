# SynqVideo.VideoApi

All URIs are relative to *https://api.synq.fm/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](VideoApi.md#create) | **POST** /video/create | Create a new video, optionally setting some metadata fields.
[**details**](VideoApi.md#details) | **POST** /video/details | Return details about a video.
[**query**](VideoApi.md#query) | **POST** /video/query | Perform a JavaScript query to return video objects matching any desired criteria.
[**stream**](VideoApi.md#stream) | **POST** /video/stream | Returns urls for streaming.
[**update**](VideoApi.md#update) | **POST** /video/update | Update a video&#39;s metadata.
[**upload**](VideoApi.md#upload) | **POST** /video/upload | Return parameters needed for uploading a video file.
[**uploader**](VideoApi.md#uploader) | **POST** /video/uploader | Return embeddable url to an uploader widget



## create

> VideoObject create(apiKey, opts)

Create a new video, optionally setting some metadata fields.

Create a new video, optionally setting some metadata fields. You may optionally set some of the metadata associated with the video. Only fields inside the \&quot;userdata\&quot; field can be set.

### Example

```javascript
import SynqVideo from 'synq_video';

let apiInstance = new SynqVideo.VideoApi();
let apiKey = "apiKey_example"; // String | 
let opts = {
  'userdata': "userdata_example" // String | Additional metadata that will be associated with the video
};
apiInstance.create(apiKey, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **userdata** | **String**| Additional metadata that will be associated with the video | [optional] 

### Return type

[**VideoObject**](VideoObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
- **Accept**: application/json


## details

> VideoObject details(apiKey, videoId)

Return details about a video.

Return details about a video. You may optionally request that only some of the metadata fields are returned.

### Example

```javascript
import SynqVideo from 'synq_video';

let apiInstance = new SynqVideo.VideoApi();
let apiKey = "apiKey_example"; // String | 
let videoId = "videoId_example"; // String | ID of the video to retrieve the metadata from
apiInstance.details(apiKey, videoId, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **videoId** | **String**| ID of the video to retrieve the metadata from | 

### Return type

[**VideoObject**](VideoObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
- **Accept**: application/json


## query

> [Object] query(apiKey, filter)

Perform a JavaScript query to return video objects matching any desired criteria.

Find videos matching any criteria, by running a JavaScript function over each video object. A detailed tutorial on how to use this functionality is available on the [documentation page](https://www.synq.fm/queries-video-api/).

### Example

```javascript
import SynqVideo from 'synq_video';

let apiInstance = new SynqVideo.VideoApi();
let apiKey = "apiKey_example"; // String | 
let filter = "filter_example"; // String | JavaScript code to be run over each video object, to determine what should be returend.
apiInstance.query(apiKey, filter, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **filter** | **String**| JavaScript code to be run over each video object, to determine what should be returend. | 

### Return type

**[Object]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
- **Accept**: application/json


## stream

> StreamInformationObject stream(apiKey, videoId)

Returns urls for streaming.

Returns a stream url that you can stream to from your broadcasting software, and a playback url people can use to watch the stream.

### Example

```javascript
import SynqVideo from 'synq_video';

let apiInstance = new SynqVideo.VideoApi();
let apiKey = "apiKey_example"; // String | 
let videoId = "videoId_example"; // String | The ID of the video you want to stream to. The video needs to have been previously created.
apiInstance.stream(apiKey, videoId, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **videoId** | **String**| The ID of the video you want to stream to. The video needs to have been previously created. | 

### Return type

[**StreamInformationObject**](StreamInformationObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
- **Accept**: text/plain


## update

> VideoObject update(apiKey, videoId, source)

Update a video&#39;s metadata.

Update a video&#39;s metadata through JavaScript code. Only fields inside the \&quot;userdata\&quot; object can be set.

### Example

```javascript
import SynqVideo from 'synq_video';

let apiInstance = new SynqVideo.VideoApi();
let apiKey = "apiKey_example"; // String | 
let videoId = "videoId_example"; // String | The ID of the video whose metadata will be updated
let source = "source_example"; // String | JavaScript code to execute on the video object.
apiInstance.update(apiKey, videoId, source, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **videoId** | **String**| The ID of the video whose metadata will be updated | 
 **source** | **String**| JavaScript code to execute on the video object. | 

### Return type

[**VideoObject**](VideoObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
- **Accept**: application/json


## upload

> UploadParameterObject upload(apiKey, videoId)

Return parameters needed for uploading a video file.

Return parameters needed for uploading a video file to Amazon Simple Storage Service. See http://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-post-example.html as well as the language-specific code-examples. #### *Example request* &#x60;&#x60;&#x60;shell curl -s https://api.synq.fm/v1/video/upload \\   -F api_key&#x3D;${SYNQ_API_KEY} \\   -F video_id&#x3D;2d81c30ce62f4dfdb501dbca96c7ae56 &#x60;&#x60;&#x60;  #### *Example response* &#x60;&#x60;&#x60;json {   \&quot;action\&quot;: \&quot;https://synqfm.s3.amazonaws.com/\&quot;,   \&quot;AWSAccessKeyId\&quot;: \&quot;AKIAIP77Y7MMX3ITZMFA\&quot;,   \&quot;Content-Type\&quot;: \&quot;video/mp4\&quot;,   \&quot;Policy\&quot;: \&quot;eyJleHBpcmF0aW9uIiA6ICIyMDE2LTA0LTIyVDE5OjAyOjI2LjE3MloiLCAiY29uZGl0aW9ucyIgOiBbeyJidWNrZXQiIDogInN5bnFmbSJ9LCB7ImFjbCIgOiAicHVibGljLXJlYWQifSwgWyJzdGFydHMtd2l0aCIsICIka2V5IiwgInByb2plY3RzLzZlLzYzLzZlNjNiNzUyYTE4NTRkZGU4ODViNWNjNDcyZWRmNTY5L3VwbG9hZHMvdmlkZW9zLzJkLzgxLzJkODFjMzBjZTYyZjRkZmRiNTAxZGJjYTk2YzdhZTU2Lm1wNCJdLCBbInN0YXJ0cy13aXRoIiwgIiRDb250ZW50LVR5cGUiLCAidmlkZW8vbXA0Il0sIFsiY29udGVudC1sZW5ndGgtcmFuZ2UiLCAwLCAxMDk5NTExNjI3Nzc2XV19\&quot;,   \&quot;Signature\&quot;: \&quot;ysqDemlKXKr6hKzVFP0hCGgf/cs&#x3D;\&quot;,   \&quot;acl\&quot;: \&quot;public-read\&quot;,   \&quot;key\&quot;: \&quot;projects/6e/63/6e63b752a1854dde885b5cc472edf569/uploads/videos/2d/81/2d81c30ce62f4dfdb501dbca96c7ae56.mp4\&quot; } &#x60;&#x60;&#x60;  To upload the file, you can then make a multipart POST request to the URL in &#x60;action&#x60;, and for all the other parameters returned, set them as form parameters.  Given the parameters above, you would upload a file &#x60;test.mp4&#x60; using cURL like this:  &#x60;&#x60;&#x60;shell curl -s https://synqfm.s3.amazonaws.com/ \\   -F AWSAccessKeyId&#x3D;\&quot;AKIAIP77Y7MMX3ITZMFA\&quot; \\   -F Content-Type&#x3D;\&quot;video/mp4\&quot; \\   -F Policy&#x3D;\&quot;eyJleHBpcmF0aW9uIiA6ICIyMDE2LTA0LTIyVDE5OjAyOjI2LjE3MloiLCAiY29uZGl0aW9ucyIgOiBbeyJidWNrZXQiIDogInN5bnFmbSJ9LCB7ImFjbCIgOiAicHVibGljLXJlYWQifSwgWyJzdGFydHMtd2l0aCIsICIka2V5IiwgInByb2plY3RzLzZlLzYzLzZlNjNiNzUyYTE4NTRkZGU4ODViNWNjNDcyZWRmNTY5L3VwbG9hZHMvdmlkZW9zLzJkLzgxLzJkODFjMzBjZTYyZjRkZmRiNTAxZGJjYTk2YzdhZTU2Lm1wNCJdLCBbInN0YXJ0cy13aXRoIiwgIiRDb250ZW50LVR5cGUiLCAidmlkZW8vbXA0Il0sIFsiY29udGVudC1sZW5ndGgtcmFuZ2UiLCAwLCAxMDk5NTExNjI3Nzc2XV19\&quot; \\   -F Signature&#x3D;\&quot;ysqDemlKXKr6hKzVFP0hCGgf/cs&#x3D;\&quot; \\   -F acl&#x3D;\&quot;public-read\&quot; \\   -F key&#x3D;\&quot;projects/6e/63/6e63b752a1854dde885b5cc472edf569/uploads/videos/2d/81/2d81c30ce62f4dfdb501dbca96c7ae56.mp4\&quot; \\   -F file&#x3D;\&quot;@my_video_file.mp4\&quot; &#x60;&#x60;&#x60;  

### Example

```javascript
import SynqVideo from 'synq_video';

let apiInstance = new SynqVideo.VideoApi();
let apiKey = "apiKey_example"; // String | 
let videoId = "videoId_example"; // String | The ID of the video you are going to upload into. The video needs to have been previously created.
apiInstance.upload(apiKey, videoId, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **videoId** | **String**| The ID of the video you are going to upload into. The video needs to have been previously created. | 

### Return type

[**UploadParameterObject**](UploadParameterObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
- **Accept**: application/json


## uploader

> UploaderInformationObject uploader(apiKey, videoId, opts)

Return embeddable url to an uploader widget

Returns an embeddable url, that contains an uploader widget that allows you to easily upload any mp4. Great way to simplify the uploading process for end users.

### Example

```javascript
import SynqVideo from 'synq_video';

let apiInstance = new SynqVideo.VideoApi();
let apiKey = "apiKey_example"; // String | 
let videoId = "videoId_example"; // String | The ID of the video you are going to upload into. The video needs to have been previously created.
let opts = {
  'timeout': "'2 hours'" // String | How long the uploader widget works for. Anything from '30 minutes' to '2 days'.
};
apiInstance.uploader(apiKey, videoId, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **videoId** | **String**| The ID of the video you are going to upload into. The video needs to have been previously created. | 
 **timeout** | **String**| How long the uploader widget works for. Anything from &#39;30 minutes&#39; to &#39;2 days&#39;. | [optional] [default to &#39;2 hours&#39;]

### Return type

[**UploaderInformationObject**](UploaderInformationObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data, application/x-www-form-urlencoded
- **Accept**: text/plain

