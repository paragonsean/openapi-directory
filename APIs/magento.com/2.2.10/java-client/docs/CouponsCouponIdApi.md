# CouponsCouponIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesRuleCouponRepositoryV1DeleteByIdDelete**](CouponsCouponIdApi.md#salesRuleCouponRepositoryV1DeleteByIdDelete) | **DELETE** /V1/coupons/{couponId} | coupons/{couponId} |
| [**salesRuleCouponRepositoryV1GetByIdGet**](CouponsCouponIdApi.md#salesRuleCouponRepositoryV1GetByIdGet) | **GET** /V1/coupons/{couponId} | coupons/{couponId} |
| [**salesRuleCouponRepositoryV1SavePut**](CouponsCouponIdApi.md#salesRuleCouponRepositoryV1SavePut) | **PUT** /V1/coupons/{couponId} | coupons/{couponId} |


<a id="salesRuleCouponRepositoryV1DeleteByIdDelete"></a>
# **salesRuleCouponRepositoryV1DeleteByIdDelete**
> Boolean salesRuleCouponRepositoryV1DeleteByIdDelete(couponId)

coupons/{couponId}

Delete coupon by coupon id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CouponsCouponIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CouponsCouponIdApi apiInstance = new CouponsCouponIdApi(defaultClient);
    Integer couponId = 56; // Integer | 
    try {
      Boolean result = apiInstance.salesRuleCouponRepositoryV1DeleteByIdDelete(couponId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CouponsCouponIdApi#salesRuleCouponRepositoryV1DeleteByIdDelete");
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
| **couponId** | **Integer**|  | |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

<a id="salesRuleCouponRepositoryV1GetByIdGet"></a>
# **salesRuleCouponRepositoryV1GetByIdGet**
> SalesRuleDataCouponInterface salesRuleCouponRepositoryV1GetByIdGet(couponId)

coupons/{couponId}

Get coupon by coupon id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CouponsCouponIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CouponsCouponIdApi apiInstance = new CouponsCouponIdApi(defaultClient);
    Integer couponId = 56; // Integer | 
    try {
      SalesRuleDataCouponInterface result = apiInstance.salesRuleCouponRepositoryV1GetByIdGet(couponId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CouponsCouponIdApi#salesRuleCouponRepositoryV1GetByIdGet");
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
| **couponId** | **Integer**|  | |

### Return type

[**SalesRuleDataCouponInterface**](SalesRuleDataCouponInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

<a id="salesRuleCouponRepositoryV1SavePut"></a>
# **salesRuleCouponRepositoryV1SavePut**
> SalesRuleDataCouponInterface salesRuleCouponRepositoryV1SavePut(couponId, salesRuleCouponRepositoryV1SavePostRequest)

coupons/{couponId}

Save a coupon.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CouponsCouponIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CouponsCouponIdApi apiInstance = new CouponsCouponIdApi(defaultClient);
    String couponId = "couponId_example"; // String | 
    SalesRuleCouponRepositoryV1SavePostRequest salesRuleCouponRepositoryV1SavePostRequest = new SalesRuleCouponRepositoryV1SavePostRequest(); // SalesRuleCouponRepositoryV1SavePostRequest | 
    try {
      SalesRuleDataCouponInterface result = apiInstance.salesRuleCouponRepositoryV1SavePut(couponId, salesRuleCouponRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CouponsCouponIdApi#salesRuleCouponRepositoryV1SavePut");
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
| **couponId** | **String**|  | |
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

