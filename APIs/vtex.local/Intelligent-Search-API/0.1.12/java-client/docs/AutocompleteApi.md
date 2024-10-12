# AutocompleteApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**autocompleteSuggestionsGet**](AutocompleteApi.md#autocompleteSuggestionsGet) | **GET** /autocomplete_suggestions | Get list of suggested terms and attributes similar to the search term |
| [**topSearchesGet**](AutocompleteApi.md#topSearchesGet) | **GET** /top_searches | Get list of the 10 most searched terms |


<a id="autocompleteSuggestionsGet"></a>
# **autocompleteSuggestionsGet**
> AutocompleteSearchSuggestions autocompleteSuggestionsGet(query, locale)

Get list of suggested terms and attributes similar to the search term

Lists the suggested terms and attributes similar to the search term.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutocompleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    AutocompleteApi apiInstance = new AutocompleteApi(defaultClient);
    String query = "query_example"; // String | Search term. It can contain any character.
    String locale = "en-US"; // String | Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language.
    try {
      AutocompleteSearchSuggestions result = apiInstance.autocompleteSuggestionsGet(query, locale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutocompleteApi#autocompleteSuggestionsGet");
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
| **query** | **String**| Search term. It can contain any character. | [optional] |
| **locale** | **String**| Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language. | [optional] |

### Return type

[**AutocompleteSearchSuggestions**](AutocompleteSearchSuggestions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **5XX** | Server error. |  -  |

<a id="topSearchesGet"></a>
# **topSearchesGet**
> TopSearches topSearchesGet(locale)

Get list of the 10 most searched terms

Lists the 10 most searched terms.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AutocompleteApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    AutocompleteApi apiInstance = new AutocompleteApi(defaultClient);
    String locale = "en-US"; // String | Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language.
    try {
      TopSearches result = apiInstance.topSearchesGet(locale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AutocompleteApi#topSearchesGet");
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
| **locale** | **String**| Indicates the target language as a BCP 47 language code. The Intelligent Search must have indexed the account in the target language. | [optional] |

### Return type

[**TopSearches**](TopSearches.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **5XX** | Server error. |  -  |

