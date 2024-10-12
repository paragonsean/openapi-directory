# SuggestApi

All URIs are relative to *https://api.infermedica.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSuggestions**](SuggestApi.md#getSuggestions) | **POST** /suggest | Query diagnostic engine for related symptoms |


<a id="getSuggestions"></a>
# **getSuggestions**
> List&lt;SuggestResult&gt; getSuggestions(body, maxResults)

Query diagnostic engine for related symptoms

Suggests possible symptoms based on provided patient information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SuggestApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.infermedica.com/v2");

    SuggestApi apiInstance = new SuggestApi(defaultClient);
    SuggestRequest body = new SuggestRequest(); // SuggestRequest | 
    Integer maxResults = 8; // Integer | maximum number of results
    try {
      List<SuggestResult> result = apiInstance.getSuggestions(body, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SuggestApi#getSuggestions");
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
| **body** | [**SuggestRequest**](SuggestRequest.md)|  | |
| **maxResults** | **Integer**| maximum number of results | [optional] [default to 8] |

### Return type

[**List&lt;SuggestResult&gt;**](SuggestResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

