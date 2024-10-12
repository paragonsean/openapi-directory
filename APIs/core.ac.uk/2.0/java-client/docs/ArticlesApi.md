# ArticlesApi

All URIs are relative to *http://core.ac.uk/api-v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getArticleByCoreId**](ArticlesApi.md#getArticleByCoreId) | **GET** /articles/get/{coreId} | Get article by CORE ID |
| [**getArticleByCoreIdBatch**](ArticlesApi.md#getArticleByCoreIdBatch) | **POST** /articles/get | Batch operation for retrieving articles by CORE ID |
| [**getArticleHistoryByCoreId**](ArticlesApi.md#getArticleHistoryByCoreId) | **GET** /articles/get/{coreId}/history | Get article history by CORE ID |
| [**getArticlePdfByCoreId**](ArticlesApi.md#getArticlePdfByCoreId) | **GET** /articles/get/{coreId}/download/pdf | Get fulltext PDF by CORE ID |
| [**nearDuplicateArticles**](ArticlesApi.md#nearDuplicateArticles) | **POST** /articles/dedup | Get all near duplicate articles |
| [**searchArticles**](ArticlesApi.md#searchArticles) | **GET** /articles/search/{query} | Search through all documents |
| [**searchArticlesBatch**](ArticlesApi.md#searchArticlesBatch) | **POST** /articles/search | Batch operation for search through articles |
| [**similarArticles**](ArticlesApi.md#similarArticles) | **POST** /articles/similar | Get articles by similarity to a text |


<a id="getArticleByCoreId"></a>
# **getArticleByCoreId**
> ArticleResponse getArticleByCoreId(coreId, metadata, fulltext, citations, similar, duplicate, urls, faithfulMetadata)

Get article by CORE ID

Method will retrieve an article based on given CORE ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://core.ac.uk/api-v2");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long coreId = 56L; // Long | CORE ID of the article that needs to be fetched.
    Boolean metadata = true; // Boolean | Whether to retrieve the full article metadata or only the ID. The default value is true.
    Boolean fulltext = false; // Boolean | Whether to retrieve full text of the article. The default value is false
    Boolean citations = false; // Boolean | Whether to retrieve citations found in the article. The default value is false
    Boolean similar = false; // Boolean | Whether to retrieve a list of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time
    Boolean duplicate = false; // Boolean | Whether to retrieve a list of CORE IDs of different versions of the article. The default value is false
    Boolean urls = false; // Boolean | Whether to retrieve a list of URLs from which the article can be downloaded. This can include links to PDFs as well as HTML pages. The default value is false
    Boolean faithfulMetadata = false; // Boolean | Returns the records raw XML metadata from the original repository. The default value is false
    try {
      ArticleResponse result = apiInstance.getArticleByCoreId(coreId, metadata, fulltext, citations, similar, duplicate, urls, faithfulMetadata);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#getArticleByCoreId");
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
| **coreId** | **Long**| CORE ID of the article that needs to be fetched. | |
| **metadata** | **Boolean**| Whether to retrieve the full article metadata or only the ID. The default value is true. | [optional] [default to true] |
| **fulltext** | **Boolean**| Whether to retrieve full text of the article. The default value is false | [optional] [default to false] |
| **citations** | **Boolean**| Whether to retrieve citations found in the article. The default value is false | [optional] [default to false] |
| **similar** | **Boolean**| Whether to retrieve a list of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time | [optional] [default to false] |
| **duplicate** | **Boolean**| Whether to retrieve a list of CORE IDs of different versions of the article. The default value is false | [optional] [default to false] |
| **urls** | **Boolean**| Whether to retrieve a list of URLs from which the article can be downloaded. This can include links to PDFs as well as HTML pages. The default value is false | [optional] [default to false] |
| **faithfulMetadata** | **Boolean**| Returns the records raw XML metadata from the original repository. The default value is false | [optional] [default to false] |

### Return type

[**ArticleResponse**](ArticleResponse.md)

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

<a id="getArticleByCoreIdBatch"></a>
# **getArticleByCoreIdBatch**
> List&lt;ArticleResponse&gt; getArticleByCoreIdBatch(body, metadata, fulltext, citations, similar, duplicate, urls, faithfulMetadata)

Batch operation for retrieving articles by CORE ID

Method accepts a JSON array of CORE IDs and retrieves a list of articles. The response array is ordered based on the order of the IDs in the request array.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://core.ac.uk/api-v2");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    List<Integer> body = Arrays.asList(); // List<Integer> | JSON array with CORE IDs of articles that need to be fetched
    Boolean metadata = true; // Boolean | Whether to retrieve the full article metadata or only the IDs. The default value is true
    Boolean fulltext = false; // Boolean | Whether to retrieve fulltexts of the articles. The default value is false
    Boolean citations = false; // Boolean | Whether to retrieve citations found in the articles. The default value is false
    Boolean similar = false; // Boolean | Whether to retrieve lists of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time
    Boolean duplicate = false; // Boolean | Whether to retrieve CORE IDs of different versions of the articles. The default value is false
    Boolean urls = false; // Boolean | Whether to retrieve lists of URLs of the article fulltexts. The default value is false
    Boolean faithfulMetadata = false; // Boolean | Returns the records raw XML metadata from the original repository. The default value is false
    try {
      List<ArticleResponse> result = apiInstance.getArticleByCoreIdBatch(body, metadata, fulltext, citations, similar, duplicate, urls, faithfulMetadata);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#getArticleByCoreIdBatch");
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
| **body** | [**List&lt;Integer&gt;**](Integer.md)| JSON array with CORE IDs of articles that need to be fetched | |
| **metadata** | **Boolean**| Whether to retrieve the full article metadata or only the IDs. The default value is true | [optional] [default to true] |
| **fulltext** | **Boolean**| Whether to retrieve fulltexts of the articles. The default value is false | [optional] [default to false] |
| **citations** | **Boolean**| Whether to retrieve citations found in the articles. The default value is false | [optional] [default to false] |
| **similar** | **Boolean**| Whether to retrieve lists of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time | [optional] [default to false] |
| **duplicate** | **Boolean**| Whether to retrieve CORE IDs of different versions of the articles. The default value is false | [optional] [default to false] |
| **urls** | **Boolean**| Whether to retrieve lists of URLs of the article fulltexts. The default value is false | [optional] [default to false] |
| **faithfulMetadata** | **Boolean**| Returns the records raw XML metadata from the original repository. The default value is false | [optional] [default to false] |

### Return type

[**List&lt;ArticleResponse&gt;**](ArticleResponse.md)

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

<a id="getArticleHistoryByCoreId"></a>
# **getArticleHistoryByCoreId**
> ArticleHistoryResponse getArticleHistoryByCoreId(coreId, page, pageSize)

Get article history by CORE ID

Method accepts a single CORE ID and returns a list of all historical versions of the article, which are stored in CORE database. The results are ordered from the newest one to the oldest one.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://core.ac.uk/api-v2");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    String coreId = "coreId_example"; // String | CORE ID of the article which history should be fetched
    Integer page = 1; // Integer | Which page of the history results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page).
    Integer pageSize = 10; // Integer | The number of results to return per page. Can be any number between 10 and 100, default is 10.
    try {
      ArticleHistoryResponse result = apiInstance.getArticleHistoryByCoreId(coreId, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#getArticleHistoryByCoreId");
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
| **coreId** | **String**| CORE ID of the article which history should be fetched | |
| **page** | **Integer**| Which page of the history results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page). | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of results to return per page. Can be any number between 10 and 100, default is 10. | [optional] [default to 10] |

### Return type

[**ArticleHistoryResponse**](ArticleHistoryResponse.md)

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

<a id="getArticlePdfByCoreId"></a>
# **getArticlePdfByCoreId**
> getArticlePdfByCoreId(coreId)

Get fulltext PDF by CORE ID

Method will retrieve an article based on given CORE ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://core.ac.uk/api-v2");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    String coreId = "coreId_example"; // String | ID of article history that needs to be fetched
    try {
      apiInstance.getArticlePdfByCoreId(coreId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#getArticlePdfByCoreId");
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
| **coreId** | **String**| ID of article history that needs to be fetched | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **401** | Invalid or no API key provided |  -  |
| **404** | No Article pdf found |  -  |
| **429** | Too many requests in given amount of time |  -  |

<a id="nearDuplicateArticles"></a>
# **nearDuplicateArticles**
> Object nearDuplicateArticles(doi, title, year, description, fulltext, identifier, repositoryId)

Get all near duplicate articles

Method accepts values for several parameters and retrieves a JSON array of articles which have near duplicate content matching the input parameters&#39; values. The response array contains ids of the near duplicate articles along with their relevance scores.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://core.ac.uk/api-v2");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    String doi = "doi_example"; // String | The DOI for which the duplicates will be identified
    String title = "title_example"; // String | Title to match when looking for duplicate articles. Only useful when either value for @year or @description is supplied.
    String year = "year_example"; // String | Year the article was published. Only useful when value for @title is supplied. 
    String description = "description_example"; // String | Abstract for an article based on which its duplicates will be found. Only useful when value for @title is supplied.
    String fulltext = "fulltext_example"; // String | Full text for an article based on which its duplicates will be found.
    String identifier = "identifier_example"; // String | Article identifier for which the duplicates will be identified. Only useful when either values for @doi or (@title and @year) or (@title and @abstract) or @fulltext are supplied.
    String repositoryId = "repositoryId_example"; // String | Limit the duplicates search to particular repository id. 
    try {
      Object result = apiInstance.nearDuplicateArticles(doi, title, year, description, fulltext, identifier, repositoryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#nearDuplicateArticles");
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
| **doi** | **String**| The DOI for which the duplicates will be identified | [optional] |
| **title** | **String**| Title to match when looking for duplicate articles. Only useful when either value for @year or @description is supplied. | [optional] |
| **year** | **String**| Year the article was published. Only useful when value for @title is supplied.  | [optional] |
| **description** | **String**| Abstract for an article based on which its duplicates will be found. Only useful when value for @title is supplied. | [optional] |
| **fulltext** | **String**| Full text for an article based on which its duplicates will be found. | [optional] |
| **identifier** | **String**| Article identifier for which the duplicates will be identified. Only useful when either values for @doi or (@title and @year) or (@title and @abstract) or @fulltext are supplied. | [optional] |
| **repositoryId** | **String**| Limit the duplicates search to particular repository id.  | [optional] |

### Return type

**Object**

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Insufficient/Unsuitable input parameters. |  -  |
| **401** | Invalid or no API key provided |  -  |
| **503** | Could not run the deduplication service at this time; please try again later. |  -  |

<a id="searchArticles"></a>
# **searchArticles**
> ArticleSearchResponse searchArticles(query, page, pageSize, metadata, fulltext, citations, similar, duplicate, urls, faithfulMetadata)

Search through all documents

Searches through all articles and returns a JSON array with search results. Method searches through all article fields.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://core.ac.uk/api-v2");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    Long query = 56L; // Long | The search query
    Integer page = 1; // Integer | Which page of the search results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page).
    Integer pageSize = 10; // Integer | The number of results to return per page. Can be any number between 10 and 100, default is 10.
    Boolean metadata = true; // Boolean | Whether to retrieve the full article metadata or only the ID. The default value is true.
    Boolean fulltext = false; // Boolean | Whether to retrieve full text of the article. The default value is false
    Boolean citations = false; // Boolean | Whether to retrieve citations found in the article. The default value is false
    Boolean similar = false; // Boolean | Whether to retrieve a list of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time
    Boolean duplicate = false; // Boolean | Whether to retrieve a list of CORE IDs of different versions of the article. The default value is false
    Boolean urls = false; // Boolean | Whether to retrieve a list of URLs from which the article can be downloaded. This can include links to PDFs as well as HTML pages. The default value is false
    Boolean faithfulMetadata = false; // Boolean | Returns the records raw XML metadata from the original repository. The default value is false
    try {
      ArticleSearchResponse result = apiInstance.searchArticles(query, page, pageSize, metadata, fulltext, citations, similar, duplicate, urls, faithfulMetadata);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#searchArticles");
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
| **query** | **Long**| The search query | |
| **page** | **Integer**| Which page of the search results should be retrieved. Can be any number betwen 1 and 100, default is 1 (first page). | [optional] [default to 1] |
| **pageSize** | **Integer**| The number of results to return per page. Can be any number between 10 and 100, default is 10. | [optional] [default to 10] |
| **metadata** | **Boolean**| Whether to retrieve the full article metadata or only the ID. The default value is true. | [optional] [default to true] |
| **fulltext** | **Boolean**| Whether to retrieve full text of the article. The default value is false | [optional] [default to false] |
| **citations** | **Boolean**| Whether to retrieve citations found in the article. The default value is false | [optional] [default to false] |
| **similar** | **Boolean**| Whether to retrieve a list of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time | [optional] [default to false] |
| **duplicate** | **Boolean**| Whether to retrieve a list of CORE IDs of different versions of the article. The default value is false | [optional] [default to false] |
| **urls** | **Boolean**| Whether to retrieve a list of URLs from which the article can be downloaded. This can include links to PDFs as well as HTML pages. The default value is false | [optional] [default to false] |
| **faithfulMetadata** | **Boolean**| Returns the records raw XML metadata from the original repository. The default value is false | [optional] [default to false] |

### Return type

[**ArticleSearchResponse**](ArticleSearchResponse.md)

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

<a id="searchArticlesBatch"></a>
# **searchArticlesBatch**
> List&lt;ArticleSearchResponse&gt; searchArticlesBatch(body, metadata, fulltext, citations, similar, duplicate, urls, faithfulMetadata)

Batch operation for search through articles

Method accepts a JSON array of search queries and parameters. It then searches through all articles and returns a JSON array of search results for each of the queries. Method searches through all article fields (title, authors, subjects, identifiers, etc.).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://core.ac.uk/api-v2");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    List<SearchRequest> body = Arrays.asList(); // List<SearchRequest> | JSON array with search queries and parameters. One request can contain up to 100 queries
    Boolean metadata = true; // Boolean | Whether to retrieve the full article metadata or only the ID. The default value is true.
    Boolean fulltext = false; // Boolean | Whether to retrieve full text of the article. The default value is false
    Boolean citations = false; // Boolean | Whether to retrieve citations found in the article. The default value is false
    Boolean similar = false; // Boolean | Whether to retrieve a list of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time
    Boolean duplicate = false; // Boolean | Whether to retrieve a list of CORE IDs of different versions of the article. The default value is false
    Boolean urls = false; // Boolean | Whether to retrieve a list of URLs from which the article can be downloaded. This can include links to PDFs as well as HTML pages. The default value is false
    Boolean faithfulMetadata = false; // Boolean | Whether to retrieve the raw XML metadata of the article. The default value is false
    try {
      List<ArticleSearchResponse> result = apiInstance.searchArticlesBatch(body, metadata, fulltext, citations, similar, duplicate, urls, faithfulMetadata);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#searchArticlesBatch");
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
| **metadata** | **Boolean**| Whether to retrieve the full article metadata or only the ID. The default value is true. | [optional] [default to true] |
| **fulltext** | **Boolean**| Whether to retrieve full text of the article. The default value is false | [optional] [default to false] |
| **citations** | **Boolean**| Whether to retrieve citations found in the article. The default value is false | [optional] [default to false] |
| **similar** | **Boolean**| Whether to retrieve a list of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time | [optional] [default to false] |
| **duplicate** | **Boolean**| Whether to retrieve a list of CORE IDs of different versions of the article. The default value is false | [optional] [default to false] |
| **urls** | **Boolean**| Whether to retrieve a list of URLs from which the article can be downloaded. This can include links to PDFs as well as HTML pages. The default value is false | [optional] [default to false] |
| **faithfulMetadata** | **Boolean**| Whether to retrieve the raw XML metadata of the article. The default value is false | [optional] [default to false] |

### Return type

[**List&lt;ArticleSearchResponse&gt;**](ArticleSearchResponse.md)

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

<a id="similarArticles"></a>
# **similarArticles**
> ArticleSimilarResponse similarArticles(body, limit, metadata, fulltext, citations, similar, duplicate, urls, faithfulMetadata)

Get articles by similarity to a text

Method accepts a text and retrieves a JSON array of articles which are similar to the given text. The response array is ordered based on similarity score, starting from the most similar.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArticlesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://core.ac.uk/api-v2");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ArticlesApi apiInstance = new ArticlesApi(defaultClient);
    SimilarRequest body = new SimilarRequest(); // SimilarRequest | The text that requires similar articles to be calculated on
    Integer limit = 10; // Integer | How many similar articles to retrieve at most. Can be any number betwen 1 and 100, default is 10
    Boolean metadata = true; // Boolean | Whether to retrieve the full article metadata or only the IDs of the similar articles. The default value is true
    Boolean fulltext = false; // Boolean | Whether to retrieve fulltexts of the similar articles. The default value is false
    Boolean citations = false; // Boolean | Whether to retrieve citations found in the articles. The default value is false
    Boolean similar = false; // Boolean | Whether to retrieve lists of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time
    Boolean duplicate = false; // Boolean | Whether to retrieve CORE IDs of different versions of the articles. The default value is false
    Boolean urls = false; // Boolean | Whether to retrieve lists of URLs of the article fulltexts. The default value is false
    Boolean faithfulMetadata = false; // Boolean | Whether to retrieve the raw XML metadata of the articles. The default value is false
    try {
      ArticleSimilarResponse result = apiInstance.similarArticles(body, limit, metadata, fulltext, citations, similar, duplicate, urls, faithfulMetadata);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArticlesApi#similarArticles");
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
| **body** | [**SimilarRequest**](SimilarRequest.md)| The text that requires similar articles to be calculated on | |
| **limit** | **Integer**| How many similar articles to retrieve at most. Can be any number betwen 1 and 100, default is 10 | [optional] [default to 10] |
| **metadata** | **Boolean**| Whether to retrieve the full article metadata or only the IDs of the similar articles. The default value is true | [optional] [default to true] |
| **fulltext** | **Boolean**| Whether to retrieve fulltexts of the similar articles. The default value is false | [optional] [default to false] |
| **citations** | **Boolean**| Whether to retrieve citations found in the articles. The default value is false | [optional] [default to false] |
| **similar** | **Boolean**| Whether to retrieve lists of similar articles. The default value is false. Because the similar articles are calculated on demand, setting this parameter to true might slightly slow down the response time | [optional] [default to false] |
| **duplicate** | **Boolean**| Whether to retrieve CORE IDs of different versions of the articles. The default value is false | [optional] [default to false] |
| **urls** | **Boolean**| Whether to retrieve lists of URLs of the article fulltexts. The default value is false | [optional] [default to false] |
| **faithfulMetadata** | **Boolean**| Whether to retrieve the raw XML metadata of the articles. The default value is false | [optional] [default to false] |

### Return type

[**ArticleSimilarResponse**](ArticleSimilarResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **400** | Missing text in request body or parameter out of bounds or invalid parameter |  -  |
| **401** | Invalid or no API key provided |  -  |
| **429** | Too many requests in given amount of time |  -  |

