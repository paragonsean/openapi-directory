# MdesCustomerService.TransactionsApi

All URIs are relative to *https://api.mastercard.com/mdes/csapi/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transactionsPost**](TransactionsApi.md#transactionsPost) | **POST** /transactions | 



## transactionsPost

> TransactionsResponseSchema transactionsPost(opts)



Used to retrieve transactions performed by a token. It only returns transactions performed within the last 30 days, to help identify a particular token, or to identify a particular recent transaction. It is not intended to provide the full transaction history of a token or Account PAN.&lt;br&gt;&lt;br&gt;_Notes:_ The Transaction History API response is not supported for static Card on File (CoF) tokens.&lt;br&gt;If a set of tokens has been re-mapped to a new FPAN, all digital transactions will be made available before or after the FPAN has been updated. MDES does not return the value of the FPAN which was mapped to the particular token at the time of the transaction. However, MDES will return the history of all transactions performed on that particular token in the last 30 days, based on old and/or new FPAN. 

### Example

```javascript
import MdesCustomerService from 'mdes_customer_service';

let apiInstance = new MdesCustomerService.TransactionsApi();
let opts = {
  'transactionsRequestSchema': new MdesCustomerService.TransactionsRequestSchema() // TransactionsRequestSchema | Contains the details of the request message.
};
apiInstance.transactionsPost(opts, (error, data, response) => {
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
 **transactionsRequestSchema** | [**TransactionsRequestSchema**](TransactionsRequestSchema.md)| Contains the details of the request message. | [optional] 

### Return type

[**TransactionsResponseSchema**](TransactionsResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

