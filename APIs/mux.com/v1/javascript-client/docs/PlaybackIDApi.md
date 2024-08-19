# MuxApi.PlaybackIDApi

All URIs are relative to *https://api.mux.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAssetOrLivestreamId**](PlaybackIDApi.md#getAssetOrLivestreamId) | **GET** /video/v1/playback-ids/{PLAYBACK_ID} | Retrieve an Asset or Live Stream ID



## getAssetOrLivestreamId

> GetAssetOrLiveStreamIdResponse getAssetOrLivestreamId(PLAYBACK_ID)

Retrieve an Asset or Live Stream ID

Retrieves the Identifier of the Asset or Live Stream associated with the Playback ID.

### Example

```javascript
import MuxApi from 'mux_api';
let defaultClient = MuxApi.ApiClient.instance;
// Configure HTTP basic authorization: accessToken
let accessToken = defaultClient.authentications['accessToken'];
accessToken.username = 'YOUR USERNAME';
accessToken.password = 'YOUR PASSWORD';

let apiInstance = new MuxApi.PlaybackIDApi();
let PLAYBACK_ID = "PLAYBACK_ID_example"; // String | The live stream's playback ID.
apiInstance.getAssetOrLivestreamId(PLAYBACK_ID, (error, data, response) => {
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
 **PLAYBACK_ID** | **String**| The live stream&#39;s playback ID. | 

### Return type

[**GetAssetOrLiveStreamIdResponse**](GetAssetOrLiveStreamIdResponse.md)

### Authorization

[accessToken](../README.md#accessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

