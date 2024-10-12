# RationaleApi

All URIs are relative to *https://api.infermedica.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**computeRationale**](RationaleApi.md#computeRationale) | **POST** /rationale | Query diagnostic engine for question rationale |


<a id="computeRationale"></a>
# **computeRationale**
> RationaleResponse computeRationale(body)

Query diagnostic engine for question rationale

Returns rationale behind the question asked by the system.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RationaleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.infermedica.com/v2");

    RationaleApi apiInstance = new RationaleApi(defaultClient);
    RationaleRequest body = new RationaleRequest(); // RationaleRequest | 
    try {
      RationaleResponse result = apiInstance.computeRationale(body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RationaleApi#computeRationale");
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
| **body** | [**RationaleRequest**](RationaleRequest.md)|  | |

### Return type

[**RationaleResponse**](RationaleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

