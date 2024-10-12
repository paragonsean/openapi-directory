# GuestCartsCartIdShippingMethodsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteGuestShippingMethodManagementV1GetListGet**](GuestCartsCartIdShippingMethodsApi.md#quoteGuestShippingMethodManagementV1GetListGet) | **GET** /V1/guest-carts/{cartId}/shipping-methods | guest-carts/{cartId}/shipping-methods |


<a id="quoteGuestShippingMethodManagementV1GetListGet"></a>
# **quoteGuestShippingMethodManagementV1GetListGet**
> List&lt;QuoteDataShippingMethodInterface&gt; quoteGuestShippingMethodManagementV1GetListGet(cartId)

guest-carts/{cartId}/shipping-methods

List applicable shipping methods for a specified quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdShippingMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdShippingMethodsApi apiInstance = new GuestCartsCartIdShippingMethodsApi(defaultClient);
    String cartId = "cartId_example"; // String | The shopping cart ID.
    try {
      List<QuoteDataShippingMethodInterface> result = apiInstance.quoteGuestShippingMethodManagementV1GetListGet(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdShippingMethodsApi#quoteGuestShippingMethodManagementV1GetListGet");
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
| **cartId** | **String**| The shopping cart ID. | |

### Return type

[**List&lt;QuoteDataShippingMethodInterface&gt;**](QuoteDataShippingMethodInterface.md)

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

