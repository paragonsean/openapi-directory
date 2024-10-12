# CartsMineTotalsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteCartTotalRepositoryV1GetGet**](CartsMineTotalsApi.md#quoteCartTotalRepositoryV1GetGet) | **GET** /V1/carts/mine/totals | carts/mine/totals |


<a id="quoteCartTotalRepositoryV1GetGet"></a>
# **quoteCartTotalRepositoryV1GetGet**
> QuoteDataTotalsInterface quoteCartTotalRepositoryV1GetGet()

carts/mine/totals

Returns quote totals data for a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineTotalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineTotalsApi apiInstance = new CartsMineTotalsApi(defaultClient);
    try {
      QuoteDataTotalsInterface result = apiInstance.quoteCartTotalRepositoryV1GetGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineTotalsApi#quoteCartTotalRepositoryV1GetGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

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

