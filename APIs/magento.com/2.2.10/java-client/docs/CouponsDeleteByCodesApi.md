# CouponsDeleteByCodesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesRuleCouponManagementV1DeleteByCodesPost**](CouponsDeleteByCodesApi.md#salesRuleCouponManagementV1DeleteByCodesPost) | **POST** /V1/coupons/deleteByCodes | coupons/deleteByCodes |


<a id="salesRuleCouponManagementV1DeleteByCodesPost"></a>
# **salesRuleCouponManagementV1DeleteByCodesPost**
> SalesRuleDataCouponMassDeleteResultInterface salesRuleCouponManagementV1DeleteByCodesPost(salesRuleCouponManagementV1DeleteByCodesPostRequest)

coupons/deleteByCodes

Delete coupon by coupon codes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CouponsDeleteByCodesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CouponsDeleteByCodesApi apiInstance = new CouponsDeleteByCodesApi(defaultClient);
    SalesRuleCouponManagementV1DeleteByCodesPostRequest salesRuleCouponManagementV1DeleteByCodesPostRequest = new SalesRuleCouponManagementV1DeleteByCodesPostRequest(); // SalesRuleCouponManagementV1DeleteByCodesPostRequest | 
    try {
      SalesRuleDataCouponMassDeleteResultInterface result = apiInstance.salesRuleCouponManagementV1DeleteByCodesPost(salesRuleCouponManagementV1DeleteByCodesPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CouponsDeleteByCodesApi#salesRuleCouponManagementV1DeleteByCodesPost");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **salesRuleCouponManagementV1DeleteByCodesPostRequest** | [**SalesRuleCouponManagementV1DeleteByCodesPostRequest**](SalesRuleCouponManagementV1DeleteByCodesPostRequest.md)|  | [optional] |

### Return type

[**SalesRuleDataCouponMassDeleteResultInterface**](SalesRuleDataCouponMassDeleteResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

