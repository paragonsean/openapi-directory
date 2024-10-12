# TwilioApi.Api20100401DomainApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSipDomain**](Api20100401DomainApi.md#createSipDomain) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/Domains.json | 
[**deleteSipDomain**](Api20100401DomainApi.md#deleteSipDomain) | **DELETE** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{Sid}.json | 
[**fetchSipDomain**](Api20100401DomainApi.md#fetchSipDomain) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{Sid}.json | 
[**listSipDomain**](Api20100401DomainApi.md#listSipDomain) | **GET** /2010-04-01/Accounts/{AccountSid}/SIP/Domains.json | 
[**updateSipDomain**](Api20100401DomainApi.md#updateSipDomain) | **POST** /2010-04-01/Accounts/{AccountSid}/SIP/Domains/{Sid}.json | 



## createSipDomain

> ApiV2010AccountSipSipDomain createSipDomain(accountSid, domainName, opts)



Create a new Domain

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401DomainApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
let domainName = "domainName_example"; // String | The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and \\\"-\\\" and must end with `sip.twilio.com`.
let opts = {
  'byocTrunkSid': "byocTrunkSid_example", // String | The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be associated with.
  'emergencyCallerSid': "emergencyCallerSid_example", // String | Whether an emergency caller sid is configured for the domain. If present, this phone number will be used as the callback for the emergency call.
  'emergencyCallingEnabled': true, // Boolean | Whether emergency calling is enabled for the domain. If enabled, allows emergency calls on the domain from phone numbers with validated addresses.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you created to describe the resource. It can be up to 64 characters long.
  'secure': true, // Boolean | Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be negotiated on all incoming calls to this sip domain.
  'sipRegistration': true, // Boolean | Whether to allow SIP Endpoints to register with the domain to receive calls. Can be `true` or `false`. `true` allows SIP Endpoints to register with the domain to receive calls, `false` does not.
  'voiceFallbackMethod': "voiceFallbackMethod_example", // String | The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
  'voiceFallbackUrl': "voiceFallbackUrl_example", // String | The URL that we should call when an error occurs while retrieving or executing the TwiML from `voice_url`.
  'voiceMethod': "voiceMethod_example", // String | The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`.
  'voiceStatusCallbackMethod': "voiceStatusCallbackMethod_example", // String | The HTTP method we should use to call `voice_status_callback_url`. Can be: `GET` or `POST`.
  'voiceStatusCallbackUrl': "voiceStatusCallbackUrl_example", // String | The URL that we should call to pass status parameters (such as call ended) to your application.
  'voiceUrl': "voiceUrl_example" // String | The URL we should when the domain receives a call.
};
apiInstance.createSipDomain(accountSid, domainName, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. | 
 **domainName** | **String**| The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and \\\&quot;-\\\&quot; and must end with &#x60;sip.twilio.com&#x60;. | 
 **byocTrunkSid** | **String**| The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be associated with. | [optional] 
 **emergencyCallerSid** | **String**| Whether an emergency caller sid is configured for the domain. If present, this phone number will be used as the callback for the emergency call. | [optional] 
 **emergencyCallingEnabled** | **Boolean**| Whether emergency calling is enabled for the domain. If enabled, allows emergency calls on the domain from phone numbers with validated addresses. | [optional] 
 **friendlyName** | **String**| A descriptive string that you created to describe the resource. It can be up to 64 characters long. | [optional] 
 **secure** | **Boolean**| Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be negotiated on all incoming calls to this sip domain. | [optional] 
 **sipRegistration** | **Boolean**| Whether to allow SIP Endpoints to register with the domain to receive calls. Can be &#x60;true&#x60; or &#x60;false&#x60;. &#x60;true&#x60; allows SIP Endpoints to register with the domain to receive calls, &#x60;false&#x60; does not. | [optional] 
 **voiceFallbackMethod** | **String**| The HTTP method we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **voiceFallbackUrl** | **String**| The URL that we should call when an error occurs while retrieving or executing the TwiML from &#x60;voice_url&#x60;. | [optional] 
 **voiceMethod** | **String**| The HTTP method we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **voiceStatusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;voice_status_callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **voiceStatusCallbackUrl** | **String**| The URL that we should call to pass status parameters (such as call ended) to your application. | [optional] 
 **voiceUrl** | **String**| The URL we should when the domain receives a call. | [optional] 

### Return type

[**ApiV2010AccountSipSipDomain**](ApiV2010AccountSipSipDomain.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSipDomain

> deleteSipDomain(accountSid, sid)



Delete an instance of a Domain

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401DomainApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resources to delete.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the SipDomain resource to delete.
apiInstance.deleteSipDomain(accountSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resources to delete. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the SipDomain resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSipDomain

> ApiV2010AccountSipSipDomain fetchSipDomain(accountSid, sid)



Fetch an instance of a Domain

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401DomainApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resource to fetch.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the SipDomain resource to fetch.
apiInstance.fetchSipDomain(accountSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resource to fetch. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the SipDomain resource to fetch. | 

### Return type

[**ApiV2010AccountSipSipDomain**](ApiV2010AccountSipSipDomain.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSipDomain

> ListSipDomainResponse listSipDomain(accountSid, opts)



Retrieve a list of domains belonging to the account used to make the request

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401DomainApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resources to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSipDomain(accountSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resources to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSipDomainResponse**](ListSipDomainResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSipDomain

> ApiV2010AccountSipSipDomain updateSipDomain(accountSid, sid, opts)



Update the attributes of a domain

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401DomainApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resource to update.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the SipDomain resource to update.
let opts = {
  'byocTrunkSid': "byocTrunkSid_example", // String | The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be associated with.
  'domainName': "domainName_example", // String | The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and \\\"-\\\" and must end with `sip.twilio.com`.
  'emergencyCallerSid': "emergencyCallerSid_example", // String | Whether an emergency caller sid is configured for the domain. If present, this phone number will be used as the callback for the emergency call.
  'emergencyCallingEnabled': true, // Boolean | Whether emergency calling is enabled for the domain. If enabled, allows emergency calls on the domain from phone numbers with validated addresses.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you created to describe the resource. It can be up to 64 characters long.
  'secure': true, // Boolean | Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be negotiated on all incoming calls to this sip domain.
  'sipRegistration': true, // Boolean | Whether to allow SIP Endpoints to register with the domain to receive calls. Can be `true` or `false`. `true` allows SIP Endpoints to register with the domain to receive calls, `false` does not.
  'voiceFallbackMethod': "voiceFallbackMethod_example", // String | The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
  'voiceFallbackUrl': "voiceFallbackUrl_example", // String | The URL that we should call when an error occurs while retrieving or executing the TwiML requested by `voice_url`.
  'voiceMethod': "voiceMethod_example", // String | The HTTP method we should use to call `voice_url`
  'voiceStatusCallbackMethod': "voiceStatusCallbackMethod_example", // String | The HTTP method we should use to call `voice_status_callback_url`. Can be: `GET` or `POST`.
  'voiceStatusCallbackUrl': "voiceStatusCallbackUrl_example", // String | The URL that we should call to pass status parameters (such as call ended) to your application.
  'voiceUrl': "voiceUrl_example" // String | The URL we should call when the domain receives a call.
};
apiInstance.updateSipDomain(accountSid, sid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the SipDomain resource to update. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the SipDomain resource to update. | 
 **byocTrunkSid** | **String**| The SID of the BYOC Trunk(Bring Your Own Carrier) resource that the Sip Domain will be associated with. | [optional] 
 **domainName** | **String**| The unique address you reserve on Twilio to which you route your SIP traffic. Domain names can contain letters, digits, and \\\&quot;-\\\&quot; and must end with &#x60;sip.twilio.com&#x60;. | [optional] 
 **emergencyCallerSid** | **String**| Whether an emergency caller sid is configured for the domain. If present, this phone number will be used as the callback for the emergency call. | [optional] 
 **emergencyCallingEnabled** | **Boolean**| Whether emergency calling is enabled for the domain. If enabled, allows emergency calls on the domain from phone numbers with validated addresses. | [optional] 
 **friendlyName** | **String**| A descriptive string that you created to describe the resource. It can be up to 64 characters long. | [optional] 
 **secure** | **Boolean**| Whether secure SIP is enabled for the domain. If enabled, TLS will be enforced and SRTP will be negotiated on all incoming calls to this sip domain. | [optional] 
 **sipRegistration** | **Boolean**| Whether to allow SIP Endpoints to register with the domain to receive calls. Can be &#x60;true&#x60; or &#x60;false&#x60;. &#x60;true&#x60; allows SIP Endpoints to register with the domain to receive calls, &#x60;false&#x60; does not. | [optional] 
 **voiceFallbackMethod** | **String**| The HTTP method we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **voiceFallbackUrl** | **String**| The URL that we should call when an error occurs while retrieving or executing the TwiML requested by &#x60;voice_url&#x60;. | [optional] 
 **voiceMethod** | **String**| The HTTP method we should use to call &#x60;voice_url&#x60; | [optional] 
 **voiceStatusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;voice_status_callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **voiceStatusCallbackUrl** | **String**| The URL that we should call to pass status parameters (such as call ended) to your application. | [optional] 
 **voiceUrl** | **String**| The URL we should call when the domain receives a call. | [optional] 

### Return type

[**ApiV2010AccountSipSipDomain**](ApiV2010AccountSipSipDomain.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

