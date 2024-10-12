# CartsCartIdPaymentMethodsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CartsCartIdPaymentMethodsGet**](CartsCartIdPaymentMethodsApi.md#v1CartsCartIdPaymentMethodsGet) | **GET** /V1/carts/{cartId}/payment-methods | carts/{cartId}/payment-methods |


<a id="v1CartsCartIdPaymentMethodsGet"></a>
# **v1CartsCartIdPaymentMethodsGet**
> List&lt;QuoteDataPaymentMethodInterface&gt; v1CartsCartIdPaymentMethodsGet(cartId)

carts/{cartId}/payment-methods

Lists available payment methods for a specified shopping cart. This call returns an array of objects, but detailed information about each object’s attributes might not be included.  See https://devdocs.magento.com/codelinks/attributes.html#PaymentMethodManagementInterface to determine which call to use to get detailed information about all attributes for an object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdPaymentMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdPaymentMethodsApi apiInstance = new CartsCartIdPaymentMethodsApi(defaultClient);
    Integer cartId = 56; // Integer | The cart ID.
    try {
      List<QuoteDataPaymentMethodInterface> result = apiInstance.v1CartsCartIdPaymentMethodsGet(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdPaymentMethodsApi#v1CartsCartIdPaymentMethodsGet");
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

