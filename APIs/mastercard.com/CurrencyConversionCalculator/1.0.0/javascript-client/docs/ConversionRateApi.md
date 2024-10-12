# ApiForTheSettlementCurrencyRateConverter.ConversionRateApi

All URIs are relative to *http://api.mastercard.com/mcapi/settlement/currencyrate*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getConversionDetailUsingGET**](ConversionRateApi.md#getConversionDetailUsingGET) | **GET** /conversion-rate | Get the currency conversion rate details.



## getConversionDetailUsingGET

> ConversionRateRequest getConversionDetailUsingGET(fxDate, transCurr, crdhldBillCurr, transAmt, opts)

Get the currency conversion rate details.

Get the currency conversion rate details.

### Example

```javascript
import ApiForTheSettlementCurrencyRateConverter from 'api_for_the_settlement_currency_rate_converter';

let apiInstance = new ApiForTheSettlementCurrencyRateConverter.ConversionRateApi();
let fxDate = "fxDate_example"; // String | Date of the requested FX rates.
let transCurr = "transCurr_example"; // String | Currency of the transaction.
let crdhldBillCurr = "crdhldBillCurr_example"; // String | Cardholder billing currency.
let transAmt = 3.4; // Number | Amount in the transaction currency.
let opts = {
  'bankFee': 3.4 // Number | Additional fees imposed by the bank.
};
apiInstance.getConversionDetailUsingGET(fxDate, transCurr, crdhldBillCurr, transAmt, opts, (error, data, response) => {
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
 **fxDate** | **String**| Date of the requested FX rates. | 
 **transCurr** | **String**| Currency of the transaction. | 
 **crdhldBillCurr** | **String**| Cardholder billing currency. | 
 **transAmt** | **Number**| Amount in the transaction currency. | 
 **bankFee** | **Number**| Additional fees imposed by the bank. | [optional] 

### Return type

[**ConversionRateRequest**](ConversionRateRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json;charset=UTF-8

