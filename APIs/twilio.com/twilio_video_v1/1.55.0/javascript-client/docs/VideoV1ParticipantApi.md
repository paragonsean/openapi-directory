# TwilioVideo.VideoV1ParticipantApi

All URIs are relative to *https://video.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchRoomParticipant**](VideoV1ParticipantApi.md#fetchRoomParticipant) | **GET** /v1/Rooms/{RoomSid}/Participants/{Sid} | 
[**listRoomParticipant**](VideoV1ParticipantApi.md#listRoomParticipant) | **GET** /v1/Rooms/{RoomSid}/Participants | 
[**updateRoomParticipant**](VideoV1ParticipantApi.md#updateRoomParticipant) | **POST** /v1/Rooms/{RoomSid}/Participants/{Sid} | 



## fetchRoomParticipant

> VideoV1RoomRoomParticipant fetchRoomParticipant(roomSid, sid)





### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1ParticipantApi();
let roomSid = "roomSid_example"; // String | The SID of the room with the Participant resource to fetch.
let sid = "sid_example"; // String | The SID of the RoomParticipant resource to fetch.
apiInstance.fetchRoomParticipant(roomSid, sid, (error, data, response) => {
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
 **roomSid** | **String**| The SID of the room with the Participant resource to fetch. | 
 **sid** | **String**| The SID of the RoomParticipant resource to fetch. | 

### Return type

[**VideoV1RoomRoomParticipant**](VideoV1RoomRoomParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRoomParticipant

> ListRoomParticipantResponse listRoomParticipant(roomSid, opts)





### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1ParticipantApi();
let roomSid = "roomSid_example"; // String | The SID of the room with the Participant resources to read.
let opts = {
  'status': "status_example", // RoomParticipantEnumStatus | Read only the participants with this status. Can be: `connected` or `disconnected`. For `in-progress` Rooms the default Status is `connected`, for `completed` Rooms only `disconnected` Participants are returned.
  'identity': "identity_example", // String | Read only the Participants with this [User](https://www.twilio.com/docs/chat/rest/user-resource) `identity` value.
  'dateCreatedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Read only Participants that started after this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
  'dateCreatedBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Read only Participants that started before this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listRoomParticipant(roomSid, opts, (error, data, response) => {
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
 **roomSid** | **String**| The SID of the room with the Participant resources to read. | 
 **status** | **RoomParticipantEnumStatus**| Read only the participants with this status. Can be: &#x60;connected&#x60; or &#x60;disconnected&#x60;. For &#x60;in-progress&#x60; Rooms the default Status is &#x60;connected&#x60;, for &#x60;completed&#x60; Rooms only &#x60;disconnected&#x60; Participants are returned. | [optional] 
 **identity** | **String**| Read only the Participants with this [User](https://www.twilio.com/docs/chat/rest/user-resource) &#x60;identity&#x60; value. | [optional] 
 **dateCreatedAfter** | **Date**| Read only Participants that started after this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format. | [optional] 
 **dateCreatedBefore** | **Date**| Read only Participants that started before this date in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#UTC) format. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListRoomParticipantResponse**](ListRoomParticipantResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateRoomParticipant

> VideoV1RoomRoomParticipant updateRoomParticipant(roomSid, sid, opts)





### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1ParticipantApi();
let roomSid = "roomSid_example"; // String | The SID of the room with the participant to update.
let sid = "sid_example"; // String | The SID of the RoomParticipant resource to update.
let opts = {
  'status': "status_example" // RoomParticipantEnumStatus | 
};
apiInstance.updateRoomParticipant(roomSid, sid, opts, (error, data, response) => {
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
 **status** | **RoomParticipantEnumStatus**|  | [optional] 

### Return type

[**VideoV1RoomRoomParticipant**](VideoV1RoomRoomParticipant.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

