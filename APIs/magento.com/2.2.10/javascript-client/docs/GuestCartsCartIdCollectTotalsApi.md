# MagentoB2B.GuestCartsCartIdCollectTotalsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteGuestCartTotalManagementV1CollectTotalsPut**](GuestCartsCartIdCollectTotalsApi.md#quoteGuestCartTotalManagementV1CollectTotalsPut) | **PUT** /V1/guest-carts/{cartId}/collect-totals | guest-carts/{cartId}/collect-totals



## quoteGuestCartTotalManagementV1CollectTotalsPut

> QuoteDataTotalsInterface quoteGuestCartTotalManagementV1CollectTotalsPut(cartId, opts)

guest-carts/{cartId}/collect-totals

Set shipping/billing methods and additional data for cart and collect totals for guest.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdCollectTotalsApi();
let cartId = "cartId_example"; // String | The cart ID.
let opts = {
  'quoteCartTotalManagementV1CollectTotalsPutRequest': new MagentoB2B.QuoteCartTotalManagementV1CollectTotalsPutRequest() // QuoteCartTotalManagementV1CollectTotalsPutRequest | 
};
apiInstance.quoteGuestCartTotalManagementV1CollectTotalsPut(cartId, opts, (error, data, response) => {
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
 **quoteCartTotalManagementV1CollectTotalsPutRequest** | [**QuoteCartTotalManagementV1CollectTotalsPutRequest**](QuoteCartTotalManagementV1CollectTotalsPutRequest.md)|  | [optional] 

### Return type

[**QuoteDataTotalsInterface**](QuoteDataTotalsInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

