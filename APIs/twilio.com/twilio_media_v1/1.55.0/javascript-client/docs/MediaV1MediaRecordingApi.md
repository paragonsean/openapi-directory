# TwilioMedia.MediaV1MediaRecordingApi

All URIs are relative to *https://media.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteMediaRecording**](MediaV1MediaRecordingApi.md#deleteMediaRecording) | **DELETE** /v1/MediaRecordings/{Sid} | 
[**fetchMediaRecording**](MediaV1MediaRecordingApi.md#fetchMediaRecording) | **GET** /v1/MediaRecordings/{Sid} | 
[**listMediaRecording**](MediaV1MediaRecordingApi.md#listMediaRecording) | **GET** /v1/MediaRecordings | 



## deleteMediaRecording

> deleteMediaRecording(sid)



Deletes a MediaRecording resource identified by a SID.

### Example

```javascript
import TwilioMedia from 'twilio_media';
let defaultClient = TwilioMedia.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMedia.MediaV1MediaRecordingApi();
let sid = "sid_example"; // String | The SID of the MediaRecording resource to delete.
apiInstance.deleteMediaRecording(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the MediaRecording resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchMediaRecording

> MediaV1MediaRecording fetchMediaRecording(sid)



Returns a single MediaRecording resource identified by a SID.

### Example

```javascript
import TwilioMedia from 'twilio_media';
let defaultClient = TwilioMedia.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMedia.MediaV1MediaRecordingApi();
let sid = "sid_example"; // String | The SID of the MediaRecording resource to fetch.
apiInstance.fetchMediaRecording(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the MediaRecording resource to fetch. | 

### Return type

[**MediaV1MediaRecording**](MediaV1MediaRecording.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMediaRecording

> ListMediaRecordingResponse listMediaRecording(opts)



Returns a list of MediaRecordings.

### Example

```javascript
import TwilioMedia from 'twilio_media';
let defaultClient = TwilioMedia.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMedia.MediaV1MediaRecordingApi();
let opts = {
  'order': "order_example", // MediaRecordingEnumOrder | The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
  'status': "status_example", // MediaRecordingEnumStatus | Status to filter by, with possible values `processing`, `completed`, `deleted`, or `failed`.
  'processorSid': "processorSid_example", // String | SID of a MediaProcessor to filter by.
  'sourceSid': "sourceSid_example", // String | SID of a MediaRecording source to filter by.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listMediaRecording(opts, (error, data, response) => {
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
 **order** | **MediaRecordingEnumOrder**| The sort order of the list by &#x60;date_created&#x60;. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending) with &#x60;desc&#x60; as the default. | [optional] 
 **status** | **MediaRecordingEnumStatus**| Status to filter by, with possible values &#x60;processing&#x60;, &#x60;completed&#x60;, &#x60;deleted&#x60;, or &#x60;failed&#x60;. | [optional] 
 **processorSid** | **String**| SID of a MediaProcessor to filter by. | [optional] 
 **sourceSid** | **String**| SID of a MediaRecording source to filter by. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListMediaRecordingResponse**](ListMediaRecordingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

