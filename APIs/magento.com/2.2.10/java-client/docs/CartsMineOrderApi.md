# CartsMineOrderApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteCartManagementV1PlaceOrderPut**](CartsMineOrderApi.md#quoteCartManagementV1PlaceOrderPut) | **PUT** /V1/carts/mine/order | carts/mine/order |


<a id="quoteCartManagementV1PlaceOrderPut"></a>
# **quoteCartManagementV1PlaceOrderPut**
> Integer quoteCartManagementV1PlaceOrderPut(quoteCartManagementV1PlaceOrderPutRequest)

carts/mine/order

Places an order for a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineOrderApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineOrderApi apiInstance = new CartsMineOrderApi(defaultClient);
    QuoteCartManagementV1PlaceOrderPutRequest quoteCartManagementV1PlaceOrderPutRequest = new QuoteCartManagementV1PlaceOrderPutRequest(); // QuoteCartManagementV1PlaceOrderPutRequest | 
    try {
      Integer result = apiInstance.quoteCartManagementV1PlaceOrderPut(quoteCartManagementV1PlaceOrderPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineOrderApi#quoteCartManagementV1PlaceOrderPut");
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

