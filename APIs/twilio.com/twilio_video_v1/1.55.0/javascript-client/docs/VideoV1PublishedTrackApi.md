# TwilioVideo.VideoV1PublishedTrackApi

All URIs are relative to *https://video.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchRoomParticipantPublishedTrack**](VideoV1PublishedTrackApi.md#fetchRoomParticipantPublishedTrack) | **GET** /v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/PublishedTracks/{Sid} | 
[**listRoomParticipantPublishedTrack**](VideoV1PublishedTrackApi.md#listRoomParticipantPublishedTrack) | **GET** /v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/PublishedTracks | 



## fetchRoomParticipantPublishedTrack

> VideoV1RoomRoomParticipantRoomParticipantPublishedTrack fetchRoomParticipantPublishedTrack(roomSid, participantSid, sid)



Returns a single Track resource represented by TrackName or SID.

### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1PublishedTrackApi();
let roomSid = "roomSid_example"; // String | The SID of the Room resource where the Track resource to fetch is published.
let participantSid = "participantSid_example"; // String | The SID of the Participant resource with the published track to fetch.
let sid = "sid_example"; // String | The SID of the RoomParticipantPublishedTrack resource to fetch.
apiInstance.fetchRoomParticipantPublishedTrack(roomSid, participantSid, sid, (error, data, response) => {
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
 **roomSid** | **String**| The SID of the Room resource where the Track resource to fetch is published. | 
 **participantSid** | **String**| The SID of the Participant resource with the published track to fetch. | 
 **sid** | **String**| The SID of the RoomParticipantPublishedTrack resource to fetch. | 

### Return type

[**VideoV1RoomRoomParticipantRoomParticipantPublishedTrack**](VideoV1RoomRoomParticipantRoomParticipantPublishedTrack.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRoomParticipantPublishedTrack

> ListRoomParticipantPublishedTrackResponse listRoomParticipantPublishedTrack(roomSid, participantSid, opts)



Returns a list of tracks associated with a given Participant. Only &#x60;currently&#x60; Published Tracks are in the list resource.

### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1PublishedTrackApi();
let roomSid = "roomSid_example"; // String | The SID of the Room resource where the Track resources to read are published.
let participantSid = "participantSid_example"; // String | The SID of the Participant resource with the published tracks to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listRoomParticipantPublishedTrack(roomSid, participantSid, opts, (error, data, response) => {
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
 **roomSid** | **String**| The SID of the Room resource where the Track resources to read are published. | 
 **participantSid** | **String**| The SID of the Participant resource with the published tracks to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListRoomParticipantPublishedTrackResponse**](ListRoomParticipantPublishedTrackResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

