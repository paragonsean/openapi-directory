# GuestCartsCartIdTotalsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteGuestCartTotalRepositoryV1GetGet**](GuestCartsCartIdTotalsApi.md#quoteGuestCartTotalRepositoryV1GetGet) | **GET** /V1/guest-carts/{cartId}/totals | guest-carts/{cartId}/totals |


<a id="quoteGuestCartTotalRepositoryV1GetGet"></a>
# **quoteGuestCartTotalRepositoryV1GetGet**
> QuoteDataTotalsInterface quoteGuestCartTotalRepositoryV1GetGet(cartId)

guest-carts/{cartId}/totals

Return quote totals data for a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdTotalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdTotalsApi apiInstance = new GuestCartsCartIdTotalsApi(defaultClient);
    String cartId = "cartId_example"; // String | The cart ID.
    try {
      QuoteDataTotalsInterface result = apiInstance.quoteGuestCartTotalRepositoryV1GetGet(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdTotalsApi#quoteGuestCartTotalRepositoryV1GetGet");
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
| **0** | Unexpected error |  -  |

