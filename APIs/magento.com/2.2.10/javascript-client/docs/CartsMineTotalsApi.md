# MagentoB2B.CartsMineTotalsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteCartTotalRepositoryV1GetGet**](CartsMineTotalsApi.md#quoteCartTotalRepositoryV1GetGet) | **GET** /V1/carts/mine/totals | carts/mine/totals



## quoteCartTotalRepositoryV1GetGet

> QuoteDataTotalsInterface quoteCartTotalRepositoryV1GetGet()

carts/mine/totals

Returns quote totals data for a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineTotalsApi();
apiInstance.quoteCartTotalRepositoryV1GetGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**QuoteDataTotalsInterface**](QuoteDataTotalsInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

