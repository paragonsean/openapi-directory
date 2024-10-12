# MagentoB2B.NegotiableCartsCartIdCouponsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**negotiableQuoteCouponManagementV1RemoveDelete**](NegotiableCartsCartIdCouponsApi.md#negotiableQuoteCouponManagementV1RemoveDelete) | **DELETE** /V1/negotiable-carts/{cartId}/coupons | negotiable-carts/{cartId}/coupons



## negotiableQuoteCouponManagementV1RemoveDelete

> Boolean negotiableQuoteCouponManagementV1RemoveDelete(cartId)

negotiable-carts/{cartId}/coupons

Deletes a coupon from a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.NegotiableCartsCartIdCouponsApi();
let cartId = 56; // Number | The cart ID.
apiInstance.negotiableQuoteCouponManagementV1RemoveDelete(cartId, (error, data, response) => {
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

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

