# CartsMinePaymentMethodsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quotePaymentMethodManagementV1GetListGet**](CartsMinePaymentMethodsApi.md#quotePaymentMethodManagementV1GetListGet) | **GET** /V1/carts/mine/payment-methods | carts/mine/payment-methods |


<a id="quotePaymentMethodManagementV1GetListGet"></a>
# **quotePaymentMethodManagementV1GetListGet**
> List&lt;QuoteDataPaymentMethodInterface&gt; quotePaymentMethodManagementV1GetListGet()

carts/mine/payment-methods

Lists available payment methods for a specified shopping cart. This call returns an array of objects, but detailed information about each object’s attributes might not be included.  See https://devdocs.magento.com/codelinks/attributes.html#PaymentMethodManagementInterface to determine which call to use to get detailed information about all attributes for an object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMinePaymentMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMinePaymentMethodsApi apiInstance = new CartsMinePaymentMethodsApi(defaultClient);
    try {
      List<QuoteDataPaymentMethodInterface> result = apiInstance.quotePaymentMethodManagementV1GetListGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMinePaymentMethodsApi#quotePaymentMethodManagementV1GetListGet");
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

[**List&lt;QuoteDataPaymentMethodInterface&gt;**](QuoteDataPaymentMethodInterface.md)

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

