# TwilioPricing.PricingV2CountryApi

All URIs are relative to *https://pricing.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchTrunkingCountry**](PricingV2CountryApi.md#fetchTrunkingCountry) | **GET** /v2/Trunking/Countries/{IsoCountry} | 
[**fetchVoiceCountry**](PricingV2CountryApi.md#fetchVoiceCountry) | **GET** /v2/Voice/Countries/{IsoCountry} | 
[**listTrunkingCountry**](PricingV2CountryApi.md#listTrunkingCountry) | **GET** /v2/Trunking/Countries | 
[**listVoiceCountry**](PricingV2CountryApi.md#listVoiceCountry) | **GET** /v2/Voice/Countries | 



## fetchTrunkingCountry

> PricingV2TrunkingCountryInstance fetchTrunkingCountry(isoCountry)



Fetch a specific Country.

### Example

```javascript
import TwilioPricing from 'twilio_pricing';
let defaultClient = TwilioPricing.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPricing.PricingV2CountryApi();
let isoCountry = "isoCountry_example"; // String | The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the origin-based voice pricing information to fetch.
apiInstance.fetchTrunkingCountry(isoCountry, (error, data, response) => {
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
 **isoCountry** | **String**| The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the origin-based voice pricing information to fetch. | 

### Return type

[**PricingV2TrunkingCountryInstance**](PricingV2TrunkingCountryInstance.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fetchVoiceCountry

> PricingV2VoiceVoiceCountryInstance fetchVoiceCountry(isoCountry)



Fetch a specific Country.

### Example

```javascript
import TwilioPricing from 'twilio_pricing';
let defaultClient = TwilioPricing.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPricing.PricingV2CountryApi();
let isoCountry = "isoCountry_example"; // String | The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the origin-based voice pricing information to fetch.
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
 **isoCountry** | **String**| The [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the origin-based voice pricing information to fetch. | 

### Return type

[**PricingV2VoiceVoiceCountryInstance**](PricingV2VoiceVoiceCountryInstance.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTrunkingCountry

> ListTrunkingCountryResponse listTrunkingCountry(opts)





### Example

```javascript
import TwilioPricing from 'twilio_pricing';
let defaultClient = TwilioPricing.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPricing.PricingV2CountryApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listTrunkingCountry(opts, (error, data, response) => {
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

[**ListTrunkingCountryResponse**](ListTrunkingCountryResponse.md)

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

let apiInstance = new TwilioPricing.PricingV2CountryApi();
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

