# MagentoB2B.NegotiableCartsCartIdTotalsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**negotiableQuoteCartTotalRepositoryV1GetGet**](NegotiableCartsCartIdTotalsApi.md#negotiableQuoteCartTotalRepositoryV1GetGet) | **GET** /V1/negotiable-carts/{cartId}/totals | negotiable-carts/{cartId}/totals



## negotiableQuoteCartTotalRepositoryV1GetGet

> QuoteDataTotalsInterface negotiableQuoteCartTotalRepositoryV1GetGet(cartId)

negotiable-carts/{cartId}/totals

Returns quote totals data for a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.NegotiableCartsCartIdTotalsApi();
let cartId = 56; // Number | The cart ID.
apiInstance.negotiableQuoteCartTotalRepositoryV1GetGet(cartId, (error, data, response) => {
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
 **cartId** | **Number**| The cart ID. | 

### Return type

[**QuoteDataTotalsInterface**](QuoteDataTotalsInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

