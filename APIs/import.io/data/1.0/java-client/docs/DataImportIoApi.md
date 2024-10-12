# DataImportIoApi

All URIs are relative to *https://data.import.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**extractorExtractorIdCsvLatestGet**](DataImportIoApi.md#extractorExtractorIdCsvLatestGet) | **GET** /extractor/{extractorId}/csv/latest | Get the latest crawl run results as a csv |
| [**extractorExtractorIdJsonLatestGet**](DataImportIoApi.md#extractorExtractorIdJsonLatestGet) | **GET** /extractor/{extractorId}/json/latest | Get the latest crawl run results as json |


<a id="extractorExtractorIdCsvLatestGet"></a>
# **extractorExtractorIdCsvLatestGet**
> Map&lt;String, String&gt; extractorExtractorIdCsvLatestGet(extractorId)

Get the latest crawl run results as a csv

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataImportIoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://data.import.io");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataImportIoApi apiInstance = new DataImportIoApi(defaultClient);
    String extractorId = "extractorId_example"; // String | the id of the extractor to start get the latest crawl run data
    try {
      Map<String, String> result = apiInstance.extractorExtractorIdCsvLatestGet(extractorId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataImportIoApi#extractorExtractorIdCsvLatestGet");
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
| **extractorId** | **String**| the id of the extractor to start get the latest crawl run data | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | User doesn&#39;t own this extractor, or doesn&#39;t have a valid session. |  -  |
| **404** | Not found: Extractor has not been run. |  -  |

<a id="extractorExtractorIdJsonLatestGet"></a>
# **extractorExtractorIdJsonLatestGet**
> Map&lt;String, String&gt; extractorExtractorIdJsonLatestGet(extractorId)

Get the latest crawl run results as json

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataImportIoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://data.import.io");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DataImportIoApi apiInstance = new DataImportIoApi(defaultClient);
    String extractorId = "extractorId_example"; // String | The id of the extractor to start get the latest crawl run data
    try {
      Map<String, String> result = apiInstance.extractorExtractorIdJsonLatestGet(extractorId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataImportIoApi#extractorExtractorIdJsonLatestGet");
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
| **extractorId** | **String**| The id of the extractor to start get the latest crawl run data | |

### Return type

**Map&lt;String, String&gt;**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; boundary=NL

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | User doesn&#39;t own this extractor, or doesn&#39;t have a valid session. |  -  |
| **404** | Not found: Extractor has not been run. |  -  |

