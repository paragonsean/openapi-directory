# TwilioVideo.VideoV1RoomRecordingApi

All URIs are relative to *https://video.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteRoomRecording**](VideoV1RoomRecordingApi.md#deleteRoomRecording) | **DELETE** /v1/Rooms/{RoomSid}/Recordings/{Sid} | 
[**fetchRoomRecording**](VideoV1RoomRecordingApi.md#fetchRoomRecording) | **GET** /v1/Rooms/{RoomSid}/Recordings/{Sid} | 
[**listRoomRecording**](VideoV1RoomRecordingApi.md#listRoomRecording) | **GET** /v1/Rooms/{RoomSid}/Recordings | 



## deleteRoomRecording

> deleteRoomRecording(roomSid, sid)





### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1RoomRecordingApi();
let roomSid = "roomSid_example"; // String | The SID of the room with the RoomRecording resource to delete.
let sid = "sid_example"; // String | The SID of the RoomRecording resource to delete.
apiInstance.deleteRoomRecording(roomSid, sid, (error, data, response) => {
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
 **roomSid** | **String**| The SID of the room with the RoomRecording resource to delete. | 
 **sid** | **String**| The SID of the RoomRecording resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchRoomRecording

> VideoV1RoomRoomRecording fetchRoomRecording(roomSid, sid)





### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1RoomRecordingApi();
let roomSid = "roomSid_example"; // String | The SID of the Room resource with the recording to fetch.
let sid = "sid_example"; // String | The SID of the RoomRecording resource to fetch.
apiInstance.fetchRoomRecording(roomSid, sid, (error, data, response) => {
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
 **roomSid** | **String**| The SID of the Room resource with the recording to fetch. | 
 **sid** | **String**| The SID of the RoomRecording resource to fetch. | 

### Return type

[**VideoV1RoomRoomRecording**](VideoV1RoomRoomRecording.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRoomRecording

> ListRoomRecordingResponse listRoomRecording(roomSid, opts)





### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1RoomRecordingApi();
let roomSid = "roomSid_example"; // String | The SID of the room with the RoomRecording resources to read.
let opts = {
  'status': "status_example", // RoomRecordingEnumStatus | Read only the recordings with this status. Can be: `processing`, `completed`, or `deleted`.
  'sourceSid': "sourceSid_example", // String | Read only the recordings that have this `source_sid`.
  'dateCreatedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
  'dateCreatedBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Read only Recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listRoomRecording(roomSid, opts, (error, data, response) => {
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
 **roomSid** | **String**| The SID of the room with the RoomRecording resources to read. | 
 **status** | **RoomRecordingEnumStatus**| Read only the recordings with this status. Can be: &#x60;processing&#x60;, &#x60;completed&#x60;, or &#x60;deleted&#x60;. | [optional] 
 **sourceSid** | **String**| Read only the recordings that have this &#x60;source_sid&#x60;. | [optional] 
 **dateCreatedAfter** | **Date**| Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone. | [optional] 
 **dateCreatedBefore** | **Date**| Read only Recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) datetime with time zone. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListRoomRecordingResponse**](ListRoomRecordingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

