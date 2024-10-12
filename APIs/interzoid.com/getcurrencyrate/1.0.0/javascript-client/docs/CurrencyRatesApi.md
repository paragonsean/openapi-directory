# InterzoidGetCurrencyRateApi.CurrencyRatesApi

All URIs are relative to *https://api.interzoid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getcurrencyrate**](CurrencyRatesApi.md#getcurrencyrate) | **GET** /getcurrencyrate | Gets a foreign currency rate for one US Dollar



## getcurrencyrate

> Getcurrencyrate200Response getcurrencyrate(license, symbol)

Gets a foreign currency rate for one US Dollar

Use a currency symbol (EUR, GBP, CNY, JPY, AUD, etc.) to obtain a live currency foreign exchange rate for one US Dollar. See the API home page for list of all supported currencies.

### Example

```javascript
import InterzoidGetCurrencyRateApi from 'interzoid_get_currency_rate_api';

let apiInstance = new InterzoidGetCurrencyRateApi.CurrencyRatesApi();
let license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
let symbol = "symbol_example"; // String | Currency symbol to retrieve current rate for
apiInstance.getcurrencyrate(license, symbol, (error, data, response) => {
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
 **license** | **String**| Your Interzoid license API key. Register at www.interzoid.com/register | 
 **symbol** | **String**| Currency symbol to retrieve current rate for | 

### Return type

[**Getcurrencyrate200Response**](Getcurrencyrate200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

