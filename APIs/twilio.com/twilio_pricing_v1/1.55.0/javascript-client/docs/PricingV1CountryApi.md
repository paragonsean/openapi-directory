# TwilioPricing.PricingV1CountryApi

All URIs are relative to *https://pricing.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchMessagingCountry**](PricingV1CountryApi.md#fetchMessagingCountry) | **GET** /v1/Messaging/Countries/{IsoCountry} | 
[**fetchPhoneNumberCountry**](PricingV1CountryApi.md#fetchPhoneNumberCountry) | **GET** /v1/PhoneNumbers/Countries/{IsoCountry} | 
[**fetchVoiceCountry**](PricingV1CountryApi.md#fetchVoiceCountry) | **GET** /v1/Voice/Countries/{IsoCountry} | 
[**listMessagingCountry**](PricingV1CountryApi.md#listMessagingCountry) | **GET** /v1/Messaging/Countries | 
[**listPhoneNumberCountry**](PricingV1CountryApi.md#listPhoneNumberCountry) | **GET** /v1/PhoneNumbers/Countries | 
[**listVoiceCountry**](PricingV1CountryApi.md#listVoiceCountry) | **GET** /v1/Voice/Countries | 



## fetchMessagingCountry

> PricingV1MessagingMessagingCountryInstance fetchMessagingCountry(isoCountry)





### Example

```javascript
import TwilioPricing from 'twilio_pricing';
let defaultClient = TwilioPricing.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPricing.PricingV1CountryApi();
let isoCountry = "isoCountry_example"; // String | The [ISO country code](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the pricing information to fetch.
apiInstance.fetchMessagingCountry(isoCountry, (error, data, response) => {
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
 **isoCountry** | **String**| The [ISO country code](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the pricing information to fetch. | 

### Return type

[**PricingV1MessagingMessagingCountryInstance**](PricingV1MessagingMessagingCountryInstance.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fetchPhoneNumberCountry

> PricingV1PhoneNumberPhoneNumberCountryInstance fetchPhoneNumberCountry(isoCountry)





### Example

```javascript
import TwilioPricing from 'twilio_pricing';
let defaultClient = TwilioPricing.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPricing.PricingV1CountryApi();
let isoCountry = "isoCountry_example"; // String | The [ISO country code](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the pricing information to fetch.
apiInstance.fetchPhoneNumberCountry(isoCountry, (error, data, response) => {
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
 **isoCountry** | **String**| The [ISO country code](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the pricing information to fetch. | 

### Return type

[**PricingV1PhoneNumberPhoneNumberCountryInstance**](PricingV1PhoneNumberPhoneNumberCountryInstance.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fetchVoiceCountry

> PricingV1VoiceVoiceCountryInstance fetchVoiceCountry(isoCountry)





### Example

```javascript
import TwilioPricing from 'twilio_pricing';
let defaultClient = TwilioPricing.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPricing.PricingV1CountryApi();
let isoCountry = "isoCountry_example"; // String | The [ISO country code](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the pricing information to fetch.
apiInstance.fetchVoiceCountry(isoCountry, (error, data, response) => {
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
 **isoCountry** | **String**| The [ISO country code](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the pricing information to fetch. | 

### Return type

[**PricingV1VoiceVoiceCountryInstance**](PricingV1VoiceVoiceCountryInstance.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMessagingCountry

> ListMessagingCountryResponse listMessagingCountry(opts)





### Example

```javascript
import TwilioPricing from 'twilio_pricing';
let defaultClient = TwilioPricing.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPricing.PricingV1CountryApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listMessagingCountry(opts, (error, data, response) => {
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

[**ListMessagingCountryResponse**](ListMessagingCountryResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPhoneNumberCountry

> ListPhoneNumberCountryResponse listPhoneNumberCountry(opts)





### Example

```javascript
import TwilioPricing from 'twilio_pricing';
let defaultClient = TwilioPricing.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPricing.PricingV1CountryApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listPhoneNumberCountry(opts, (error, data, response) => {
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

[**ListPhoneNumberCountryResponse**](ListPhoneNumberCountryResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listVoiceCountry

> ListVoiceCountryResponse listVoiceCountry(opts)





### Example

```javascript
import TwilioPricing from 'twilio_pricing';
let defaultClient = TwilioPricing.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPricing.PricingV1CountryApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listVoiceCountry(opts, (error, data, response) => {
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

[**ListVoiceCountryResponse**](ListVoiceCountryResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

