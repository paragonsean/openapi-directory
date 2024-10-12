# MagentoB2B.GuestCartsCartIdCouponsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**quoteGuestCouponManagementV1GetGet**](GuestCartsCartIdCouponsApi.md#quoteGuestCouponManagementV1GetGet) | **GET** /V1/guest-carts/{cartId}/coupons | guest-carts/{cartId}/coupons
[**quoteGuestCouponManagementV1RemoveDelete**](GuestCartsCartIdCouponsApi.md#quoteGuestCouponManagementV1RemoveDelete) | **DELETE** /V1/guest-carts/{cartId}/coupons | guest-carts/{cartId}/coupons



## quoteGuestCouponManagementV1GetGet

> String quoteGuestCouponManagementV1GetGet(cartId)

guest-carts/{cartId}/coupons

Return information for a coupon in a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdCouponsApi();
let cartId = "cartId_example"; // String | The cart ID.
apiInstance.quoteGuestCouponManagementV1GetGet(cartId, (error, data, response) => {
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

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## quoteGuestCouponManagementV1RemoveDelete

> Boolean quoteGuestCouponManagementV1RemoveDelete(cartId)

guest-carts/{cartId}/coupons

Delete a coupon from a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdCouponsApi();
let cartId = "cartId_example"; // String | The cart ID.
apiInstance.quoteGuestCouponManagementV1RemoveDelete(cartId, (error, data, response) => {
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

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

