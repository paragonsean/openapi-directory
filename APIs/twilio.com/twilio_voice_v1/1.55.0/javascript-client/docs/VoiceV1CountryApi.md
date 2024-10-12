# TwilioVoice.VoiceV1CountryApi

All URIs are relative to *https://voice.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchDialingPermissionsCountry**](VoiceV1CountryApi.md#fetchDialingPermissionsCountry) | **GET** /v1/DialingPermissions/Countries/{IsoCode} | 
[**listDialingPermissionsCountry**](VoiceV1CountryApi.md#listDialingPermissionsCountry) | **GET** /v1/DialingPermissions/Countries | 



## fetchDialingPermissionsCountry

> VoiceV1DialingPermissionsDialingPermissionsCountryInstance fetchDialingPermissionsCountry(isoCode)



Retrieve voice dialing country permissions identified by the given ISO country code

### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1CountryApi();
let isoCode = "isoCode_example"; // String | The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the DialingPermissions Country resource to fetch
apiInstance.fetchDialingPermissionsCountry(isoCode, (error, data, response) => {
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
 **isoCode** | **String**| The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the DialingPermissions Country resource to fetch | 

### Return type

[**VoiceV1DialingPermissionsDialingPermissionsCountryInstance**](VoiceV1DialingPermissionsDialingPermissionsCountryInstance.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDialingPermissionsCountry

> ListDialingPermissionsCountryResponse listDialingPermissionsCountry(opts)



Retrieve all voice dialing country permissions for this account

### Example

```javascript
import TwilioVoice from 'twilio_voice';
let defaultClient = TwilioVoice.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioVoice.VoiceV1CountryApi();
let opts = {
  'isoCode': "isoCode_example", // String | Filter to retrieve the country permissions by specifying the [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)
  'continent': "continent_example", // String | Filter to retrieve the country permissions by specifying the continent
  'countryCode': "countryCode_example", // String | Filter the results by specified [country codes](https://www.itu.int/itudoc/itu-t/ob-lists/icc/e164_763.html)
  'lowRiskNumbersEnabled': true, // Boolean | Filter to retrieve the country permissions with dialing to low-risk numbers enabled. Can be: `true` or `false`.
  'highRiskSpecialNumbersEnabled': true, // Boolean | Filter to retrieve the country permissions with dialing to high-risk special service numbers enabled. Can be: `true` or `false`
  'highRiskTollfraudNumbersEnabled': true, // Boolean | Filter to retrieve the country permissions with dialing to high-risk [toll fraud](https://www.twilio.com/blog/how-to-protect-your-account-from-toll-fraud-with-voice-dialing-geo-permissions-html) numbers enabled. Can be: `true` or `false`.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listDialingPermissionsCountry(opts, (error, data, response) => {
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
 **isoCode** | **String**| Filter to retrieve the country permissions by specifying the [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) | [optional] 
 **continent** | **String**| Filter to retrieve the country permissions by specifying the continent | [optional] 
 **countryCode** | **String**| Filter the results by specified [country codes](https://www.itu.int/itudoc/itu-t/ob-lists/icc/e164_763.html) | [optional] 
 **lowRiskNumbersEnabled** | **Boolean**| Filter to retrieve the country permissions with dialing to low-risk numbers enabled. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
 **highRiskSpecialNumbersEnabled** | **Boolean**| Filter to retrieve the country permissions with dialing to high-risk special service numbers enabled. Can be: &#x60;true&#x60; or &#x60;false&#x60; | [optional] 
 **highRiskTollfraudNumbersEnabled** | **Boolean**| Filter to retrieve the country permissions with dialing to high-risk [toll fraud](https://www.twilio.com/blog/how-to-protect-your-account-from-toll-fraud-with-voice-dialing-geo-permissions-html) numbers enabled. Can be: &#x60;true&#x60; or &#x60;false&#x60;. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListDialingPermissionsCountryResponse**](ListDialingPermissionsCountryResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

