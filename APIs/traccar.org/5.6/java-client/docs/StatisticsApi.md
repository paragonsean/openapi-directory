# StatisticsApi

All URIs are relative to *https://demo.traccar.org/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**statisticsGet**](StatisticsApi.md#statisticsGet) | **GET** /statistics | Fetch server Statistics |


<a id="statisticsGet"></a>
# **statisticsGet**
> List&lt;Statistics&gt; statisticsGet(from, to)

Fetch server Statistics

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.traccar.org/api");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    StatisticsApi apiInstance = new StatisticsApi(defaultClient);
    OffsetDateTime from = OffsetDateTime.now(); // OffsetDateTime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    OffsetDateTime to = OffsetDateTime.now(); // OffsetDateTime | in IS0 8601 format. eg. `1963-11-22T18:30:00Z`
    try {
      List<Statistics> result = apiInstance.statisticsGet(from, to);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatisticsApi#statisticsGet");
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
| **from** | **OffsetDateTime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | |
| **to** | **OffsetDateTime**| in IS0 8601 format. eg. &#x60;1963-11-22T18:30:00Z&#x60; | |

### Return type

[**List&lt;Statistics&gt;**](Statistics.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

