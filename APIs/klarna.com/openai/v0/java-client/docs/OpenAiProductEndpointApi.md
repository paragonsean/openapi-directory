# OpenAiProductEndpointApi

All URIs are relative to *https://www.klarna.com/us/shopping*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productsUsingGET**](OpenAiProductEndpointApi.md#productsUsingGET) | **GET** /public/openai/v0/products | API for fetching Klarna product information |


<a id="productsUsingGET"></a>
# **productsUsingGET**
> ProductResponse productsUsingGET(q, size, budget)

API for fetching Klarna product information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OpenAiProductEndpointApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.klarna.com/us/shopping");

    OpenAiProductEndpointApi apiInstance = new OpenAiProductEndpointApi(defaultClient);
    String q = "q_example"; // String | A precise query that matches one very small category or product that needs to be searched for to find the products the user is looking for. If the user explicitly stated what they want, use that as a query. The query is as specific as possible to the product name or category mentioned by the user in its singular form, and don't contain any clarifiers like latest, newest, cheapest, budget, premium, expensive or similar. The query is always taken from the latest topic, if there is a new topic a new query is started.
    Integer size = 56; // Integer | number of products returned
    Integer budget = 56; // Integer | maximum price of the matching product in local currency, filters results
    try {
      ProductResponse result = apiInstance.productsUsingGET(q, size, budget);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OpenAiProductEndpointApi#productsUsingGET");
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
| **q** | **String**| A precise query that matches one very small category or product that needs to be searched for to find the products the user is looking for. If the user explicitly stated what they want, use that as a query. The query is as specific as possible to the product name or category mentioned by the user in its singular form, and don&#39;t contain any clarifiers like latest, newest, cheapest, budget, premium, expensive or similar. The query is always taken from the latest topic, if there is a new topic a new query is started. | |
| **size** | **Integer**| number of products returned | [optional] |
| **budget** | **Integer**| maximum price of the matching product in local currency, filters results | [optional] |

### Return type

[**ProductResponse**](ProductResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Products found |  -  |
| **503** | one or more services are unavailable |  -  |

