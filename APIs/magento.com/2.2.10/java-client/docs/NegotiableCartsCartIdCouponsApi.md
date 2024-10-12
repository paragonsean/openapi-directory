# NegotiableCartsCartIdCouponsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**negotiableQuoteCouponManagementV1RemoveDelete**](NegotiableCartsCartIdCouponsApi.md#negotiableQuoteCouponManagementV1RemoveDelete) | **DELETE** /V1/negotiable-carts/{cartId}/coupons | negotiable-carts/{cartId}/coupons |


<a id="negotiableQuoteCouponManagementV1RemoveDelete"></a>
# **negotiableQuoteCouponManagementV1RemoveDelete**
> Boolean negotiableQuoteCouponManagementV1RemoveDelete(cartId)

negotiable-carts/{cartId}/coupons

Deletes a coupon from a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegotiableCartsCartIdCouponsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    NegotiableCartsCartIdCouponsApi apiInstance = new NegotiableCartsCartIdCouponsApi(defaultClient);
    Integer cartId = 56; // Integer | The cart ID.
    try {
      Boolean result = apiInstance.negotiableQuoteCouponManagementV1RemoveDelete(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegotiableCartsCartIdCouponsApi#negotiableQuoteCouponManagementV1RemoveDelete");
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

