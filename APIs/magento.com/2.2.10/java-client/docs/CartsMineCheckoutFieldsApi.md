# CartsMineCheckoutFieldsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**temandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPost**](CartsMineCheckoutFieldsApi.md#temandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPost) | **POST** /V1/carts/mine/checkout-fields | carts/mine/checkout-fields |


<a id="temandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPost"></a>
# **temandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPost**
> ErrorResponse temandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPost(temandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest)

carts/mine/checkout-fields



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineCheckoutFieldsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineCheckoutFieldsApi apiInstance = new CartsMineCheckoutFieldsApi(defaultClient);
    TemandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest temandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest = new TemandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest(); // TemandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest | 
    try {
      ErrorResponse result = apiInstance.temandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPost(temandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineCheckoutFieldsApi#temandoShippingQuoteCartCheckoutFieldManagementV1SaveCheckoutFieldsPost");
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
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

