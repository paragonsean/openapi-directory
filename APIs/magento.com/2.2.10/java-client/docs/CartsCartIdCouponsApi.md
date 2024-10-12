# CartsCartIdCouponsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CartsCartIdCouponsDelete**](CartsCartIdCouponsApi.md#v1CartsCartIdCouponsDelete) | **DELETE** /V1/carts/{cartId}/coupons | carts/{cartId}/coupons |
| [**v1CartsCartIdCouponsGet**](CartsCartIdCouponsApi.md#v1CartsCartIdCouponsGet) | **GET** /V1/carts/{cartId}/coupons | carts/{cartId}/coupons |


<a id="v1CartsCartIdCouponsDelete"></a>
# **v1CartsCartIdCouponsDelete**
> Boolean v1CartsCartIdCouponsDelete(cartId)

carts/{cartId}/coupons

Deletes a coupon from a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdCouponsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdCouponsApi apiInstance = new CartsCartIdCouponsApi(defaultClient);
    Integer cartId = 56; // Integer | The cart ID.
    try {
      Boolean result = apiInstance.v1CartsCartIdCouponsDelete(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdCouponsApi#v1CartsCartIdCouponsDelete");
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

<a id="v1CartsCartIdCouponsGet"></a>
# **v1CartsCartIdCouponsGet**
> String v1CartsCartIdCouponsGet(cartId)

carts/{cartId}/coupons

Returns information for a coupon in a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdCouponsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdCouponsApi apiInstance = new CartsCartIdCouponsApi(defaultClient);
    Integer cartId = 56; // Integer | The cart ID.
    try {
      String result = apiInstance.v1CartsCartIdCouponsGet(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdCouponsApi#v1CartsCartIdCouponsGet");
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

