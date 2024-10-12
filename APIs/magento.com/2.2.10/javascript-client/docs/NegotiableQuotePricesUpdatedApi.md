# MagentoB2B.NegotiableQuotePricesUpdatedApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**negotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPost**](NegotiableQuotePricesUpdatedApi.md#negotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPost) | **POST** /V1/negotiableQuote/pricesUpdated | negotiableQuote/pricesUpdated



## negotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPost

> Boolean negotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPost(opts)

negotiableQuote/pricesUpdated

Refreshes item prices, taxes, discounts, cart rules in the negotiable quote as per the latest changes in the catalog / shared catalog and in the price rules. Depending on the negotiable quote state and totals, all or just some of quote numbers will be recalculated. &#39;Update Prices&#39; parameter forces refresh on any quote that is not locked for admin user, including the quotes with a negotiated price. The request can be applied to one or more quotes at the same time.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.NegotiableQuotePricesUpdatedApi();
let opts = {
  'negotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPostRequest': new MagentoB2B.NegotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPostRequest() // NegotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPostRequest | 
};
apiInstance.negotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPost(opts, (error, data, response) => {
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
 **negotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPostRequest** | [**NegotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPostRequest**](NegotiableQuoteNegotiableQuotePriceManagementV1PricesUpdatedPostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

