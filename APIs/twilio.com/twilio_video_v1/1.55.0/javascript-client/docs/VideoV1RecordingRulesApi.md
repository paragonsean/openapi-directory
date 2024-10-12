# TwilioVideo.VideoV1RecordingRulesApi

All URIs are relative to *https://video.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchRoomRecordingRule**](VideoV1RecordingRulesApi.md#fetchRoomRecordingRule) | **GET** /v1/Rooms/{RoomSid}/RecordingRules | 
[**updateRoomRecordingRule**](VideoV1RecordingRulesApi.md#updateRoomRecordingRule) | **POST** /v1/Rooms/{RoomSid}/RecordingRules | 



## fetchRoomRecordingRule

> VideoV1RoomRoomRecordingRule fetchRoomRecordingRule(roomSid)



Returns a list of Recording Rules for the Room.

### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1RecordingRulesApi();
let roomSid = "roomSid_example"; // String | The SID of the Room resource where the recording rules to fetch apply.
apiInstance.fetchRoomRecordingRule(roomSid, (error, data, response) => {
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
 **roomSid** | **String**| The SID of the Room resource where the recording rules to fetch apply. | 

### Return type

[**VideoV1RoomRoomRecordingRule**](VideoV1RoomRoomRecordingRule.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateRoomRecordingRule

> VideoV1RoomRoomRecordingRule updateRoomRecordingRule(roomSid, opts)



Update the Recording Rules for the Room

### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1RecordingRulesApi();
let roomSid = "roomSid_example"; // String | The SID of the Room resource where the recording rules to update apply.
let opts = {
  'rules': null // Object | A JSON-encoded array of recording rules.
};
apiInstance.updateRoomRecordingRule(roomSid, opts, (error, data, response) => {
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
 **roomSid** | **String**| The SID of the Room resource where the recording rules to update apply. | 
 **rules** | [**Object**](Object.md)| A JSON-encoded array of recording rules. | [optional] 

### Return type

[**VideoV1RoomRoomRecordingRule**](VideoV1RoomRoomRecordingRule.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

