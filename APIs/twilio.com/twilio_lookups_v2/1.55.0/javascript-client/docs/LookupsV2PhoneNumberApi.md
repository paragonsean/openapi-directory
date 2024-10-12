# TwilioLookups.LookupsV2PhoneNumberApi

All URIs are relative to *https://lookups.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchPhoneNumber**](LookupsV2PhoneNumberApi.md#fetchPhoneNumber) | **GET** /v2/PhoneNumbers/{PhoneNumber} | 



## fetchPhoneNumber

> LookupsV2PhoneNumber fetchPhoneNumber(phoneNumber, opts)





### Example

```javascript
import TwilioLookups from 'twilio_lookups';
let defaultClient = TwilioLookups.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioLookups.LookupsV2PhoneNumberApi();
let phoneNumber = "phoneNumber_example"; // String | The phone number to lookup in E.164 or national format. Default country code is +1 (North America).
let opts = {
  'fields': "fields_example", // String | A comma-separated list of fields to return. Possible values are validation, caller_name, sim_swap, call_forwarding, line_status, line_type_intelligence, identity_match, reassigned_number, sms_pumping_risk, phone_number_quality_score.
  'countryCode': "countryCode_example", // String | The [country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) used if the phone number provided is in national format.
  'firstName': "firstName_example", // String | User’s first name. This query parameter is only used (optionally) for identity_match package requests.
  'lastName': "lastName_example", // String | User’s last name. This query parameter is only used (optionally) for identity_match package requests.
  'addressLine1': "addressLine1_example", // String | User’s first address line. This query parameter is only used (optionally) for identity_match package requests.
  'addressLine2': "addressLine2_example", // String | User’s second address line. This query parameter is only used (optionally) for identity_match package requests.
  'city': "city_example", // String | User’s city. This query parameter is only used (optionally) for identity_match package requests.
  'state': "state_example", // String | User’s country subdivision, such as state, province, or locality. This query parameter is only used (optionally) for identity_match package requests.
  'postalCode': "postalCode_example", // String | User’s postal zip code. This query parameter is only used (optionally) for identity_match package requests.
  'addressCountryCode': "addressCountryCode_example", // String | User’s country, up to two characters. This query parameter is only used (optionally) for identity_match package requests.
  'nationalId': "nationalId_example", // String | User’s national ID, such as SSN or Passport ID. This query parameter is only used (optionally) for identity_match package requests.
  'dateOfBirth': "dateOfBirth_example", // String | User’s date of birth, in YYYYMMDD format. This query parameter is only used (optionally) for identity_match package requests.
  'lastVerifiedDate': "lastVerifiedDate_example" // String | The date you obtained consent to call or text the end-user of the phone number or a date on which you are reasonably certain that the end-user could still be reached at that number. This query parameter is only used (optionally) for reassigned_number package requests.
};
apiInstance.fetchPhoneNumber(phoneNumber, opts, (error, data, response) => {
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
 **phoneNumber** | **String**| The phone number to lookup in E.164 or national format. Default country code is +1 (North America). | 
 **fields** | **String**| A comma-separated list of fields to return. Possible values are validation, caller_name, sim_swap, call_forwarding, line_status, line_type_intelligence, identity_match, reassigned_number, sms_pumping_risk, phone_number_quality_score. | [optional] 
 **countryCode** | **String**| The [country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) used if the phone number provided is in national format. | [optional] 
 **firstName** | **String**| User’s first name. This query parameter is only used (optionally) for identity_match package requests. | [optional] 
 **lastName** | **String**| User’s last name. This query parameter is only used (optionally) for identity_match package requests. | [optional] 
 **addressLine1** | **String**| User’s first address line. This query parameter is only used (optionally) for identity_match package requests. | [optional] 
 **addressLine2** | **String**| User’s second address line. This query parameter is only used (optionally) for identity_match package requests. | [optional] 
 **city** | **String**| User’s city. This query parameter is only used (optionally) for identity_match package requests. | [optional] 
 **state** | **String**| User’s country subdivision, such as state, province, or locality. This query parameter is only used (optionally) for identity_match package requests. | [optional] 
 **postalCode** | **String**| User’s postal zip code. This query parameter is only used (optionally) for identity_match package requests. | [optional] 
 **addressCountryCode** | **String**| User’s country, up to two characters. This query parameter is only used (optionally) for identity_match package requests. | [optional] 
 **nationalId** | **String**| User’s national ID, such as SSN or Passport ID. This query parameter is only used (optionally) for identity_match package requests. | [optional] 
 **dateOfBirth** | **String**| User’s date of birth, in YYYYMMDD format. This query parameter is only used (optionally) for identity_match package requests. | [optional] 
 **lastVerifiedDate** | **String**| The date you obtained consent to call or text the end-user of the phone number or a date on which you are reasonably certain that the end-user could still be reached at that number. This query parameter is only used (optionally) for reassigned_number package requests. | [optional] 

### Return type

[**LookupsV2PhoneNumber**](LookupsV2PhoneNumber.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

