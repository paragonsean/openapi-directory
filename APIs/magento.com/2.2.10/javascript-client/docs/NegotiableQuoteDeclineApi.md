# MagentoB2B.NegotiableQuoteDeclineApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**negotiableQuoteNegotiableQuoteManagementV1DeclinePost**](NegotiableQuoteDeclineApi.md#negotiableQuoteNegotiableQuoteManagementV1DeclinePost) | **POST** /V1/negotiableQuote/decline | negotiableQuote/decline



## negotiableQuoteNegotiableQuoteManagementV1DeclinePost

> Boolean negotiableQuoteNegotiableQuoteManagementV1DeclinePost(opts)

negotiableQuote/decline

Decline the B2B quote. All custom pricing will be removed from this quote. The buyer will be able to place an order using their standard catalog prices and discounts.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.NegotiableQuoteDeclineApi();
let opts = {
  'negotiableQuoteNegotiableQuoteManagementV1DeclinePostRequest': new MagentoB2B.NegotiableQuoteNegotiableQuoteManagementV1DeclinePostRequest() // NegotiableQuoteNegotiableQuoteManagementV1DeclinePostRequest | 
};
apiInstance.negotiableQuoteNegotiableQuoteManagementV1DeclinePost(opts, (error, data, response) => {
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
 **negotiableQuoteNegotiableQuoteManagementV1DeclinePostRequest** | [**NegotiableQuoteNegotiableQuoteManagementV1DeclinePostRequest**](NegotiableQuoteNegotiableQuoteManagementV1DeclinePostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

