# MagentoB2B.NegotiableQuoteQuoteIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**negotiableQuoteNegotiableCartRepositoryV1SavePut**](NegotiableQuoteQuoteIdApi.md#negotiableQuoteNegotiableCartRepositoryV1SavePut) | **PUT** /V1/negotiableQuote/{quoteId} | negotiableQuote/{quoteId}



## negotiableQuoteNegotiableCartRepositoryV1SavePut

> ErrorResponse negotiableQuoteNegotiableCartRepositoryV1SavePut(quoteId, opts)

negotiableQuote/{quoteId}

Save quote

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.NegotiableQuoteQuoteIdApi();
let quoteId = "quoteId_example"; // String | 
let opts = {
  'quoteCartRepositoryV1SavePutRequest': new MagentoB2B.QuoteCartRepositoryV1SavePutRequest() // QuoteCartRepositoryV1SavePutRequest | 
};
apiInstance.negotiableQuoteNegotiableCartRepositoryV1SavePut(quoteId, opts, (error, data, response) => {
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
 **quoteId** | **String**|  | 
 **quoteCartRepositoryV1SavePutRequest** | [**QuoteCartRepositoryV1SavePutRequest**](QuoteCartRepositoryV1SavePutRequest.md)|  | [optional] 

### Return type

[**ErrorResponse**](ErrorResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

