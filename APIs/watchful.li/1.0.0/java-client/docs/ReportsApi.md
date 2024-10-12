# ReportsApi

All URIs are relative to *https://watchful.li/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**reportsSitesIdGet**](ReportsApi.md#reportsSitesIdGet) | **GET** /reports/sites/{id} | Returns a PDF report for a specific site |
| [**reportsTagsIdGet**](ReportsApi.md#reportsTagsIdGet) | **GET** /reports/tags/{id} | Find sites by ID |


<a id="reportsSitesIdGet"></a>
# **reportsSitesIdGet**
> Object reportsSitesIdGet(id, from, to, reports, logType, compare)

Returns a PDF report for a specific site

Returns a PDF report based on a site ID

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
    defaultClient.setBasePath("https://watchful.li/api/v1");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    Long id = 56L; // Long | ID that needs to be fetched
    String from = "from_example"; // String | Start of the report, format YYYY-MM-DD, default today-30day 
    String to = "to_example"; // String | End of the report, format YYYY-MM-DD, default today
    String reports = "reports_example"; // String | Type of reports separate by comas: Ga,Logs,Uptime
    String logType = ""; // String | Type of the log to show in the report
    Integer compare = 0; // Integer | Define if you want show previous values in Google Analytics graph
    try {
      Object result = apiInstance.reportsSitesIdGet(id, from, to, reports, logType, compare);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsSitesIdGet");
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
| **id** | **Long**| ID that needs to be fetched | |
| **from** | **String**| Start of the report, format YYYY-MM-DD, default today-30day  | [optional] |
| **to** | **String**| End of the report, format YYYY-MM-DD, default today | [optional] |
| **reports** | **String**| Type of reports separate by comas: Ga,Logs,Uptime | [optional] |
| **logType** | **String**| Type of the log to show in the report | [optional] [enum: , plugin_sends_error, curlerror, modified_file, word_not_in_homepage, file_not_exists, update_available, new_extension, deleted_extension, extension_not_saved, modified_value_files] |
| **compare** | **Integer**| Define if you want show previous values in Google Analytics graph | [optional] [enum: 0, 1] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

<a id="reportsTagsIdGet"></a>
# **reportsTagsIdGet**
> Object reportsTagsIdGet(id, from, to, reports, logType, compare)

Find sites by ID

Returns a report based on a site ID

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
    defaultClient.setBasePath("https://watchful.li/api/v1");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    Long id = 56L; // Long | ID that needs to be fetched
    String from = "from_example"; // String | Start of the report, format YYYY-MM-DD, default today-30day 
    String to = "to_example"; // String | End of the report, format YYYY-MM-DD, default today
    String reports = "reports_example"; // String | Type of reports separate by comas: Ga,Logs,Uptime
    String logType = ""; // String | Type of the log to show in the report
    Integer compare = 0; // Integer | Define if you want show previous values in Google Analytics graph
    try {
      Object result = apiInstance.reportsTagsIdGet(id, from, to, reports, logType, compare);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#reportsTagsIdGet");
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
| **id** | **Long**| ID that needs to be fetched | |
| **from** | **String**| Start of the report, format YYYY-MM-DD, default today-30day  | [optional] |
| **to** | **String**| End of the report, format YYYY-MM-DD, default today | [optional] |
| **reports** | **String**| Type of reports separate by comas: Ga,Logs,Uptime | [optional] |
| **logType** | **String**| Type of the log to show in the report | [optional] [enum: , plugin_sends_error, curlerror, modified_file, word_not_in_homepage, file_not_exists, update_available, new_extension, deleted_extension, extension_not_saved, modified_value_files] |
| **compare** | **Integer**| Define if you want show previous values in Google Analytics graph | [optional] [enum: 0, 1] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/pdf

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |
| **403** | Invalid API Key |  -  |
| **404** | Invalid ID |  -  |

