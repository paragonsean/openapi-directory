# CartsCartIdOrderApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CartsCartIdOrderPut**](CartsCartIdOrderApi.md#v1CartsCartIdOrderPut) | **PUT** /V1/carts/{cartId}/order | carts/{cartId}/order |


<a id="v1CartsCartIdOrderPut"></a>
# **v1CartsCartIdOrderPut**
> Integer v1CartsCartIdOrderPut(cartId, quoteCartManagementV1PlaceOrderPutRequest)

carts/{cartId}/order

Places an order for a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdOrderApi apiInstance = new CartsCartIdOrderApi(defaultClient);
    Integer cartId = 56; // Integer | The cart ID.
    QuoteCartManagementV1PlaceOrderPutRequest quoteCartManagementV1PlaceOrderPutRequest = new QuoteCartManagementV1PlaceOrderPutRequest(); // QuoteCartManagementV1PlaceOrderPutRequest | 
    try {
      Integer result = apiInstance.v1CartsCartIdOrderPut(cartId, quoteCartManagementV1PlaceOrderPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdOrderApi#v1CartsCartIdOrderPut");
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
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

