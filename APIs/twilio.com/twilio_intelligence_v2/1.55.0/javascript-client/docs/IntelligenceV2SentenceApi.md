# TwilioIntelligence.IntelligenceV2SentenceApi

All URIs are relative to *https://intelligence.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listSentence**](IntelligenceV2SentenceApi.md#listSentence) | **GET** /v2/Transcripts/{TranscriptSid}/Sentences | 



## listSentence

> ListSentenceResponse listSentence(transcriptSid, opts)



Get all Transcript Sentences by TranscriptSid

### Example

```javascript
import TwilioIntelligence from 'twilio_intelligence';
let defaultClient = TwilioIntelligence.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIntelligence.IntelligenceV2SentenceApi();
let transcriptSid = "transcriptSid_example"; // String | The unique SID identifier of the Transcript.
let opts = {
  'redacted': true, // Boolean | Grant access to PII Redacted/Unredacted Sentences. If redaction is enabled, the default is `true` to access redacted sentences.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSentence(transcriptSid, opts, (error, data, response) => {
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
 **transcriptSid** | **String**| The unique SID identifier of the Transcript. | 
 **redacted** | **Boolean**| Grant access to PII Redacted/Unredacted Sentences. If redaction is enabled, the default is &#x60;true&#x60; to access redacted sentences. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSentenceResponse**](ListSentenceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

