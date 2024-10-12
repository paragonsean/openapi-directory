# VoiceApi.StreamAudioApi

All URIs are relative to *https://api.nexmo.com/v1/calls*

Method | HTTP request | Description
------------- | ------------- | -------------
[**startStream**](StreamAudioApi.md#startStream) | **PUT** /{uuid}/stream | Play an audio file into a call
[**stopStream**](StreamAudioApi.md#stopStream) | **DELETE** /{uuid}/stream | Stop playing an audio file into a call



## startStream

> StartStreamResponse startStream(uuid, startStreamRequest)

Play an audio file into a call

Play an audio file into a call

### Example

```javascript
import VoiceApi from 'voice_api';
let defaultClient = VoiceApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new VoiceApi.StreamAudioApi();
let uuid = "63f61863-4a51-4f6b-86e1-46edebcf9356"; // String | UUID of the Call Leg
let startStreamRequest = new VoiceApi.StartStreamRequest(); // StartStreamRequest | action to perform
apiInstance.startStream(uuid, startStreamRequest, (error, data, response) => {
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
 **uuid** | **String**| UUID of the Call Leg | 
 **startStreamRequest** | [**StartStreamRequest**](StartStreamRequest.md)| action to perform | 

### Return type

[**StartStreamResponse**](StartStreamResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopStream

> StopStreamResponse stopStream(uuid)

Stop playing an audio file into a call

Stop playing an audio file into a call

### Example

```javascript
import VoiceApi from 'voice_api';
let defaultClient = VoiceApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new VoiceApi.StreamAudioApi();
let uuid = "63f61863-4a51-4f6b-86e1-46edebcf9356"; // String | UUID of the Call Leg
apiInstance.stopStream(uuid, (error, data, response) => {
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
 **uuid** | **String**| UUID of the Call Leg | 

### Return type

[**StopStreamResponse**](StopStreamResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

