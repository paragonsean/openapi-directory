# SwaggerDocsApi

All URIs are relative to *http://nsidc.org/api/dataset/2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**facets**](SwaggerDocsApi.md#facets) | **GET** /Facets | View the facet information corresponding to a search |
| [**id**](SwaggerDocsApi.md#id) | **GET** /suggest | Suggest search terms based on a partial query |
| [**openSearch**](SwaggerDocsApi.md#openSearch) | **GET** /OpenSearch | Search documents using the OpenSearch 1.1 Specification |
| [**opensearchDescription**](SwaggerDocsApi.md#opensearchDescription) | **GET** /OpenSearchDescription | Describes the web interface of NSIDC&#39;s data search engine |


<a id="facets"></a>
# **facets**
> String facets(searchTerms, count, startIndex, spatial, sortKeys, startDate, endDate, facetFilters, source)

View the facet information corresponding to a search

In the NSIDC Search and Arctic Data Explorer interfaces, this endpoint is used in conjunction with /OpenSearch whenever a user submits a new search. Consequently, it has the same parameters as /OpenSearch.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwaggerDocsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://nsidc.org/api/dataset/2");

    SwaggerDocsApi apiInstance = new SwaggerDocsApi(defaultClient);
    String searchTerms = "searchTerms_example"; // String | URL-encoded keyword or keywords desired by the client; OpenSearch 1.1
    Integer count = 25; // Integer | The number of search results per page desired by the client; OpenSearch 1.1
    Integer startIndex = 1; // Integer | First search result desired by the search client; OpenSearch 1.1
    String spatial = "-180.0,-90.0,180.0,90.0"; // String | 4 comma separated values - W, S, E, N; OpenSearch-Geo 1.0, \"box\" parameter
    String sortKeys = "score,,desc"; // String | Sort the results by most relevant (default), smallest or largest spatial area, shortest or longest temporal duration, or most recently updated; partial implementation of OpenSearch SRU 1.0
    LocalDate startDate = LocalDate.now(); // LocalDate | The start date in yyyy-mm-dd format
    LocalDate endDate = LocalDate.now(); // LocalDate | The end date in yyyy-mm-dd format
    String facetFilters = "facetFilters_example"; // String | Describes faceted restrictions on the search. A URL-encoded JSON object where the keys are the names of the facet, and the values are arrays of the selected facet values
    String source = "NSIDC"; // String | Custom parameter for selecting which source to use; the Arctic Data Explorer (ADE) uses data aggregated from many sources, including, but not limited to, NSIDC
    try {
      String result = apiInstance.facets(searchTerms, count, startIndex, spatial, sortKeys, startDate, endDate, facetFilters, source);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwaggerDocsApi#facets");
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
| **searchTerms** | **String**| URL-encoded keyword or keywords desired by the client; OpenSearch 1.1 | [optional] |
| **count** | **Integer**| The number of search results per page desired by the client; OpenSearch 1.1 | [optional] [default to 25] |
| **startIndex** | **Integer**| First search result desired by the search client; OpenSearch 1.1 | [optional] [default to 1] |
| **spatial** | **String**| 4 comma separated values - W, S, E, N; OpenSearch-Geo 1.0, \&quot;box\&quot; parameter | [optional] [default to -180.0,-90.0,180.0,90.0] |
| **sortKeys** | **String**| Sort the results by most relevant (default), smallest or largest spatial area, shortest or longest temporal duration, or most recently updated; partial implementation of OpenSearch SRU 1.0 | [optional] [default to score,,desc] [enum: score,,desc, spatial_area,,asc, spatial_area,,desc, temporal_duration,,asc, temporal_duration,,desc, updated,,desc] |
| **startDate** | **LocalDate**| The start date in yyyy-mm-dd format | [optional] |
| **endDate** | **LocalDate**| The end date in yyyy-mm-dd format | [optional] |
| **facetFilters** | **String**| Describes faceted restrictions on the search. A URL-encoded JSON object where the keys are the names of the facet, and the values are arrays of the selected facet values | [optional] |
| **source** | **String**| Custom parameter for selecting which source to use; the Arctic Data Explorer (ADE) uses data aggregated from many sources, including, but not limited to, NSIDC | [optional] [default to NSIDC] [enum: NSIDC, ADE] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/nsidcfacets+xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad request |  -  |
| **500** | Internal server error |  -  |

<a id="id"></a>
# **id**
> String id(q, source)

Suggest search terms based on a partial query

In NSIDC Search and the Arctic Data Explorer, this endpoint is queried whenever the user types into the search terms box, and the returned suggestions are displayed in a dropdown beneath the search terms box. The q parameter and returned JSON follow the specifications of the OpenSearch Suggestions 1.0 extension.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwaggerDocsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://nsidc.org/api/dataset/2");

    SwaggerDocsApi apiInstance = new SwaggerDocsApi(defaultClient);
    String q = "q_example"; // String | Search terms typed into the interface (minimum two characters)
    String source = "NSIDC"; // String | Custom parameter for selecting which source to use; the Arctic Data Explorer (ADE) uses data aggregated from many sources, including, but not limited to, NSIDC
    try {
      String result = apiInstance.id(q, source);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwaggerDocsApi#id");
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
| **q** | **String**| Search terms typed into the interface (minimum two characters) | |
| **source** | **String**| Custom parameter for selecting which source to use; the Arctic Data Explorer (ADE) uses data aggregated from many sources, including, but not limited to, NSIDC | [default to NSIDC] [enum: NSIDC, ADE] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-suggestions+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad request |  -  |
| **500** | Internal server error |  -  |

<a id="openSearch"></a>
# **openSearch**
> String openSearch(searchTerms, count, startIndex, spatial, sortKeys, startDate, endDate, facetFilters, source)

Search documents using the OpenSearch 1.1 Specification

This endpoint uses parameters from the OpenSearch 1.1 specification, as well as parameters from the OpenSearch Geo (1.0) and SRU (1.0) extensions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwaggerDocsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://nsidc.org/api/dataset/2");

    SwaggerDocsApi apiInstance = new SwaggerDocsApi(defaultClient);
    String searchTerms = "searchTerms_example"; // String | URL-encoded keyword or keywords desired by the client; OpenSearch 1.1
    Integer count = 25; // Integer | The number of search results per page desired by the client; OpenSearch 1.1
    Integer startIndex = 1; // Integer | First search result desired by the search client; OpenSearch 1.1
    String spatial = "-180.0,-90.0,180.0,90.0"; // String | 4 comma separated values - W, S, E, N; OpenSearch-Geo 1.0, \"box\" parameter
    String sortKeys = "score,,desc"; // String | Sort the results by most relevant (default), smallest or largest spatial area, shortest or longest temporal duration, or most recently updated; partial implementation of OpenSearch SRU 1.0
    LocalDate startDate = LocalDate.now(); // LocalDate | The start date in yyyy-mm-dd format
    LocalDate endDate = LocalDate.now(); // LocalDate | The end date in yyyy-mm-dd format
    String facetFilters = "facetFilters_example"; // String | Describes faceted restrictions on the search. A URL-encoded JSON object where the keys are the names of the facet, and the values are arrays of the selected facet values
    String source = "NSIDC"; // String | Custom parameter for selecting which source to use; the Arctic Data Explorer (ADE) uses data aggregated from many sources, including, but not limited to, NSIDC
    try {
      String result = apiInstance.openSearch(searchTerms, count, startIndex, spatial, sortKeys, startDate, endDate, facetFilters, source);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwaggerDocsApi#openSearch");
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
| **searchTerms** | **String**| URL-encoded keyword or keywords desired by the client; OpenSearch 1.1 | [optional] |
| **count** | **Integer**| The number of search results per page desired by the client; OpenSearch 1.1 | [optional] [default to 25] |
| **startIndex** | **Integer**| First search result desired by the search client; OpenSearch 1.1 | [optional] [default to 1] |
| **spatial** | **String**| 4 comma separated values - W, S, E, N; OpenSearch-Geo 1.0, \&quot;box\&quot; parameter | [optional] [default to -180.0,-90.0,180.0,90.0] |
| **sortKeys** | **String**| Sort the results by most relevant (default), smallest or largest spatial area, shortest or longest temporal duration, or most recently updated; partial implementation of OpenSearch SRU 1.0 | [optional] [default to score,,desc] [enum: score,,desc, spatial_area,,asc, spatial_area,,desc, temporal_duration,,asc, temporal_duration,,desc, updated,,desc] |
| **startDate** | **LocalDate**| The start date in yyyy-mm-dd format | [optional] |
| **endDate** | **LocalDate**| The end date in yyyy-mm-dd format | [optional] |
| **facetFilters** | **String**| Describes faceted restrictions on the search. A URL-encoded JSON object where the keys are the names of the facet, and the values are arrays of the selected facet values | [optional] |
| **source** | **String**| Custom parameter for selecting which source to use; the Arctic Data Explorer (ADE) uses data aggregated from many sources, including, but not limited to, NSIDC | [optional] [default to NSIDC] [enum: NSIDC, ADE] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/atom+xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad request |  -  |
| **500** | Internal server error |  -  |

<a id="opensearchDescription"></a>
# **opensearchDescription**
> String opensearchDescription()

Describes the web interface of NSIDC&#39;s data search engine

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SwaggerDocsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://nsidc.org/api/dataset/2");

    SwaggerDocsApi apiInstance = new SwaggerDocsApi(defaultClient);
    try {
      String result = apiInstance.opensearchDescription();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SwaggerDocsApi#opensearchDescription");
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

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/opensearchdescription+xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

