# CartsMineShippingMethodsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteShippingMethodManagementV1GetListGet**](CartsMineShippingMethodsApi.md#quoteShippingMethodManagementV1GetListGet) | **GET** /V1/carts/mine/shipping-methods | carts/mine/shipping-methods |


<a id="quoteShippingMethodManagementV1GetListGet"></a>
# **quoteShippingMethodManagementV1GetListGet**
> List&lt;QuoteDataShippingMethodInterface&gt; quoteShippingMethodManagementV1GetListGet()

carts/mine/shipping-methods

Lists applicable shipping methods for a specified quote.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineShippingMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineShippingMethodsApi apiInstance = new CartsMineShippingMethodsApi(defaultClient);
    try {
      List<QuoteDataShippingMethodInterface> result = apiInstance.quoteShippingMethodManagementV1GetListGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineShippingMethodsApi#quoteShippingMethodManagementV1GetListGet");
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

