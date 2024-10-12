# AllApi

All URIs are relative to *http://core.ac.uk/api-v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchPost**](AllApi.md#searchPost) | **POST** /search | Batch operation for search through all resources |
| [**searchQueryGet**](AllApi.md#searchQueryGet) | **GET** /search/{query} | Search through all resources |


<a id="searchPost"></a>
# **searchPost**
> List&lt;SearchAllResponse&gt; searchPost(body)

Batch operation for search through all resources

Method accepts a JSON array of search queries. It searches through all resources and returns a JSON array with search results for each of the queries. Method searches through all resources and all fields. The results are ordered by relevance score and contain type of the relevant resource and its ID. Furthermore, the responses are oredered based on the order of the request items. The metadata of each resource need to be obtained through an appropriate method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://core.ac.uk/api-v2");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    AllApi apiInstance = new AllApi(defaultClient);
    List<SearchRequest> body = Arrays.asList(); // List<SearchRequest> | JSON array with search queries and pagination parameters. One request can contain up to 100 queries
    try {
      List<SearchAllResponse> result = apiInstance.searchPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#searchPost");
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
| **body** | [**List&lt;SearchRequest&gt;**](SearchRequest.md)| JSON array with search queries and pagination parameters. One request can contain up to 100 queries | |

### Return type

[**List&lt;SearchAllResponse&gt;**](SearchAllResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Missing or malformed JSON in request body |  -  |
| **401** | Invalid or no API key provided |  -  |
| **403** | Too many queries in request body |  -  |
| **429** | Too many requests in given amount of time |  -  |

<a id="searchQueryGet"></a>
# **searchQueryGet**
> SearchAllResponse searchQueryGet(query, page, pageSize)

Search through all resources

Searches through all resources and returns a JSON array with search results. Method searches through all resources and all fields. The results are ordered by relevance score and contain type of the relevant resource and its ID. The metadata of each resource need to be obtained through an appropriate method.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AllApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://core.ac.uk/api-v2");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    AllApi apiInstance = new AllApi(defaultClient);
    String query = "query_example"; // String | The search query
    Integer page = 1; // Integer | Which page of the search results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page).
    Integer pageSize = 10; // Integer | The number of results to return per page. Can be any number between 10 and 100, default is 10.
    try {
      SearchAllResponse result = apiInstance.searchQueryGet(query, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AllApi#searchQueryGet");
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
| **query** | **String**| The search query | |
| **page** | **Integer**| Which page of the search results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page). | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of results to return per page. Can be any number between 10 and 100, default is 10. | [optional] [default to 10] |

### Return type

[**SearchAllResponse**](SearchAllResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Parameter invalid or out of bounds |  -  |
| **401** | Invalid or no API key provided |  -  |
| **429** | Too many requests in given amount of time |  -  |

