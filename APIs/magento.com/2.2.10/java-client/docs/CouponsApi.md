# CouponsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesRuleCouponRepositoryV1SavePost**](CouponsApi.md#salesRuleCouponRepositoryV1SavePost) | **POST** /V1/coupons | coupons |


<a id="salesRuleCouponRepositoryV1SavePost"></a>
# **salesRuleCouponRepositoryV1SavePost**
> SalesRuleDataCouponInterface salesRuleCouponRepositoryV1SavePost(salesRuleCouponRepositoryV1SavePostRequest)

coupons

Save a coupon.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CouponsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CouponsApi apiInstance = new CouponsApi(defaultClient);
    SalesRuleCouponRepositoryV1SavePostRequest salesRuleCouponRepositoryV1SavePostRequest = new SalesRuleCouponRepositoryV1SavePostRequest(); // SalesRuleCouponRepositoryV1SavePostRequest | 
    try {
      SalesRuleDataCouponInterface result = apiInstance.salesRuleCouponRepositoryV1SavePost(salesRuleCouponRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CouponsApi#salesRuleCouponRepositoryV1SavePost");
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
| **salesRuleCouponRepositoryV1SavePostRequest** | [**SalesRuleCouponRepositoryV1SavePostRequest**](SalesRuleCouponRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**SalesRuleDataCouponInterface**](SalesRuleDataCouponInterface.md)

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

