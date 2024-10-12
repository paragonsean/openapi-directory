# SearchApi

All URIs are relative to *http://opentrials.local/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**autocomplete**](SearchApi.md#autocomplete) | **GET** /search/autocomplete/{in} |  |
| [**searchFDADocuments**](SearchApi.md#searchFDADocuments) | **GET** /search/fda_documents |  |


<a id="autocomplete"></a>
# **autocomplete**
> AutocompleteResults autocomplete(in, q, page, perPage)



Autocomplete search feature for supported database entities (&#x60;location&#x60;). It has the same options as a regular &#x60;search&#x60; operation, with an extra **required** &#x60;in&#x60; parameter indicating the entity type to search.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://opentrials.local/v1");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String in = "location"; // String | The entity to search for
    String q = "q_example"; // String | The search query
    Integer page = 1; // Integer | The page number
    Integer perPage = 20; // Integer | Number of items per page
    try {
      AutocompleteResults result = apiInstance.autocomplete(in, q, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#autocomplete");
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
| **in** | **String**| The entity to search for | [enum: location] |
| **q** | **String**| The search query | [optional] |
| **page** | **Integer**| The page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of items per page | [optional] [default to 20] |

### Return type

[**AutocompleteResults**](AutocompleteResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

<a id="searchFDADocuments"></a>
# **searchFDADocuments**
> FDADocumentSearchResults searchFDADocuments(q, text, page, perPage)



Search the FDA documents

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://opentrials.local/v1");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String q = "q_example"; // String | The search query (follows the [ElasticSearch Query String](https://www.elastic.co/guide/en/elasticsearch/reference/2.3/query-dsl-query-string-query.html#query-string-syntax) syntax)
    String text = "text_example"; // String | Search query on the documents file's text (follows the [ElasticSearch Simple Query String](https://www.elastic.co/guide/en/elasticsearch/reference/2.3/query-dsl-simple-query-string-query.html#_simple_query_string_syntax) syntax)
    Integer page = 1; // Integer | The page number
    Integer perPage = 20; // Integer | Number of items per page
    try {
      FDADocumentSearchResults result = apiInstance.searchFDADocuments(q, text, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchFDADocuments");
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
| **q** | **String**| The search query (follows the [ElasticSearch Query String](https://www.elastic.co/guide/en/elasticsearch/reference/2.3/query-dsl-query-string-query.html#query-string-syntax) syntax) | [optional] |
| **text** | **String**| Search query on the documents file&#39;s text (follows the [ElasticSearch Simple Query String](https://www.elastic.co/guide/en/elasticsearch/reference/2.3/query-dsl-simple-query-string-query.html#_simple_query_string_syntax) syntax) | [optional] |
| **page** | **Integer**| The page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of items per page | [optional] [default to 20] |

### Return type

[**FDADocumentSearchResults**](FDADocumentSearchResults.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **0** | Error |  -  |

