# SendPersonToMerchant.MerchantTransferFundingAndPaymentApi

All URIs are relative to *https://api.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createMerchantTransfer**](MerchantTransferFundingAndPaymentApi.md#createMerchantTransfer) | **POST** /send/#env/v1/partners/{partnerId}/merchant/transfer | Initiates a Mastercard Merchant Presented QR purchase transaction by securing funds from a consumer’s account with a Funding Transaction and pushing funds to a merchant account with a Payment Transaction.



## createMerchantTransfer

> MerchantTransfer14Wrapper createMerchantTransfer(partnerId, merchantTransfer)

Initiates a Mastercard Merchant Presented QR purchase transaction by securing funds from a consumer’s account with a Funding Transaction and pushing funds to a merchant account with a Payment Transaction.

Initiates a Mastercard Merchant Presented QR purchase transaction by securing funds from a consumer’s account with a Funding Transaction and pushing funds to a merchant account with a Payment Transaction.

### Example

```javascript
import SendPersonToMerchant from 'send_person_to_merchant';

let apiInstance = new SendPersonToMerchant.MerchantTransferFundingAndPaymentApi();
let partnerId = "ptnr_A37V2q91WUqSonkfEG29Q-Bf4s9"; // String | Path Param - Provider assigned partner id.   Type: Alphanumeric Special  [a-zA-Z0-9_-], Length: 32
let merchantTransfer = new SendPersonToMerchant.MerchantTransfer1Wrapper(); // MerchantTransfer1Wrapper | Contains the details of the request message.
apiInstance.createMerchantTransfer(partnerId, merchantTransfer, (error, data, response) => {
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
 **partnerId** | **String**| Path Param - Provider assigned partner id.   Type: Alphanumeric Special  [a-zA-Z0-9_-], Length: 32 | 
 **merchantTransfer** | [**MerchantTransfer1Wrapper**](MerchantTransfer1Wrapper.md)| Contains the details of the request message. | 

### Return type

[**MerchantTransfer14Wrapper**](MerchantTransfer14Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

