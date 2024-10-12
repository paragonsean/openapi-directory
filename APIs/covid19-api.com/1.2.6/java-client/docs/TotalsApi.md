# TotalsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDailyReportTotals**](TotalsApi.md#getDailyReportTotals) | **GET** /report/totals | getDailyReportTotals |
| [**getLatestTotals**](TotalsApi.md#getLatestTotals) | **GET** /totals | getLatestTotals |


<a id="getDailyReportTotals"></a>
# **getDailyReportTotals**
> List&lt;GetDailyReportTotals200ResponseInner&gt; getDailyReportTotals(date, dateFormat, format)

getDailyReportTotals

Get daily report data for whole world.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TotalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    TotalsApi apiInstance = new TotalsApi(defaultClient);
    String date = "date_example"; // String | Date of the report. If you don't put this field all dates will be returned.
    String dateFormat = "YYYY-MM-DD"; // String | Date format. If you dont want to use ISO 8601 standard (YYYY-MM-DD), you can provide different format.
    String format = "json"; // String | Format of the response. If you don't put this field JSON will be response format.
    try {
      List<GetDailyReportTotals200ResponseInner> result = apiInstance.getDailyReportTotals(date, dateFormat, format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TotalsApi#getDailyReportTotals");
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
| **date** | **String**| Date of the report. If you don&#39;t put this field all dates will be returned. | [optional] |
| **dateFormat** | **String**| Date format. If you dont want to use ISO 8601 standard (YYYY-MM-DD), you can provide different format. | [optional] [default to YYYY-MM-DD] [enum: YYYY-MM-DD, YYYY-DD-MM, DD-MM-YYYY, MM-DD-YYYY] |
| **format** | **String**| Format of the response. If you don&#39;t put this field JSON will be response format. | [optional] [default to json] [enum: json, xml] |

### Return type

[**List&lt;GetDailyReportTotals200ResponseInner&gt;**](GetDailyReportTotals200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Data about COVID-19 for whole world |  -  |

<a id="getLatestTotals"></a>
# **getLatestTotals**
> List&lt;GetLatestTotals200ResponseInner&gt; getLatestTotals(format)

getLatestTotals

Get latest data for whole world.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TotalsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    TotalsApi apiInstance = new TotalsApi(defaultClient);
    String format = "json"; // String | Format of the response
    try {
      List<GetLatestTotals200ResponseInner> result = apiInstance.getLatestTotals(format);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TotalsApi#getLatestTotals");
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
| **format** | **String**| Format of the response | [optional] [default to json] [enum: json, xml] |

### Return type

[**List&lt;GetLatestTotals200ResponseInner&gt;**](GetLatestTotals200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Latest data about COVID-19 for whole world |  -  |

