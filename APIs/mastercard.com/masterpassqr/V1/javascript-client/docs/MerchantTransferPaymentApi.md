# SendPersonToMerchant.MerchantTransferPaymentApi

All URIs are relative to *https://api.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createMerchantPayment**](MerchantTransferPaymentApi.md#createMerchantPayment) | **POST** /send/#env/v1/partners/{partnerId}/merchant/transfers/payment | Initiates a Mastercard Merchant Presented QR purchase transaction by pushing funds to a merchant account.



## createMerchantPayment

> MerchantTransfer40Wrapper createMerchantPayment(partnerId, opts)

Initiates a Mastercard Merchant Presented QR purchase transaction by pushing funds to a merchant account.

Initiates a Mastercard Merchant Presented QR purchase transaction by pushing funds to a merchant account.

### Example

```javascript
import SendPersonToMerchant from 'send_person_to_merchant';

let apiInstance = new SendPersonToMerchant.MerchantTransferPaymentApi();
let partnerId = "partnerId_example"; // String | Path Param - Provider assigned partner id. Details - string, 32
let opts = {
  'merchantPaymentTransfer': new SendPersonToMerchant.MerchantPaymentTransfer29Wrapper() // MerchantPaymentTransfer29Wrapper | Contains the details of the request message.
};
apiInstance.createMerchantPayment(partnerId, opts, (error, data, response) => {
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
 **merchantPaymentTransfer** | [**MerchantPaymentTransfer29Wrapper**](MerchantPaymentTransfer29Wrapper.md)| Contains the details of the request message. | [optional] 

### Return type

[**MerchantTransfer40Wrapper**](MerchantTransfer40Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

