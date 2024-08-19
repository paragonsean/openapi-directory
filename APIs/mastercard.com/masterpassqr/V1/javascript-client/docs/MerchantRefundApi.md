# SendPersonToMerchant.MerchantRefundApi

All URIs are relative to *https://api.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createMerchantRefund**](MerchantRefundApi.md#createMerchantRefund) | **POST** /send/#env/v1/partners/{partnerId}/merchant/transfers/refund | Initiates a Mastercard Merchant Presented QR Refund transaction by pushing funds from a merchant account back to the customer&#39;s account.



## createMerchantRefund

> MerchantTransfer104Wrapper createMerchantRefund(partnerId, opts)

Initiates a Mastercard Merchant Presented QR Refund transaction by pushing funds from a merchant account back to the customer&#39;s account.

Initiates a Mastercard Merchant Presented QR Refund transaction by pushing funds from a merchant account back to the customer&#39;s account.

### Example

```javascript
import SendPersonToMerchant from 'send_person_to_merchant';

let apiInstance = new SendPersonToMerchant.MerchantRefundApi();
let partnerId = "partnerId_example"; // String | Path Param - Provider assigned partner id. Details - string, 32
let opts = {
  'merchantRefundTransfer': new SendPersonToMerchant.MerchantRefundTransfer93Wrapper() // MerchantRefundTransfer93Wrapper | Contains the details of the request message.
};
apiInstance.createMerchantRefund(partnerId, opts, (error, data, response) => {
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
 **merchantRefundTransfer** | [**MerchantRefundTransfer93Wrapper**](MerchantRefundTransfer93Wrapper.md)| Contains the details of the request message. | [optional] 

### Return type

[**MerchantTransfer104Wrapper**](MerchantTransfer104Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

