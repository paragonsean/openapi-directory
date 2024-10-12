# Vimeo.WatchLaterQueueEssentialsApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addVideoToWatchLater**](WatchLaterQueueEssentialsApi.md#addVideoToWatchLater) | **PUT** /users/{user_id}/watchlater/{video_id} | Add a video to a user&#39;s Watch Later queue
[**addVideoToWatchLaterAlt1**](WatchLaterQueueEssentialsApi.md#addVideoToWatchLaterAlt1) | **PUT** /me/watchlater/{video_id} | Add a video to a user&#39;s Watch Later queue
[**checkWatchLaterQueue**](WatchLaterQueueEssentialsApi.md#checkWatchLaterQueue) | **GET** /users/{user_id}/watchlater/{video_id} | Check if a user has added a specific video to their Watch Later queue
[**checkWatchLaterQueueAlt1**](WatchLaterQueueEssentialsApi.md#checkWatchLaterQueueAlt1) | **GET** /me/watchlater/{video_id} | Check if a user has added a specific video to their Watch Later queue
[**deleteVideoFromWatchLater**](WatchLaterQueueEssentialsApi.md#deleteVideoFromWatchLater) | **DELETE** /users/{user_id}/watchlater/{video_id} | Remove a video from a user&#39;s Watch Later queue
[**deleteVideoFromWatchLaterAlt1**](WatchLaterQueueEssentialsApi.md#deleteVideoFromWatchLaterAlt1) | **DELETE** /me/watchlater/{video_id} | Remove a video from a user&#39;s Watch Later queue
[**getWatchLaterQueue**](WatchLaterQueueEssentialsApi.md#getWatchLaterQueue) | **GET** /users/{user_id}/watchlater | Get all the videos in a user&#39;s Watch Later queue
[**getWatchLaterQueueAlt1**](WatchLaterQueueEssentialsApi.md#getWatchLaterQueueAlt1) | **GET** /me/watchlater | Get all the videos in a user&#39;s Watch Later queue



## addVideoToWatchLater

> addVideoToWatchLater(userId, videoId)

Add a video to a user&#39;s Watch Later queue

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

let apiInstance = new Vimeo.WatchLaterQueueEssentialsApi();
let userId = 152184; // Number | The ID of the user.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.addVideoToWatchLater(userId, videoId, (error, data, response) => {
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
 **userId** | **Number**| The ID of the user. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addVideoToWatchLaterAlt1

> addVideoToWatchLaterAlt1(videoId)

Add a video to a user&#39;s Watch Later queue

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

let apiInstance = new Vimeo.WatchLaterQueueEssentialsApi();
let videoId = 258684937; // Number | The ID of the video.
apiInstance.addVideoToWatchLaterAlt1(videoId, (error, data, response) => {
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
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## checkWatchLaterQueue

> Video checkWatchLaterQueue(userId, videoId)

Check if a user has added a specific video to their Watch Later queue

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

let apiInstance = new Vimeo.WatchLaterQueueEssentialsApi();
let userId = 152184; // Number | The ID of the user.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.checkWatchLaterQueue(userId, videoId, (error, data, response) => {
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
 **userId** | **Number**| The ID of the user. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

[**Video**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.video+json


## checkWatchLaterQueueAlt1

> Video checkWatchLaterQueueAlt1(videoId)

Check if a user has added a specific video to their Watch Later queue

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

let apiInstance = new Vimeo.WatchLaterQueueEssentialsApi();
let videoId = 258684937; // Number | The ID of the video.
apiInstance.checkWatchLaterQueueAlt1(videoId, (error, data, response) => {
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

[**Video**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.video+json


## deleteVideoFromWatchLater

> deleteVideoFromWatchLater(userId, videoId)

Remove a video from a user&#39;s Watch Later queue

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

let apiInstance = new Vimeo.WatchLaterQueueEssentialsApi();
let userId = 152184; // Number | The ID of the user.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.deleteVideoFromWatchLater(userId, videoId, (error, data, response) => {
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
 **userId** | **Number**| The ID of the user. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteVideoFromWatchLaterAlt1

> deleteVideoFromWatchLaterAlt1(videoId)

Remove a video from a user&#39;s Watch Later queue

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

let apiInstance = new Vimeo.WatchLaterQueueEssentialsApi();
let videoId = 258684937; // Number | The ID of the video.
apiInstance.deleteVideoFromWatchLaterAlt1(videoId, (error, data, response) => {
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
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getWatchLaterQueue

> [Video] getWatchLaterQueue(userId, opts)

Get all the videos in a user&#39;s Watch Later queue

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

let apiInstance = new Vimeo.WatchLaterQueueEssentialsApi();
let userId = 152184; // Number | The ID of the user.
let opts = {
  'direction': "asc", // String | The sort direction of the results.
  'filter': "filter_example", // String | The attribute by which to filter the results.
  'filterEmbeddable': true, // Boolean | Whether to filter the results by embeddable videos (`true`) or non-embeddable videos (`false`). Required only if **filter** is `embeddable`.
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10, // Number | The number of items to show on each page of results, up to a maximum of 100.
  'query': "Stop motion", // String | The search query to use to filter the results.
  'sort': "sort_example" // String | The way to sort the results.
};
apiInstance.getWatchLaterQueue(userId, opts, (error, data, response) => {
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
 **userId** | **Number**| The ID of the user. | 
 **direction** | **String**| The sort direction of the results. | [optional] 
 **filter** | **String**| The attribute by which to filter the results. | [optional] 
 **filterEmbeddable** | **Boolean**| Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;. | [optional] 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 
 **query** | **String**| The search query to use to filter the results. | [optional] 
 **sort** | **String**| The way to sort the results. | [optional] 

### Return type

[**[Video]**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.video+json


## getWatchLaterQueueAlt1

> [Video] getWatchLaterQueueAlt1(opts)

Get all the videos in a user&#39;s Watch Later queue

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

let apiInstance = new Vimeo.WatchLaterQueueEssentialsApi();
let opts = {
  'direction': "asc", // String | The sort direction of the results.
  'filter': "filter_example", // String | The attribute by which to filter the results.
  'filterEmbeddable': true, // Boolean | Whether to filter the results by embeddable videos (`true`) or non-embeddable videos (`false`). Required only if **filter** is `embeddable`.
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10, // Number | The number of items to show on each page of results, up to a maximum of 100.
  'query': "Stop motion", // String | The search query to use to filter the results.
  'sort': "sort_example" // String | The way to sort the results.
};
apiInstance.getWatchLaterQueueAlt1(opts, (error, data, response) => {
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
 **direction** | **String**| The sort direction of the results. | [optional] 
 **filter** | **String**| The attribute by which to filter the results. | [optional] 
 **filterEmbeddable** | **Boolean**| Whether to filter the results by embeddable videos (&#x60;true&#x60;) or non-embeddable videos (&#x60;false&#x60;). Required only if **filter** is &#x60;embeddable&#x60;. | [optional] 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 
 **query** | **String**| The search query to use to filter the results. | [optional] 
 **sort** | **String**| The way to sort the results. | [optional] 

### Return type

[**[Video]**](Video.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.video+json

