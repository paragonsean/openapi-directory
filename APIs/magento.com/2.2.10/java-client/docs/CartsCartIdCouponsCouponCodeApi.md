# CartsCartIdCouponsCouponCodeApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CartsCartIdCouponsCouponCodePut**](CartsCartIdCouponsCouponCodeApi.md#v1CartsCartIdCouponsCouponCodePut) | **PUT** /V1/carts/{cartId}/coupons/{couponCode} | carts/{cartId}/coupons/{couponCode} |


<a id="v1CartsCartIdCouponsCouponCodePut"></a>
# **v1CartsCartIdCouponsCouponCodePut**
> Boolean v1CartsCartIdCouponsCouponCodePut(cartId, couponCode)

carts/{cartId}/coupons/{couponCode}

Adds a coupon by code to a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdCouponsCouponCodeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdCouponsCouponCodeApi apiInstance = new CartsCartIdCouponsCouponCodeApi(defaultClient);
    Integer cartId = 56; // Integer | The cart ID.
    String couponCode = "couponCode_example"; // String | The coupon code data.
    try {
      Boolean result = apiInstance.v1CartsCartIdCouponsCouponCodePut(cartId, couponCode);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdCouponsCouponCodeApi#v1CartsCartIdCouponsCouponCodePut");
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

