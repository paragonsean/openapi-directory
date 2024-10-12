# MagentoB2B.CartsMineCouponsCouponCodeApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteCouponManagementV1SetPut**](CartsMineCouponsCouponCodeApi.md#quoteCouponManagementV1SetPut) | **PUT** /V1/carts/mine/coupons/{couponCode} | carts/mine/coupons/{couponCode}



## quoteCouponManagementV1SetPut

> Boolean quoteCouponManagementV1SetPut(couponCode)

carts/mine/coupons/{couponCode}

Adds a coupon by code to a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineCouponsCouponCodeApi();
let couponCode = "couponCode_example"; // String | The coupon code data.
apiInstance.quoteCouponManagementV1SetPut(couponCode, (error, data, response) => {
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
 **couponCode** | **String**| The coupon code data. | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

