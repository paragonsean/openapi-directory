# NegotiableCartsCartIdCouponsCouponCodeApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**negotiableQuoteCouponManagementV1SetPut**](NegotiableCartsCartIdCouponsCouponCodeApi.md#negotiableQuoteCouponManagementV1SetPut) | **PUT** /V1/negotiable-carts/{cartId}/coupons/{couponCode} | negotiable-carts/{cartId}/coupons/{couponCode} |


<a id="negotiableQuoteCouponManagementV1SetPut"></a>
# **negotiableQuoteCouponManagementV1SetPut**
> Boolean negotiableQuoteCouponManagementV1SetPut(cartId, couponCode)

negotiable-carts/{cartId}/coupons/{couponCode}

Adds a coupon by code to a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegotiableCartsCartIdCouponsCouponCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    NegotiableCartsCartIdCouponsCouponCodeApi apiInstance = new NegotiableCartsCartIdCouponsCouponCodeApi(defaultClient);
    Integer cartId = 56; // Integer | The cart ID.
    String couponCode = "couponCode_example"; // String | The coupon code data.
    try {
      Boolean result = apiInstance.negotiableQuoteCouponManagementV1SetPut(cartId, couponCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegotiableCartsCartIdCouponsCouponCodeApi#negotiableQuoteCouponManagementV1SetPut");
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
| **cartId** | **Integer**| The cart ID. | |
| **couponCode** | **String**| The coupon code data. | |

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

