# GuestCartsCartIdDeliveryOptionApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**temandoShippingQuoteGuestCartDeliveryOptionManagementV1SavePost**](GuestCartsCartIdDeliveryOptionApi.md#temandoShippingQuoteGuestCartDeliveryOptionManagementV1SavePost) | **POST** /V1/guest-carts/{cartId}/delivery-option | guest-carts/{cartId}/delivery-option |


<a id="temandoShippingQuoteGuestCartDeliveryOptionManagementV1SavePost"></a>
# **temandoShippingQuoteGuestCartDeliveryOptionManagementV1SavePost**
> ErrorResponse temandoShippingQuoteGuestCartDeliveryOptionManagementV1SavePost(cartId, temandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest)

guest-carts/{cartId}/delivery-option

Handle selected delivery option.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdDeliveryOptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdDeliveryOptionApi apiInstance = new GuestCartsCartIdDeliveryOptionApi(defaultClient);
    String cartId = "cartId_example"; // String | The shopping cart ID.
    TemandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest temandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest = new TemandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest(); // TemandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest | 
    try {
      ErrorResponse result = apiInstance.temandoShippingQuoteGuestCartDeliveryOptionManagementV1SavePost(cartId, temandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdDeliveryOptionApi#temandoShippingQuoteGuestCartDeliveryOptionManagementV1SavePost");
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
| **temandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest** | [**TemandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest**](TemandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest.md)|  | [optional] |

### Return type

[**ErrorResponse**](ErrorResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

