# Shotstack.EditApi

All URIs are relative to *https://api.shotstack.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRender**](EditApi.md#getRender) | **GET** /render/{id} | Get Render Status
[**postRender**](EditApi.md#postRender) | **POST** /render | Render Asset



## getRender

> RenderResponse getRender(id)

Get Render Status

Get the rendering status, temporary asset url and details of a render by ID.  **base URL:** https://api.shotstack.io/{version}

### Example

```javascript
import Shotstack from 'shotstack';
let defaultClient = Shotstack.ApiClient.instance;
// Configure API key authorization: DeveloperKey
let DeveloperKey = defaultClient.authentications['DeveloperKey'];
DeveloperKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DeveloperKey.apiKeyPrefix = 'Token';

let apiInstance = new Shotstack.EditApi();
let id = "id_example"; // String | The id of the timeline render task in UUID format
apiInstance.getRender(id, (error, data, response) => {
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
 **id** | **String**| The id of the timeline render task in UUID format | 

### Return type

[**RenderResponse**](RenderResponse.md)

### Authorization

[DeveloperKey](../README.md#DeveloperKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postRender

> QueuedResponse postRender(edit)

Render Asset

Queue and render the contents of a timeline as a video, image or audio file.

### Example

```javascript
import Shotstack from 'shotstack';
let defaultClient = Shotstack.ApiClient.instance;
// Configure API key authorization: DeveloperKey
let DeveloperKey = defaultClient.authentications['DeveloperKey'];
DeveloperKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//DeveloperKey.apiKeyPrefix = 'Token';

let apiInstance = new Shotstack.EditApi();
let edit = {"output":{"format":"mp4","resolution":"sd"},"timeline":{"background":"#000000","soundtrack":{"effect":"fadeInFadeOut","src":"https://s3-ap-northeast-1.amazonaws.com/my-bucket/music.mp3"},"tracks":[{"clips":[{"asset":{"style":"minimal","text":"Hello World","type":"title"},"effect":"slideRight","length":4,"start":0,"transition":{"in":"fade","out":"fade"}},{"asset":{"src":"https://s3-ap-northeast-1.amazonaws.com/my-bucket/my-image.jpg","type":"image"},"effect":"zoomIn","filter":"greyscale","length":4,"start":3}]},{"clips":[{"asset":{"src":"https://s3-ap-northeast-1.amazonaws.com/my-bucket/my-clip-1.mp4","trim":10.5,"type":"video"},"length":4.5,"start":7},{"asset":{"src":"https://s3-ap-northeast-1.amazonaws.com/my-bucket/my-clip-2.mp4","type":"video","volume":0.5},"length":5,"start":11.5,"transition":{"out":"wipeLeft"}}]}]}}; // Edit | The video, image or audio edit specified using JSON.  **base URL:** https://api.shotstack.io/{version}
apiInstance.postRender(edit, (error, data, response) => {
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
 **edit** | [**Edit**](Edit.md)| The video, image or audio edit specified using JSON.  **base URL:** https://api.shotstack.io/{version} | 

### Return type

[**QueuedResponse**](QueuedResponse.md)

### Authorization

[DeveloperKey](../README.md#DeveloperKey)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

