# MagentoB2B.NegotiableQuoteQuoteIdShippingMethodApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**negotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPut**](NegotiableQuoteQuoteIdShippingMethodApi.md#negotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPut) | **PUT** /V1/negotiableQuote/{quoteId}/shippingMethod | negotiableQuote/{quoteId}/shippingMethod



## negotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPut

> Boolean negotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPut(quoteId, opts)

negotiableQuote/{quoteId}/shippingMethod

Updates the shipping method on a negotiable quote.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.NegotiableQuoteQuoteIdShippingMethodApi();
let quoteId = 56; // Number | Negotiable Quote id
let opts = {
  'negotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest': new MagentoB2B.NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest() // NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest | 
};
apiInstance.negotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPut(quoteId, opts, (error, data, response) => {
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
 **quoteId** | **Number**| Negotiable Quote id | 
 **negotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest** | [**NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest**](NegotiableQuoteNegotiableQuoteShippingManagementV1SetShippingMethodPutRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

