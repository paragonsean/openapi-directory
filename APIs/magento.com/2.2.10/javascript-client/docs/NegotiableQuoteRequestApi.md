# MagentoB2B.NegotiableQuoteRequestApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**negotiableQuoteNegotiableQuoteManagementV1CreatePost**](NegotiableQuoteRequestApi.md#negotiableQuoteNegotiableQuoteManagementV1CreatePost) | **POST** /V1/negotiableQuote/request | negotiableQuote/request



## negotiableQuoteNegotiableQuoteManagementV1CreatePost

> Boolean negotiableQuoteNegotiableQuoteManagementV1CreatePost(opts)

negotiableQuote/request

Create a B2B quote based on a regular Magento quote. If the B2B quote requires a shipping address (for negotiation or tax calculations), add it to the regular quote before you create a B2B quote.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.NegotiableQuoteRequestApi();
let opts = {
  'negotiableQuoteNegotiableQuoteManagementV1CreatePostRequest': new MagentoB2B.NegotiableQuoteNegotiableQuoteManagementV1CreatePostRequest() // NegotiableQuoteNegotiableQuoteManagementV1CreatePostRequest | 
};
apiInstance.negotiableQuoteNegotiableQuoteManagementV1CreatePost(opts, (error, data, response) => {
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
 **negotiableQuoteNegotiableQuoteManagementV1CreatePostRequest** | [**NegotiableQuoteNegotiableQuoteManagementV1CreatePostRequest**](NegotiableQuoteNegotiableQuoteManagementV1CreatePostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

