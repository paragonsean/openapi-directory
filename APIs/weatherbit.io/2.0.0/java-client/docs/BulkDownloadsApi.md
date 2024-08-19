# BulkDownloadsApi

All URIs are relative to *https://api.weatherbit.io/v2.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkFilesFileGet**](BulkDownloadsApi.md#bulkFilesFileGet) | **GET** /bulk/files/{file} | Download pre-generated bulk datasets |


<a id="bulkFilesFileGet"></a>
# **bulkFilesFileGet**
> Error bulkFilesFileGet(_file, key)

Download pre-generated bulk datasets

Downloads bulk data files - OPTIONS: ( current.csv.gz, forecast_hourly.csv.gz, forecast_daily.csv.gz). Units are Metric (Celcius, m/s, etc).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BulkDownloadsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.weatherbit.io/v2.0");

    BulkDownloadsApi apiInstance = new BulkDownloadsApi(defaultClient);
    String _file = "_file_example"; // String | Filename (ie. current.csv.gz)
    String key = "key_example"; // String | Your registered API key.
    try {
      Error result = apiInstance.bulkFilesFileGet(_file, key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BulkDownloadsApi#bulkFilesFileGet");
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
| **_file** | **String**| Filename (ie. current.csv.gz) | |
| **key** | **String**| Your registered API key. | |

### Return type

[**Error**](Error.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | No Data. |  -  |

