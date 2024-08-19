# ApiForTheSettlementCurrencyRateConverter.CurrenciesApi

All URIs are relative to *http://api.mastercard.com/mcapi/settlement/currencyrate*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCurrencyRateDataUsingGET**](CurrenciesApi.md#getCurrencyRateDataUsingGET) | **GET** /settlement-currencies | getCurrencyRateData



## getCurrencyRateDataUsingGET

> SettlementCurrencyRequest getCurrencyRateDataUsingGET()

getCurrencyRateData

List of supported currencies.

### Example

```javascript
import ApiForTheSettlementCurrencyRateConverter from 'api_for_the_settlement_currency_rate_converter';

let apiInstance = new ApiForTheSettlementCurrencyRateConverter.CurrenciesApi();
apiInstance.getCurrencyRateDataUsingGET((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**SettlementCurrencyRequest**](SettlementCurrencyRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8

