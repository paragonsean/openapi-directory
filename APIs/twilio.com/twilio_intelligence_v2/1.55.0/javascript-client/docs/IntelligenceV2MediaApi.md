# TwilioIntelligence.IntelligenceV2MediaApi

All URIs are relative to *https://intelligence.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchMedia**](IntelligenceV2MediaApi.md#fetchMedia) | **GET** /v2/Transcripts/{Sid}/Media | 



## fetchMedia

> IntelligenceV2TranscriptMedia fetchMedia(sid, opts)



Get download URLs for media if possible

### Example

```javascript
import TwilioIntelligence from 'twilio_intelligence';
let defaultClient = TwilioIntelligence.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioIntelligence.IntelligenceV2MediaApi();
let sid = "sid_example"; // String | The unique SID identifier of the Transcript.
let opts = {
  'redacted': true // Boolean | Grant access to PII Redacted/Unredacted Media. If redaction is enabled, the default is `true` to access redacted media.
};
apiInstance.fetchMedia(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The unique SID identifier of the Transcript. | 
 **redacted** | **Boolean**| Grant access to PII Redacted/Unredacted Media. If redaction is enabled, the default is &#x60;true&#x60; to access redacted media. | [optional] 

### Return type

[**IntelligenceV2TranscriptMedia**](IntelligenceV2TranscriptMedia.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

