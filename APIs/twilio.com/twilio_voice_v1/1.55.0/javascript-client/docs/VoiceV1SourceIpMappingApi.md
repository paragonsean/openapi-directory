# TwilioVoice.VoiceV1SourceIpMappingApi

All URIs are relative to *https://voice.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSourceIpMapping**](VoiceV1SourceIpMappingApi.md#createSourceIpMapping) | **POST** /v1/SourceIpMappings | 
[**deleteSourceIpMapping**](VoiceV1SourceIpMappingApi.md#deleteSourceIpMapping) | **DELETE** /v1/SourceIpMappings/{Sid} | 
[**fetchSourceIpMapping**](VoiceV1SourceIpMappingApi.md#fetchSourceIpMapping) | **GET** /v1/SourceIpMappings/{Sid} | 
[**listSourceIpMapping**](VoiceV1SourceIpMappingApi.md#listSourceIpMapping) | **GET** /v1/SourceIpMappings | 
[**updateSourceIpMapping**](VoiceV1SourceIpMappingApi.md#updateSourceIpMapping) | **POST** /v1/SourceIpMappings/{Sid} | 



## createSourceIpMapping

> VoiceV1SourceIpMapping createSourceIpMapping(ipRecordSid, sipDomainSid)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1SourceIpMappingApi();
let ipRecordSid = "ipRecordSid_example"; // String | The Twilio-provided string that uniquely identifies the IP Record resource to map from.
let sipDomainSid = "sipDomainSid_example"; // String | The SID of the SIP Domain that the IP Record should be mapped to.
apiInstance.createSourceIpMapping(ipRecordSid, sipDomainSid, (error, data, response) => {
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
 **ipRecordSid** | **String**| The Twilio-provided string that uniquely identifies the IP Record resource to map from. | 
 **sipDomainSid** | **String**| The SID of the SIP Domain that the IP Record should be mapped to. | 

### Return type

[**VoiceV1SourceIpMapping**](VoiceV1SourceIpMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSourceIpMapping

> deleteSourceIpMapping(sid)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1SourceIpMappingApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the IP Record resource to delete.
apiInstance.deleteSourceIpMapping(sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the IP Record resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSourceIpMapping

> VoiceV1SourceIpMapping fetchSourceIpMapping(sid)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1SourceIpMappingApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the IP Record resource to fetch.
apiInstance.fetchSourceIpMapping(sid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the IP Record resource to fetch. | 

### Return type

[**VoiceV1SourceIpMapping**](VoiceV1SourceIpMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSourceIpMapping

> ListSourceIpMappingResponse listSourceIpMapping(opts)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1SourceIpMappingApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSourceIpMapping(opts, (error, data, response) => {
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

[**ListSourceIpMappingResponse**](ListSourceIpMappingResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSourceIpMapping

> VoiceV1SourceIpMapping updateSourceIpMapping(sid, sipDomainSid)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1SourceIpMappingApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the IP Record resource to update.
let sipDomainSid = "sipDomainSid_example"; // String | The SID of the SIP Domain that the IP Record should be mapped to.
apiInstance.updateSourceIpMapping(sid, sipDomainSid, (error, data, response) => {
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
 **sid** | **String**| The Twilio-provided string that uniquely identifies the IP Record resource to update. | 
 **sipDomainSid** | **String**| The SID of the SIP Domain that the IP Record should be mapped to. | 

### Return type

[**VoiceV1SourceIpMapping**](VoiceV1SourceIpMapping.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

