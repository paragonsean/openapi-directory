# MagentoB2B.NegotiableQuoteQuoteIdCommentsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**negotiableQuoteCommentLocatorV1GetListForQuoteGet**](NegotiableQuoteQuoteIdCommentsApi.md#negotiableQuoteCommentLocatorV1GetListForQuoteGet) | **GET** /V1/negotiableQuote/{quoteId}/comments | negotiableQuote/{quoteId}/comments



## negotiableQuoteCommentLocatorV1GetListForQuoteGet

> [NegotiableQuoteDataCommentInterface] negotiableQuoteCommentLocatorV1GetListForQuoteGet(quoteId)

negotiableQuote/{quoteId}/comments

Returns comments for a specified negotiable quote.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.NegotiableQuoteQuoteIdCommentsApi();
let quoteId = 56; // Number | Negotiable Quote ID.
apiInstance.negotiableQuoteCommentLocatorV1GetListForQuoteGet(quoteId, (error, data, response) => {
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
 **quoteId** | **Number**| Negotiable Quote ID. | 

### Return type

[**[NegotiableQuoteDataCommentInterface]**](NegotiableQuoteDataCommentInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

