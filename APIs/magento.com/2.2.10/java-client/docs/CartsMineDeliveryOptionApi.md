# CartsMineDeliveryOptionApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**temandoShippingQuoteCartDeliveryOptionManagementV1SavePost**](CartsMineDeliveryOptionApi.md#temandoShippingQuoteCartDeliveryOptionManagementV1SavePost) | **POST** /V1/carts/mine/delivery-option | carts/mine/delivery-option |


<a id="temandoShippingQuoteCartDeliveryOptionManagementV1SavePost"></a>
# **temandoShippingQuoteCartDeliveryOptionManagementV1SavePost**
> ErrorResponse temandoShippingQuoteCartDeliveryOptionManagementV1SavePost(temandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest)

carts/mine/delivery-option

Handle selected delivery option.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineDeliveryOptionApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineDeliveryOptionApi apiInstance = new CartsMineDeliveryOptionApi(defaultClient);
    TemandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest temandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest = new TemandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest(); // TemandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest | 
    try {
      ErrorResponse result = apiInstance.temandoShippingQuoteCartDeliveryOptionManagementV1SavePost(temandoShippingQuoteCartDeliveryOptionManagementV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineDeliveryOptionApi#temandoShippingQuoteCartDeliveryOptionManagementV1SavePost");
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
| **401** | 401 Unauthorized |  -  |
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

