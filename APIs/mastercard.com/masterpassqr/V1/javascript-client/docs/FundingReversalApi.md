# SendPersonToMerchant.FundingReversalApi

All URIs are relative to *https://api.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createFundingReversal**](FundingReversalApi.md#createFundingReversal) | **POST** /send/v1/partners/{partner-id}/transfers/{transfer-id}/transactions/{transaction-id}/reversals | Funding Reversals must be submitted within 30 minutes of the funding transfer request, and should only be submitted for the following conditions:  Funding Transaction must be reversed if payment transaction cannot complete successfully, i.e. the payment transaction is rejected or declined.  Upon a successful reversal of a funding transaction, the refund must be credited to the sending consumer’s Funding Account.



## createFundingReversal

> Transfer145Wrapper createFundingReversal(partnerId, transferId, transactionId, opts)

Funding Reversals must be submitted within 30 minutes of the funding transfer request, and should only be submitted for the following conditions:  Funding Transaction must be reversed if payment transaction cannot complete successfully, i.e. the payment transaction is rejected or declined.  Upon a successful reversal of a funding transaction, the refund must be credited to the sending consumer’s Funding Account.

Funding Reversals must be submitted within 30 minutes of the funding transfer request, and should only be submitted for the following conditions:  Funding Transaction must be reversed if payment transaction cannot complete successfully, i.e. the payment transaction is rejected or declined.  Upon a successful reversal of a funding transaction, the refund must be credited to the sending consumer’s Funding Account.

### Example

```javascript
import SendPersonToMerchant from 'send_person_to_merchant';

let apiInstance = new SendPersonToMerchant.FundingReversalApi();
let partnerId = "partnerId_example"; // String | Path Param - Provider assigned partner id. Details - string, 32
let transferId = "transferId_example"; // String | Valid transfer id
let transactionId = "transactionId_example"; // String | Valid transaction id
let opts = {
  'fundingReversal': new SendPersonToMerchant.FundingReversal144Wrapper() // FundingReversal144Wrapper | Contains the details of the request message.
};
apiInstance.createFundingReversal(partnerId, transferId, transactionId, opts, (error, data, response) => {
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
 **partnerId** | **String**| Path Param - Provider assigned partner id. Details - string, 32 | 
 **transferId** | **String**| Valid transfer id | 
 **transactionId** | **String**| Valid transaction id | 
 **fundingReversal** | [**FundingReversal144Wrapper**](FundingReversal144Wrapper.md)| Contains the details of the request message. | [optional] 

### Return type

[**Transfer145Wrapper**](Transfer145Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/xml
- **Accept**: application/xml

