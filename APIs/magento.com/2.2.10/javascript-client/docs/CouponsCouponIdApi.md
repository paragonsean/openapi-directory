# MagentoB2B.CouponsCouponIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesRuleCouponRepositoryV1DeleteByIdDelete**](CouponsCouponIdApi.md#salesRuleCouponRepositoryV1DeleteByIdDelete) | **DELETE** /V1/coupons/{couponId} | coupons/{couponId}
[**salesRuleCouponRepositoryV1GetByIdGet**](CouponsCouponIdApi.md#salesRuleCouponRepositoryV1GetByIdGet) | **GET** /V1/coupons/{couponId} | coupons/{couponId}
[**salesRuleCouponRepositoryV1SavePut**](CouponsCouponIdApi.md#salesRuleCouponRepositoryV1SavePut) | **PUT** /V1/coupons/{couponId} | coupons/{couponId}



## salesRuleCouponRepositoryV1DeleteByIdDelete

> Boolean salesRuleCouponRepositoryV1DeleteByIdDelete(couponId)

coupons/{couponId}

Delete coupon by coupon id.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CouponsCouponIdApi();
let couponId = 56; // Number | 
apiInstance.salesRuleCouponRepositoryV1DeleteByIdDelete(couponId, (error, data, response) => {
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
 **couponId** | **Number**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## salesRuleCouponRepositoryV1GetByIdGet

> SalesRuleDataCouponInterface salesRuleCouponRepositoryV1GetByIdGet(couponId)

coupons/{couponId}

Get coupon by coupon id.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CouponsCouponIdApi();
let couponId = 56; // Number | 
apiInstance.salesRuleCouponRepositoryV1GetByIdGet(couponId, (error, data, response) => {
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
 **couponId** | **Number**|  | 

### Return type

[**SalesRuleDataCouponInterface**](SalesRuleDataCouponInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## salesRuleCouponRepositoryV1SavePut

> SalesRuleDataCouponInterface salesRuleCouponRepositoryV1SavePut(couponId, opts)

coupons/{couponId}

Save a coupon.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CouponsCouponIdApi();
let couponId = "couponId_example"; // String | 
let opts = {
  'salesRuleCouponRepositoryV1SavePostRequest': new MagentoB2B.SalesRuleCouponRepositoryV1SavePostRequest() // SalesRuleCouponRepositoryV1SavePostRequest | 
};
apiInstance.salesRuleCouponRepositoryV1SavePut(couponId, opts, (error, data, response) => {
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
 **couponId** | **String**|  | 
 **salesRuleCouponRepositoryV1SavePostRequest** | [**SalesRuleCouponRepositoryV1SavePostRequest**](SalesRuleCouponRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**SalesRuleDataCouponInterface**](SalesRuleDataCouponInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

