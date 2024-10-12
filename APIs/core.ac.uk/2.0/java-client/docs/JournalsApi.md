# JournalsApi

All URIs are relative to *http://core.ac.uk/api-v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getJournalByIssn**](JournalsApi.md#getJournalByIssn) | **GET** /journals/get/{issn} | Find journal by ISSN |
| [**getJournalByIssnBatch**](JournalsApi.md#getJournalByIssnBatch) | **POST** /journals/get | Batch operation for retrieving journals by ISSN |
| [**journalsSearchPost**](JournalsApi.md#journalsSearchPost) | **POST** /journals/search | Batch operation for search through journals |
| [**journalsSearchQueryGet**](JournalsApi.md#journalsSearchQueryGet) | **GET** /journals/search/{query} | Search through journals |


<a id="getJournalByIssn"></a>
# **getJournalByIssn**
> JournalResponse getJournalByIssn(issn)

Find journal by ISSN

Returns a journal with given ISSN identifier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JournalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://core.ac.uk/api-v2");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    JournalsApi apiInstance = new JournalsApi(defaultClient);
    String issn = "issn_example"; // String | ISSN identifier of journal that needs to be fetched.
    try {
      JournalResponse result = apiInstance.getJournalByIssn(issn);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JournalsApi#getJournalByIssn");
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
| **issn** | **String**| ISSN identifier of journal that needs to be fetched. | |

### Return type

[**JournalResponse**](JournalResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Invalid ISSN identifier supplied |  -  |
| **401** | Invalid or no API key provided |  -  |

<a id="getJournalByIssnBatch"></a>
# **getJournalByIssnBatch**
> List&lt;JournalResponse&gt; getJournalByIssnBatch(body)

Batch operation for retrieving journals by ISSN

Method accepts a JSON array of ISSNs and retrieves a list of journals.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JournalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://core.ac.uk/api-v2");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    JournalsApi apiInstance = new JournalsApi(defaultClient);
    List<String> body = Arrays.asList(); // List<String> | JSON array with ISSNs of journals that need to be fetched
    try {
      List<JournalResponse> result = apiInstance.getJournalByIssnBatch(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JournalsApi#getJournalByIssnBatch");
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
| **body** | [**List&lt;String&gt;**](String.md)| JSON array with ISSNs of journals that need to be fetched | |

### Return type

[**List&lt;JournalResponse&gt;**](JournalResponse.md)

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

<a id="journalsSearchPost"></a>
# **journalsSearchPost**
> List&lt;JournalResponse&gt; journalsSearchPost(body)

Batch operation for search through journals

Method accepts a JSON array of search queries and parameters. It then searches through all journals and returns a JSON array of search results for each of the queries. Method searches through all journal fields (title, identifiers, subjects, language, rights and publisher).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JournalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://core.ac.uk/api-v2");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    JournalsApi apiInstance = new JournalsApi(defaultClient);
    List<SearchRequest> body = Arrays.asList(); // List<SearchRequest> | JSON array with search queries and parameters. One request can contain up to 100 queries.
    try {
      List<JournalResponse> result = apiInstance.journalsSearchPost(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JournalsApi#journalsSearchPost");
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
| **body** | [**List&lt;SearchRequest&gt;**](SearchRequest.md)| JSON array with search queries and parameters. One request can contain up to 100 queries. | |

### Return type

[**List&lt;JournalResponse&gt;**](JournalResponse.md)

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

<a id="journalsSearchQueryGet"></a>
# **journalsSearchQueryGet**
> JournalSearchResponse journalsSearchQueryGet(query, page, pageSize)

Search through journals

Searches through all journals and returns a JSON array of search results. Method searches through all journal fields (title, identifiers, subjects, language, rights and publisher).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.JournalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://core.ac.uk/api-v2");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    JournalsApi apiInstance = new JournalsApi(defaultClient);
    String query = "query_example"; // String | Search query
    Integer page = 1; // Integer | Which page of the search results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page).
    Integer pageSize = 10; // Integer | The number of results to return per page. Can be any number between 10 and 100, default is 10.
    try {
      JournalSearchResponse result = apiInstance.journalsSearchQueryGet(query, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling JournalsApi#journalsSearchQueryGet");
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
| **query** | **String**| Search query | |
| **page** | **Integer**| Which page of the search results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page). | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of results to return per page. Can be any number between 10 and 100, default is 10. | [optional] [default to 10] |

### Return type

[**JournalSearchResponse**](JournalSearchResponse.md)

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

