# TwilioVideo.VideoV1AnonymizeApi

All URIs are relative to *https://video.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**updateRoomParticipantAnonymize**](VideoV1AnonymizeApi.md#updateRoomParticipantAnonymize) | **POST** /v1/Rooms/{RoomSid}/Participants/{Sid}/Anonymize | 



## updateRoomParticipantAnonymize

> VideoV1RoomRoomParticipantRoomParticipantAnonymize updateRoomParticipantAnonymize(roomSid, sid)





### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1AnonymizeApi();
let roomSid = "roomSid_example"; // String | The SID of the room with the participant to update.
let sid = "sid_example"; // String | The SID of the RoomParticipant resource to update.
apiInstance.updateRoomParticipantAnonymize(roomSid, sid, (error, data, response) => {
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
 **roomSid** | **String**| The SID of the room with the participant to update. | 
 **sid** | **String**| The SID of the RoomParticipant resource to update. | 

### Return type

[**VideoV1RoomRoomParticipantRoomParticipantAnonymize**](VideoV1RoomRoomParticipantRoomParticipantAnonymize.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

