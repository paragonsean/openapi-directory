# SearchApi

All URIs are relative to *https://api.trakt.tv*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getIDLookupResults**](SearchApi.md#getIDLookupResults) | **GET** /search/{id_type}/{id} | Get ID lookup results |
| [**getTextQueryResults**](SearchApi.md#getTextQueryResults) | **GET** /search/{type} | Get text query results |


<a id="getIDLookupResults"></a>
# **getIDLookupResults**
> getIDLookupResults(idType, id, type, traktApiVersion, traktApiKey)

Get ID lookup results

#### &amp;#128196; Pagination &amp;#10024; Extended Info  Lookup items by their Trakt, IMDB, TMDB, or TVDB ID. If you use the search url without a &#x60;type&#x60; it might return multiple items if the &#x60;id_type&#x60; is not globally unique. Specify the &#x60;type&#x60; of results by sending a single value or a comma delimited string for multiple types.  | Type | URL | |---|---| | &#x60;trakt&#x60; | &#x60;/search/trakt/:id&#x60; | |  | &#x60;/search/trakt/:id?type&#x3D;movie&#x60; | |  | &#x60;/search/trakt/:id?type&#x3D;show&#x60; | |  | &#x60;/search/trakt/:id?type&#x3D;episode&#x60; | |  | &#x60;/search/trakt/:id?type&#x3D;person&#x60; | | &#x60;imdb&#x60; | &#x60;/search/imdb/:id&#x60; | | &#x60;tmdb&#x60; | &#x60;/search/tmdb/:id&#x60; | |  | &#x60;/search/tmdb/:id?type&#x3D;movie&#x60; | |  | &#x60;/search/tmdb/:id?type&#x3D;show&#x60; | |  | &#x60;/search/tmdb/:id?type&#x3D;episode&#x60; | |  | &#x60;/search/tmdb/:id?type&#x3D;person&#x60; | | &#x60;tvdb&#x60; | &#x60;/search/tvdb/:id&#x60; | |  | &#x60;/search/tvdb/:id?type&#x3D;show&#x60; | |  | &#x60;/search/tvdb/:id?type&#x3D;episode&#x60; |

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
    defaultClient.setBasePath("https://api.trakt.tv");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String idType = "trakt"; // String | Type of ID to lookup.
    String id = "tt0848228"; // String | ID that matches with the type.
    String type = "movie"; // String | Search type.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    try {
      apiInstance.getIDLookupResults(idType, id, type, traktApiVersion, traktApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#getIDLookupResults");
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
| **idType** | **String**| Type of ID to lookup. | [enum: trakt, imdb, tmdb, tvdb] |
| **id** | **String**| ID that matches with the type. | |
| **type** | **String**| Search type. | [optional] [enum: movie, show, episode, person, list] |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | &#x60;&#x60;&#x60; /search/trakt/12601?type&#x3D;movie /search/imdb/tt1104001 &#x60;&#x60;&#x60; |  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  |

<a id="getTextQueryResults"></a>
# **getTextQueryResults**
> getTextQueryResults(type, query, traktApiVersion, traktApiKey, body)

Get text query results

#### &amp;#128196; Pagination &amp;#10024; Extended Info &amp;#127898; Filters  Search all text fields that a media object contains (i.e. title, overview, etc). Results are ordered by the most relevant score. Specify the &#x60;type&#x60; of results by sending a single value or a comma delimited string for multiple types.  #### Special Characters  Our search engine (Solr) gives the following characters special meaning when they appear in a query:  &#x60;+ - &amp;&amp; || ! ( ) { } [ ] ^ \&quot; ~ * ? : /&#x60;  To interpret any of these characters literally (and not as a special character), precede the character with a backslash &#x60;\\&#x60; character.  #### Search Fields  By default, all text fields are used to search for the &#x60;query&#x60;. You can optionally specify the &#x60;fields&#x60; parameter with a single value or comma delimited string for multiple fields. Each &#x60;type&#x60; has specific &#x60;fields&#x60; that can be specified. This can be useful if you want to support more strict searches (i.e. title only).  | Type | Field | |---|---| | &#x60;movie&#x60; | &#x60;title&#x60; | |  | &#x60;tagline&#x60; | |  | &#x60;overview&#x60; | |  | &#x60;people&#x60; | |  | &#x60;translations&#x60; | |  | &#x60;aliases&#x60; | | &#x60;show&#x60; | &#x60;title&#x60; | |  | &#x60;overview&#x60; | |  | &#x60;people&#x60; | |  | &#x60;translations&#x60; | |  | &#x60;aliases&#x60; | | &#x60;episode&#x60; | &#x60;title&#x60; | |  | &#x60;overview&#x60; | | &#x60;person&#x60; | &#x60;name&#x60; | |  | &#x60;biography&#x60; | | &#x60;list&#x60; | &#x60;name&#x60; | |  | &#x60;description&#x60; |

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
    defaultClient.setBasePath("https://api.trakt.tv");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String type = "movie"; // String | Search type.
    String query = "tron"; // String | Search all text based fields.
    String traktApiVersion = "2"; // String | e.g. 2
    String traktApiKey = "[client_id]"; // String | e.g. [client_id]
    String body = "body_example"; // String | Specific text fields.
    try {
      apiInstance.getTextQueryResults(type, query, traktApiVersion, traktApiKey, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#getTextQueryResults");
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
| **type** | **String**| Search type. | [enum: movie, show, episode, person, list] |
| **query** | **String**| Search all text based fields. | |
| **traktApiVersion** | **String**| e.g. 2 | [optional] |
| **traktApiKey** | **String**| e.g. [client_id] | [optional] |
| **body** | **String**| Specific text fields. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | &#x60;&#x60;&#x60; /search/movie,show,episode,person,list?query&#x3D;tron &#x60;&#x60;&#x60; |  * X-Pagination-Item-Count -  <br>  * X-Pagination-Limit -  <br>  * X-Pagination-Page -  <br>  * X-Pagination-Page-Count -  <br>  |

