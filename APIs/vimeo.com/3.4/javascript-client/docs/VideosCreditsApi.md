# Vimeo.VideosCreditsApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addVideoCredit**](VideosCreditsApi.md#addVideoCredit) | **POST** /videos/{video_id}/credits | Credit a user in a video
[**addVideoCreditAlt1**](VideosCreditsApi.md#addVideoCreditAlt1) | **POST** /channels/{channel_id}/videos/{video_id}/credits | Credit a user in a video
[**deleteVideoCredit**](VideosCreditsApi.md#deleteVideoCredit) | **DELETE** /videos/{video_id}/credits/{credit_id} | Delete a credit for a user in a video
[**editVideoCredit**](VideosCreditsApi.md#editVideoCredit) | **PATCH** /videos/{video_id}/credits/{credit_id} | Edit a credit for a user in a video
[**getVideoCredit**](VideosCreditsApi.md#getVideoCredit) | **GET** /videos/{video_id}/credits/{credit_id} | Get a specific credited user in a video
[**getVideoCredits**](VideosCreditsApi.md#getVideoCredits) | **GET** /videos/{video_id}/credits | Get all the credited users in a video
[**getVideoCreditsAlt1**](VideosCreditsApi.md#getVideoCreditsAlt1) | **GET** /channels/{channel_id}/videos/{video_id}/credits | Get all the credited users in a video



## addVideoCredit

> Credit addVideoCredit(videoId, addVideoCreditAlt1Request)

Credit a user in a video

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

let apiInstance = new Vimeo.VideosCreditsApi();
let videoId = 258684937; // Number | The ID of the video.
let addVideoCreditAlt1Request = new Vimeo.AddVideoCreditAlt1Request(); // AddVideoCreditAlt1Request | 
apiInstance.addVideoCredit(videoId, addVideoCreditAlt1Request, (error, data, response) => {
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
 **addVideoCreditAlt1Request** | [**AddVideoCreditAlt1Request**](AddVideoCreditAlt1Request.md)|  | 

### Return type

[**Credit**](Credit.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.credit+json
- **Accept**: application/vnd.vimeo.credit+json


## addVideoCreditAlt1

> Credit addVideoCreditAlt1(channelId, videoId, addVideoCreditAlt1Request)

Credit a user in a video

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

let apiInstance = new Vimeo.VideosCreditsApi();
let channelId = 927; // Number | The ID of the channel.
let videoId = 258684937; // Number | The ID of the video.
let addVideoCreditAlt1Request = new Vimeo.AddVideoCreditAlt1Request(); // AddVideoCreditAlt1Request | 
apiInstance.addVideoCreditAlt1(channelId, videoId, addVideoCreditAlt1Request, (error, data, response) => {
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
 **channelId** | **Number**| The ID of the channel. | 
 **videoId** | **Number**| The ID of the video. | 
 **addVideoCreditAlt1Request** | [**AddVideoCreditAlt1Request**](AddVideoCreditAlt1Request.md)|  | 

### Return type

[**Credit**](Credit.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.credit+json
- **Accept**: application/vnd.vimeo.credit+json


## deleteVideoCredit

> deleteVideoCredit(creditId, videoId)

Delete a credit for a user in a video

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

let apiInstance = new Vimeo.VideosCreditsApi();
let creditId = 12345; // Number | The ID of the credit.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.deleteVideoCredit(creditId, videoId, (error, data, response) => {
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
 **creditId** | **Number**| The ID of the credit. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## editVideoCredit

> Credit editVideoCredit(creditId, videoId, opts)

Edit a credit for a user in a video

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

let apiInstance = new Vimeo.VideosCreditsApi();
let creditId = 12345; // Number | The ID of the credit.
let videoId = 258684937; // Number | The ID of the video.
let opts = {
  'editVideoCreditRequest': new Vimeo.EditVideoCreditRequest() // EditVideoCreditRequest | 
};
apiInstance.editVideoCredit(creditId, videoId, opts, (error, data, response) => {
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
 **creditId** | **Number**| The ID of the credit. | 
 **videoId** | **Number**| The ID of the video. | 
 **editVideoCreditRequest** | [**EditVideoCreditRequest**](EditVideoCreditRequest.md)|  | [optional] 

### Return type

[**Credit**](Credit.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/vnd.vimeo.credit+json
- **Accept**: application/vnd.vimeo.credit+json


## getVideoCredit

> Credit getVideoCredit(creditId, videoId)

Get a specific credited user in a video

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

let apiInstance = new Vimeo.VideosCreditsApi();
let creditId = 12345; // Number | The ID of the credit.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.getVideoCredit(creditId, videoId, (error, data, response) => {
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
 **creditId** | **Number**| The ID of the credit. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

[**Credit**](Credit.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.credit+json


## getVideoCredits

> [Credit] getVideoCredits(videoId, opts)

Get all the credited users in a video

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

let apiInstance = new Vimeo.VideosCreditsApi();
let videoId = 258684937; // Number | The ID of the video.
let opts = {
  'direction': "asc", // String | The sort direction of the results.
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10, // Number | The number of items to show on each page of results, up to a maximum of 100.
  'query': "Stop motion", // String | The search query to use to filter the results.
  'sort': "sort_example" // String | The way to sort the results.
};
apiInstance.getVideoCredits(videoId, opts, (error, data, response) => {
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
 **direction** | **String**| The sort direction of the results. | [optional] 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 
 **query** | **String**| The search query to use to filter the results. | [optional] 
 **sort** | **String**| The way to sort the results. | [optional] 

### Return type

[**[Credit]**](Credit.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.credit+json


## getVideoCreditsAlt1

> [Credit] getVideoCreditsAlt1(channelId, videoId, opts)

Get all the credited users in a video

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

let apiInstance = new Vimeo.VideosCreditsApi();
let channelId = 927; // Number | The ID of the channel.
let videoId = 258684937; // Number | The ID of the video.
let opts = {
  'direction': "asc", // String | The sort direction of the results.
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10, // Number | The number of items to show on each page of results, up to a maximum of 100.
  'query': "Stop motion", // String | The search query to use to filter the results.
  'sort': "sort_example" // String | The way to sort the results.
};
apiInstance.getVideoCreditsAlt1(channelId, videoId, opts, (error, data, response) => {
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
 **channelId** | **Number**| The ID of the channel. | 
 **videoId** | **Number**| The ID of the video. | 
 **direction** | **String**| The sort direction of the results. | [optional] 
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 
 **query** | **String**| The search query to use to filter the results. | [optional] 
 **sort** | **String**| The way to sort the results. | [optional] 

### Return type

[**[Credit]**](Credit.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.credit+json

