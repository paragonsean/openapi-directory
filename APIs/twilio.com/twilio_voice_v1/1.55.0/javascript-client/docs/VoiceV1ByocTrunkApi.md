# TwilioVoice.VoiceV1ByocTrunkApi

All URIs are relative to *https://voice.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createByocTrunk**](VoiceV1ByocTrunkApi.md#createByocTrunk) | **POST** /v1/ByocTrunks | 
[**deleteByocTrunk**](VoiceV1ByocTrunkApi.md#deleteByocTrunk) | **DELETE** /v1/ByocTrunks/{Sid} | 
[**fetchByocTrunk**](VoiceV1ByocTrunkApi.md#fetchByocTrunk) | **GET** /v1/ByocTrunks/{Sid} | 
[**listByocTrunk**](VoiceV1ByocTrunkApi.md#listByocTrunk) | **GET** /v1/ByocTrunks | 
[**updateByocTrunk**](VoiceV1ByocTrunkApi.md#updateByocTrunk) | **POST** /v1/ByocTrunks/{Sid} | 



## createByocTrunk

> VoiceV1ByocTrunk createByocTrunk(opts)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1ByocTrunkApi();
let opts = {
  'cnamLookupEnabled': true, // Boolean | Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
  'connectionPolicySid': "connectionPolicySid_example", // String | The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
  'fromDomainSid': "fromDomainSid_example", // String | The SID of the SIP Domain that should be used in the `From` header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to \\\"call back\\\" an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to \\\"sip.twilio.com\\\".
  'statusCallbackMethod': "statusCallbackMethod_example", // String | The HTTP method we should use to call `status_callback_url`. Can be: `GET` or `POST`.
  'statusCallbackUrl': "statusCallbackUrl_example", // String | The URL that we should call to pass status parameters (such as call ended) to your application.
  'voiceFallbackMethod': "voiceFallbackMethod_example", // String | The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
  'voiceFallbackUrl': "voiceFallbackUrl_example", // String | The URL that we should call when an error occurs while retrieving or executing the TwiML from `voice_url`.
  'voiceMethod': "voiceMethod_example", // String | The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`.
  'voiceUrl': "voiceUrl_example" // String | The URL we should call when the BYOC Trunk receives a call.
};
apiInstance.createByocTrunk(opts, (error, data, response) => {
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
 **cnamLookupEnabled** | **Boolean**| Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information. | [optional] 
 **connectionPolicySid** | **String**| The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long. | [optional] 
 **fromDomainSid** | **String**| The SID of the SIP Domain that should be used in the &#x60;From&#x60; header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to \\\&quot;call back\\\&quot; an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to \\\&quot;sip.twilio.com\\\&quot;. | [optional] 
 **statusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;status_callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **statusCallbackUrl** | **String**| The URL that we should call to pass status parameters (such as call ended) to your application. | [optional] 
 **voiceFallbackMethod** | **String**| The HTTP method we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **voiceFallbackUrl** | **String**| The URL that we should call when an error occurs while retrieving or executing the TwiML from &#x60;voice_url&#x60;. | [optional] 
 **voiceMethod** | **String**| The HTTP method we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **voiceUrl** | **String**| The URL we should call when the BYOC Trunk receives a call. | [optional] 

### Return type

[**VoiceV1ByocTrunk**](VoiceV1ByocTrunk.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteByocTrunk

> deleteByocTrunk(sid)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1ByocTrunkApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the BYOC Trunk resource to delete.
apiInstance.deleteByocTrunk(sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the BYOC Trunk resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchByocTrunk

> VoiceV1ByocTrunk fetchByocTrunk(sid)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1ByocTrunkApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the BYOC Trunk resource to fetch.
apiInstance.fetchByocTrunk(sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the BYOC Trunk resource to fetch. | 

### Return type

[**VoiceV1ByocTrunk**](VoiceV1ByocTrunk.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listByocTrunk

> ListByocTrunkResponse listByocTrunk(opts)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1ByocTrunkApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listByocTrunk(opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListByocTrunkResponse**](ListByocTrunkResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateByocTrunk

> VoiceV1ByocTrunk updateByocTrunk(sid, opts)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1ByocTrunkApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the BYOC Trunk resource to update.
let opts = {
  'cnamLookupEnabled': true, // Boolean | Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information.
  'connectionPolicySid': "connectionPolicySid_example", // String | The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
  'fromDomainSid': "fromDomainSid_example", // String | The SID of the SIP Domain that should be used in the `From` header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to \\\"call back\\\" an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to \\\"sip.twilio.com\\\".
  'statusCallbackMethod': "statusCallbackMethod_example", // String | The HTTP method we should use to call `status_callback_url`. Can be: `GET` or `POST`.
  'statusCallbackUrl': "statusCallbackUrl_example", // String | The URL that we should call to pass status parameters (such as call ended) to your application.
  'voiceFallbackMethod': "voiceFallbackMethod_example", // String | The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
  'voiceFallbackUrl': "voiceFallbackUrl_example", // String | The URL that we should call when an error occurs while retrieving or executing the TwiML requested by `voice_url`.
  'voiceMethod': "voiceMethod_example", // String | The HTTP method we should use to call `voice_url`
  'voiceUrl': "voiceUrl_example" // String | The URL we should call when the BYOC Trunk receives a call.
};
apiInstance.updateByocTrunk(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the BYOC Trunk resource to update. | 
 **cnamLookupEnabled** | **Boolean**| Whether Caller ID Name (CNAM) lookup is enabled for the trunk. If enabled, all inbound calls to the BYOC Trunk from the United States and Canada automatically perform a CNAM Lookup and display Caller ID data on your phone. See [CNAM Lookups](https://www.twilio.com/docs/sip-trunking#CNAM) for more information. | [optional] 
 **connectionPolicySid** | **String**| The SID of the Connection Policy that Twilio will use when routing traffic to your communications infrastructure. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long. | [optional] 
 **fromDomainSid** | **String**| The SID of the SIP Domain that should be used in the &#x60;From&#x60; header of originating calls sent to your SIP infrastructure. If your SIP infrastructure allows users to \\\&quot;call back\\\&quot; an incoming call, configure this with a [SIP Domain](https://www.twilio.com/docs/voice/api/sending-sip) to ensure proper routing. If not configured, the from domain will default to \\\&quot;sip.twilio.com\\\&quot;. | [optional] 
 **statusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;status_callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **statusCallbackUrl** | **String**| The URL that we should call to pass status parameters (such as call ended) to your application. | [optional] 
 **voiceFallbackMethod** | **String**| The HTTP method we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **voiceFallbackUrl** | **String**| The URL that we should call when an error occurs while retrieving or executing the TwiML requested by &#x60;voice_url&#x60;. | [optional] 
 **voiceMethod** | **String**| The HTTP method we should use to call &#x60;voice_url&#x60; | [optional] 
 **voiceUrl** | **String**| The URL we should call when the BYOC Trunk receives a call. | [optional] 

### Return type

[**VoiceV1ByocTrunk**](VoiceV1ByocTrunk.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

