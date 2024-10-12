# TwilioApi.Api20100401MobileApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createIncomingPhoneNumberMobile**](Api20100401MobileApi.md#createIncomingPhoneNumberMobile) | **POST** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/Mobile.json | 
[**listAvailablePhoneNumberMobile**](Api20100401MobileApi.md#listAvailablePhoneNumberMobile) | **GET** /2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/Mobile.json | 
[**listIncomingPhoneNumberMobile**](Api20100401MobileApi.md#listIncomingPhoneNumberMobile) | **GET** /2010-04-01/Accounts/{AccountSid}/IncomingPhoneNumbers/Mobile.json | 



## createIncomingPhoneNumberMobile

> ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberMobile createIncomingPhoneNumberMobile(accountSid, phoneNumber, opts)





### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401MobileApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
let phoneNumber = "phoneNumber_example"; // String | The phone number to purchase specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234.
let opts = {
  'addressSid': "addressSid_example", // String | The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations.
  'apiVersion': "apiVersion_example", // String | The API version to use for incoming calls made to the new phone number. The default is `2010-04-01`.
  'bundleSid': "bundleSid_example", // String | The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations.
  'emergencyAddressSid': "emergencyAddressSid_example", // String | The SID of the emergency address configuration to use for emergency calling from the new phone number.
  'emergencyStatus': "emergencyStatus_example", // IncomingPhoneNumberMobileEnumEmergencyStatus | 
  'friendlyName': "friendlyName_example", // String | A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, the is a formatted version of the phone number.
  'identitySid': "identitySid_example", // String | The SID of the Identity resource that we should associate with the new phone number. Some regions require an identity to meet local regulations.
  'smsApplicationSid': "smsApplicationSid_example", // String | The SID of the application that should handle SMS messages sent to the new phone number. If an `sms_application_sid` is present, we ignore all of the `sms_*_url` urls and use those of the application.
  'smsFallbackMethod': "smsFallbackMethod_example", // String | The HTTP method that we should use to call `sms_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`.
  'smsFallbackUrl': "smsFallbackUrl_example", // String | The URL that we should call when an error occurs while requesting or executing the TwiML defined by `sms_url`.
  'smsMethod': "smsMethod_example", // String | The HTTP method that we should use to call `sms_url`. Can be: `GET` or `POST` and defaults to `POST`.
  'smsUrl': "smsUrl_example", // String | The URL we should call when the new phone number receives an incoming SMS message.
  'statusCallback': "statusCallback_example", // String | The URL we should call using the `status_callback_method` to send status information to your application.
  'statusCallbackMethod': "statusCallbackMethod_example", // String | The HTTP method we should use to call `status_callback`. Can be: `GET` or `POST` and defaults to `POST`.
  'trunkSid': "trunkSid_example", // String | The SID of the Trunk we should use to handle calls to the new phone number. If a `trunk_sid` is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a `trunk_sid` will automatically delete your `voice_application_sid` and vice versa.
  'voiceApplicationSid': "voiceApplicationSid_example", // String | The SID of the application we should use to handle calls to the new phone number. If a `voice_application_sid` is present, we ignore all of the voice urls and use only those set on the application. Setting a `voice_application_sid` will automatically delete your `trunk_sid` and vice versa.
  'voiceCallerIdLookup': true, // Boolean | Whether to lookup the caller's name from the CNAM database and post it to your app. Can be: `true` or `false` and defaults to `false`.
  'voiceFallbackMethod': "voiceFallbackMethod_example", // String | The HTTP method that we should use to call `voice_fallback_url`. Can be: `GET` or `POST` and defaults to `POST`.
  'voiceFallbackUrl': "voiceFallbackUrl_example", // String | The URL that we should call when an error occurs retrieving or executing the TwiML requested by `url`.
  'voiceMethod': "voiceMethod_example", // String | The HTTP method that we should use to call `voice_url`. Can be: `GET` or `POST` and defaults to `POST`.
  'voiceReceiveMode': "voiceReceiveMode_example", // IncomingPhoneNumberMobileEnumVoiceReceiveMode | 
  'voiceUrl': "voiceUrl_example" // String | The URL that we should call to answer a call to the new phone number. The `voice_url` will not be called if a `voice_application_sid` or a `trunk_sid` is set.
};
apiInstance.createIncomingPhoneNumberMobile(accountSid, phoneNumber, opts, (error, data, response) => {
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
 **phoneNumber** | **String**| The phone number to purchase specified in [E.164](https://www.twilio.com/docs/glossary/what-e164) format.  E.164 phone numbers consist of a + followed by the country code and subscriber number without punctuation characters. For example, +14155551234. | 
 **addressSid** | **String**| The SID of the Address resource we should associate with the new phone number. Some regions require addresses to meet local regulations. | [optional] 
 **apiVersion** | **String**| The API version to use for incoming calls made to the new phone number. The default is &#x60;2010-04-01&#x60;. | [optional] 
 **bundleSid** | **String**| The SID of the Bundle resource that you associate with the phone number. Some regions require a Bundle to meet local Regulations. | [optional] 
 **emergencyAddressSid** | **String**| The SID of the emergency address configuration to use for emergency calling from the new phone number. | [optional] 
 **emergencyStatus** | **IncomingPhoneNumberMobileEnumEmergencyStatus**|  | [optional] 
 **friendlyName** | **String**| A descriptive string that you created to describe the new phone number. It can be up to 64 characters long. By default, the is a formatted version of the phone number. | [optional] 
 **identitySid** | **String**| The SID of the Identity resource that we should associate with the new phone number. Some regions require an identity to meet local regulations. | [optional] 
 **smsApplicationSid** | **String**| The SID of the application that should handle SMS messages sent to the new phone number. If an &#x60;sms_application_sid&#x60; is present, we ignore all of the &#x60;sms_*_url&#x60; urls and use those of the application. | [optional] 
 **smsFallbackMethod** | **String**| The HTTP method that we should use to call &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] 
 **smsFallbackUrl** | **String**| The URL that we should call when an error occurs while requesting or executing the TwiML defined by &#x60;sms_url&#x60;. | [optional] 
 **smsMethod** | **String**| The HTTP method that we should use to call &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] 
 **smsUrl** | **String**| The URL we should call when the new phone number receives an incoming SMS message. | [optional] 
 **statusCallback** | **String**| The URL we should call using the &#x60;status_callback_method&#x60; to send status information to your application. | [optional] 
 **statusCallbackMethod** | **String**| The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] 
 **trunkSid** | **String**| The SID of the Trunk we should use to handle calls to the new phone number. If a &#x60;trunk_sid&#x60; is present, we ignore all of the voice urls and voice applications and use only those set on the Trunk. Setting a &#x60;trunk_sid&#x60; will automatically delete your &#x60;voice_application_sid&#x60; and vice versa. | [optional] 
 **voiceApplicationSid** | **String**| The SID of the application we should use to handle calls to the new phone number. If a &#x60;voice_application_sid&#x60; is present, we ignore all of the voice urls and use only those set on the application. Setting a &#x60;voice_application_sid&#x60; will automatically delete your &#x60;trunk_sid&#x60; and vice versa. | [optional] 
 **voiceCallerIdLookup** | **Boolean**| Whether to lookup the caller&#39;s name from the CNAM database and post it to your app. Can be: &#x60;true&#x60; or &#x60;false&#x60; and defaults to &#x60;false&#x60;. | [optional] 
 **voiceFallbackMethod** | **String**| The HTTP method that we should use to call &#x60;voice_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] 
 **voiceFallbackUrl** | **String**| The URL that we should call when an error occurs retrieving or executing the TwiML requested by &#x60;url&#x60;. | [optional] 
 **voiceMethod** | **String**| The HTTP method that we should use to call &#x60;voice_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and defaults to &#x60;POST&#x60;. | [optional] 
 **voiceReceiveMode** | **IncomingPhoneNumberMobileEnumVoiceReceiveMode**|  | [optional] 
 **voiceUrl** | **String**| The URL that we should call to answer a call to the new phone number. The &#x60;voice_url&#x60; will not be called if a &#x60;voice_application_sid&#x60; or a &#x60;trunk_sid&#x60; is set. | [optional] 

### Return type

[**ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberMobile**](ApiV2010AccountIncomingPhoneNumberIncomingPhoneNumberMobile.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## listAvailablePhoneNumberMobile

> ListAvailablePhoneNumberMobileResponse listAvailablePhoneNumberMobile(accountSid, countryCode, opts)





### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401MobileApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the AvailablePhoneNumber resources.
let countryCode = "countryCode_example"; // String | The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country from which to read phone numbers.
let opts = {
  'areaCode': 56, // Number | The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada.
  'contains': "contains_example", // String | The pattern on which to match phone numbers. Valid characters are `*`, `0-9`, `a-z`, and `A-Z`. The `*` character matches any single digit. For examples, see [Example 2](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-2) and [Example 3](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-3). If specified, this value must have at least two characters.
  'smsEnabled': true, // Boolean | Whether the phone numbers can receive text messages. Can be: `true` or `false`.
  'mmsEnabled': true, // Boolean | Whether the phone numbers can receive MMS messages. Can be: `true` or `false`.
  'voiceEnabled': true, // Boolean | Whether the phone numbers can receive calls. Can be: `true` or `false`.
  'excludeAllAddressRequired': true, // Boolean | Whether to exclude phone numbers that require an [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`.
  'excludeLocalAddressRequired': true, // Boolean | Whether to exclude phone numbers that require a local [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`.
  'excludeForeignAddressRequired': true, // Boolean | Whether to exclude phone numbers that require a foreign [Address](https://www.twilio.com/docs/usage/api/address). Can be: `true` or `false` and the default is `false`.
  'beta': true, // Boolean | Whether to read phone numbers that are new to the Twilio platform. Can be: `true` or `false` and the default is `true`.
  'nearNumber': "nearNumber_example", // String | Given a phone number, find a geographically close number within `distance` miles. Distance defaults to 25 miles. Applies to only phone numbers in the US and Canada.
  'nearLatLong': "nearLatLong_example", // String | Given a latitude/longitude pair `lat,long` find geographically close numbers within `distance` miles. Applies to only phone numbers in the US and Canada.
  'distance': 56, // Number | The search radius, in miles, for a `near_` query.  Can be up to `500` and the default is `25`. Applies to only phone numbers in the US and Canada.
  'inPostalCode': "inPostalCode_example", // String | Limit results to a particular postal code. Given a phone number, search within the same postal code as that number. Applies to only phone numbers in the US and Canada.
  'inRegion': "inRegion_example", // String | Limit results to a particular region, state, or province. Given a phone number, search within the same region as that number. Applies to only phone numbers in the US and Canada.
  'inRateCenter': "inRateCenter_example", // String | Limit results to a specific rate center, or given a phone number search within the same rate center as that number. Requires `in_lata` to be set as well. Applies to only phone numbers in the US and Canada.
  'inLata': "inLata_example", // String | Limit results to a specific local access and transport area ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)). Given a phone number, search within the same [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area) as that number. Applies to only phone numbers in the US and Canada.
  'inLocality': "inLocality_example", // String | Limit results to a particular locality or city. Given a phone number, search within the same Locality as that number.
  'faxEnabled': true, // Boolean | Whether the phone numbers can receive faxes. Can be: `true` or `false`.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listAvailablePhoneNumberMobile(accountSid, countryCode, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) requesting the AvailablePhoneNumber resources. | 
 **countryCode** | **String**| The [ISO-3166-1](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country from which to read phone numbers. | 
 **areaCode** | **Number**| The area code of the phone numbers to read. Applies to only phone numbers in the US and Canada. | [optional] 
 **contains** | **String**| The pattern on which to match phone numbers. Valid characters are &#x60;*&#x60;, &#x60;0-9&#x60;, &#x60;a-z&#x60;, and &#x60;A-Z&#x60;. The &#x60;*&#x60; character matches any single digit. For examples, see [Example 2](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-2) and [Example 3](https://www.twilio.com/docs/phone-numbers/api/availablephonenumber-resource#local-get-basic-example-3). If specified, this value must have at least two characters. | [optional] 
 **smsEnabled** | **Boolean**| Whether the phone numbers can receive text messages. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
 **mmsEnabled** | **Boolean**| Whether the phone numbers can receive MMS messages. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
 **voiceEnabled** | **Boolean**| Whether the phone numbers can receive calls. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
 **excludeAllAddressRequired** | **Boolean**| Whether to exclude phone numbers that require an [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional] 
 **excludeLocalAddressRequired** | **Boolean**| Whether to exclude phone numbers that require a local [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional] 
 **excludeForeignAddressRequired** | **Boolean**| Whether to exclude phone numbers that require a foreign [Address](https://www.twilio.com/docs/usage/api/address). Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;false&#x60;. | [optional] 
 **beta** | **Boolean**| Whether to read phone numbers that are new to the Twilio platform. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. | [optional] 
 **nearNumber** | **String**| Given a phone number, find a geographically close number within &#x60;distance&#x60; miles. Distance defaults to 25 miles. Applies to only phone numbers in the US and Canada. | [optional] 
 **nearLatLong** | **String**| Given a latitude/longitude pair &#x60;lat,long&#x60; find geographically close numbers within &#x60;distance&#x60; miles. Applies to only phone numbers in the US and Canada. | [optional] 
 **distance** | **Number**| The search radius, in miles, for a &#x60;near_&#x60; query.  Can be up to &#x60;500&#x60; and the default is &#x60;25&#x60;. Applies to only phone numbers in the US and Canada. | [optional] 
 **inPostalCode** | **String**| Limit results to a particular postal code. Given a phone number, search within the same postal code as that number. Applies to only phone numbers in the US and Canada. | [optional] 
 **inRegion** | **String**| Limit results to a particular region, state, or province. Given a phone number, search within the same region as that number. Applies to only phone numbers in the US and Canada. | [optional] 
 **inRateCenter** | **String**| Limit results to a specific rate center, or given a phone number search within the same rate center as that number. Requires &#x60;in_lata&#x60; to be set as well. Applies to only phone numbers in the US and Canada. | [optional] 
 **inLata** | **String**| Limit results to a specific local access and transport area ([LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area)). Given a phone number, search within the same [LATA](https://en.wikipedia.org/wiki/Local_access_and_transport_area) as that number. Applies to only phone numbers in the US and Canada. | [optional] 
 **inLocality** | **String**| Limit results to a particular locality or city. Given a phone number, search within the same Locality as that number. | [optional] 
 **faxEnabled** | **Boolean**| Whether the phone numbers can receive faxes. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListAvailablePhoneNumberMobileResponse**](ListAvailablePhoneNumberMobileResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listIncomingPhoneNumberMobile

> ListIncomingPhoneNumberMobileResponse listIncomingPhoneNumberMobile(accountSid, opts)





### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401MobileApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read.
let opts = {
  'beta': true, // Boolean | Whether to include phone numbers new to the Twilio platform. Can be: `true` or `false` and the default is `true`.
  'friendlyName': "friendlyName_example", // String | A string that identifies the resources to read.
  'phoneNumber': "phoneNumber_example", // String | The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use '*' as a wildcard for any digit.
  'origin': "origin_example", // String | Whether to include phone numbers based on their origin. Can be: `twilio` or `hosted`. By default, phone numbers of all origin are included.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listIncomingPhoneNumberMobile(accountSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the resources to read. | 
 **beta** | **Boolean**| Whether to include phone numbers new to the Twilio platform. Can be: &#x60;true&#x60; or &#x60;false&#x60; and the default is &#x60;true&#x60;. | [optional] 
 **friendlyName** | **String**| A string that identifies the resources to read. | [optional] 
 **phoneNumber** | **String**| The phone numbers of the IncomingPhoneNumber resources to read. You can specify partial numbers and use &#39;*&#39; as a wildcard for any digit. | [optional] 
 **origin** | **String**| Whether to include phone numbers based on their origin. Can be: &#x60;twilio&#x60; or &#x60;hosted&#x60;. By default, phone numbers of all origin are included. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListIncomingPhoneNumberMobileResponse**](ListIncomingPhoneNumberMobileResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

