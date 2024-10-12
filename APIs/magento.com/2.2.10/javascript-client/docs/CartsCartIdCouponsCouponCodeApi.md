# MagentoB2B.CartsCartIdCouponsCouponCodeApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CartsCartIdCouponsCouponCodePut**](CartsCartIdCouponsCouponCodeApi.md#v1CartsCartIdCouponsCouponCodePut) | **PUT** /V1/carts/{cartId}/coupons/{couponCode} | carts/{cartId}/coupons/{couponCode}



## v1CartsCartIdCouponsCouponCodePut

> Boolean v1CartsCartIdCouponsCouponCodePut(cartId, couponCode)

carts/{cartId}/coupons/{couponCode}

Adds a coupon by code to a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdCouponsCouponCodeApi();
let cartId = 56; // Number | The cart ID.
let couponCode = "couponCode_example"; // String | The coupon code data.
apiInstance.v1CartsCartIdCouponsCouponCodePut(cartId, couponCode, (error, data, response) => {
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
 **couponCode** | **String**| The coupon code data. | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

