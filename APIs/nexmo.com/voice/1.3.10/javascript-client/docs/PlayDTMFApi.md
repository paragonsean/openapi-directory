# VoiceApi.PlayDTMFApi

All URIs are relative to *https://api.nexmo.com/v1/calls*

Method | HTTP request | Description
------------- | ------------- | -------------
[**startDTMF**](PlayDTMFApi.md#startDTMF) | **PUT** /{uuid}/dtmf | Play DTMF tones into a call



## startDTMF

> DTMFResponse startDTMF(uuid, dTMFRequest)

Play DTMF tones into a call

Play DTMF tones into a call

### Example

```javascript
import VoiceApi from 'voice_api';
let defaultClient = VoiceApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new VoiceApi.PlayDTMFApi();
let uuid = "63f61863-4a51-4f6b-86e1-46edebcf9356"; // String | UUID of the Call Leg
let dTMFRequest = new VoiceApi.DTMFRequest(); // DTMFRequest | action to perform
apiInstance.startDTMF(uuid, dTMFRequest, (error, data, response) => {
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
 **dTMFRequest** | [**DTMFRequest**](DTMFRequest.md)| action to perform | 

### Return type

[**DTMFResponse**](DTMFResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

