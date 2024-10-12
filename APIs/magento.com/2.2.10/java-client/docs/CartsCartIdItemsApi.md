# CartsCartIdItemsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CartsCartIdItemsGet**](CartsCartIdItemsApi.md#v1CartsCartIdItemsGet) | **GET** /V1/carts/{cartId}/items | carts/{cartId}/items |


<a id="v1CartsCartIdItemsGet"></a>
# **v1CartsCartIdItemsGet**
> List&lt;QuoteDataCartItemInterface&gt; v1CartsCartIdItemsGet(cartId)

carts/{cartId}/items

Lists items that are assigned to a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdItemsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdItemsApi apiInstance = new CartsCartIdItemsApi(defaultClient);
    Integer cartId = 56; // Integer | The cart ID.
    try {
      List<QuoteDataCartItemInterface> result = apiInstance.v1CartsCartIdItemsGet(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdItemsApi#v1CartsCartIdItemsGet");
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

[**List&lt;QuoteDataCartItemInterface&gt;**](QuoteDataCartItemInterface.md)

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

