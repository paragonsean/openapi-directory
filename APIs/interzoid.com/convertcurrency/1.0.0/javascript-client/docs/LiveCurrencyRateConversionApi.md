# InterzoidConvertCurrencyRateApi.LiveCurrencyRateConversionApi

All URIs are relative to *https://api.interzoid.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convertcurrency**](LiveCurrencyRateConversionApi.md#convertcurrency) | **GET** /convertcurrency | Converts amount in one currency to that of another



## convertcurrency

> Convertcurrency200Response convertcurrency(license, from, to, amount)

Converts amount in one currency to that of another

Provide an amount in one currency (EUR, GBP, CNY, JPY, AUD, etc.), and also a second currency to convert it to. The API will return the result using current foreign exchange rates. See the API home page for a list of all supported currencies.

### Example

```javascript
import InterzoidConvertCurrencyRateApi from 'interzoid_convert_currency_rate_api';

let apiInstance = new InterzoidConvertCurrencyRateApi.LiveCurrencyRateConversionApi();
let license = "license_example"; // String | Your Interzoid license API key. Register at www.interzoid.com/register
let from = "from_example"; // String | Currency symbol for the converted from amount
let to = "to_example"; // String | Currency symbol for the converted to amount
let amount = "amount_example"; // String | The amount of currency to be converted
apiInstance.convertcurrency(license, from, to, amount, (error, data, response) => {
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
 **from** | **String**| Currency symbol for the converted from amount | 
 **to** | **String**| Currency symbol for the converted to amount | 
 **amount** | **String**| The amount of currency to be converted | 

### Return type

[**Convertcurrency200Response**](Convertcurrency200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

