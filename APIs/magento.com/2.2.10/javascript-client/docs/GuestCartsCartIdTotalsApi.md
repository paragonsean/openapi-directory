# MagentoB2B.GuestCartsCartIdTotalsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteGuestCartTotalRepositoryV1GetGet**](GuestCartsCartIdTotalsApi.md#quoteGuestCartTotalRepositoryV1GetGet) | **GET** /V1/guest-carts/{cartId}/totals | guest-carts/{cartId}/totals



## quoteGuestCartTotalRepositoryV1GetGet

> QuoteDataTotalsInterface quoteGuestCartTotalRepositoryV1GetGet(cartId)

guest-carts/{cartId}/totals

Return quote totals data for a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdTotalsApi();
let cartId = "cartId_example"; // String | The cart ID.
apiInstance.quoteGuestCartTotalRepositoryV1GetGet(cartId, (error, data, response) => {
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
 **cartId** | **String**| The cart ID. | 

### Return type

[**QuoteDataTotalsInterface**](QuoteDataTotalsInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

