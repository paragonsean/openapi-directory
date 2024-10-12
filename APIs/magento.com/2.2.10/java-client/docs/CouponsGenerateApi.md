# CouponsGenerateApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesRuleCouponManagementV1GeneratePost**](CouponsGenerateApi.md#salesRuleCouponManagementV1GeneratePost) | **POST** /V1/coupons/generate | coupons/generate |


<a id="salesRuleCouponManagementV1GeneratePost"></a>
# **salesRuleCouponManagementV1GeneratePost**
> List&lt;String&gt; salesRuleCouponManagementV1GeneratePost(salesRuleCouponManagementV1GeneratePostRequest)

coupons/generate

Generate coupon for a rule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CouponsGenerateApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CouponsGenerateApi apiInstance = new CouponsGenerateApi(defaultClient);
    SalesRuleCouponManagementV1GeneratePostRequest salesRuleCouponManagementV1GeneratePostRequest = new SalesRuleCouponManagementV1GeneratePostRequest(); // SalesRuleCouponManagementV1GeneratePostRequest | 
    try {
      List<String> result = apiInstance.salesRuleCouponManagementV1GeneratePost(salesRuleCouponManagementV1GeneratePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CouponsGenerateApi#salesRuleCouponManagementV1GeneratePost");
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
| **salesRuleCouponManagementV1GeneratePostRequest** | [**SalesRuleCouponManagementV1GeneratePostRequest**](SalesRuleCouponManagementV1GeneratePostRequest.md)|  | [optional] |

### Return type

**List&lt;String&gt;**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

