# MagentoB2B.CouponsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesRuleCouponRepositoryV1SavePost**](CouponsApi.md#salesRuleCouponRepositoryV1SavePost) | **POST** /V1/coupons | coupons



## salesRuleCouponRepositoryV1SavePost

> SalesRuleDataCouponInterface salesRuleCouponRepositoryV1SavePost(opts)

coupons

Save a coupon.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CouponsApi();
let opts = {
  'salesRuleCouponRepositoryV1SavePostRequest': new MagentoB2B.SalesRuleCouponRepositoryV1SavePostRequest() // SalesRuleCouponRepositoryV1SavePostRequest | 
};
apiInstance.salesRuleCouponRepositoryV1SavePost(opts, (error, data, response) => {
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
 **salesRuleCouponRepositoryV1SavePostRequest** | [**SalesRuleCouponRepositoryV1SavePostRequest**](SalesRuleCouponRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**SalesRuleDataCouponInterface**](SalesRuleDataCouponInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

