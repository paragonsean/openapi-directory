# ChartsChartDataApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**chartChartdataGetId**](ChartsChartDataApi.md#chartChartdataGetId) | **GET** /Charts/ChartData/{id} | ChartData: Get by Id |


<a id="chartChartdataGetId"></a>
# **chartChartdataGetId**
> ChartChartData chartChartdataGetId(id)

ChartData: Get by Id

Get by Id: Use this method to retrieve a ChartData object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChartsChartDataApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ChartsChartDataApi apiInstance = new ChartsChartDataApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      ChartChartData result = apiInstance.chartChartdataGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChartsChartDataApi#chartChartdataGetId");
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

[**ChartChartData**](ChartChartData.md)

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

