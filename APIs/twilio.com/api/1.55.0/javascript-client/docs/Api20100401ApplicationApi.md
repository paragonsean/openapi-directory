# TwilioApi.Api20100401ApplicationApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createApplication**](Api20100401ApplicationApi.md#createApplication) | **POST** /2010-04-01/Accounts/{AccountSid}/Applications.json | 
[**deleteApplication**](Api20100401ApplicationApi.md#deleteApplication) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Applications/{Sid}.json | 
[**fetchApplication**](Api20100401ApplicationApi.md#fetchApplication) | **GET** /2010-04-01/Accounts/{AccountSid}/Applications/{Sid}.json | 
[**listApplication**](Api20100401ApplicationApi.md#listApplication) | **GET** /2010-04-01/Accounts/{AccountSid}/Applications.json | 
[**updateApplication**](Api20100401ApplicationApi.md#updateApplication) | **POST** /2010-04-01/Accounts/{AccountSid}/Applications/{Sid}.json | 



## createApplication

> ApiV2010AccountApplication createApplication(accountSid, opts)



Create a new application within your account

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401ApplicationApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
let opts = {
  'apiVersion': "apiVersion_example", // String | The API version to use to start a new TwiML session. Can be: `2010-04-01` or `2008-08-01`. The default value is the account's default API version.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the new application. It can be up to 64 characters long.
  'messageStatusCallback': "messageStatusCallback_example", // String | The URL we should call using a POST method to send message status information to your application.
  'publicApplicationConnectEnabled': true, // Boolean | Whether to allow other Twilio accounts to dial this applicaton using Dial verb. Can be: `true` or `false`.
  'smsFallbackMethod': "smsFallbackMethod_example", // String | The HTTP method we should use to call `sms_fallback_url`. Can be: `GET` or `POST`.
  'smsFallbackUrl': "smsFallbackUrl_example", // String | The URL that we should call when an error occurs while retrieving or executing the TwiML from `sms_url`.
  'smsMethod': "smsMethod_example", // String | The HTTP method we should use to call `sms_url`. Can be: `GET` or `POST`.
  'smsStatusCallback': "smsStatusCallback_example", // String | The URL we should call using a POST method to send status information about SMS messages sent by the application.
  'smsUrl': "smsUrl_example", // String | The URL we should call when the phone number receives an incoming SMS message.
  'statusCallback': "statusCallback_example", // String | The URL we should call using the `status_callback_method` to send status information to your application.
  'statusCallbackMethod': "statusCallbackMethod_example", // String | The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST`.
  'voiceCallerIdLookup': true, // Boolean | Whether we should look up the caller's caller-ID name from the CNAM database (additional charges apply). Can be: `true` or `false`.
  'voiceFallbackMethod': "voiceFallbackMethod_example", // String | The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
  'voiceFallbackUrl': "voiceFallbackUrl_example", // String | The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`.
  'voiceMethod': "voiceMethod_example", // String | The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`.
  'voiceUrl': "voiceUrl_example" // String | The URL we should call when the phone number assigned to this application receives a call.
};
apiInstance.createApplication(accountSid, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The API version to use to start a new TwiML session. Can be: &#x60;2010-04-01&#x60; or &#x60;2008-08-01&#x60;. The default value is the account&#39;s default API version. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the new application. It can be up to 64 characters long. | [optional] 
 **messageStatusCallback** | **String**| The URL we should call using a POST method to send message status information to your application. | [optional] 
 **publicApplicationConnectEnabled** | **Boolean**| Whether to allow other Twilio accounts to dial this applicaton using Dial verb. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
 **smsFallbackMethod** | **String**| The HTTP method we should use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **smsFallbackUrl** | **String**| The URL that we should call when an error occurs while retrieving or executing the TwiML from &#x60;sms_url&#x60;. | [optional] 
 **smsMethod** | **String**| The HTTP method we should use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **smsStatusCallback** | **String**| The URL we should call using a POST method to send status information about SMS messages sent by the application. | [optional] 
 **smsUrl** | **String**| The URL we should call when the phone number receives an incoming SMS message. | [optional] 
 **statusCallback** | **String**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional] 
 **statusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **voiceCallerIdLookup** | **Boolean**| Whether we should look up the caller&#39;s caller-ID name from the CNAM database (additional charges apply). Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
 **voiceFallbackMethod** | **String**| The HTTP method we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **voiceFallbackUrl** | **String**| The URL that we should call when an error occurs retrieving or executing the TwiML requested by &#x60;url&#x60;. | [optional] 
 **voiceMethod** | **String**| The HTTP method we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **voiceUrl** | **String**| The URL we should call when the phone number assigned to this application receives a call. | [optional] 

### Return type

[**ApiV2010AccountApplication**](ApiV2010AccountApplication.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteApplication

> deleteApplication(accountSid, sid)



Delete the application by the specified application sid

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401ApplicationApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resources to delete.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Application resource to delete.
apiInstance.deleteApplication(accountSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resources to delete. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Application resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchApplication

> ApiV2010AccountApplication fetchApplication(accountSid, sid)



Fetch the application specified by the provided sid

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401ApplicationApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resource to fetch.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Application resource to fetch.
apiInstance.fetchApplication(accountSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resource to fetch. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Application resource to fetch. | 

### Return type

[**ApiV2010AccountApplication**](ApiV2010AccountApplication.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listApplication

> ListApplicationResponse listApplication(accountSid, opts)



Retrieve a list of applications representing an application within the requesting account

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401ApplicationApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resources to read.
let opts = {
  'friendlyName': "friendlyName_example", // String | The string that identifies the Application resources to read.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listApplication(accountSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resources to read. | 
 **friendlyName** | **String**| The string that identifies the Application resources to read. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListApplicationResponse**](ListApplicationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateApplication

> ApiV2010AccountApplication updateApplication(accountSid, sid, opts)



Updates the application&#39;s properties

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401ApplicationApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resources to update.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Application resource to update.
let opts = {
  'apiVersion': "apiVersion_example", // String | The API version to use to start a new TwiML session. Can be: `2010-04-01` or `2008-08-01`. The default value is your account's default API version.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
  'messageStatusCallback': "messageStatusCallback_example", // String | The URL we should call using a POST method to send message status information to your application.
  'publicApplicationConnectEnabled': true, // Boolean | Whether to allow other Twilio accounts to dial this applicaton using Dial verb. Can be: `true` or `false`.
  'smsFallbackMethod': "smsFallbackMethod_example", // String | The HTTP method we should use to call `sms_fallback_url`. Can be: `GET` or `POST`.
  'smsFallbackUrl': "smsFallbackUrl_example", // String | The URL that we should call when an error occurs while retrieving or executing the TwiML from `sms_url`.
  'smsMethod': "smsMethod_example", // String | The HTTP method we should use to call `sms_url`. Can be: `GET` or `POST`.
  'smsStatusCallback': "smsStatusCallback_example", // String | Same as message_status_callback: The URL we should call using a POST method to send status information about SMS messages sent by the application. Deprecated, included for backwards compatibility.
  'smsUrl': "smsUrl_example", // String | The URL we should call when the phone number receives an incoming SMS message.
  'statusCallback': "statusCallback_example", // String | The URL we should call using the `status_callback_method` to send status information to your application.
  'statusCallbackMethod': "statusCallbackMethod_example", // String | The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST`.
  'voiceCallerIdLookup': true, // Boolean | Whether we should look up the caller's caller-ID name from the CNAM database (additional charges apply). Can be: `true` or `false`.
  'voiceFallbackMethod': "voiceFallbackMethod_example", // String | The HTTP method we should use to call `voice_fallback_url`. Can be: `GET` or `POST`.
  'voiceFallbackUrl': "voiceFallbackUrl_example", // String | The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`.
  'voiceMethod': "voiceMethod_example", // String | The HTTP method we should use to call `voice_url`. Can be: `GET` or `POST`.
  'voiceUrl': "voiceUrl_example" // String | The URL we should call when the phone number assigned to this application receives a call.
};
apiInstance.updateApplication(accountSid, sid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Application resources to update. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Application resource to update. | 
 **apiVersion** | **String**| The API version to use to start a new TwiML session. Can be: &#x60;2010-04-01&#x60; or &#x60;2008-08-01&#x60;. The default value is your account&#39;s default API version. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] 
 **messageStatusCallback** | **String**| The URL we should call using a POST method to send message status information to your application. | [optional] 
 **publicApplicationConnectEnabled** | **Boolean**| Whether to allow other Twilio accounts to dial this applicaton using Dial verb. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
 **smsFallbackMethod** | **String**| The HTTP method we should use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **smsFallbackUrl** | **String**| The URL that we should call when an error occurs while retrieving or executing the TwiML from &#x60;sms_url&#x60;. | [optional] 
 **smsMethod** | **String**| The HTTP method we should use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **smsStatusCallback** | **String**| Same as message_status_callback: The URL we should call using a POST method to send status information about SMS messages sent by the application. Deprecated, included for backwards compatibility. | [optional] 
 **smsUrl** | **String**| The URL we should call when the phone number receives an incoming SMS message. | [optional] 
 **statusCallback** | **String**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional] 
 **statusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **voiceCallerIdLookup** | **Boolean**| Whether we should look up the caller&#39;s caller-ID name from the CNAM database (additional charges apply). Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
 **voiceFallbackMethod** | **String**| The HTTP method we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **voiceFallbackUrl** | **String**| The URL that we should call when an error occurs retrieving or executing the TwiML requested by &#x60;url&#x60;. | [optional] 
 **voiceMethod** | **String**| The HTTP method we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **voiceUrl** | **String**| The URL we should call when the phone number assigned to this application receives a call. | [optional] 

### Return type

[**ApiV2010AccountApplication**](ApiV2010AccountApplication.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

