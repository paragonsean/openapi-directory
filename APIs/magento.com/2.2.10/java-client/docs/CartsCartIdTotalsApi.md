# CartsCartIdTotalsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1CartsCartIdTotalsGet**](CartsCartIdTotalsApi.md#v1CartsCartIdTotalsGet) | **GET** /V1/carts/{cartId}/totals | carts/{cartId}/totals |


<a id="v1CartsCartIdTotalsGet"></a>
# **v1CartsCartIdTotalsGet**
> QuoteDataTotalsInterface v1CartsCartIdTotalsGet(cartId)

carts/{cartId}/totals

Returns quote totals data for a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdTotalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdTotalsApi apiInstance = new CartsCartIdTotalsApi(defaultClient);
    Integer cartId = 56; // Integer | The cart ID.
    try {
      QuoteDataTotalsInterface result = apiInstance.v1CartsCartIdTotalsGet(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdTotalsApi#v1CartsCartIdTotalsGet");
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

[**QuoteDataTotalsInterface**](QuoteDataTotalsInterface.md)

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

