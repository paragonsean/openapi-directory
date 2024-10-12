# StatisticsApi

All URIs are relative to *https://api.semantria.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getStatistic**](StatisticsApi.md#getStatistic) | **GET** /statistics.{content_type} | Retrieve usage statistics |


<a id="getStatistic"></a>
# **getStatistic**
> Statistic getStatistic(contentType, configId, interval)

Retrieve usage statistics

This method retrieves overall and per configuration usage statistics for specific timeframe. Statistics ordered per available configurations. Available interval values are current &lt;b&gt;hour&lt;/b&gt;, &lt;b&gt;day&lt;/b&gt;, &lt;b&gt;week&lt;/b&gt;, &lt;b&gt;month&lt;/b&gt; and &lt;b&gt;year&lt;/b&gt;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.semantria.com");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    String contentType = "contentType_example"; // String | 
    String configId = "configId_example"; // String | Configuration identifier for usage statistics retrieving.
    String interval = "interval_example"; // String | Hour, Day, Week, Month, Year values are supported.
    try {
      Statistic result = apiInstance.getStatistic(contentType, configId, interval);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#getStatistic");
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
| **contentType** | **String**|  | |
| **configId** | **String**| Configuration identifier for usage statistics retrieving. | [optional] |
| **interval** | **String**| Hour, Day, Week, Month, Year values are supported. | [optional] |

### Return type

[**Statistic**](Statistic.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Client request accepted. Server responds with statistics details. |  -  |
| **401** | Authentication failed. |  -  |
| **402** | Unauthorized. Limit of system calls is reached or subscription is expired. |  -  |
| **500** | Server side issue. Server may respond with the details in response body. |  -  |

