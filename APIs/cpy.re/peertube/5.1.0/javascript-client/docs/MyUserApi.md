# PeerTube.MyUserApi

All URIs are relative to *https://peertube2.cpy.re*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV1UsersMeAvatarDelete**](MyUserApi.md#apiV1UsersMeAvatarDelete) | **DELETE** /api/v1/users/me/avatar | Delete my avatar
[**apiV1UsersMeAvatarPickPost**](MyUserApi.md#apiV1UsersMeAvatarPickPost) | **POST** /api/v1/users/me/avatar/pick | Update my user avatar
[**apiV1UsersMeVideoQuotaUsedGet**](MyUserApi.md#apiV1UsersMeVideoQuotaUsedGet) | **GET** /api/v1/users/me/video-quota-used | Get my user used quota
[**apiV1UsersMeVideosGet**](MyUserApi.md#apiV1UsersMeVideosGet) | **GET** /api/v1/users/me/videos | Get videos of my user
[**apiV1UsersMeVideosImportsGet_0**](MyUserApi.md#apiV1UsersMeVideosImportsGet_0) | **GET** /api/v1/users/me/videos/imports | Get video imports of my user
[**apiV1UsersMeVideosVideoIdRatingGet**](MyUserApi.md#apiV1UsersMeVideosVideoIdRatingGet) | **GET** /api/v1/users/me/videos/{videoId}/rating | Get rate of my user for a video
[**getMyAbuses_0**](MyUserApi.md#getMyAbuses_0) | **GET** /api/v1/users/me/abuses | List my abuses
[**getUserInfo**](MyUserApi.md#getUserInfo) | **GET** /api/v1/users/me | Get my user information
[**putUserInfo**](MyUserApi.md#putUserInfo) | **PUT** /api/v1/users/me | Update my user information



## apiV1UsersMeAvatarDelete

> apiV1UsersMeAvatarDelete()

Delete my avatar

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.MyUserApi();
apiInstance.apiV1UsersMeAvatarDelete((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## apiV1UsersMeAvatarPickPost

> ApiV1UsersMeAvatarPickPost200Response apiV1UsersMeAvatarPickPost(opts)

Update my user avatar

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.MyUserApi();
let opts = {
  'avatarfile': "/path/to/file" // File | The file to upload
};
apiInstance.apiV1UsersMeAvatarPickPost(opts, (error, data, response) => {
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
 **avatarfile** | **File**| The file to upload | [optional] 

### Return type

[**ApiV1UsersMeAvatarPickPost200Response**](ApiV1UsersMeAvatarPickPost200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## apiV1UsersMeVideoQuotaUsedGet

> ApiV1UsersMeVideoQuotaUsedGet200Response apiV1UsersMeVideoQuotaUsedGet()

Get my user used quota

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.MyUserApi();
apiInstance.apiV1UsersMeVideoQuotaUsedGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiV1UsersMeVideoQuotaUsedGet200Response**](ApiV1UsersMeVideoQuotaUsedGet200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1UsersMeVideosGet

> VideoListResponse apiV1UsersMeVideosGet(opts)

Get videos of my user

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.MyUserApi();
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt" // String | Sort column
};
apiInstance.apiV1UsersMeVideosGet(opts, (error, data, response) => {
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
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**| Sort column | [optional] 

### Return type

[**VideoListResponse**](VideoListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1UsersMeVideosImportsGet_0

> VideoImportsList apiV1UsersMeVideosImportsGet_0(opts)

Get video imports of my user

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.MyUserApi();
let opts = {
  'start': 56, // Number | Offset used to paginate results
  'count': 15, // Number | Number of items to return
  'sort': "-createdAt", // String | Sort column
  'targetUrl': "targetUrl_example", // String | Filter on import target URL
  'videoChannelSyncId': 3.4, // Number | Filter on imports created by a specific channel synchronization
  'search': "search_example" // String | Search in video names
};
apiInstance.apiV1UsersMeVideosImportsGet_0(opts, (error, data, response) => {
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
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]
 **sort** | **String**| Sort column | [optional] 
 **targetUrl** | **String**| Filter on import target URL | [optional] 
 **videoChannelSyncId** | **Number**| Filter on imports created by a specific channel synchronization | [optional] 
 **search** | **String**| Search in video names | [optional] 

### Return type

[**VideoImportsList**](VideoImportsList.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV1UsersMeVideosVideoIdRatingGet

> GetMeVideoRating apiV1UsersMeVideosVideoIdRatingGet(videoId)

Get rate of my user for a video

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.MyUserApi();
let videoId = 56; // Number | The video id
apiInstance.apiV1UsersMeVideosVideoIdRatingGet(videoId, (error, data, response) => {
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
 **videoId** | **Number**| The video id | 

### Return type

[**GetMeVideoRating**](GetMeVideoRating.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMyAbuses_0

> GetAbuses200Response getMyAbuses_0(opts)

List my abuses

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.MyUserApi();
let opts = {
  'id': 56, // Number | only list the report with this id
  'state': new PeerTube.AbuseStateSet(), // AbuseStateSet | 
  'sort': "sort_example", // String | Sort abuses by criteria
  'start': 56, // Number | Offset used to paginate results
  'count': 15 // Number | Number of items to return
};
apiInstance.getMyAbuses_0(opts, (error, data, response) => {
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
 **id** | **Number**| only list the report with this id | [optional] 
 **state** | [**AbuseStateSet**](.md)|  | [optional] 
 **sort** | **String**| Sort abuses by criteria | [optional] 
 **start** | **Number**| Offset used to paginate results | [optional] 
 **count** | **Number**| Number of items to return | [optional] [default to 15]

### Return type

[**GetAbuses200Response**](GetAbuses200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserInfo

> [User] getUserInfo()

Get my user information

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.MyUserApi();
apiInstance.getUserInfo((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[User]**](User.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putUserInfo

> putUserInfo(updateMe)

Update my user information

### Example

```javascript
import PeerTube from 'peer_tube';
let defaultClient = PeerTube.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PeerTube.MyUserApi();
let updateMe = new PeerTube.UpdateMe(); // UpdateMe | 
apiInstance.putUserInfo(updateMe, (error, data, response) => {
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
 **updateMe** | [**UpdateMe**](UpdateMe.md)|  | 

### Return type

null (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

