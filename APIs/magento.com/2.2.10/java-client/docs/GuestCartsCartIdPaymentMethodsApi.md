# GuestCartsCartIdPaymentMethodsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteGuestPaymentMethodManagementV1GetListGet**](GuestCartsCartIdPaymentMethodsApi.md#quoteGuestPaymentMethodManagementV1GetListGet) | **GET** /V1/guest-carts/{cartId}/payment-methods | guest-carts/{cartId}/payment-methods |


<a id="quoteGuestPaymentMethodManagementV1GetListGet"></a>
# **quoteGuestPaymentMethodManagementV1GetListGet**
> List&lt;QuoteDataPaymentMethodInterface&gt; quoteGuestPaymentMethodManagementV1GetListGet(cartId)

guest-carts/{cartId}/payment-methods

List available payment methods for a specified shopping cart. This call returns an array of objects, but detailed information about each object’s attributes might not be included.  See https://devdocs.magento.com/codelinks/attributes.html#GuestPaymentMethodManagementInterface to determine which call to use to get detailed information about all attributes for an object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdPaymentMethodsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdPaymentMethodsApi apiInstance = new GuestCartsCartIdPaymentMethodsApi(defaultClient);
    String cartId = "cartId_example"; // String | The cart ID.
    try {
      List<QuoteDataPaymentMethodInterface> result = apiInstance.quoteGuestPaymentMethodManagementV1GetListGet(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdPaymentMethodsApi#quoteGuestPaymentMethodManagementV1GetListGet");
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
| **0** | Unexpected error |  -  |

