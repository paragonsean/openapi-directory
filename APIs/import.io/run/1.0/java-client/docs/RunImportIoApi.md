# RunImportIoApi

All URIs are relative to *https://run.import.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**extractorExtractorIdCancelPost**](RunImportIoApi.md#extractorExtractorIdCancelPost) | **POST** /extractor/{extractorId}/cancel | Cancel an existing crawl. |
| [**extractorExtractorIdStartPost**](RunImportIoApi.md#extractorExtractorIdStartPost) | **POST** /extractor/{extractorId}/start | Launch a crawl from an extractor that a user owns. |


<a id="extractorExtractorIdCancelPost"></a>
# **extractorExtractorIdCancelPost**
> Map&lt;String, String&gt; extractorExtractorIdCancelPost(extractorId)

Cancel an existing crawl.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RunImportIoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://run.import.io");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RunImportIoApi apiInstance = new RunImportIoApi(defaultClient);
    String extractorId = "extractorId_example"; // String | extractorId
    try {
      Map<String, String> result = apiInstance.extractorExtractorIdCancelPost(extractorId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RunImportIoApi#extractorExtractorIdCancelPost");
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
| **extractorId** | **String**| extractorId | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | No in progress crawl found to cancel. |  -  |
| **401** | User doesn&#39;t own this extractor, or doesn&#39;t have a valid session. |  -  |
| **404** | Unable to find supplied extractor ID. |  -  |

<a id="extractorExtractorIdStartPost"></a>
# **extractorExtractorIdStartPost**
> Map&lt;String, String&gt; extractorExtractorIdStartPost(extractorId)

Launch a crawl from an extractor that a user owns.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RunImportIoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://run.import.io");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RunImportIoApi apiInstance = new RunImportIoApi(defaultClient);
    String extractorId = "extractorId_example"; // String | the id of the extractor to start crawling with
    try {
      Map<String, String> result = apiInstance.extractorExtractorIdStartPost(extractorId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RunImportIoApi#extractorExtractorIdStartPost");
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
| **extractorId** | **String**| the id of the extractor to start crawling with | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Extractor is archived or a crawl already in progress. |  -  |
| **401** | User doesn&#39;t own this extractor, or doesn&#39;t have a valid session. |  -  |
| **404** | Unable to find supplied extractor ID. |  -  |

