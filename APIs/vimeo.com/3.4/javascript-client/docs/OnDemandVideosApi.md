# Vimeo.OnDemandVideosApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addVideoToVod**](OnDemandVideosApi.md#addVideoToVod) | **PUT** /ondemand/pages/{ondemand_id}/videos/{video_id} | Add a video to an On Demand page
[**deleteVideoFromVod**](OnDemandVideosApi.md#deleteVideoFromVod) | **DELETE** /ondemand/pages/{ondemand_id}/videos/{video_id} | Remove a video from an On Demand page
[**getVodVideo**](OnDemandVideosApi.md#getVodVideo) | **GET** /ondemand/pages/{ondemand_id}/videos/{video_id} | Get a specific video on an On Demand page
[**getVodVideos**](OnDemandVideosApi.md#getVodVideos) | **GET** /ondemand/pages/{ondemand_id}/videos | Get all the videos on an On Demand page



## addVideoToVod

> OnDemandVideo addVideoToVod(ondemandId, videoId, addVideoToVodRequest)

Add a video to an On Demand page

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

let apiInstance = new Vimeo.OnDemandVideosApi();
let ondemandId = 61326; // Number | The ID of the On Demand.
let videoId = 12345; // Number | The ID of the video.
let addVideoToVodRequest = new Vimeo.AddVideoToVodRequest(); // AddVideoToVodRequest | 
apiInstance.addVideoToVod(ondemandId, videoId, addVideoToVodRequest, (error, data, response) => {
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
 **ondemandId** | **Number**| The ID of the On Demand. | 
 **videoId** | **Number**| The ID of the video. | 
 **addVideoToVodRequest** | [**AddVideoToVodRequest**](AddVideoToVodRequest.md)|  | 

### Return type

[**OnDemandVideo**](OnDemandVideo.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.ondemand.video+json
- **Accept**: application/vnd.vimeo.ondemand.video+json


## deleteVideoFromVod

> deleteVideoFromVod(ondemandId, videoId)

Remove a video from an On Demand page

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

let apiInstance = new Vimeo.OnDemandVideosApi();
let ondemandId = 61326; // Number | The ID of the On Demand.
let videoId = 12345; // Number | The ID of the video.
apiInstance.deleteVideoFromVod(ondemandId, videoId, (error, data, response) => {
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
 **ondemandId** | **Number**| The ID of the On Demand. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.video+json


## getVodVideo

> Video getVodVideo(ondemandId, videoId)

Get a specific video on an On Demand page

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

let apiInstance = new Vimeo.OnDemandVideosApi();
let ondemandId = 61326; // Number | The ID of the On Demand.
let videoId = 12345; // Number | The ID of the video.
apiInstance.getVodVideo(ondemandId, videoId, (error, data, response) => {
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
 **ondemandId** | **Number**| The ID of the On Demand. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

[**Video**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.video+json


## getVodVideos

> [Video] getVodVideos(ondemandId, opts)

Get all the videos on an On Demand page

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

let apiInstance = new Vimeo.OnDemandVideosApi();
let ondemandId = 61326; // Number | The ID of the On Demand.
let opts = {
  'direction': "asc", // String | The sort direction of the results.
  'filter': "filter_example", // String | The attribute by which to filter the results.
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10, // Number | The number of items to show on each page of results, up to a maximum of 100.
  'sort': "sort_example" // String | The way to sort the results.
};
apiInstance.getVodVideos(ondemandId, opts, (error, data, response) => {
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
 **ondemandId** | **Number**| The ID of the On Demand. | 
 **direction** | **String**| The sort direction of the results. | [optional] 
 **filter** | **String**| The attribute by which to filter the results. | [optional] 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 
 **sort** | **String**| The way to sort the results. | [optional] 

### Return type

[**[Video]**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.ondemand.video+json

