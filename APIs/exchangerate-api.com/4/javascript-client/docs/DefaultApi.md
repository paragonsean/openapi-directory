# ExchangeRateApi.DefaultApi

All URIs are relative to *https://api.exchangerate-api.com/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**latestBaseCurrencyGet**](DefaultApi.md#latestBaseCurrencyGet) | **GET** /latest/{base_currency} | Returns latest exchange rates in parameter-supplied base currency.



## latestBaseCurrencyGet

> LatestBaseCurrencyGet200Response latestBaseCurrencyGet(baseCurrency)

Returns latest exchange rates in parameter-supplied base currency.

### Example

```javascript
import ExchangeRateApi from 'exchange_rate_api';

let apiInstance = new ExchangeRateApi.DefaultApi();
let baseCurrency = "baseCurrency_example"; // String | **Base Currency**. *Example: USD*. You an use any of the ISO 4217 currency codes we support. See https://www.exchangerate-api.com/docs/supported-currencies
apiInstance.latestBaseCurrencyGet(baseCurrency, (error, data, response) => {
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
 **baseCurrency** | **String**| **Base Currency**. *Example: USD*. You an use any of the ISO 4217 currency codes we support. See https://www.exchangerate-api.com/docs/supported-currencies | 

### Return type

[**LatestBaseCurrencyGet200Response**](LatestBaseCurrencyGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

