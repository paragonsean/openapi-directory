# TwilioInsights.InsightsV1RoomApi

All URIs are relative to *https://insights.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchVideoRoomSummary**](InsightsV1RoomApi.md#fetchVideoRoomSummary) | **GET** /v1/Video/Rooms/{RoomSid} | 
[**listVideoRoomSummary**](InsightsV1RoomApi.md#listVideoRoomSummary) | **GET** /v1/Video/Rooms | 



## fetchVideoRoomSummary

> InsightsV1VideoRoomSummary fetchVideoRoomSummary(roomSid)



Get Video Log Analyzer data for a Room.

### Example

```javascript
import TwilioInsights from 'twilio_insights';
let defaultClient = TwilioInsights.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioInsights.InsightsV1RoomApi();
let roomSid = "roomSid_example"; // String | The SID of the Room resource.
apiInstance.fetchVideoRoomSummary(roomSid, (error, data, response) => {
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

### Return type

[**InsightsV1VideoRoomSummary**](InsightsV1VideoRoomSummary.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listVideoRoomSummary

> ListVideoRoomSummaryResponse listVideoRoomSummary(opts)



Get a list of Programmable Video Rooms.

### Example

```javascript
import TwilioInsights from 'twilio_insights';
let defaultClient = TwilioInsights.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioInsights.InsightsV1RoomApi();
let opts = {
  'roomType': ["null"], // [VideoRoomSummaryEnumRoomType] | Type of room. Can be `go`, `peer_to_peer`, `group`, or `group_small`.
  'codec': ["null"], // [VideoRoomSummaryEnumCodec] | Codecs used by participants in the room. Can be `VP8`, `H264`, or `VP9`.
  'roomName': "roomName_example", // String | Room friendly name.
  'createdAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Only read rooms that started on or after this ISO 8601 timestamp.
  'createdBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Only read rooms that started before this ISO 8601 timestamp.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listVideoRoomSummary(opts, (error, data, response) => {
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
 **roomType** | [**[VideoRoomSummaryEnumRoomType]**](VideoRoomSummaryEnumRoomType.md)| Type of room. Can be &#x60;go&#x60;, &#x60;peer_to_peer&#x60;, &#x60;group&#x60;, or &#x60;group_small&#x60;. | [optional] 
 **codec** | [**[VideoRoomSummaryEnumCodec]**](VideoRoomSummaryEnumCodec.md)| Codecs used by participants in the room. Can be &#x60;VP8&#x60;, &#x60;H264&#x60;, or &#x60;VP9&#x60;. | [optional] 
 **roomName** | **String**| Room friendly name. | [optional] 
 **createdAfter** | **Date**| Only read rooms that started on or after this ISO 8601 timestamp. | [optional] 
 **createdBefore** | **Date**| Only read rooms that started before this ISO 8601 timestamp. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListVideoRoomSummaryResponse**](ListVideoRoomSummaryResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

