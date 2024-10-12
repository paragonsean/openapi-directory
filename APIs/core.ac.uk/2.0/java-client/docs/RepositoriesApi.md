# RepositoriesApi

All URIs are relative to *http://core.ac.uk/api-v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getRepositoryById**](RepositoriesApi.md#getRepositoryById) | **GET** /repositories/get/{repositoryId} | Get repository by CORE repository ID |
| [**getRepositoryByIdBatch**](RepositoriesApi.md#getRepositoryByIdBatch) | **POST** /repositories/get | Batch operation for retrieving repositories by CORE repository ID |
| [**repositoriesSearchPost**](RepositoriesApi.md#repositoriesSearchPost) | **POST** /repositories/search | Batch operation for searching through repositories |
| [**repositoriesSearchQueryGet**](RepositoriesApi.md#repositoriesSearchQueryGet) | **GET** /repositories/search/{query} | Search through all repositories |


<a id="getRepositoryById"></a>
# **getRepositoryById**
> RepositoryResponse getRepositoryById(repositoryId, stats, depositHistory, depositHistoryCumulative)

Get repository by CORE repository ID

Method will retrieve a repository based on given CORE repository ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://core.ac.uk/api-v2");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    Integer repositoryId = 56; // Integer | CORE repository ID of the article that needs to be fetched.
    Boolean stats = false; // Boolean | Whether to retrieve statistics about the repository. The default value is false
    Boolean depositHistory = false; // Boolean | Returns deposit history over time
    Boolean depositHistoryCumulative = false; // Boolean | Returns deposit history over time
    try {
      RepositoryResponse result = apiInstance.getRepositoryById(repositoryId, stats, depositHistory, depositHistoryCumulative);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#getRepositoryById");
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
| **repositoryId** | **Integer**| CORE repository ID of the article that needs to be fetched. | |
| **stats** | **Boolean**| Whether to retrieve statistics about the repository. The default value is false | [optional] [default to false] |
| **depositHistory** | **Boolean**| Returns deposit history over time | [optional] [default to false] |
| **depositHistoryCumulative** | **Boolean**| Returns deposit history over time | [optional] [default to false] |

### Return type

[**RepositoryResponse**](RepositoryResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Invalid identifier supplied |  -  |
| **401** | Invalid or no API key provided |  -  |
| **429** | Too many requests in given amount of time |  -  |

<a id="getRepositoryByIdBatch"></a>
# **getRepositoryByIdBatch**
> List&lt;RepositoryResponse&gt; getRepositoryByIdBatch(body, stats, depositHistory, depositHistoryCumulative)

Batch operation for retrieving repositories by CORE repository ID

Method accepts a JSON array of CORE repository IDs and retrieves a list of repositories. The response array is ordered based on the order of the IDs in the request array. The maximum number of IDs in request is 100.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://core.ac.uk/api-v2");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    List<Integer> body = Arrays.asList(); // List<Integer> | JSON array with CORE repository IDs of repositories that need to be fetched
    Boolean stats = false; // Boolean | Whether to retrieve statistics about the repository. The default value is false
    Boolean depositHistory = false; // Boolean | Returns deposit history over time
    Boolean depositHistoryCumulative = false; // Boolean | Returns deposit history over time
    try {
      List<RepositoryResponse> result = apiInstance.getRepositoryByIdBatch(body, stats, depositHistory, depositHistoryCumulative);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#getRepositoryByIdBatch");
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
| **body** | [**List&lt;Integer&gt;**](Integer.md)| JSON array with CORE repository IDs of repositories that need to be fetched | |
| **stats** | **Boolean**| Whether to retrieve statistics about the repository. The default value is false | [optional] [default to false] |
| **depositHistory** | **Boolean**| Returns deposit history over time | [optional] [default to false] |
| **depositHistoryCumulative** | **Boolean**| Returns deposit history over time | [optional] [default to false] |

### Return type

[**List&lt;RepositoryResponse&gt;**](RepositoryResponse.md)

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

<a id="repositoriesSearchPost"></a>
# **repositoriesSearchPost**
> RepositorySearchResponse repositoriesSearchPost(body, stats, depositHistory, depositHistoryCumulative)

Batch operation for searching through repositories

Method accepts a JSON array of search queries and parameters. It then searches through all repositories and returns a JSON array of search results for each of the queries. Method searches through all repository fields.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://core.ac.uk/api-v2");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    List<SearchRequest> body = Arrays.asList(); // List<SearchRequest> | JSON array with search queries and parameters. One request can contain up to 100 queries
    Boolean stats = false; // Boolean | Whether to retrieve statistics about the repository. The default value is false
    Boolean depositHistory = false; // Boolean | Returns deposit history over time
    Boolean depositHistoryCumulative = false; // Boolean | Returns deposit history over time
    try {
      RepositorySearchResponse result = apiInstance.repositoriesSearchPost(body, stats, depositHistory, depositHistoryCumulative);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesSearchPost");
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
| **body** | [**List&lt;SearchRequest&gt;**](SearchRequest.md)| JSON array with search queries and parameters. One request can contain up to 100 queries | |
| **stats** | **Boolean**| Whether to retrieve statistics about the repository. The default value is false | [optional] [default to false] |
| **depositHistory** | **Boolean**| Returns deposit history over time | [optional] [default to false] |
| **depositHistoryCumulative** | **Boolean**| Returns deposit history over time | [optional] [default to false] |

### Return type

[**RepositorySearchResponse**](RepositorySearchResponse.md)

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

<a id="repositoriesSearchQueryGet"></a>
# **repositoriesSearchQueryGet**
> RepositorySearchResponse repositoriesSearchQueryGet(query, page, pageSize, stats, depositHistory, depositHistoryCumulative)

Search through all repositories

Searches through all repositories and returns a JSON array with search results. Method searches through all repository fields.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://core.ac.uk/api-v2");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    RepositoriesApi apiInstance = new RepositoriesApi(defaultClient);
    String query = "query_example"; // String | The search query
    Integer page = 1; // Integer | Which page of the search results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page).
    Integer pageSize = 10; // Integer | The number of results to return per page. Can be any number between 10 and 100, default is 10.
    Boolean stats = false; // Boolean | Whether to retrieve statistics about the repository. The default value is false
    Boolean depositHistory = false; // Boolean | Returns deposit history over time
    Boolean depositHistoryCumulative = false; // Boolean | Returns deposit history over time
    try {
      RepositorySearchResponse result = apiInstance.repositoriesSearchQueryGet(query, page, pageSize, stats, depositHistory, depositHistoryCumulative);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoriesApi#repositoriesSearchQueryGet");
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
| **stats** | **Boolean**| Whether to retrieve statistics about the repository. The default value is false | [optional] [default to false] |
| **depositHistory** | **Boolean**| Returns deposit history over time | [optional] [default to false] |
| **depositHistoryCumulative** | **Boolean**| Returns deposit history over time | [optional] [default to false] |

### Return type

[**RepositorySearchResponse**](RepositorySearchResponse.md)

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

