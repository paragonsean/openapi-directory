# ApiVideo.CaptionsApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dELETEVideosVideoIdCaptionsLanguage**](CaptionsApi.md#dELETEVideosVideoIdCaptionsLanguage) | **DELETE** /videos/{videoId}/captions/{language} | Delete a caption
[**gETVideosVideoIdCaptions**](CaptionsApi.md#gETVideosVideoIdCaptions) | **GET** /videos/{videoId}/captions | List video captions
[**gETVideosVideoIdCaptionsLanguage**](CaptionsApi.md#gETVideosVideoIdCaptionsLanguage) | **GET** /videos/{videoId}/captions/{language} | Show a caption
[**pATCHVideosVideoIdCaptionsLanguage**](CaptionsApi.md#pATCHVideosVideoIdCaptionsLanguage) | **PATCH** /videos/{videoId}/captions/{language} | Update caption
[**pOSTVideosVideoIdCaptionsLanguage**](CaptionsApi.md#pOSTVideosVideoIdCaptionsLanguage) | **POST** /videos/{videoId}/captions/{language} | Upload a caption



## dELETEVideosVideoIdCaptionsLanguage

> dELETEVideosVideoIdCaptionsLanguage(videoId, language)

Delete a caption

Delete a caption in a specific language by providing the video ID for the video you want to delete the caption from and the language the caption is in.

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.CaptionsApi();
let videoId = "vi4k0jvEUuaTdRAEjQ4Prklgc"; // String | The unique identifier for the video you want to delete a caption from.
let language = "en"; // String | A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation.
apiInstance.dELETEVideosVideoIdCaptionsLanguage(videoId, language, (error, data, response) => {
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
 **videoId** | **String**| The unique identifier for the video you want to delete a caption from. | 
 **language** | **String**| A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation. | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gETVideosVideoIdCaptions

> CaptionsListResponse gETVideosVideoIdCaptions(videoId, opts)

List video captions

Retrieve a list of available captions for the videoId you provide.

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.CaptionsApi();
let videoId = "vi4k0jvEUuaTdRAEjQ4Prklg"; // String | The unique identifier for the video you want to retrieve a list of captions for.
let opts = {
  'currentPage': 2, // Number | Choose the number of search results to return per page. Minimum value: 1
  'pageSize': 30 // Number | Results per page. Allowed values 1-100, default is 25.
};
apiInstance.gETVideosVideoIdCaptions(videoId, opts, (error, data, response) => {
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
 **videoId** | **String**| The unique identifier for the video you want to retrieve a list of captions for. | 
 **currentPage** | **Number**| Choose the number of search results to return per page. Minimum value: 1 | [optional] [default to 1]
 **pageSize** | **Number**| Results per page. Allowed values 1-100, default is 25. | [optional] [default to 25]

### Return type

[**CaptionsListResponse**](CaptionsListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gETVideosVideoIdCaptionsLanguage

> Subtitle gETVideosVideoIdCaptionsLanguage(videoId, language)

Show a caption

Display a caption for a video in a specific language. If the language is available, the caption is returned. Otherwise, you will get a response indicating the caption was not found. Tutorials that use the [captions endpoint](https://api.video/blog/endpoints/captions).

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.CaptionsApi();
let videoId = "vi4k0jvEUuaTdRAEjQ4Prklg"; // String | The unique identifier for the video you want captions for.
let language = "en"; // String | A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation
apiInstance.gETVideosVideoIdCaptionsLanguage(videoId, language, (error, data, response) => {
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
 **videoId** | **String**| The unique identifier for the video you want captions for. | 
 **language** | **String**| A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation | 

### Return type

[**Subtitle**](Subtitle.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pATCHVideosVideoIdCaptionsLanguage

> Subtitle pATCHVideosVideoIdCaptionsLanguage(videoId, language, opts)

Update caption

To have the captions on automatically, use this PATCH to set default: true.

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.CaptionsApi();
let videoId = "vi4k0jvEUuaTdRAEjQ4Prklg"; // String | The unique identifier for the video you want to have automatic captions for. 
let language = "en"; // String | A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation.
let opts = {
  'captionsUpdatePayload': new ApiVideo.CaptionsUpdatePayload() // CaptionsUpdatePayload | 
};
apiInstance.pATCHVideosVideoIdCaptionsLanguage(videoId, language, opts, (error, data, response) => {
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
 **videoId** | **String**| The unique identifier for the video you want to have automatic captions for.  | 
 **language** | **String**| A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation. | 
 **captionsUpdatePayload** | [**CaptionsUpdatePayload**](CaptionsUpdatePayload.md)|  | [optional] 

### Return type

[**Subtitle**](Subtitle.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## pOSTVideosVideoIdCaptionsLanguage

> Subtitle pOSTVideosVideoIdCaptionsLanguage(videoId, language, file)

Upload a caption

Upload a VTT file to add captions to your video.  Read our [captioning tutorial](https://api.video/blog/tutorials/adding-captions) for more details.

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.CaptionsApi();
let videoId = "vi4k0jvEUuaTdRAEjQ4Prklg"; // String | The unique identifier for the video you want to add a caption to.
let language = "en"; // String | A valid BCP 47 language representation.
let file = "/path/to/file"; // File | The video text track (VTT) you want to upload.
apiInstance.pOSTVideosVideoIdCaptionsLanguage(videoId, language, file, (error, data, response) => {
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
 **videoId** | **String**| The unique identifier for the video you want to add a caption to. | 
 **language** | **String**| A valid BCP 47 language representation. | 
 **file** | **File**| The video text track (VTT) you want to upload. | 

### Return type

[**Subtitle**](Subtitle.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

