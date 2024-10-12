# MagentoB2B.NegotiableQuoteSubmitToCustomerApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**negotiableQuoteNegotiableQuoteManagementV1AdminSendPost**](NegotiableQuoteSubmitToCustomerApi.md#negotiableQuoteNegotiableQuoteManagementV1AdminSendPost) | **POST** /V1/negotiableQuote/submitToCustomer | negotiableQuote/submitToCustomer



## negotiableQuoteNegotiableQuoteManagementV1AdminSendPost

> Boolean negotiableQuoteNegotiableQuoteManagementV1AdminSendPost(opts)

negotiableQuote/submitToCustomer

Submit the B2B quote to the customer. The quote status for the customer will be changed to &#39;Updated&#39;, and the customer can work with the quote.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.NegotiableQuoteSubmitToCustomerApi();
let opts = {
  'negotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest': new MagentoB2B.NegotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest() // NegotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest | 
};
apiInstance.negotiableQuoteNegotiableQuoteManagementV1AdminSendPost(opts, (error, data, response) => {
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
 **negotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest** | [**NegotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest**](NegotiableQuoteNegotiableQuoteManagementV1AdminSendPostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

