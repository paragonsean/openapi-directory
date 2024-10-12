# TwilioVoice.VoiceV1IpRecordApi

All URIs are relative to *https://voice.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createIpRecord**](VoiceV1IpRecordApi.md#createIpRecord) | **POST** /v1/IpRecords | 
[**deleteIpRecord**](VoiceV1IpRecordApi.md#deleteIpRecord) | **DELETE** /v1/IpRecords/{Sid} | 
[**fetchIpRecord**](VoiceV1IpRecordApi.md#fetchIpRecord) | **GET** /v1/IpRecords/{Sid} | 
[**listIpRecord**](VoiceV1IpRecordApi.md#listIpRecord) | **GET** /v1/IpRecords | 
[**updateIpRecord**](VoiceV1IpRecordApi.md#updateIpRecord) | **POST** /v1/IpRecords/{Sid} | 



## createIpRecord

> VoiceV1IpRecord createIpRecord(ipAddress, opts)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1IpRecordApi();
let ipAddress = "ipAddress_example"; // String | An IP address in dotted decimal notation, IPv4 only.
let opts = {
  'cidrPrefixLength': 56, // Number | An integer representing the length of the [CIDR](https://tools.ietf.org/html/rfc4632) prefix to use with this IP address. By default the entire IP address is used, which for IPv4 is value 32.
  'friendlyName': "friendlyName_example" // String | A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
};
apiInstance.createIpRecord(ipAddress, opts, (error, data, response) => {
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
 **ipAddress** | **String**| An IP address in dotted decimal notation, IPv4 only. | 
 **cidrPrefixLength** | **Number**| An integer representing the length of the [CIDR](https://tools.ietf.org/html/rfc4632) prefix to use with this IP address. By default the entire IP address is used, which for IPv4 is value 32. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long. | [optional] 

### Return type

[**VoiceV1IpRecord**](VoiceV1IpRecord.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteIpRecord

> deleteIpRecord(sid)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1IpRecordApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the IP Record resource to delete.
apiInstance.deleteIpRecord(sid, (error, data, response) => {
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


## fetchIpRecord

> VoiceV1IpRecord fetchIpRecord(sid)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1IpRecordApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the IP Record resource to fetch.
apiInstance.fetchIpRecord(sid, (error, data, response) => {
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

[**VoiceV1IpRecord**](VoiceV1IpRecord.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listIpRecord

> ListIpRecordResponse listIpRecord(opts)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1IpRecordApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listIpRecord(opts, (error, data, response) => {
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

[**ListIpRecordResponse**](ListIpRecordResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateIpRecord

> VoiceV1IpRecord updateIpRecord(sid, opts)





### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1IpRecordApi();
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the IP Record resource to update.
let opts = {
  'friendlyName': "friendlyName_example" // String | A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long.
};
apiInstance.updateIpRecord(sid, opts, (error, data, response) => {
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
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It is not unique and can be up to 255 characters long. | [optional] 

### Return type

[**VoiceV1IpRecord**](VoiceV1IpRecord.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

