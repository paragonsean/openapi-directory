# GuestCartsCartIdOrderApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteGuestCartManagementV1PlaceOrderPut**](GuestCartsCartIdOrderApi.md#quoteGuestCartManagementV1PlaceOrderPut) | **PUT** /V1/guest-carts/{cartId}/order | guest-carts/{cartId}/order |


<a id="quoteGuestCartManagementV1PlaceOrderPut"></a>
# **quoteGuestCartManagementV1PlaceOrderPut**
> Integer quoteGuestCartManagementV1PlaceOrderPut(cartId, quoteCartManagementV1PlaceOrderPutRequest)

guest-carts/{cartId}/order

Place an order for a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdOrderApi apiInstance = new GuestCartsCartIdOrderApi(defaultClient);
    String cartId = "cartId_example"; // String | The cart ID.
    QuoteCartManagementV1PlaceOrderPutRequest quoteCartManagementV1PlaceOrderPutRequest = new QuoteCartManagementV1PlaceOrderPutRequest(); // QuoteCartManagementV1PlaceOrderPutRequest | 
    try {
      Integer result = apiInstance.quoteGuestCartManagementV1PlaceOrderPut(cartId, quoteCartManagementV1PlaceOrderPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdOrderApi#quoteGuestCartManagementV1PlaceOrderPut");
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
| **quoteCartManagementV1PlaceOrderPutRequest** | [**QuoteCartManagementV1PlaceOrderPutRequest**](QuoteCartManagementV1PlaceOrderPutRequest.md)|  | [optional] |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **0** | Unexpected error |  -  |

