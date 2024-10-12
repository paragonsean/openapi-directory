# TwilioVideo.VideoV1SubscribedTrackApi

All URIs are relative to *https://video.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchRoomParticipantSubscribedTrack**](VideoV1SubscribedTrackApi.md#fetchRoomParticipantSubscribedTrack) | **GET** /v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/SubscribedTracks/{Sid} | 
[**listRoomParticipantSubscribedTrack**](VideoV1SubscribedTrackApi.md#listRoomParticipantSubscribedTrack) | **GET** /v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/SubscribedTracks | 



## fetchRoomParticipantSubscribedTrack

> VideoV1RoomRoomParticipantRoomParticipantSubscribedTrack fetchRoomParticipantSubscribedTrack(roomSid, participantSid, sid)



Returns a single Track resource represented by &#x60;track_sid&#x60;.  Note: This is one resource with the Video API that requires a SID, be Track Name on the subscriber side is not guaranteed to be unique.

### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1SubscribedTrackApi();
let roomSid = "roomSid_example"; // String | The SID of the Room where the Track resource to fetch is subscribed.
let participantSid = "participantSid_example"; // String | The SID of the participant that subscribes to the Track resource to fetch.
let sid = "sid_example"; // String | The SID of the RoomParticipantSubscribedTrack resource to fetch.
apiInstance.fetchRoomParticipantSubscribedTrack(roomSid, participantSid, sid, (error, data, response) => {
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
 **roomSid** | **String**| The SID of the Room where the Track resource to fetch is subscribed. | 
 **participantSid** | **String**| The SID of the participant that subscribes to the Track resource to fetch. | 
 **sid** | **String**| The SID of the RoomParticipantSubscribedTrack resource to fetch. | 

### Return type

[**VideoV1RoomRoomParticipantRoomParticipantSubscribedTrack**](VideoV1RoomRoomParticipantRoomParticipantSubscribedTrack.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRoomParticipantSubscribedTrack

> ListRoomParticipantSubscribedTrackResponse listRoomParticipantSubscribedTrack(roomSid, participantSid, opts)



Returns a list of tracks that are subscribed for the participant.

### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1SubscribedTrackApi();
let roomSid = "roomSid_example"; // String | The SID of the Room resource with the Track resources to read.
let participantSid = "participantSid_example"; // String | The SID of the participant that subscribes to the Track resources to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listRoomParticipantSubscribedTrack(roomSid, participantSid, opts, (error, data, response) => {
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
 **roomSid** | **String**| The SID of the Room resource with the Track resources to read. | 
 **participantSid** | **String**| The SID of the participant that subscribes to the Track resources to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListRoomParticipantSubscribedTrackResponse**](ListRoomParticipantSubscribedTrackResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

