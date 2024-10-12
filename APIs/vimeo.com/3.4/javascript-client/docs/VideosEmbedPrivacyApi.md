# Vimeo.VideosEmbedPrivacyApi

All URIs are relative to *https://api.vimeo.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addVideoPrivacyDomain**](VideosEmbedPrivacyApi.md#addVideoPrivacyDomain) | **PUT** /videos/{video_id}/privacy/domains/{domain} | Permit a video to be embedded on a domain
[**deleteVideoPrivacyDomain**](VideosEmbedPrivacyApi.md#deleteVideoPrivacyDomain) | **DELETE** /videos/{video_id}/privacy/domains/{domain} | Restrict a video from being embedded on a domain
[**getVideoPrivacyDomains**](VideosEmbedPrivacyApi.md#getVideoPrivacyDomains) | **GET** /videos/{video_id}/privacy/domains | Get all the domains on which a video can be embedded



## addVideoPrivacyDomain

> addVideoPrivacyDomain(domain, videoId)

Permit a video to be embedded on a domain

If domain privacy is enabled for this video, this method permits the video to be embedded on the specified domain.

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

let apiInstance = new Vimeo.VideosEmbedPrivacyApi();
let domain = "example.com"; // String | The domain name.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.addVideoPrivacyDomain(domain, videoId, (error, data, response) => {
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
 **domain** | **String**| The domain name. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteVideoPrivacyDomain

> deleteVideoPrivacyDomain(domain, videoId)

Restrict a video from being embedded on a domain

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

let apiInstance = new Vimeo.VideosEmbedPrivacyApi();
let domain = "example.com"; // String | The domain name.
let videoId = 258684937; // Number | The ID of the video.
apiInstance.deleteVideoPrivacyDomain(domain, videoId, (error, data, response) => {
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
 **domain** | **String**| The domain name. | 
 **videoId** | **Number**| The ID of the video. | 

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVideoPrivacyDomains

> [Domain] getVideoPrivacyDomains(videoId, opts)

Get all the domains on which a video can be embedded

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

let apiInstance = new Vimeo.VideosEmbedPrivacyApi();
let videoId = 258684937; // Number | The ID of the video.
let opts = {
  'page': 1, // Number | The page number of the results to show.
  'perPage': 10 // Number | The number of items to show on each page of results, up to a maximum of 100.
};
apiInstance.getVideoPrivacyDomains(videoId, opts, (error, data, response) => {
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
 **page** | **Number**| The page number of the results to show. | [optional] 
 **perPage** | **Number**| The number of items to show on each page of results, up to a maximum of 100. | [optional] 

### Return type

[**[Domain]**](Domain.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.vimeo.domain+json

