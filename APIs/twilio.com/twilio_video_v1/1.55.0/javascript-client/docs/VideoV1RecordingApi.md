# TwilioVideo.VideoV1RecordingApi

All URIs are relative to *https://video.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteRecording**](VideoV1RecordingApi.md#deleteRecording) | **DELETE** /v1/Recordings/{Sid} | 
[**fetchRecording**](VideoV1RecordingApi.md#fetchRecording) | **GET** /v1/Recordings/{Sid} | 
[**listRecording**](VideoV1RecordingApi.md#listRecording) | **GET** /v1/Recordings | 



## deleteRecording

> deleteRecording(sid)



Delete a Recording resource identified by a Recording SID.

### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1RecordingApi();
let sid = "sid_example"; // String | The SID of the Recording resource to delete.
apiInstance.deleteRecording(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Recording resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchRecording

> VideoV1Recording fetchRecording(sid)



Returns a single Recording resource identified by a Recording SID.

### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1RecordingApi();
let sid = "sid_example"; // String | The SID of the Recording resource to fetch.
apiInstance.fetchRecording(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Recording resource to fetch. | 

### Return type

[**VideoV1Recording**](VideoV1Recording.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listRecording

> ListRecordingResponse listRecording(opts)



List of all Track recordings.

### Example

```javascript
import TwilioVideo from 'twilio_video';
let defaultClient = TwilioVideo.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVideo.VideoV1RecordingApi();
let opts = {
  'status': "status_example", // RecordingEnumStatus | Read only the recordings that have this status. Can be: `processing`, `completed`, or `deleted`.
  'sourceSid': "sourceSid_example", // String | Read only the recordings that have this `source_sid`.
  'groupingSid': ["null"], // [String] | Read only recordings with this `grouping_sid`, which may include a `participant_sid` and/or a `room_sid`.
  'dateCreatedAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone.
  'dateCreatedBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | Read only recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone, given as `YYYY-MM-DDThh:mm:ss+|-hh:mm` or `YYYY-MM-DDThh:mm:ssZ`.
  'mediaType': "mediaType_example", // RecordingEnumType | Read only recordings that have this media type. Can be either `audio` or `video`.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listRecording(opts, (error, data, response) => {
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
 **status** | **RecordingEnumStatus**| Read only the recordings that have this status. Can be: &#x60;processing&#x60;, &#x60;completed&#x60;, or &#x60;deleted&#x60;. | [optional] 
 **sourceSid** | **String**| Read only the recordings that have this &#x60;source_sid&#x60;. | [optional] 
 **groupingSid** | [**[String]**](String.md)| Read only recordings with this &#x60;grouping_sid&#x60;, which may include a &#x60;participant_sid&#x60; and/or a &#x60;room_sid&#x60;. | [optional] 
 **dateCreatedAfter** | **Date**| Read only recordings that started on or after this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone. | [optional] 
 **dateCreatedBefore** | **Date**| Read only recordings that started before this [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date-time with time zone, given as &#x60;YYYY-MM-DDThh:mm:ss+|-hh:mm&#x60; or &#x60;YYYY-MM-DDThh:mm:ssZ&#x60;. | [optional] 
 **mediaType** | **RecordingEnumType**| Read only recordings that have this media type. Can be either &#x60;audio&#x60; or &#x60;video&#x60;. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListRecordingResponse**](ListRecordingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

