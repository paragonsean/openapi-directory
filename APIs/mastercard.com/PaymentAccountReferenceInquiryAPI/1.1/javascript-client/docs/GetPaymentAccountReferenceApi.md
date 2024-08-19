# PaymentAccountReferenceInquiryApi.GetPaymentAccountReferenceApi

All URIs are relative to *https://sandbox.mastercard.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**parPaymentaccountreference10GetPaymentAccountReferencePost**](GetPaymentAccountReferenceApi.md#parPaymentaccountreference10GetPaymentAccountReferencePost) | **POST** /par/paymentaccountreference/1/0/getPaymentAccountReference | Submit an encrypted PAN to obtain the PAR linked to the account.



## parPaymentaccountreference10GetPaymentAccountReferencePost

> GetPaymentAccountReferenceResponseSchema parPaymentaccountreference10GetPaymentAccountReferencePost(opts)

Submit an encrypted PAN to obtain the PAR linked to the account.

The API performs a PAR query into the PAR Vault with the supplied PAN. When a PAR is returned from the PAR vault the API will encrypt it using the wrapped encryption method with the  Mastercard Customer?s Encryption Public Key and include it in the API response. 

### Example

```javascript
import PaymentAccountReferenceInquiryApi from 'payment_account_reference_inquiry_api';

let apiInstance = new PaymentAccountReferenceInquiryApi.GetPaymentAccountReferenceApi();
let opts = {
  'getPaymentAccountReferenceRequestSchema': new PaymentAccountReferenceInquiryApi.GetPaymentAccountReferenceRequestSchema() // GetPaymentAccountReferenceRequestSchema | Contains the details of the get PAR API request message.
};
apiInstance.parPaymentaccountreference10GetPaymentAccountReferencePost(opts, (error, data, response) => {
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
 **getPaymentAccountReferenceRequestSchema** | [**GetPaymentAccountReferenceRequestSchema**](GetPaymentAccountReferenceRequestSchema.md)| Contains the details of the get PAR API request message. | [optional] 

### Return type

[**GetPaymentAccountReferenceResponseSchema**](GetPaymentAccountReferenceResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

