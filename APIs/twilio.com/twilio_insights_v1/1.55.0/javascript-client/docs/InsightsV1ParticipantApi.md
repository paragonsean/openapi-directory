# TwilioInsights.InsightsV1ParticipantApi

All URIs are relative to *https://insights.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchVideoParticipantSummary**](InsightsV1ParticipantApi.md#fetchVideoParticipantSummary) | **GET** /v1/Video/Rooms/{RoomSid}/Participants/{ParticipantSid} | 
[**listVideoParticipantSummary**](InsightsV1ParticipantApi.md#listVideoParticipantSummary) | **GET** /v1/Video/Rooms/{RoomSid}/Participants | 



## fetchVideoParticipantSummary

> InsightsV1VideoRoomSummaryVideoParticipantSummary fetchVideoParticipantSummary(roomSid, participantSid)



Get Video Log Analyzer data for a Room Participant.

### Example

```javascript
import TwilioInsights from 'twilio_insights';
let defaultClient = TwilioInsights.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioInsights.InsightsV1ParticipantApi();
let roomSid = "roomSid_example"; // String | The SID of the Room resource.
let participantSid = "participantSid_example"; // String | The SID of the Participant resource.
apiInstance.fetchVideoParticipantSummary(roomSid, participantSid, (error, data, response) => {
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
 **roomSid** | **String**| The SID of the Room resource. | 
 **participantSid** | **String**| The SID of the Participant resource. | 

### Return type

[**InsightsV1VideoRoomSummaryVideoParticipantSummary**](InsightsV1VideoRoomSummaryVideoParticipantSummary.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listVideoParticipantSummary

> ListVideoParticipantSummaryResponse listVideoParticipantSummary(roomSid, opts)



Get a list of room participants.

### Example

```javascript
import TwilioInsights from 'twilio_insights';
let defaultClient = TwilioInsights.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioInsights.InsightsV1ParticipantApi();
let roomSid = "roomSid_example"; // String | The SID of the Room resource.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listVideoParticipantSummary(roomSid, opts, (error, data, response) => {
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
 **roomSid** | **String**| The SID of the Room resource. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListVideoParticipantSummaryResponse**](ListVideoParticipantSummaryResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

