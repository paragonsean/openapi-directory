# MagentoB2B.CartsCartIdCouponsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CartsCartIdCouponsDelete**](CartsCartIdCouponsApi.md#v1CartsCartIdCouponsDelete) | **DELETE** /V1/carts/{cartId}/coupons | carts/{cartId}/coupons
[**v1CartsCartIdCouponsGet**](CartsCartIdCouponsApi.md#v1CartsCartIdCouponsGet) | **GET** /V1/carts/{cartId}/coupons | carts/{cartId}/coupons



## v1CartsCartIdCouponsDelete

> Boolean v1CartsCartIdCouponsDelete(cartId)

carts/{cartId}/coupons

Deletes a coupon from a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdCouponsApi();
let cartId = 56; // Number | The cart ID.
apiInstance.v1CartsCartIdCouponsDelete(cartId, (error, data, response) => {
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


## v1CartsCartIdCouponsGet

> String v1CartsCartIdCouponsGet(cartId)

carts/{cartId}/coupons

Returns information for a coupon in a specified cart.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsCartIdCouponsApi();
let cartId = 56; // Number | The cart ID.
apiInstance.v1CartsCartIdCouponsGet(cartId, (error, data, response) => {
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

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

