# TwilioMedia.MediaV1PlaybackGrantApi

All URIs are relative to *https://media.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createPlayerStreamerPlaybackGrant**](MediaV1PlaybackGrantApi.md#createPlayerStreamerPlaybackGrant) | **POST** /v1/PlayerStreamers/{Sid}/PlaybackGrant | 
[**fetchPlayerStreamerPlaybackGrant**](MediaV1PlaybackGrantApi.md#fetchPlayerStreamerPlaybackGrant) | **GET** /v1/PlayerStreamers/{Sid}/PlaybackGrant | 



## createPlayerStreamerPlaybackGrant

> MediaV1PlayerStreamerPlayerStreamerPlaybackGrant createPlayerStreamerPlaybackGrant(sid, opts)





### Example

```javascript
import TwilioMedia from 'twilio_media';
let defaultClient = TwilioMedia.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMedia.MediaV1PlaybackGrantApi();
let sid = "sid_example"; // String | The unique string generated to identify the PlayerStreamer resource associated with this PlaybackGrant
let opts = {
  'accessControlAllowOrigin': "accessControlAllowOrigin_example", // String | The full origin URL where the livestream can be streamed. If this is not provided, it can be streamed from any domain.
  'ttl': 56 // Number | The time to live of the PlaybackGrant. Default value is 15 seconds. Maximum value is 60 seconds.
};
apiInstance.createPlayerStreamerPlaybackGrant(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The unique string generated to identify the PlayerStreamer resource associated with this PlaybackGrant | 
 **accessControlAllowOrigin** | **String**| The full origin URL where the livestream can be streamed. If this is not provided, it can be streamed from any domain. | [optional] 
 **ttl** | **Number**| The time to live of the PlaybackGrant. Default value is 15 seconds. Maximum value is 60 seconds. | [optional] 

### Return type

[**MediaV1PlayerStreamerPlayerStreamerPlaybackGrant**](MediaV1PlayerStreamerPlayerStreamerPlaybackGrant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## fetchPlayerStreamerPlaybackGrant

> MediaV1PlayerStreamerPlayerStreamerPlaybackGrant fetchPlayerStreamerPlaybackGrant(sid)



**This method is not enabled.** Returns a single PlaybackGrant resource identified by a SID.

### Example

```javascript
import TwilioMedia from 'twilio_media';
let defaultClient = TwilioMedia.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMedia.MediaV1PlaybackGrantApi();
let sid = "sid_example"; // String | The SID of the PlayerStreamer resource to fetch.
apiInstance.fetchPlayerStreamerPlaybackGrant(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the PlayerStreamer resource to fetch. | 

### Return type

[**MediaV1PlayerStreamerPlayerStreamerPlaybackGrant**](MediaV1PlayerStreamerPlayerStreamerPlaybackGrant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

