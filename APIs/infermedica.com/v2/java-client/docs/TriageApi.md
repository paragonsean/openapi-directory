# TriageApi

All URIs are relative to *https://api.infermedica.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**computeTriage**](TriageApi.md#computeTriage) | **POST** /triage | Query diagnostic engine for triage level |


<a id="computeTriage"></a>
# **computeTriage**
> TriageResponse computeTriage(body)

Query diagnostic engine for triage level

Estimates triage level based on provided patient information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TriageApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.infermedica.com/v2");

    TriageApi apiInstance = new TriageApi(defaultClient);
    DiagnosisRequest body = new DiagnosisRequest(); // DiagnosisRequest | 
    try {
      TriageResponse result = apiInstance.computeTriage(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TriageApi#computeTriage");
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

### Return type

[**TriageResponse**](TriageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

