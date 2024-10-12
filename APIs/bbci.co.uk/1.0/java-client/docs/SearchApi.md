# SearchApi

All URIs are relative to *https://ibl.api.bbci.co.uk/ibl/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**search**](SearchApi.md#search) | **GET** /search | Search |
| [**searchSuggest**](SearchApi.md#searchSuggest) | **GET** /search-suggest | Search-suggest |


<a id="search"></a>
# **search**
> Object search(q, lang, rights, availability)

Search

Search

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
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String q = "q_example"; // String | The term to search for.
    String lang = "en"; // String | The language for any applicable localised strings.
    String rights = "mobile"; // String | The rights group to limit results to.
    String availability = "all"; // String | Whether to return all, or available programmes
    try {
      Object result = apiInstance.search(q, lang, rights, availability);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#search");
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
| **q** | **String**| The term to search for. | |
| **lang** | **String**| The language for any applicable localised strings. | [enum: en, cy, ga, gd, pi] |
| **rights** | **String**| The rights group to limit results to. | [default to web] [enum: mobile, tv, web] |
| **availability** | **String**| Whether to return all, or available programmes | [default to available] [enum: all, available] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="searchSuggest"></a>
# **searchSuggest**
> Object searchSuggest(q, lang, rights, availability)

Search-suggest

Search-suggest

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
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String q = "q_example"; // String | The term to search for.
    String lang = "en"; // String | The language for any applicable localised strings.
    String rights = "mobile"; // String | The rights group to limit results to.
    String availability = "all"; // String | Whether to return all, or available programmes
    try {
      Object result = apiInstance.searchSuggest(q, lang, rights, availability);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchSuggest");
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
| **q** | **String**| The term to search for. | |
| **lang** | **String**| The language for any applicable localised strings. | [enum: en, cy, ga, gd, pi] |
| **rights** | **String**| The rights group to limit results to. | [default to web] [enum: mobile, tv, web] |
| **availability** | **String**| Whether to return all, or available programmes | [default to available] [enum: all, available] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

