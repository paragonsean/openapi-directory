# TwilioIntelligence.IntelligenceV2TranscriptApi

All URIs are relative to *https://intelligence.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTranscript**](IntelligenceV2TranscriptApi.md#createTranscript) | **POST** /v2/Transcripts | 
[**deleteTranscript**](IntelligenceV2TranscriptApi.md#deleteTranscript) | **DELETE** /v2/Transcripts/{Sid} | 
[**fetchTranscript**](IntelligenceV2TranscriptApi.md#fetchTranscript) | **GET** /v2/Transcripts/{Sid} | 
[**listTranscript**](IntelligenceV2TranscriptApi.md#listTranscript) | **GET** /v2/Transcripts | 



## createTranscript

> IntelligenceV2Transcript createTranscript(channel, serviceSid, opts)



Create a new Transcript for the service

### Example

```javascript
import TwilioIntelligence from 'twilio_intelligence';
let defaultClient = TwilioIntelligence.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIntelligence.IntelligenceV2TranscriptApi();
let channel = null; // Object | JSON object describing Media Channel including Source and Participants
let serviceSid = "serviceSid_example"; // String | The unique SID identifier of the Service.
let opts = {
  'customerKey': "customerKey_example", // String | Used to store client provided metadata. Maximum of 64 double-byte UTF8 characters.
  'mediaStartTime': new Date("2013-10-20T19:20:30+01:00") // Date | The date that this Transcript's media was started, given in ISO 8601 format.
};
apiInstance.createTranscript(channel, serviceSid, opts, (error, data, response) => {
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
 **channel** | [**Object**](Object.md)| JSON object describing Media Channel including Source and Participants | 
 **serviceSid** | **String**| The unique SID identifier of the Service. | 
 **customerKey** | **String**| Used to store client provided metadata. Maximum of 64 double-byte UTF8 characters. | [optional] 
 **mediaStartTime** | **Date**| The date that this Transcript&#39;s media was started, given in ISO 8601 format. | [optional] 

### Return type

[**IntelligenceV2Transcript**](IntelligenceV2Transcript.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteTranscript

> deleteTranscript(sid)



Delete a specific Transcript.

### Example

```javascript
import TwilioIntelligence from 'twilio_intelligence';
let defaultClient = TwilioIntelligence.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIntelligence.IntelligenceV2TranscriptApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this Transcript.
apiInstance.deleteTranscript(sid, (error, data, response) => {
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
 **sid** | **String**| A 34 character string that uniquely identifies this Transcript. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchTranscript

> IntelligenceV2Transcript fetchTranscript(sid)



Fetch a specific Transcript.

### Example

```javascript
import TwilioIntelligence from 'twilio_intelligence';
let defaultClient = TwilioIntelligence.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIntelligence.IntelligenceV2TranscriptApi();
let sid = "sid_example"; // String | A 34 character string that uniquely identifies this Transcript.
apiInstance.fetchTranscript(sid, (error, data, response) => {
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
 **sid** | **String**| A 34 character string that uniquely identifies this Transcript. | 

### Return type

[**IntelligenceV2Transcript**](IntelligenceV2Transcript.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTranscript

> ListTranscriptResponse listTranscript(opts)



Retrieve a list of Transcripts for a given service.

### Example

```javascript
import TwilioIntelligence from 'twilio_intelligence';
let defaultClient = TwilioIntelligence.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIntelligence.IntelligenceV2TranscriptApi();
let opts = {
  'serviceSid': "serviceSid_example", // String | The unique SID identifier of the Service.
  'beforeStartTime': "beforeStartTime_example", // String | Filter by before StartTime.
  'afterStartTime': "afterStartTime_example", // String | Filter by after StartTime.
  'beforeDateCreated': "beforeDateCreated_example", // String | Filter by before DateCreated.
  'afterDateCreated': "afterDateCreated_example", // String | Filter by after DateCreated.
  'status': "status_example", // String | Filter by status.
  'languageCode': "languageCode_example", // String | Filter by Language Code.
  'sourceSid': "sourceSid_example", // String | Filter by SourceSid.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listTranscript(opts, (error, data, response) => {
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
 **serviceSid** | **String**| The unique SID identifier of the Service. | [optional] 
 **beforeStartTime** | **String**| Filter by before StartTime. | [optional] 
 **afterStartTime** | **String**| Filter by after StartTime. | [optional] 
 **beforeDateCreated** | **String**| Filter by before DateCreated. | [optional] 
 **afterDateCreated** | **String**| Filter by after DateCreated. | [optional] 
 **status** | **String**| Filter by status. | [optional] 
 **languageCode** | **String**| Filter by Language Code. | [optional] 
 **sourceSid** | **String**| Filter by SourceSid. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListTranscriptResponse**](ListTranscriptResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

