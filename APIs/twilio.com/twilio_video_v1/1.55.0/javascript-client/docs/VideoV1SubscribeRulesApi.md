# TwilioVideo.VideoV1SubscribeRulesApi

All URIs are relative to *https://video.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchRoomParticipantSubscribeRule**](VideoV1SubscribeRulesApi.md#fetchRoomParticipantSubscribeRule) | **GET** /v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/SubscribeRules | 
[**updateRoomParticipantSubscribeRule**](VideoV1SubscribeRulesApi.md#updateRoomParticipantSubscribeRule) | **POST** /v1/Rooms/{RoomSid}/Participants/{ParticipantSid}/SubscribeRules | 



## fetchRoomParticipantSubscribeRule

> VideoV1RoomRoomParticipantRoomParticipantSubscribeRule fetchRoomParticipantSubscribeRule(roomSid, participantSid)



Returns a list of Subscribe Rules for the Participant.

### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1SubscribeRulesApi();
let roomSid = "roomSid_example"; // String | The SID of the Room resource where the subscribe rules to fetch apply.
let participantSid = "participantSid_example"; // String | The SID of the Participant resource with the subscribe rules to fetch.
apiInstance.fetchRoomParticipantSubscribeRule(roomSid, participantSid, (error, data, response) => {
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
 **roomSid** | **String**| The SID of the Room resource where the subscribe rules to fetch apply. | 
 **participantSid** | **String**| The SID of the Participant resource with the subscribe rules to fetch. | 

### Return type

[**VideoV1RoomRoomParticipantRoomParticipantSubscribeRule**](VideoV1RoomRoomParticipantRoomParticipantSubscribeRule.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateRoomParticipantSubscribeRule

> VideoV1RoomRoomParticipantRoomParticipantSubscribeRule updateRoomParticipantSubscribeRule(roomSid, participantSid, opts)



Update the Subscribe Rules for the Participant

### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1SubscribeRulesApi();
let roomSid = "roomSid_example"; // String | The SID of the Room resource where the subscribe rules to update apply.
let participantSid = "participantSid_example"; // String | The SID of the Participant resource to update the Subscribe Rules.
let opts = {
  'rules': null // Object | A JSON-encoded array of subscribe rules. See the [Specifying Subscribe Rules](https://www.twilio.com/docs/video/api/track-subscriptions#specifying-sr) section for further information.
};
apiInstance.updateRoomParticipantSubscribeRule(roomSid, participantSid, opts, (error, data, response) => {
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
 **roomSid** | **String**| The SID of the Room resource where the subscribe rules to update apply. | 
 **participantSid** | **String**| The SID of the Participant resource to update the Subscribe Rules. | 
 **rules** | [**Object**](Object.md)| A JSON-encoded array of subscribe rules. See the [Specifying Subscribe Rules](https://www.twilio.com/docs/video/api/track-subscriptions#specifying-sr) section for further information. | [optional] 

### Return type

[**VideoV1RoomRoomParticipantRoomParticipantSubscribeRule**](VideoV1RoomRoomParticipantRoomParticipantSubscribeRule.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

