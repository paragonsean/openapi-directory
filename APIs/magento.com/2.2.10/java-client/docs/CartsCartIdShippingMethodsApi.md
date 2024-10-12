# CartsCartIdShippingMethodsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CartsCartIdShippingMethodsGet**](CartsCartIdShippingMethodsApi.md#v1CartsCartIdShippingMethodsGet) | **GET** /V1/carts/{cartId}/shipping-methods | carts/{cartId}/shipping-methods |


<a id="v1CartsCartIdShippingMethodsGet"></a>
# **v1CartsCartIdShippingMethodsGet**
> List&lt;QuoteDataShippingMethodInterface&gt; v1CartsCartIdShippingMethodsGet(cartId)

carts/{cartId}/shipping-methods

Lists applicable shipping methods for a specified quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdShippingMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdShippingMethodsApi apiInstance = new CartsCartIdShippingMethodsApi(defaultClient);
    Integer cartId = 56; // Integer | The shopping cart ID.
    try {
      List<QuoteDataShippingMethodInterface> result = apiInstance.v1CartsCartIdShippingMethodsGet(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdShippingMethodsApi#v1CartsCartIdShippingMethodsGet");
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
| **cartId** | **Integer**| The shopping cart ID. | |

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
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

