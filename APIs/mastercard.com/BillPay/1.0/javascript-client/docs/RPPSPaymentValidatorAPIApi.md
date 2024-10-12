# BillPaymentValidator.RPPSPaymentValidatorAPIApi

All URIs are relative to *https://api.mastercard.com/billpayAPI/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**isRoutingValidPost**](RPPSPaymentValidatorAPIApi.md#isRoutingValidPost) | **POST** /isRoutingValid | Bill Payment Validator service returns the processing status for a potential RPPS transaction



## isRoutingValidPost

> BillPayResponse isRoutingValidPost(opts)

Bill Payment Validator service returns the processing status for a potential RPPS transaction

Bill Payment Validator performs real time transaction validation against the specified Biller ID&#39;s account masks, account check digits and all other registered RPPS processing parameters.

### Example

```javascript
import BillPaymentValidator from 'bill_payment_validator';

let apiInstance = new BillPaymentValidator.RPPSPaymentValidatorAPIApi();
let opts = {
  'billPayRequest': new BillPaymentValidator.BillPayRequest() // BillPayRequest | Contains the details of the get PAR API request message.
};
apiInstance.isRoutingValidPost(opts, (error, data, response) => {
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
 **billPayRequest** | [**BillPayRequest**](BillPayRequest.md)| Contains the details of the get PAR API request message. | [optional] 

### Return type

[**BillPayResponse**](BillPayResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/JSON
- **Accept**: application/JSON

