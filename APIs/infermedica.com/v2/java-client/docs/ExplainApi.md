# ExplainApi

All URIs are relative to *https://api.infermedica.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**computeExplanation**](ExplainApi.md#computeExplanation) | **POST** /explain | Query diagnostic engine for explanation |


<a id="computeExplanation"></a>
# **computeExplanation**
> ExplanationResponse computeExplanation(body)

Query diagnostic engine for explanation

Explains which evidence impact probability of selected condition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExplainApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.infermedica.com/v2");

    ExplainApi apiInstance = new ExplainApi(defaultClient);
    ExplanationRequest body = new ExplanationRequest(); // ExplanationRequest | 
    try {
      ExplanationResponse result = apiInstance.computeExplanation(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExplainApi#computeExplanation");
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
| **body** | [**ExplanationRequest**](ExplanationRequest.md)|  | |

### Return type

[**ExplanationResponse**](ExplanationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

