# MagentoB2B.CartsCartIdTotalsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CartsCartIdTotalsGet**](CartsCartIdTotalsApi.md#v1CartsCartIdTotalsGet) | **GET** /V1/carts/{cartId}/totals | carts/{cartId}/totals



## v1CartsCartIdTotalsGet

> QuoteDataTotalsInterface v1CartsCartIdTotalsGet(cartId)

carts/{cartId}/totals

Returns quote totals data for a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdTotalsApi();
let cartId = 56; // Number | The cart ID.
apiInstance.v1CartsCartIdTotalsGet(cartId, (error, data, response) => {
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

