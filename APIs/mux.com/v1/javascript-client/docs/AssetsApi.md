# MuxApi.AssetsApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createAsset**](AssetsApi.md#createAsset) | **POST** /video/v1/assets | Create an asset
[**createAssetPlaybackId**](AssetsApi.md#createAssetPlaybackId) | **POST** /video/v1/assets/{ASSET_ID}/playback-ids | Create a playback ID
[**createAssetTrack**](AssetsApi.md#createAssetTrack) | **POST** /video/v1/assets/{ASSET_ID}/tracks | Create an asset track
[**deleteAsset**](AssetsApi.md#deleteAsset) | **DELETE** /video/v1/assets/{ASSET_ID} | Delete an asset
[**deleteAssetPlaybackId**](AssetsApi.md#deleteAssetPlaybackId) | **DELETE** /video/v1/assets/{ASSET_ID}/playback-ids/{PLAYBACK_ID} | Delete a playback ID
[**deleteAssetTrack**](AssetsApi.md#deleteAssetTrack) | **DELETE** /video/v1/assets/{ASSET_ID}/tracks/{TRACK_ID} | Delete an asset track
[**getAsset**](AssetsApi.md#getAsset) | **GET** /video/v1/assets/{ASSET_ID} | Retrieve an asset
[**getAssetInputInfo**](AssetsApi.md#getAssetInputInfo) | **GET** /video/v1/assets/{ASSET_ID}/input-info | Retrieve asset input info
[**getAssetPlaybackId**](AssetsApi.md#getAssetPlaybackId) | **GET** /video/v1/assets/{ASSET_ID}/playback-ids/{PLAYBACK_ID} | Retrieve a playback ID
[**listAssets**](AssetsApi.md#listAssets) | **GET** /video/v1/assets | List assets
[**updateAsset**](AssetsApi.md#updateAsset) | **PATCH** /video/v1/assets/{ASSET_ID} | Update an Asset
[**updateAssetMasterAccess**](AssetsApi.md#updateAssetMasterAccess) | **PUT** /video/v1/assets/{ASSET_ID}/master-access | Update master access
[**updateAssetMp4Support**](AssetsApi.md#updateAssetMp4Support) | **PUT** /video/v1/assets/{ASSET_ID}/mp4-support | Update MP4 support



## createAsset

> AssetResponse createAsset(createAssetRequest)

Create an asset

Create a new Mux Video asset.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.AssetsApi();
let createAssetRequest = {"input":[{"url":"https://muxed.s3.amazonaws.com/leds.mp4"}],"playback_policy":["public"]}; // CreateAssetRequest | 
apiInstance.createAsset(createAssetRequest, (error, data, response) => {
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
 **createAssetRequest** | [**CreateAssetRequest**](CreateAssetRequest.md)|  | 

### Return type

[**AssetResponse**](AssetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAssetPlaybackId

> CreatePlaybackIDResponse createAssetPlaybackId(ASSET_ID, createPlaybackIDRequest)

Create a playback ID

Creates a playback ID that can be used to stream the asset to a viewer.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.AssetsApi();
let ASSET_ID = "ASSET_ID_example"; // String | The asset ID.
let createPlaybackIDRequest = {"policy":"public"}; // CreatePlaybackIDRequest | 
apiInstance.createAssetPlaybackId(ASSET_ID, createPlaybackIDRequest, (error, data, response) => {
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
 **ASSET_ID** | **String**| The asset ID. | 
 **createPlaybackIDRequest** | [**CreatePlaybackIDRequest**](CreatePlaybackIDRequest.md)|  | 

### Return type

[**CreatePlaybackIDResponse**](CreatePlaybackIDResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createAssetTrack

> CreateTrackResponse createAssetTrack(ASSET_ID, createTrackRequest)

Create an asset track

Adds an asset track (for example, subtitles, or an alternate audio track) to an asset.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.AssetsApi();
let ASSET_ID = "ASSET_ID_example"; // String | The asset ID.
let createTrackRequest = {"closed_captions":true,"language_code":"en-US","name":"English","passthrough":"English","text_type":"subtitles","type":"text","url":"https://example.com/myVideo_en.srt"}; // CreateTrackRequest | 
apiInstance.createAssetTrack(ASSET_ID, createTrackRequest, (error, data, response) => {
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
 **ASSET_ID** | **String**| The asset ID. | 
 **createTrackRequest** | [**CreateTrackRequest**](CreateTrackRequest.md)|  | 

### Return type

[**CreateTrackResponse**](CreateTrackResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAsset

> deleteAsset(ASSET_ID)

Delete an asset

Deletes a video asset and all its data.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.AssetsApi();
let ASSET_ID = "ASSET_ID_example"; // String | The asset ID.
apiInstance.deleteAsset(ASSET_ID, (error, data, response) => {
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
 **ASSET_ID** | **String**| The asset ID. | 

### Return type

null (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteAssetPlaybackId

> deleteAssetPlaybackId(ASSET_ID, PLAYBACK_ID)

Delete a playback ID

Deletes a playback ID, rendering it nonfunctional for viewing an asset&#39;s video content. Please note that deleting the playback ID removes access to the underlying asset; a viewer who started playback before the playback ID was deleted may be able to watch the entire video for a limited duration.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.AssetsApi();
let ASSET_ID = "ASSET_ID_example"; // String | The asset ID.
let PLAYBACK_ID = "PLAYBACK_ID_example"; // String | The live stream's playback ID.
apiInstance.deleteAssetPlaybackId(ASSET_ID, PLAYBACK_ID, (error, data, response) => {
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
 **ASSET_ID** | **String**| The asset ID. | 
 **PLAYBACK_ID** | **String**| The live stream&#39;s playback ID. | 

### Return type

null (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## deleteAssetTrack

> deleteAssetTrack(ASSET_ID, TRACK_ID)

Delete an asset track

Removes a text track from an asset. Audio and video tracks on assets cannot be removed.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.AssetsApi();
let ASSET_ID = "ASSET_ID_example"; // String | The asset ID.
let TRACK_ID = "TRACK_ID_example"; // String | The track ID.
apiInstance.deleteAssetTrack(ASSET_ID, TRACK_ID, (error, data, response) => {
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
 **ASSET_ID** | **String**| The asset ID. | 
 **TRACK_ID** | **String**| The track ID. | 

### Return type

null (empty response body)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAsset

> AssetResponse getAsset(ASSET_ID)

Retrieve an asset

Retrieves the details of an asset that has previously been created. Supply the unique asset ID that was returned from your previous request, and Mux will return the corresponding asset information. The same information is returned when creating an asset.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.AssetsApi();
let ASSET_ID = "ASSET_ID_example"; // String | The asset ID.
apiInstance.getAsset(ASSET_ID, (error, data, response) => {
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
 **ASSET_ID** | **String**| The asset ID. | 

### Return type

[**AssetResponse**](AssetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAssetInputInfo

> GetAssetInputInfoResponse getAssetInputInfo(ASSET_ID)

Retrieve asset input info

Returns a list of the input objects that were used to create the asset along with any settings that were applied to each input.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.AssetsApi();
let ASSET_ID = "ASSET_ID_example"; // String | The asset ID.
apiInstance.getAssetInputInfo(ASSET_ID, (error, data, response) => {
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
 **ASSET_ID** | **String**| The asset ID. | 

### Return type

[**GetAssetInputInfoResponse**](GetAssetInputInfoResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAssetPlaybackId

> GetAssetPlaybackIDResponse getAssetPlaybackId(ASSET_ID, PLAYBACK_ID)

Retrieve a playback ID

Retrieves information about the specified playback ID.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.AssetsApi();
let ASSET_ID = "ASSET_ID_example"; // String | The asset ID.
let PLAYBACK_ID = "PLAYBACK_ID_example"; // String | The live stream's playback ID.
apiInstance.getAssetPlaybackId(ASSET_ID, PLAYBACK_ID, (error, data, response) => {
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
 **ASSET_ID** | **String**| The asset ID. | 
 **PLAYBACK_ID** | **String**| The live stream&#39;s playback ID. | 

### Return type

[**GetAssetPlaybackIDResponse**](GetAssetPlaybackIDResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAssets

> ListAssetsResponse listAssets(opts)

List assets

List all Mux assets.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.AssetsApi();
let opts = {
  'limit': 25, // Number | Number of items to include in the response
  'page': 1, // Number | Offset by this many pages, of the size of `limit`
  'liveStreamId': "liveStreamId_example", // String | Filter response to return all the assets for this live stream only
  'uploadId': "uploadId_example" // String | Filter response to return an asset created from this direct upload only
};
apiInstance.listAssets(opts, (error, data, response) => {
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
 **limit** | **Number**| Number of items to include in the response | [optional] [default to 25]
 **page** | **Number**| Offset by this many pages, of the size of &#x60;limit&#x60; | [optional] [default to 1]
 **liveStreamId** | **String**| Filter response to return all the assets for this live stream only | [optional] 
 **uploadId** | **String**| Filter response to return an asset created from this direct upload only | [optional] 

### Return type

[**ListAssetsResponse**](ListAssetsResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateAsset

> AssetResponse updateAsset(ASSET_ID, updateAssetRequest)

Update an Asset

Updates the details of an already-created Asset with the provided Asset ID. This currently supports only the &#x60;passthrough&#x60; field.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.AssetsApi();
let ASSET_ID = "ASSET_ID_example"; // String | The asset ID.
let updateAssetRequest = {"passthrough":"Example"}; // UpdateAssetRequest | 
apiInstance.updateAsset(ASSET_ID, updateAssetRequest, (error, data, response) => {
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
 **ASSET_ID** | **String**| The asset ID. | 
 **updateAssetRequest** | [**UpdateAssetRequest**](UpdateAssetRequest.md)|  | 

### Return type

[**AssetResponse**](AssetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAssetMasterAccess

> AssetResponse updateAssetMasterAccess(ASSET_ID, updateAssetMasterAccessRequest)

Update master access

Allows you to add temporary access to the master (highest-quality) version of the asset in MP4 format. A URL will be created that can be used to download the master version for 24 hours. After 24 hours Master Access will revert to \&quot;none\&quot;. This master version is not optimized for web and not meant to be streamed, only downloaded for purposes like archiving or editing the video offline.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.AssetsApi();
let ASSET_ID = "ASSET_ID_example"; // String | The asset ID.
let updateAssetMasterAccessRequest = {"master_access":"temporary"}; // UpdateAssetMasterAccessRequest | 
apiInstance.updateAssetMasterAccess(ASSET_ID, updateAssetMasterAccessRequest, (error, data, response) => {
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
 **ASSET_ID** | **String**| The asset ID. | 
 **updateAssetMasterAccessRequest** | [**UpdateAssetMasterAccessRequest**](UpdateAssetMasterAccessRequest.md)|  | 

### Return type

[**AssetResponse**](AssetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateAssetMp4Support

> AssetResponse updateAssetMp4Support(ASSET_ID, updateAssetMP4SupportRequest)

Update MP4 support

Allows you to add or remove mp4 support for assets that were created without it. Currently there are two values supported in this request, &#x60;standard&#x60; and &#x60;none&#x60;. &#x60;none&#x60; means that an asset *does not* have mp4 support, so submitting a request with &#x60;mp4_support&#x60; set to &#x60;none&#x60; will delete the mp4 assets from the asset in question.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.AssetsApi();
let ASSET_ID = "ASSET_ID_example"; // String | The asset ID.
let updateAssetMP4SupportRequest = {"mp4_support":"standard"}; // UpdateAssetMP4SupportRequest | 
apiInstance.updateAssetMp4Support(ASSET_ID, updateAssetMP4SupportRequest, (error, data, response) => {
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
 **ASSET_ID** | **String**| The asset ID. | 
 **updateAssetMP4SupportRequest** | [**UpdateAssetMP4SupportRequest**](UpdateAssetMP4SupportRequest.md)|  | 

### Return type

[**AssetResponse**](AssetResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

