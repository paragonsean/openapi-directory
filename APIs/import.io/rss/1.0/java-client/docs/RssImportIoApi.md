# RssImportIoApi

All URIs are relative to *https://rss.import.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**extractorExtractorIdRunsGet**](RssImportIoApi.md#extractorExtractorIdRunsGet) | **GET** /extractor/{extractorId}/runs | Get a feed of the runs performed on an extractor |


<a id="extractorExtractorIdRunsGet"></a>
# **extractorExtractorIdRunsGet**
> Map&lt;String, String&gt; extractorExtractorIdRunsGet(extractorId)

Get a feed of the runs performed on an extractor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RssImportIoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rss.import.io");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    RssImportIoApi apiInstance = new RssImportIoApi(defaultClient);
    String extractorId = "extractorId_example"; // String | The id of the extractor to start get the crawl run data
    try {
      Map<String, String> result = apiInstance.extractorExtractorIdRunsGet(extractorId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RssImportIoApi#extractorExtractorIdRunsGet");
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
| **extractorId** | **String**| The id of the extractor to start get the crawl run data | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | User doesn&#39;t own this extractor, or doesn&#39;t have a valid session. |  -  |
| **404** | Not found: Extractor has not been run. |  -  |

