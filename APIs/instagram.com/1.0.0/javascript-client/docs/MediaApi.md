# InstagramApi.MediaApi

All URIs are relative to *https://api.instagram.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mediaMediaIdGet**](MediaApi.md#mediaMediaIdGet) | **GET** /media/{media-id} | Get information about a media object.
[**mediaPopularGet**](MediaApi.md#mediaPopularGet) | **GET** /media/popular | Get a list of currently popular media.
[**mediaSearchGet**](MediaApi.md#mediaSearchGet) | **GET** /media/search | Search for media in a given area.
[**mediaShortcodeShortcodeGet**](MediaApi.md#mediaShortcodeShortcodeGet) | **GET** /media/shortcode/{shortcode} | Get information about a media object.



## mediaMediaIdGet

> MediaEntryResponse mediaMediaIdGet(mediaId)

Get information about a media object.

Get information about a media object. The returned type key will allow you to differentiate between image and video media.  **Note:** if you authenticate with an OAuth Token, you will receive the user_has_liked key which quickly tells you whether the current user has liked this media item. 

### Example

```javascript
import InstagramApi from 'instagram_api';
let defaultClient = InstagramApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: instagram_auth
let instagram_auth = defaultClient.authentications['instagram_auth'];
instagram_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new InstagramApi.MediaApi();
let mediaId = "mediaId_example"; // String | The ID of the media resource.
apiInstance.mediaMediaIdGet(mediaId, (error, data, response) => {
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
 **mediaId** | **String**| The ID of the media resource. | 

### Return type

[**MediaEntryResponse**](MediaEntryResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mediaPopularGet

> MediaSearchResponse mediaPopularGet()

Get a list of currently popular media.

Get a list of what media is most popular at the moment. Can return mix of &#x60;image&#x60; and &#x60;video&#x60; types.  **Warning:** [Deprecated](http://instagram.com/developer/changelog/) for Apps created **on or after** Nov 17, 2015 

### Example

```javascript
import InstagramApi from 'instagram_api';
let defaultClient = InstagramApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: instagram_auth
let instagram_auth = defaultClient.authentications['instagram_auth'];
instagram_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new InstagramApi.MediaApi();
apiInstance.mediaPopularGet((error, data, response) => {
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

[**MediaSearchResponse**](MediaSearchResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mediaSearchGet

> MediaSearchResponse mediaSearchGet(lat, lng, opts)

Search for media in a given area.

Search for media in a given area. The default time span is set to 5 days. The time span must not exceed 7 days. Defaults time stamps cover the last 5 days. Can return mix of &#x60;image&#x60; and &#x60;video&#x60; types. 

### Example

```javascript
import InstagramApi from 'instagram_api';
let defaultClient = InstagramApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: instagram_auth
let instagram_auth = defaultClient.authentications['instagram_auth'];
instagram_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new InstagramApi.MediaApi();
let lat = 3.4; // Number | Latitude of the center search coordinate. If used, `lng` is required.
let lng = 3.4; // Number | Longitude of the center search coordinate. If used, `lat` is required.
let opts = {
  'minTimestamp': 789, // Number | A unix timestamp. All media returned will be taken later than this timestamp.
  'maxTimestamp': 789, // Number | A unix timestamp. All media returned will be taken earlier than this timestamp.
  'distance': 56 // Number | Default is 1km (distance=1000), max distance is 5km.
};
apiInstance.mediaSearchGet(lat, lng, opts, (error, data, response) => {
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
 **lat** | **Number**| Latitude of the center search coordinate. If used, &#x60;lng&#x60; is required. | 
 **lng** | **Number**| Longitude of the center search coordinate. If used, &#x60;lat&#x60; is required. | 
 **minTimestamp** | **Number**| A unix timestamp. All media returned will be taken later than this timestamp. | [optional] 
 **maxTimestamp** | **Number**| A unix timestamp. All media returned will be taken earlier than this timestamp. | [optional] 
 **distance** | **Number**| Default is 1km (distance&#x3D;1000), max distance is 5km. | [optional] 

### Return type

[**MediaSearchResponse**](MediaSearchResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mediaShortcodeShortcodeGet

> MediaEntryResponse mediaShortcodeShortcodeGet(shortcode)

Get information about a media object.

This endpoint returns the same response as &#x60;GET /media/{media-id}&#x60;.  A media object&#39;s shortcode can be found in its shortlink URL. An example shortlink is &#x60;http://instagram.com/p/D/&#x60;, its corresponding shortcode is &#x60;D&#x60;. 

### Example

```javascript
import InstagramApi from 'instagram_api';
let defaultClient = InstagramApi.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: instagram_auth
let instagram_auth = defaultClient.authentications['instagram_auth'];
instagram_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new InstagramApi.MediaApi();
let shortcode = "shortcode_example"; // String | The short code of the media resource.
apiInstance.mediaShortcodeShortcodeGet(shortcode, (error, data, response) => {
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
 **shortcode** | **String**| The short code of the media resource. | 

### Return type

[**MediaEntryResponse**](MediaEntryResponse.md)

### Authorization

[api_key](../README.md#api_key), [instagram_auth](../README.md#instagram_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

