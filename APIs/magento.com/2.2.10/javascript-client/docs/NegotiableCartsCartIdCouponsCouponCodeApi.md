# MagentoB2B.NegotiableCartsCartIdCouponsCouponCodeApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**negotiableQuoteCouponManagementV1SetPut**](NegotiableCartsCartIdCouponsCouponCodeApi.md#negotiableQuoteCouponManagementV1SetPut) | **PUT** /V1/negotiable-carts/{cartId}/coupons/{couponCode} | negotiable-carts/{cartId}/coupons/{couponCode}



## negotiableQuoteCouponManagementV1SetPut

> Boolean negotiableQuoteCouponManagementV1SetPut(cartId, couponCode)

negotiable-carts/{cartId}/coupons/{couponCode}

Adds a coupon by code to a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.NegotiableCartsCartIdCouponsCouponCodeApi();
let cartId = 56; // Number | The cart ID.
let couponCode = "couponCode_example"; // String | The coupon code data.
apiInstance.negotiableQuoteCouponManagementV1SetPut(cartId, couponCode, (error, data, response) => {
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

