# SearchApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiSearchIndexTermSearchResultsSearchTermGet**](SearchApi.md#apiSearchIndexTermSearchResultsSearchTermGet) | **GET** /api/Search/IndexTermSearchResults/{searchTerm} | Returns a list of index terms which contain the search term. |
| [**apiSearchParagraphReferenceGet**](SearchApi.md#apiSearchParagraphReferenceGet) | **GET** /api/Search/Paragraph/{reference} | Returns a section overview by reference. |
| [**apiSearchParagraphSearchResultsSearchTermGet**](SearchApi.md#apiSearchParagraphSearchResultsSearchTermGet) | **GET** /api/Search/ParagraphSearchResults/{searchTerm} | Returns a list of paragraphs which contain the search term. |
| [**apiSearchSectionSearchResultsSearchTermGet**](SearchApi.md#apiSearchSectionSearchResultsSearchTermGet) | **GET** /api/Search/SectionSearchResults/{searchTerm} | Returns a list of sections which contain the search term. |


<a id="apiSearchIndexTermSearchResultsSearchTermGet"></a>
# **apiSearchIndexTermSearchResultsSearchTermGet**
> ErskineMayIndexTermSearchResultErskineMaySearch apiSearchIndexTermSearchResultsSearchTermGet(searchTerm, skip, take)

Returns a list of index terms which contain the search term.

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
    defaultClient.setBasePath("http://localhost");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String searchTerm = "searchTerm_example"; // String | Index terms which contain search term.
    Integer skip = 0; // Integer | The number of records to skip from the first, default is 0.
    Integer take = 20; // Integer | The number of records to return, default is 20, maximum is 20.
    try {
      ErskineMayIndexTermSearchResultErskineMaySearch result = apiInstance.apiSearchIndexTermSearchResultsSearchTermGet(searchTerm, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#apiSearchIndexTermSearchResultsSearchTermGet");
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
| **searchTerm** | **String**| Index terms which contain search term. | |
| **skip** | **Integer**| The number of records to skip from the first, default is 0. | [optional] [default to 0] |
| **take** | **Integer**| The number of records to return, default is 20, maximum is 20. | [optional] [default to 20] |

### Return type

[**ErskineMayIndexTermSearchResultErskineMaySearch**](ErskineMayIndexTermSearchResultErskineMaySearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiSearchParagraphReferenceGet"></a>
# **apiSearchParagraphReferenceGet**
> ErskineMaySectionOverview apiSearchParagraphReferenceGet(reference)

Returns a section overview by reference.

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
    defaultClient.setBasePath("http://localhost");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String reference = "reference_example"; // String | Section overview by reference.
    try {
      ErskineMaySectionOverview result = apiInstance.apiSearchParagraphReferenceGet(reference);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#apiSearchParagraphReferenceGet");
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
| **reference** | **String**| Section overview by reference. | |

### Return type

[**ErskineMaySectionOverview**](ErskineMaySectionOverview.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |

<a id="apiSearchParagraphSearchResultsSearchTermGet"></a>
# **apiSearchParagraphSearchResultsSearchTermGet**
> ErskineMayParagraphSearchResultErskineMaySearch apiSearchParagraphSearchResultsSearchTermGet(searchTerm, skip, take)

Returns a list of paragraphs which contain the search term.

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
    defaultClient.setBasePath("http://localhost");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String searchTerm = "searchTerm_example"; // String | Paragraphs which contain search term in their content.
    Integer skip = 0; // Integer | The number of records to skip from the first, default is 0.
    Integer take = 20; // Integer | The number of records to return, default is 20, maximum is 20.
    try {
      ErskineMayParagraphSearchResultErskineMaySearch result = apiInstance.apiSearchParagraphSearchResultsSearchTermGet(searchTerm, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#apiSearchParagraphSearchResultsSearchTermGet");
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
| **searchTerm** | **String**| Paragraphs which contain search term in their content. | |
| **skip** | **Integer**| The number of records to skip from the first, default is 0. | [optional] [default to 0] |
| **take** | **Integer**| The number of records to return, default is 20, maximum is 20. | [optional] [default to 20] |

### Return type

[**ErskineMayParagraphSearchResultErskineMaySearch**](ErskineMayParagraphSearchResultErskineMaySearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="apiSearchSectionSearchResultsSearchTermGet"></a>
# **apiSearchSectionSearchResultsSearchTermGet**
> ErskineMaySectionSearchResultErskineMaySearch apiSearchSectionSearchResultsSearchTermGet(searchTerm, skip, take)

Returns a list of sections which contain the search term.

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
    defaultClient.setBasePath("http://localhost");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String searchTerm = "searchTerm_example"; // String | Sections which contain search term in their title.
    Integer skip = 0; // Integer | The number of records to skip from the first, default is 0.
    Integer take = 20; // Integer | The number of records to return, default is 20, maximum is 20.
    try {
      ErskineMaySectionSearchResultErskineMaySearch result = apiInstance.apiSearchSectionSearchResultsSearchTermGet(searchTerm, skip, take);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#apiSearchSectionSearchResultsSearchTermGet");
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
| **searchTerm** | **String**| Sections which contain search term in their title. | |
| **skip** | **Integer**| The number of records to skip from the first, default is 0. | [optional] [default to 0] |
| **take** | **Integer**| The number of records to return, default is 20, maximum is 20. | [optional] [default to 20] |

### Return type

[**ErskineMaySectionSearchResultErskineMaySearch**](ErskineMaySectionSearchResultErskineMaySearch.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

