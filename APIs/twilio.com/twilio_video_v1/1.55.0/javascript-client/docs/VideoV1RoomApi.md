# TwilioVideo.VideoV1RoomApi

All URIs are relative to *https://video.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createRoom**](VideoV1RoomApi.md#createRoom) | **POST** /v1/Rooms | 
[**fetchRoom**](VideoV1RoomApi.md#fetchRoom) | **GET** /v1/Rooms/{Sid} | 
[**listRoom**](VideoV1RoomApi.md#listRoom) | **GET** /v1/Rooms | 
[**updateRoom**](VideoV1RoomApi.md#updateRoom) | **POST** /v1/Rooms/{Sid} | 



## createRoom

> VideoV1Room createRoom(opts)





### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1RoomApi();
let opts = {
  'audioOnly': true, // Boolean | When set to true, indicates that the participants in the room will only publish audio. No video tracks will be allowed. Group rooms only.
  'emptyRoomTimeout': 56, // Number | Configures how long (in minutes) a room will remain active after last participant leaves. Valid values range from 1 to 60 minutes (no fractions).
  'enableTurn': true, // Boolean | Deprecated, now always considered to be true.
  'largeRoom': true, // Boolean | When set to true, indicated that this is the large room.
  'maxParticipantDuration': 56, // Number | The maximum number of seconds a Participant can be connected to the room. The maximum possible value is 86400 seconds (24 hours). The default is 14400 seconds (4 hours).
  'maxParticipants': 56, // Number | The maximum number of concurrent Participants allowed in the room. Peer-to-peer rooms can have up to 10 Participants. Small Group rooms can have up to 4 Participants. Group rooms can have up to 50 Participants.
  'mediaRegion': "mediaRegion_example", // String | The region for the media server in Group Rooms.  Can be: one of the [available Media Regions](https://www.twilio.com/docs/video/ip-addresses#group-rooms-media-servers). ***This feature is not available in `peer-to-peer` rooms.***
  'recordParticipantsOnConnect': true, // Boolean | Whether to start recording when Participants connect. ***This feature is not available in `peer-to-peer` rooms.***
  'recordingRules': null, // Object | A collection of Recording Rules that describe how to include or exclude matching tracks for recording
  'statusCallback': "statusCallback_example", // String | The URL we should call using the `status_callback_method` to send status information to your application on every room event. See [Status Callbacks](https://www.twilio.com/docs/video/api/status-callbacks) for more info.
  'statusCallbackMethod': "statusCallbackMethod_example", // String | The HTTP method we should use to call `status_callback`. Can be `POST` or `GET`.
  'type': "type_example", // RoomEnumRoomType | 
  'uniqueName': "uniqueName_example", // String | An application-defined string that uniquely identifies the resource. It can be used as a `room_sid` in place of the resource's `sid` in the URL to address the resource, assuming it does not contain any [reserved characters](https://tools.ietf.org/html/rfc3986#section-2.2) that would need to be URL encoded. This value is unique for `in-progress` rooms. SDK clients can use this name to connect to the room. REST API clients can use this name in place of the Room SID to interact with the room as long as the room is `in-progress`.
  'unusedRoomTimeout': 56, // Number | Configures how long (in minutes) a room will remain active if no one joins. Valid values range from 1 to 60 minutes (no fractions).
  'videoCodecs': ["null"] // [RoomEnumVideoCodec] | An array of the video codecs that are supported when publishing a track in the room.  Can be: `VP8` and `H264`.  ***This feature is not available in `peer-to-peer` rooms***
};
apiInstance.createRoom(opts, (error, data, response) => {
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
 **audioOnly** | **Boolean**| When set to true, indicates that the participants in the room will only publish audio. No video tracks will be allowed. Group rooms only. | [optional] 
 **emptyRoomTimeout** | **Number**| Configures how long (in minutes) a room will remain active after last participant leaves. Valid values range from 1 to 60 minutes (no fractions). | [optional] 
 **enableTurn** | **Boolean**| Deprecated, now always considered to be true. | [optional] 
 **largeRoom** | **Boolean**| When set to true, indicated that this is the large room. | [optional] 
 **maxParticipantDuration** | **Number**| The maximum number of seconds a Participant can be connected to the room. The maximum possible value is 86400 seconds (24 hours). The default is 14400 seconds (4 hours). | [optional] 
 **maxParticipants** | **Number**| The maximum number of concurrent Participants allowed in the room. Peer-to-peer rooms can have up to 10 Participants. Small Group rooms can have up to 4 Participants. Group rooms can have up to 50 Participants. | [optional] 
 **mediaRegion** | **String**| The region for the media server in Group Rooms.  Can be: one of the [available Media Regions](https://www.twilio.com/docs/video/ip-addresses#group-rooms-media-servers). ***This feature is not available in &#x60;peer-to-peer&#x60; rooms.*** | [optional] 
 **recordParticipantsOnConnect** | **Boolean**| Whether to start recording when Participants connect. ***This feature is not available in &#x60;peer-to-peer&#x60; rooms.*** | [optional] 
 **recordingRules** | [**Object**](Object.md)| A collection of Recording Rules that describe how to include or exclude matching tracks for recording | [optional] 
 **statusCallback** | **String**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application on every room event. See [Status Callbacks](https://www.twilio.com/docs/video/api/status-callbacks) for more info. | [optional] 
 **statusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be &#x60;POST&#x60; or &#x60;GET&#x60;. | [optional] 
 **type** | **RoomEnumRoomType**|  | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used as a &#x60;room_sid&#x60; in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource, assuming it does not contain any [reserved characters](https://tools.ietf.org/html/rfc3986#section-2.2) that would need to be URL encoded. This value is unique for &#x60;in-progress&#x60; rooms. SDK clients can use this name to connect to the room. REST API clients can use this name in place of the Room SID to interact with the room as long as the room is &#x60;in-progress&#x60;. | [optional] 
 **unusedRoomTimeout** | **Number**| Configures how long (in minutes) a room will remain active if no one joins. Valid values range from 1 to 60 minutes (no fractions). | [optional] 
 **videoCodecs** | [**[RoomEnumVideoCodec]**](RoomEnumVideoCodec.md)| An array of the video codecs that are supported when publishing a track in the room.  Can be: &#x60;VP8&#x60; and &#x60;H264&#x60;.  ***This feature is not available in &#x60;peer-to-peer&#x60; rooms*** | [optional] 

### Return type

[**VideoV1Room**](VideoV1Room.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## fetchRoom

> VideoV1Room fetchRoom(sid)





### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1RoomApi();
let sid = "sid_example"; // String | The SID of the Room resource to fetch.
apiInstance.fetchRoom(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Room resource to fetch. | 

### Return type

[**VideoV1Room**](VideoV1Room.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRoom

> ListRoomResponse listRoom(opts)





### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1RoomApi();
let opts = {
  'status': "status_example", // RoomEnumRoomStatus | Read only the rooms with this status. Can be: `in-progress` (default) or `completed`
  'uniqueName': "uniqueName_example", // String | Read only rooms with the this `unique_name`.
  'dateCreatedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Read only rooms that started on or after this date, given as `YYYY-MM-DD`.
  'dateCreatedBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Read only rooms that started before this date, given as `YYYY-MM-DD`.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listRoom(opts, (error, data, response) => {
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
 **status** | **RoomEnumRoomStatus**| Read only the rooms with this status. Can be: &#x60;in-progress&#x60; (default) or &#x60;completed&#x60; | [optional] 
 **uniqueName** | **String**| Read only rooms with the this &#x60;unique_name&#x60;. | [optional] 
 **dateCreatedAfter** | **Date**| Read only rooms that started on or after this date, given as &#x60;YYYY-MM-DD&#x60;. | [optional] 
 **dateCreatedBefore** | **Date**| Read only rooms that started before this date, given as &#x60;YYYY-MM-DD&#x60;. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListRoomResponse**](ListRoomResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateRoom

> VideoV1Room updateRoom(sid, status)





### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1RoomApi();
let sid = "sid_example"; // String | The SID of the Room resource to update.
let status = "status_example"; // RoomEnumRoomStatus | 
apiInstance.updateRoom(sid, status, (error, data, response) => {
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
 **sid** | **String**| The SID of the Room resource to update. | 
 **status** | **RoomEnumRoomStatus**|  | 

### Return type

[**VideoV1Room**](VideoV1Room.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

