# ChartsAxesApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**chartAxesGetId**](ChartsAxesApi.md#chartAxesGetId) | **GET** /Charts/Axes/{id} | Axes: Get by Id |


<a id="chartAxesGetId"></a>
# **chartAxesGetId**
> ChartAxes chartAxesGetId(id)

Axes: Get by Id

Get by Id: Use this method to retrieve a Axes object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsAxesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsAxesApi apiInstance = new ChartsAxesApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      ChartAxes result = apiInstance.chartAxesGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsAxesApi#chartAxesGetId");
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
| **id** | **UUID**|  | |

### Return type

[**ChartAxes**](ChartAxes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

