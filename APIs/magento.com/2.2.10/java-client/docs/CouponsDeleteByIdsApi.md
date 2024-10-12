# CouponsDeleteByIdsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesRuleCouponManagementV1DeleteByIdsPost**](CouponsDeleteByIdsApi.md#salesRuleCouponManagementV1DeleteByIdsPost) | **POST** /V1/coupons/deleteByIds | coupons/deleteByIds |


<a id="salesRuleCouponManagementV1DeleteByIdsPost"></a>
# **salesRuleCouponManagementV1DeleteByIdsPost**
> SalesRuleDataCouponMassDeleteResultInterface salesRuleCouponManagementV1DeleteByIdsPost(salesRuleCouponManagementV1DeleteByIdsPostRequest)

coupons/deleteByIds

Delete coupon by coupon ids.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CouponsDeleteByIdsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CouponsDeleteByIdsApi apiInstance = new CouponsDeleteByIdsApi(defaultClient);
    SalesRuleCouponManagementV1DeleteByIdsPostRequest salesRuleCouponManagementV1DeleteByIdsPostRequest = new SalesRuleCouponManagementV1DeleteByIdsPostRequest(); // SalesRuleCouponManagementV1DeleteByIdsPostRequest | 
    try {
      SalesRuleDataCouponMassDeleteResultInterface result = apiInstance.salesRuleCouponManagementV1DeleteByIdsPost(salesRuleCouponManagementV1DeleteByIdsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CouponsDeleteByIdsApi#salesRuleCouponManagementV1DeleteByIdsPost");
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
| **salesRuleCouponManagementV1DeleteByIdsPostRequest** | [**SalesRuleCouponManagementV1DeleteByIdsPostRequest**](SalesRuleCouponManagementV1DeleteByIdsPostRequest.md)|  | [optional] |

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

