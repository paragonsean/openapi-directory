# VoiceApi.PlayTTSApi

All URIs are relative to *https://api.nexmo.com/v1/calls*

Method | HTTP request | Description
------------- | ------------- | -------------
[**startTalk**](PlayTTSApi.md#startTalk) | **PUT** /{uuid}/talk | Play text to speech into a call
[**stopTalk**](PlayTTSApi.md#stopTalk) | **DELETE** /{uuid}/talk | Stop text to speech in a call



## startTalk

> StartTalkResponse startTalk(uuid, opts)

Play text to speech into a call

Play text to speech into a call

### Example

```javascript
import VoiceApi from 'voice_api';
let defaultClient = VoiceApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new VoiceApi.PlayTTSApi();
let uuid = "63f61863-4a51-4f6b-86e1-46edebcf9356"; // String | UUID of the Call Leg
let opts = {
  'startTalkRequest': new VoiceApi.StartTalkRequest() // StartTalkRequest | Action to perform
};
apiInstance.startTalk(uuid, opts, (error, data, response) => {
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
 **startTalkRequest** | [**StartTalkRequest**](StartTalkRequest.md)| Action to perform | [optional] 

### Return type

[**StartTalkResponse**](StartTalkResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopTalk

> StopTalkResponse stopTalk(uuid)

Stop text to speech in a call

Stop text to speech in a call

### Example

```javascript
import VoiceApi from 'voice_api';
let defaultClient = VoiceApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new VoiceApi.PlayTTSApi();
let uuid = "63f61863-4a51-4f6b-86e1-46edebcf9356"; // String | UUID of the Call Leg
apiInstance.stopTalk(uuid, (error, data, response) => {
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

[**StopTalkResponse**](StopTalkResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

