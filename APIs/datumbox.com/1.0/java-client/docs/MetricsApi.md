# MetricsApi

All URIs are relative to *http://api.datumbox.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**documentSimilarity**](MetricsApi.md#documentSimilarity) | **POST** /1.0/DocumentSimilarity.json | Estimates the similarity between 2 Documents |


<a id="documentSimilarity"></a>
# **documentSimilarity**
> documentSimilarity(apiKey, copy, original)

Estimates the similarity between 2 Documents

The Document Similarity function estimates the degree of similarity between two documents. It can be used to detect duplicate webpages or detect plagiarism.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MetricsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.datumbox.com");

    MetricsApi apiInstance = new MetricsApi(defaultClient);
    String apiKey = "apiKey_example"; // String | Your API Key
    String copy = "copy_example"; // String | The second text. It should not contain HTML tags.
    String original = "original_example"; // String | The first text. It should not contain HTML tags.
    try {
      apiInstance.documentSimilarity(apiKey, copy, original);
    } catch (ApiException e) {
      System.err.println("Exception when calling MetricsApi#documentSimilarity");
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
| **apiKey** | **String**| Your API Key | |
| **copy** | **String**| The second text. It should not contain HTML tags. | [optional] |
| **original** | **String**| The first text. It should not contain HTML tags. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

