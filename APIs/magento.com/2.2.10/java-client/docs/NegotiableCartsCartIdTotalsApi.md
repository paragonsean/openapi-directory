# NegotiableCartsCartIdTotalsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**negotiableQuoteCartTotalRepositoryV1GetGet**](NegotiableCartsCartIdTotalsApi.md#negotiableQuoteCartTotalRepositoryV1GetGet) | **GET** /V1/negotiable-carts/{cartId}/totals | negotiable-carts/{cartId}/totals |


<a id="negotiableQuoteCartTotalRepositoryV1GetGet"></a>
# **negotiableQuoteCartTotalRepositoryV1GetGet**
> QuoteDataTotalsInterface negotiableQuoteCartTotalRepositoryV1GetGet(cartId)

negotiable-carts/{cartId}/totals

Returns quote totals data for a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.NegotiableCartsCartIdTotalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    NegotiableCartsCartIdTotalsApi apiInstance = new NegotiableCartsCartIdTotalsApi(defaultClient);
    Integer cartId = 56; // Integer | The cart ID.
    try {
      QuoteDataTotalsInterface result = apiInstance.negotiableQuoteCartTotalRepositoryV1GetGet(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling NegotiableCartsCartIdTotalsApi#negotiableQuoteCartTotalRepositoryV1GetGet");
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

