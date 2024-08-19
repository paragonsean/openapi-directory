# ApiForTheSettlementCurrencyRateConverter.RateIssuedApi

All URIs are relative to *http://api.mastercard.com/mcapi/settlement/currencyrate*

Method | HTTP request | Description
------------- | ------------- | -------------
[**isRateIssuedUsingGET**](RateIssuedApi.md#isRateIssuedUsingGET) | **GET** /conversion-rate-issued | Determine if the settlement rate has been issued.



## isRateIssuedUsingGET

> SettlementRateIssuedRequest isRateIssuedUsingGET(opts)

Determine if the settlement rate has been issued.

Determine if the settlement rate has been issued.

### Example

```javascript
import ApiForTheSettlementCurrencyRateConverter from 'api_for_the_settlement_currency_rate_converter';

let apiInstance = new ApiForTheSettlementCurrencyRateConverter.RateIssuedApi();
let opts = {
  'date': "date_example" // String | The date by which the rate would have been issued.
};
apiInstance.isRateIssuedUsingGET(opts, (error, data, response) => {
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
 **date** | **String**| The date by which the rate would have been issued. | [optional] 

### Return type

[**SettlementRateIssuedRequest**](SettlementRateIssuedRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8

