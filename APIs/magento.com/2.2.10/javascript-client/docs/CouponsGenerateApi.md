# MagentoB2B.CouponsGenerateApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**salesRuleCouponManagementV1GeneratePost**](CouponsGenerateApi.md#salesRuleCouponManagementV1GeneratePost) | **POST** /V1/coupons/generate | coupons/generate



## salesRuleCouponManagementV1GeneratePost

> [String] salesRuleCouponManagementV1GeneratePost(opts)

coupons/generate

Generate coupon for a rule

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CouponsGenerateApi();
let opts = {
  'salesRuleCouponManagementV1GeneratePostRequest': new MagentoB2B.SalesRuleCouponManagementV1GeneratePostRequest() // SalesRuleCouponManagementV1GeneratePostRequest | 
};
apiInstance.salesRuleCouponManagementV1GeneratePost(opts, (error, data, response) => {
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
 **salesRuleCouponManagementV1GeneratePostRequest** | [**SalesRuleCouponManagementV1GeneratePostRequest**](SalesRuleCouponManagementV1GeneratePostRequest.md)|  | [optional] 

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

