# GuestCartsCartIdCouponsCouponCodeApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteGuestCouponManagementV1SetPut**](GuestCartsCartIdCouponsCouponCodeApi.md#quoteGuestCouponManagementV1SetPut) | **PUT** /V1/guest-carts/{cartId}/coupons/{couponCode} | guest-carts/{cartId}/coupons/{couponCode} |


<a id="quoteGuestCouponManagementV1SetPut"></a>
# **quoteGuestCouponManagementV1SetPut**
> Boolean quoteGuestCouponManagementV1SetPut(cartId, couponCode)

guest-carts/{cartId}/coupons/{couponCode}

Add a coupon by code to a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdCouponsCouponCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdCouponsCouponCodeApi apiInstance = new GuestCartsCartIdCouponsCouponCodeApi(defaultClient);
    String cartId = "cartId_example"; // String | The cart ID.
    String couponCode = "couponCode_example"; // String | The coupon code data.
    try {
      Boolean result = apiInstance.quoteGuestCouponManagementV1SetPut(cartId, couponCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdCouponsCouponCodeApi#quoteGuestCouponManagementV1SetPut");
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
| **cartId** | **String**| The cart ID. | |
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
| **0** | Unexpected error |  -  |

