# PeerTube.VideoCaptionsApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addVideoCaption**](VideoCaptionsApi.md#addVideoCaption) | **PUT** /api/v1/videos/{id}/captions/{captionLanguage} | Add or replace a video caption
[**delVideoCaption**](VideoCaptionsApi.md#delVideoCaption) | **DELETE** /api/v1/videos/{id}/captions/{captionLanguage} | Delete a video caption
[**getVideoCaptions**](VideoCaptionsApi.md#getVideoCaptions) | **GET** /api/v1/videos/{id}/captions | List captions of a video



## addVideoCaption

> addVideoCaption(id, captionLanguage, opts)

Add or replace a video caption

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoCaptionsApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
let captionLanguage = "captionLanguage_example"; // String | The caption language
let opts = {
  'captionfile': "/path/to/file" // File | The file to upload.
};
apiInstance.addVideoCaption(id, captionLanguage, opts, (error, data, response) => {
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
 **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | 
 **captionLanguage** | **String**| The caption language | 
 **captionfile** | **File**| The file to upload. | [optional] 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: Not defined


## delVideoCaption

> delVideoCaption(id, captionLanguage)

Delete a video caption

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.VideoCaptionsApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
let captionLanguage = "captionLanguage_example"; // String | The caption language
apiInstance.delVideoCaption(id, captionLanguage, (error, data, response) => {
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
 **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | 
 **captionLanguage** | **String**| The caption language | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getVideoCaptions

> GetVideoCaptions200Response getVideoCaptions(id)

List captions of a video

### Example

```javascript
import PeerTube from 'peer_tube';

let apiInstance = new PeerTube.VideoCaptionsApi();
let id = new PeerTube.GetLiveIdIdParameter(); // GetLiveIdIdParameter | The object id, uuid or short uuid
apiInstance.getVideoCaptions(id, (error, data, response) => {
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
 **id** | [**GetLiveIdIdParameter**](.md)| The object id, uuid or short uuid | 

### Return type

[**GetVideoCaptions200Response**](GetVideoCaptions200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

