# PricingApi.PricingApi

All URIs are relative to *https://rest.nexmo.com/account*

Method | HTTP request | Description
------------- | ------------- | -------------
[**retrievePrefixPricing**](PricingApi.md#retrievePrefixPricing) | **GET** /get-prefix-pricing/outbound/{type} | Retrieve outbound pricing for a specific dialing prefix.
[**retrievePricingAllCountries**](PricingApi.md#retrievePricingAllCountries) | **GET** /get-full-pricing/outbound/{type} | Retrieve outbound pricing for all countries.
[**retrievePricingCountry**](PricingApi.md#retrievePricingCountry) | **GET** /get-pricing/outbound/{type} | Retrieve outbound pricing for a specific country.



## retrievePrefixPricing

> PricingCountriesResponse retrievePrefixPricing(type, apiKey, apiSecret, prefix)

Retrieve outbound pricing for a specific dialing prefix.

Retrieves the pricing information based on the dialing prefix. 

### Example

```javascript
import PricingApi from 'pricing_api';

let apiInstance = new PricingApi.PricingApi();
let type = "sms"; // String | The type of service you wish to retrieve data about: either `sms`, `sms-transit` or `voice`.
let apiKey = "apiKey_example"; // String | Your Nexmo API key.
let apiSecret = "apiSecret_example"; // String | Your Nexmo API secret.
let prefix = "prefix_example"; // String | The numerical dialing prefix to look up pricing for. Examples include 44, 1 and so on.
apiInstance.retrievePrefixPricing(type, apiKey, apiSecret, prefix, (error, data, response) => {
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
 **type** | **String**| The type of service you wish to retrieve data about: either &#x60;sms&#x60;, &#x60;sms-transit&#x60; or &#x60;voice&#x60;. | 
 **apiKey** | **String**| Your Nexmo API key. | 
 **apiSecret** | **String**| Your Nexmo API secret. | 
 **prefix** | **String**| The numerical dialing prefix to look up pricing for. Examples include 44, 1 and so on. | 

### Return type

[**PricingCountriesResponse**](PricingCountriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrievePricingAllCountries

> PricingCountriesResponse retrievePricingAllCountries(type, apiKey, apiSecret)

Retrieve outbound pricing for all countries.

Retrieves the pricing information for all countries. 

### Example

```javascript
import PricingApi from 'pricing_api';

let apiInstance = new PricingApi.PricingApi();
let type = "sms"; // String | The type of service you wish to retrieve data about: either `sms`, `sms-transit` or `voice`.
let apiKey = "apiKey_example"; // String | Your Nexmo API key.
let apiSecret = "apiSecret_example"; // String | Your Nexmo API secret.
apiInstance.retrievePricingAllCountries(type, apiKey, apiSecret, (error, data, response) => {
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
 **type** | **String**| The type of service you wish to retrieve data about: either &#x60;sms&#x60;, &#x60;sms-transit&#x60; or &#x60;voice&#x60;. | 
 **apiKey** | **String**| Your Nexmo API key. | 
 **apiSecret** | **String**| Your Nexmo API secret. | 

### Return type

[**PricingCountriesResponse**](PricingCountriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrievePricingCountry

> PricingCountryResponse retrievePricingCountry(type, apiKey, apiSecret, country)

Retrieve outbound pricing for a specific country.

Retrieves the pricing information based on the specified country. 

### Example

```javascript
import PricingApi from 'pricing_api';

let apiInstance = new PricingApi.PricingApi();
let type = "sms"; // String | The type of service you wish to retrieve data about: either `sms`, `sms-transit` or `voice`.
let apiKey = "apiKey_example"; // String | Your Nexmo API key.
let apiSecret = "apiSecret_example"; // String | Your Nexmo API secret.
let country = "country_example"; // String | A two letter [country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). For example, `CA`.
apiInstance.retrievePricingCountry(type, apiKey, apiSecret, country, (error, data, response) => {
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
 **type** | **String**| The type of service you wish to retrieve data about: either &#x60;sms&#x60;, &#x60;sms-transit&#x60; or &#x60;voice&#x60;. | 
 **apiKey** | **String**| Your Nexmo API key. | 
 **apiSecret** | **String**| Your Nexmo API secret. | 
 **country** | **String**| A two letter [country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). For example, &#x60;CA&#x60;. | 

### Return type

[**PricingCountryResponse**](PricingCountryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

