# RedFlagsApi

All URIs are relative to *https://api.infermedica.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**computeRedFlags**](RedFlagsApi.md#computeRedFlags) | **POST** /red_flags | Query the diagnostic engine for possible red flag symptoms |


<a id="computeRedFlags"></a>
# **computeRedFlags**
> List&lt;SuggestResult&gt; computeRedFlags(body, maxResults)

Query the diagnostic engine for possible red flag symptoms

Suggests possible red flag symptoms based on provided patient information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RedFlagsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.infermedica.com/v2");

    RedFlagsApi apiInstance = new RedFlagsApi(defaultClient);
    DiagnosisRequest body = new DiagnosisRequest(); // DiagnosisRequest | 
    Integer maxResults = 8; // Integer | maximum number of results
    try {
      List<SuggestResult> result = apiInstance.computeRedFlags(body, maxResults);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RedFlagsApi#computeRedFlags");
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
| **body** | [**DiagnosisRequest**](DiagnosisRequest.md)|  | |
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

