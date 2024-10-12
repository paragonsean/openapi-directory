# DiagnosisApi

All URIs are relative to *https://api.infermedica.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**computeDiagnosis**](DiagnosisApi.md#computeDiagnosis) | **POST** /diagnosis | Query diagnostic engine |


<a id="computeDiagnosis"></a>
# **computeDiagnosis**
> DiagnosisResponsePublic computeDiagnosis(body)

Query diagnostic engine

Suggests possible diagnoses and relevant observations based on provided patient information.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DiagnosisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.infermedica.com/v2");

    DiagnosisApi apiInstance = new DiagnosisApi(defaultClient);
    DiagnosisRequest body = new DiagnosisRequest(); // DiagnosisRequest | 
    try {
      DiagnosisResponsePublic result = apiInstance.computeDiagnosis(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DiagnosisApi#computeDiagnosis");
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

[**DiagnosisResponsePublic**](DiagnosisResponsePublic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

