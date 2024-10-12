# ReportsApi

All URIs are relative to *https://webtris.highwaysengland.co.uk/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reportsIndex**](ReportsApi.md#reportsIndex) | **GET** /v{version}/reports/{report_type} | Gets the daily report. |
| [**vversionReportsStartDateToEndDateReportTypeGet**](ReportsApi.md#vversionReportsStartDateToEndDateReportTypeGet) | **GET** /v{version}/reports/{start_date}/to/{end_date}/{report_type} | Gets the daily report. |


<a id="reportsIndex"></a>
# **reportsIndex**
> Object reportsIndex(reportType, sites, startDate, endDate, page, pageSize, version, reportSubTypeId)

Gets the daily report.

Get&#39;s the report.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webtris.highwaysengland.co.uk/api");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String reportType = "reportType_example"; // String | Report Type Id (i.e Daily, Monthly, Annual)
    String sites = "sites_example"; // String | Comma separated list of site Ids.
    String startDate = "startDate_example"; // String | The start date of the report in the format ddmmyyyy (i.e 31012016)
    String endDate = "endDate_example"; // String | The end date of the report in the format ddmmyyyy (i.e 31012016)
    Integer page = 56; // Integer | The page offset to return.
    Integer pageSize = 56; // Integer | The number of rows to return.
    String version = "version_example"; // String | 
    Integer reportSubTypeId = 56; // Integer | 
    try {
      Object result = apiInstance.reportsIndex(reportType, sites, startDate, endDate, page, pageSize, version, reportSubTypeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsIndex");
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
| **reportType** | **String**| Report Type Id (i.e Daily, Monthly, Annual) | |
| **sites** | **String**| Comma separated list of site Ids. | |
| **startDate** | **String**| The start date of the report in the format ddmmyyyy (i.e 31012016) | |
| **endDate** | **String**| The end date of the report in the format ddmmyyyy (i.e 31012016) | |
| **page** | **Integer**| The page offset to return. | |
| **pageSize** | **Integer**| The number of rows to return. | |
| **version** | **String**|  | |
| **reportSubTypeId** | **Integer**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Bad request |  -  |
| **500** | Internal Server Error |  -  |

<a id="vversionReportsStartDateToEndDateReportTypeGet"></a>
# **vversionReportsStartDateToEndDateReportTypeGet**
> Object vversionReportsStartDateToEndDateReportTypeGet(reportType, sites, startDate, endDate, page, pageSize, version, reportSubTypeId)

Gets the daily report.

Get&#39;s the report.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://webtris.highwaysengland.co.uk/api");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String reportType = "reportType_example"; // String | Report Type Id (i.e Daily, Monthly, Annual)
    String sites = "sites_example"; // String | Comma separated list of site Ids.
    String startDate = "startDate_example"; // String | The start date of the report in the format ddmmyyyy (i.e 31012016)
    String endDate = "endDate_example"; // String | The end date of the report in the format ddmmyyyy (i.e 31012016)
    Integer page = 56; // Integer | The page offset to return.
    Integer pageSize = 56; // Integer | The number of rows to return.
    String version = "version_example"; // String | 
    Integer reportSubTypeId = 56; // Integer | 
    try {
      Object result = apiInstance.vversionReportsStartDateToEndDateReportTypeGet(reportType, sites, startDate, endDate, page, pageSize, version, reportSubTypeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#vversionReportsStartDateToEndDateReportTypeGet");
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
| **reportType** | **String**| Report Type Id (i.e Daily, Monthly, Annual) | |
| **sites** | **String**| Comma separated list of site Ids. | |
| **startDate** | **String**| The start date of the report in the format ddmmyyyy (i.e 31012016) | |
| **endDate** | **String**| The end date of the report in the format ddmmyyyy (i.e 31012016) | |
| **page** | **Integer**| The page offset to return. | |
| **pageSize** | **Integer**| The number of rows to return. | |
| **version** | **String**|  | |
| **reportSubTypeId** | **Integer**|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Bad request |  -  |
| **500** | Internal Server Error |  -  |

