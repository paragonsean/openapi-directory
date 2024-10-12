# GuestCartsCartIdCheckoutFieldsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**temandoShippingQuoteGuestCartCheckoutFieldManagementV1SaveCheckoutFieldsPost**](GuestCartsCartIdCheckoutFieldsApi.md#temandoShippingQuoteGuestCartCheckoutFieldManagementV1SaveCheckoutFieldsPost) | **POST** /V1/guest-carts/{cartId}/checkout-fields | guest-carts/{cartId}/checkout-fields |


<a id="temandoShippingQuoteGuestCartCheckoutFieldManagementV1SaveCheckoutFieldsPost"></a>
# **temandoShippingQuoteGuestCartCheckoutFieldManagementV1SaveCheckoutFieldsPost**
> ErrorResponse temandoShippingQuoteGuestCartCheckoutFieldManagementV1SaveCheckoutFieldsPost(cartId, temandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest)

guest-carts/{cartId}/checkout-fields



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdCheckoutFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdCheckoutFieldsApi apiInstance = new GuestCartsCartIdCheckoutFieldsApi(defaultClient);
    String cartId = "cartId_example"; // String | 
    TemandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest temandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest = new TemandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest(); // TemandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest | 
    try {
      ErrorResponse result = apiInstance.temandoShippingQuoteGuestCartCheckoutFieldManagementV1SaveCheckoutFieldsPost(cartId, temandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdCheckoutFieldsApi#temandoShippingQuoteGuestCartCheckoutFieldManagementV1SaveCheckoutFieldsPost");
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
| **cartId** | **String**|  | |
| **temandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest** | [**TemandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest**](TemandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest.md)|  | [optional] |

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
| **400** | 400 Bad Request |  -  |
| **0** | Unexpected error |  -  |

