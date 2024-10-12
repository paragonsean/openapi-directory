# ExtractionImportIoApi

All URIs are relative to *https://extraction.import.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**extractorExtractorIdGet**](ExtractionImportIoApi.md#extractorExtractorIdGet) | **GET** /extractor/{extractorId} | Query by extractor endpoint, adhoc runs only. |


<a id="extractorExtractorIdGet"></a>
# **extractorExtractorIdGet**
> QueryResponse extractorExtractorIdGet(extractorId, url)

Query by extractor endpoint, adhoc runs only.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExtractionImportIoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://extraction.import.io");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    ExtractionImportIoApi apiInstance = new ExtractionImportIoApi(defaultClient);
    String extractorId = "extractorId_example"; // String | extractorId
    String url = "url_example"; // String | url
    try {
      QueryResponse result = apiInstance.extractorExtractorIdGet(extractorId, url);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExtractionImportIoApi#extractorExtractorIdGet");
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
| **url** | **String**| url | |

### Return type

[**QueryResponse**](QueryResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Invalid ID supplied |  -  |
| **401** | Unauthorized |  -  |

