# CartsMineCouponsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteCouponManagementV1GetGet**](CartsMineCouponsApi.md#quoteCouponManagementV1GetGet) | **GET** /V1/carts/mine/coupons | carts/mine/coupons |
| [**quoteCouponManagementV1RemoveDelete**](CartsMineCouponsApi.md#quoteCouponManagementV1RemoveDelete) | **DELETE** /V1/carts/mine/coupons | carts/mine/coupons |


<a id="quoteCouponManagementV1GetGet"></a>
# **quoteCouponManagementV1GetGet**
> String quoteCouponManagementV1GetGet()

carts/mine/coupons

Returns information for a coupon in a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineCouponsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineCouponsApi apiInstance = new CartsMineCouponsApi(defaultClient);
    try {
      String result = apiInstance.quoteCouponManagementV1GetGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineCouponsApi#quoteCouponManagementV1GetGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**String**

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
| **0** | Unexpected error |  -  |

<a id="quoteCouponManagementV1RemoveDelete"></a>
# **quoteCouponManagementV1RemoveDelete**
> Boolean quoteCouponManagementV1RemoveDelete()

carts/mine/coupons

Deletes a coupon from a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineCouponsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineCouponsApi apiInstance = new CartsMineCouponsApi(defaultClient);
    try {
      Boolean result = apiInstance.quoteCouponManagementV1RemoveDelete();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineCouponsApi#quoteCouponManagementV1RemoveDelete");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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
| **0** | Unexpected error |  -  |

