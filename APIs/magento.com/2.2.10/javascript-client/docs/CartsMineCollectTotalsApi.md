# MagentoB2B.CartsMineCollectTotalsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteCartTotalManagementV1CollectTotalsPut**](CartsMineCollectTotalsApi.md#quoteCartTotalManagementV1CollectTotalsPut) | **PUT** /V1/carts/mine/collect-totals | carts/mine/collect-totals



## quoteCartTotalManagementV1CollectTotalsPut

> QuoteDataTotalsInterface quoteCartTotalManagementV1CollectTotalsPut(opts)

carts/mine/collect-totals

Set shipping/billing methods and additional data for cart and collect totals.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineCollectTotalsApi();
let opts = {
  'quoteCartTotalManagementV1CollectTotalsPutRequest': new MagentoB2B.QuoteCartTotalManagementV1CollectTotalsPutRequest() // QuoteCartTotalManagementV1CollectTotalsPutRequest | 
};
apiInstance.quoteCartTotalManagementV1CollectTotalsPut(opts, (error, data, response) => {
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
 **quoteCartTotalManagementV1CollectTotalsPutRequest** | [**QuoteCartTotalManagementV1CollectTotalsPutRequest**](QuoteCartTotalManagementV1CollectTotalsPutRequest.md)|  | [optional] 

### Return type

[**QuoteDataTotalsInterface**](QuoteDataTotalsInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

