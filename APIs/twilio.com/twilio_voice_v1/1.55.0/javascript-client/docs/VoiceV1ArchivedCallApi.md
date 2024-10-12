# TwilioVoice.VoiceV1ArchivedCallApi

All URIs are relative to *https://voice.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteArchivedCall**](VoiceV1ArchivedCallApi.md#deleteArchivedCall) | **DELETE** /v1/Archives/{Date}/Calls/{Sid} | 



## deleteArchivedCall

> deleteArchivedCall(date, sid)



Delete an archived call record from Bulk Export. Note: this does not also delete the record from the Voice API.

### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1ArchivedCallApi();
let date = new Date("2013-10-20"); // Date | The date of the Call in UTC.
let sid = "sid_example"; // String | The Twilio-provided Call SID that uniquely identifies the Call resource to delete
apiInstance.deleteArchivedCall(date, sid, (error, data, response) => {
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
 **date** | **Date**| The date of the Call in UTC. | 
 **sid** | **String**| The Twilio-provided Call SID that uniquely identifies the Call resource to delete | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

