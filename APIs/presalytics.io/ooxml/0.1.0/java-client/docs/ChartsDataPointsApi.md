# ChartsDataPointsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**chartDatapointsGetId**](ChartsDataPointsApi.md#chartDatapointsGetId) | **GET** /Charts/DataPoints/{id} | DataPoints: Get by Id |


<a id="chartDatapointsGetId"></a>
# **chartDatapointsGetId**
> ChartDataPoints chartDatapointsGetId(id)

DataPoints: Get by Id

Get by Id: Use this method to retrieve a DataPoints object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsDataPointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsDataPointsApi apiInstance = new ChartsDataPointsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      ChartDataPoints result = apiInstance.chartDatapointsGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsDataPointsApi#chartDatapointsGetId");
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

[**ChartDataPoints**](ChartDataPoints.md)

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

