# TwilioIntelligence.IntelligenceV2OperatorResultApi

All URIs are relative to *https://intelligence.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchOperatorResult**](IntelligenceV2OperatorResultApi.md#fetchOperatorResult) | **GET** /v2/Transcripts/{TranscriptSid}/OperatorResults/{OperatorSid} | 
[**listOperatorResult**](IntelligenceV2OperatorResultApi.md#listOperatorResult) | **GET** /v2/Transcripts/{TranscriptSid}/OperatorResults | 



## fetchOperatorResult

> IntelligenceV2TranscriptOperatorResult fetchOperatorResult(transcriptSid, operatorSid, opts)



Fetch a specific Operator Result for the given Transcript.

### Example

```javascript
import TwilioIntelligence from 'twilio_intelligence';
let defaultClient = TwilioIntelligence.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIntelligence.IntelligenceV2OperatorResultApi();
let transcriptSid = "transcriptSid_example"; // String | A 34 character string that uniquely identifies this Transcript.
let operatorSid = "operatorSid_example"; // String | A 34 character string that identifies this Language Understanding operator sid.
let opts = {
  'redacted': true // Boolean | Grant access to PII redacted/unredacted Language Understanding operator. If redaction is enabled, the default is True.
};
apiInstance.fetchOperatorResult(transcriptSid, operatorSid, opts, (error, data, response) => {
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
 **transcriptSid** | **String**| A 34 character string that uniquely identifies this Transcript. | 
 **operatorSid** | **String**| A 34 character string that identifies this Language Understanding operator sid. | 
 **redacted** | **Boolean**| Grant access to PII redacted/unredacted Language Understanding operator. If redaction is enabled, the default is True. | [optional] 

### Return type

[**IntelligenceV2TranscriptOperatorResult**](IntelligenceV2TranscriptOperatorResult.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listOperatorResult

> ListOperatorResultResponse listOperatorResult(transcriptSid, opts)



Retrieve a list of Operator Results for the given Transcript.

### Example

```javascript
import TwilioIntelligence from 'twilio_intelligence';
let defaultClient = TwilioIntelligence.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIntelligence.IntelligenceV2OperatorResultApi();
let transcriptSid = "transcriptSid_example"; // String | A 34 character string that uniquely identifies this Transcript.
let opts = {
  'redacted': true, // Boolean | Grant access to PII redacted/unredacted Language Understanding operator. If redaction is enabled, the default is True.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listOperatorResult(transcriptSid, opts, (error, data, response) => {
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
 **transcriptSid** | **String**| A 34 character string that uniquely identifies this Transcript. | 
 **redacted** | **Boolean**| Grant access to PII redacted/unredacted Language Understanding operator. If redaction is enabled, the default is True. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListOperatorResultResponse**](ListOperatorResultResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

