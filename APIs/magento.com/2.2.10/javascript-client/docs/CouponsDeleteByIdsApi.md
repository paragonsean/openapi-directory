# MagentoB2B.CouponsDeleteByIdsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesRuleCouponManagementV1DeleteByIdsPost**](CouponsDeleteByIdsApi.md#salesRuleCouponManagementV1DeleteByIdsPost) | **POST** /V1/coupons/deleteByIds | coupons/deleteByIds



## salesRuleCouponManagementV1DeleteByIdsPost

> SalesRuleDataCouponMassDeleteResultInterface salesRuleCouponManagementV1DeleteByIdsPost(opts)

coupons/deleteByIds

Delete coupon by coupon ids.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CouponsDeleteByIdsApi();
let opts = {
  'salesRuleCouponManagementV1DeleteByIdsPostRequest': new MagentoB2B.SalesRuleCouponManagementV1DeleteByIdsPostRequest() // SalesRuleCouponManagementV1DeleteByIdsPostRequest | 
};
apiInstance.salesRuleCouponManagementV1DeleteByIdsPost(opts, (error, data, response) => {
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
 **salesRuleCouponManagementV1DeleteByIdsPostRequest** | [**SalesRuleCouponManagementV1DeleteByIdsPostRequest**](SalesRuleCouponManagementV1DeleteByIdsPostRequest.md)|  | [optional] 

### Return type

[**SalesRuleDataCouponMassDeleteResultInterface**](SalesRuleDataCouponMassDeleteResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

