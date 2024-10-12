# MagentoB2B.CouponsDeleteByCodesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesRuleCouponManagementV1DeleteByCodesPost**](CouponsDeleteByCodesApi.md#salesRuleCouponManagementV1DeleteByCodesPost) | **POST** /V1/coupons/deleteByCodes | coupons/deleteByCodes



## salesRuleCouponManagementV1DeleteByCodesPost

> SalesRuleDataCouponMassDeleteResultInterface salesRuleCouponManagementV1DeleteByCodesPost(opts)

coupons/deleteByCodes

Delete coupon by coupon codes.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CouponsDeleteByCodesApi();
let opts = {
  'salesRuleCouponManagementV1DeleteByCodesPostRequest': new MagentoB2B.SalesRuleCouponManagementV1DeleteByCodesPostRequest() // SalesRuleCouponManagementV1DeleteByCodesPostRequest | 
};
apiInstance.salesRuleCouponManagementV1DeleteByCodesPost(opts, (error, data, response) => {
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
 **salesRuleCouponManagementV1DeleteByCodesPostRequest** | [**SalesRuleCouponManagementV1DeleteByCodesPostRequest**](SalesRuleCouponManagementV1DeleteByCodesPostRequest.md)|  | [optional] 

### Return type

[**SalesRuleDataCouponMassDeleteResultInterface**](SalesRuleDataCouponMassDeleteResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

