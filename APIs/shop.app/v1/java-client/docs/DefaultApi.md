# DefaultApi

All URIs are relative to *https://server.shop.app*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**details**](DefaultApi.md#details) | **GET** /openai/details | Return more details about a list of products. |
| [**search**](DefaultApi.md#search) | **GET** /openai/search | Search for products |


<a id="details"></a>
# **details**
> SearchResponse details(ids)

Return more details about a list of products.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://server.shop.app");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String ids = "ids_example"; // String | Comma separated list of product ids
    try {
      SearchResponse result = apiInstance.details(ids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#details");
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
| **ids** | **String**| Comma separated list of product ids | |

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **503** | Service Unavailable |  -  |

<a id="search"></a>
# **search**
> SearchResponse search(query, priceMin, priceMax, similarToId, numResults)

Search for products

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://server.shop.app");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String query = "query_example"; // String | Query string to search for items.
    BigDecimal priceMin = new BigDecimal(78); // BigDecimal | The minimum price to filter by.
    BigDecimal priceMax = new BigDecimal(78); // BigDecimal | The maximum price to filter by.
    String similarToId = "similarToId_example"; // String | A product id that you want to find similar products for. (Only include one)
    String numResults = "numResults_example"; // String | How many results to return. Defaults to 5. It can be a number between 1 and 10.
    try {
      SearchResponse result = apiInstance.search(query, priceMin, priceMax, similarToId, numResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#search");
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
| **query** | **String**| Query string to search for items. | [optional] |
| **priceMin** | **BigDecimal**| The minimum price to filter by. | [optional] |
| **priceMax** | **BigDecimal**| The maximum price to filter by. | [optional] |
| **similarToId** | **String**| A product id that you want to find similar products for. (Only include one) | [optional] |
| **numResults** | **String**| How many results to return. Defaults to 5. It can be a number between 1 and 10. | [optional] |

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **503** | Service Unavailable |  -  |

