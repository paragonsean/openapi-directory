# GuestCartsCartIdCouponsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteGuestCouponManagementV1GetGet**](GuestCartsCartIdCouponsApi.md#quoteGuestCouponManagementV1GetGet) | **GET** /V1/guest-carts/{cartId}/coupons | guest-carts/{cartId}/coupons |
| [**quoteGuestCouponManagementV1RemoveDelete**](GuestCartsCartIdCouponsApi.md#quoteGuestCouponManagementV1RemoveDelete) | **DELETE** /V1/guest-carts/{cartId}/coupons | guest-carts/{cartId}/coupons |


<a id="quoteGuestCouponManagementV1GetGet"></a>
# **quoteGuestCouponManagementV1GetGet**
> String quoteGuestCouponManagementV1GetGet(cartId)

guest-carts/{cartId}/coupons

Return information for a coupon in a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdCouponsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdCouponsApi apiInstance = new GuestCartsCartIdCouponsApi(defaultClient);
    String cartId = "cartId_example"; // String | The cart ID.
    try {
      String result = apiInstance.quoteGuestCouponManagementV1GetGet(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdCouponsApi#quoteGuestCouponManagementV1GetGet");
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
| **0** | Unexpected error |  -  |

<a id="quoteGuestCouponManagementV1RemoveDelete"></a>
# **quoteGuestCouponManagementV1RemoveDelete**
> Boolean quoteGuestCouponManagementV1RemoveDelete(cartId)

guest-carts/{cartId}/coupons

Delete a coupon from a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdCouponsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdCouponsApi apiInstance = new GuestCartsCartIdCouponsApi(defaultClient);
    String cartId = "cartId_example"; // String | The cart ID.
    try {
      Boolean result = apiInstance.quoteGuestCouponManagementV1RemoveDelete(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdCouponsApi#quoteGuestCouponManagementV1RemoveDelete");
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

