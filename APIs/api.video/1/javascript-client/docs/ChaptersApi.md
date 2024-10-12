# ApiVideo.ChaptersApi

All URIs are relative to *https://ws.api.video*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dELETEVideosVideoIdChaptersLanguage**](ChaptersApi.md#dELETEVideosVideoIdChaptersLanguage) | **DELETE** /videos/{videoId}/chapters/{language} | Delete a chapter
[**gETVideosVideoIdChapters**](ChaptersApi.md#gETVideosVideoIdChapters) | **GET** /videos/{videoId}/chapters | List video chapters
[**gETVideosVideoIdChaptersLanguage**](ChaptersApi.md#gETVideosVideoIdChaptersLanguage) | **GET** /videos/{videoId}/chapters/{language} | Show a chapter
[**pOSTVideosVideoIdChaptersLanguage**](ChaptersApi.md#pOSTVideosVideoIdChaptersLanguage) | **POST** /videos/{videoId}/chapters/{language} | Upload a chapter



## dELETEVideosVideoIdChaptersLanguage

> dELETEVideosVideoIdChaptersLanguage(videoId, language)

Delete a chapter

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.ChaptersApi();
let videoId = "vi4k0jvEUuaTdRAEjQ4Jfrgz"; // String | The unique identifier for the video you want to delete a chapter from. 
let language = "en"; // String | A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation.
apiInstance.dELETEVideosVideoIdChaptersLanguage(videoId, language, (error, data, response) => {
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
 **videoId** | **String**| The unique identifier for the video you want to delete a chapter from.  | 
 **language** | **String**| A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation. | 

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gETVideosVideoIdChapters

> ChaptersListResponse gETVideosVideoIdChapters(videoId, opts)

List video chapters

Retrieve a list of all chapters for a specified video.

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.ChaptersApi();
let videoId = "vi4k0jvEUuaTdRAEjQ4Jfrgz"; // String | The unique identifier for the video you want to retrieve a list of chapters for.
let opts = {
  'currentPage': 2, // Number | Choose the number of search results to return per page. Minimum value: 1
  'pageSize': 30 // Number | Results per page. Allowed values 1-100, default is 25.
};
apiInstance.gETVideosVideoIdChapters(videoId, opts, (error, data, response) => {
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
 **videoId** | **String**| The unique identifier for the video you want to retrieve a list of chapters for. | 
 **currentPage** | **Number**| Choose the number of search results to return per page. Minimum value: 1 | [optional] [default to 1]
 **pageSize** | **Number**| Results per page. Allowed values 1-100, default is 25. | [optional] [default to 25]

### Return type

[**ChaptersListResponse**](ChaptersListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## gETVideosVideoIdChaptersLanguage

> Chapter gETVideosVideoIdChaptersLanguage(videoId, language)

Show a chapter

Chapters help your viewers find the sections of the video they are most interested in viewing. Tutorials that use the [chapters endpoint](https://api.video/blog/endpoints/chapters).

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.ChaptersApi();
let videoId = "vi4k0jvEUuaTdRAEjQ4Jfrgz"; // String | The unique identifier for the video you want to show a chapter for.
let language = "en"; // String | A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation.
apiInstance.gETVideosVideoIdChaptersLanguage(videoId, language, (error, data, response) => {
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
 **videoId** | **String**| The unique identifier for the video you want to show a chapter for. | 
 **language** | **String**| A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation. | 

### Return type

[**Chapter**](Chapter.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pOSTVideosVideoIdChaptersLanguage

> Chapter pOSTVideosVideoIdChaptersLanguage(videoId, language, file)

Upload a chapter

Chapters help break the video into sections. Read our [tutorial](https://api.video/blog/tutorials/adding-chapters-to-your-videos) for more details.

### Example

```javascript
import ApiVideo from 'api_video';
let defaultClient = ApiVideo.ApiClient.instance;
// Configure Bearer access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ApiVideo.ChaptersApi();
let videoId = "vi4k0jvEUuaTdRAEjQ4Jfrgz"; // String | The unique identifier for the video you want to upload a chapter for.
let language = "en"; // String | A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation.
let file = "/path/to/file"; // File | The VTT file describing the chapters you want to upload.
apiInstance.pOSTVideosVideoIdChaptersLanguage(videoId, language, file, (error, data, response) => {
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
 **videoId** | **String**| The unique identifier for the video you want to upload a chapter for. | 
 **language** | **String**| A valid [BCP 47](https://github.com/libyal/libfwnt/wiki/Language-Code-identifiers) language representation. | 
 **file** | **File**| The VTT file describing the chapters you want to upload. | 

### Return type

[**Chapter**](Chapter.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

