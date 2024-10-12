# TwilioApi.Api20100401MachineToMachineApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listAvailablePhoneNumberMachineToMachine**](Api20100401MachineToMachineApi.md#listAvailablePhoneNumberMachineToMachine) | **GET** /2010-04-01/Accounts/{AccountSid}/AvailablePhoneNumbers/{CountryCode}/MachineToMachine.json | 



## listAvailablePhoneNumberMachineToMachine

> ListAvailablePhoneNumberMachineToMachineResponse listAvailablePhoneNumberMachineToMachine(accountSid, countryCode, opts)





### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401MachineToMachineApi();
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
apiInstance.listAvailablePhoneNumberMachineToMachine(accountSid, countryCode, opts, (error, data, response) => {
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

[**ListAvailablePhoneNumberMachineToMachineResponse**](ListAvailablePhoneNumberMachineToMachineResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

