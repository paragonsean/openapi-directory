# MagentoB2B.GuestCartsCartIdCouponsCouponCodeApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteGuestCouponManagementV1SetPut**](GuestCartsCartIdCouponsCouponCodeApi.md#quoteGuestCouponManagementV1SetPut) | **PUT** /V1/guest-carts/{cartId}/coupons/{couponCode} | guest-carts/{cartId}/coupons/{couponCode}



## quoteGuestCouponManagementV1SetPut

> Boolean quoteGuestCouponManagementV1SetPut(cartId, couponCode)

guest-carts/{cartId}/coupons/{couponCode}

Add a coupon by code to a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdCouponsCouponCodeApi();
let cartId = "cartId_example"; // String | The cart ID.
let couponCode = "couponCode_example"; // String | The coupon code data.
apiInstance.quoteGuestCouponManagementV1SetPut(cartId, couponCode, (error, data, response) => {
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
 **couponCode** | **String**| The coupon code data. | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

