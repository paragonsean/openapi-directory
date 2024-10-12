# ReportsApi

All URIs are relative to *https://api.nativeads.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**publisherReportsDailyGet**](ReportsApi.md#publisherReportsDailyGet) | **GET** /publisher/reports/daily |  |
| [**publisherReportsWebsiteGet**](ReportsApi.md#publisherReportsWebsiteGet) | **GET** /publisher/reports/website |  |
| [**publisherReportsWidgetGet**](ReportsApi.md#publisherReportsWidgetGet) | **GET** /publisher/reports/widget |  |


<a id="publisherReportsDailyGet"></a>
# **publisherReportsDailyGet**
> ReportsDailyResponse publisherReportsDailyGet(token, startDate, endDate, limit, page)



Returns publisher statistics split by date

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
    defaultClient.setBasePath("https://api.nativeads.com");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String token = "token_example"; // String | Native Ads Publisher API authentication token
    LocalDate startDate = LocalDate.now(); // LocalDate | start date in format YYYY-MM-DD
    LocalDate endDate = LocalDate.now(); // LocalDate | end date in format YYYY-MM-DD
    Integer limit = 100; // Integer | maximum number of results per page
    Integer page = 1; // Integer | page number
    try {
      ReportsDailyResponse result = apiInstance.publisherReportsDailyGet(token, startDate, endDate, limit, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#publisherReportsDailyGet");
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
| **token** | **String**| Native Ads Publisher API authentication token | |
| **startDate** | **LocalDate**| start date in format YYYY-MM-DD | |
| **endDate** | **LocalDate**| end date in format YYYY-MM-DD | |
| **limit** | **Integer**| maximum number of results per page | [default to 100] |
| **page** | **Integer**| page number | [default to 1] |

### Return type

[**ReportsDailyResponse**](ReportsDailyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | report response |  -  |
| **400** | error message |  -  |

<a id="publisherReportsWebsiteGet"></a>
# **publisherReportsWebsiteGet**
> ReportsWebsiteResponse publisherReportsWebsiteGet(token, startDate, endDate, limit, page)



Returns publisher statistics split by website

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
    defaultClient.setBasePath("https://api.nativeads.com");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String token = "token_example"; // String | Native Ads Publisher API authentication token
    LocalDate startDate = LocalDate.now(); // LocalDate | start date in format YYYY-MM-DD
    LocalDate endDate = LocalDate.now(); // LocalDate | end date in format YYYY-MM-DD
    Integer limit = 100; // Integer | maximum number of results per page
    Integer page = 1; // Integer | page number
    try {
      ReportsWebsiteResponse result = apiInstance.publisherReportsWebsiteGet(token, startDate, endDate, limit, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#publisherReportsWebsiteGet");
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
| **token** | **String**| Native Ads Publisher API authentication token | |
| **startDate** | **LocalDate**| start date in format YYYY-MM-DD | |
| **endDate** | **LocalDate**| end date in format YYYY-MM-DD | |
| **limit** | **Integer**| maximum number of results per page | [default to 100] |
| **page** | **Integer**| page number | [default to 1] |

### Return type

[**ReportsWebsiteResponse**](ReportsWebsiteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | report response |  -  |
| **400** | authentication error |  -  |

<a id="publisherReportsWidgetGet"></a>
# **publisherReportsWidgetGet**
> ReportsWidgetResponse publisherReportsWidgetGet(token, startDate, endDate, limit, page)



Returns publisher statistics split by widget

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
    defaultClient.setBasePath("https://api.nativeads.com");

    ReportsApi apiInstance = new ReportsApi(defaultClient);
    String token = "token_example"; // String | Native Ads Publisher API authentication token
    LocalDate startDate = LocalDate.now(); // LocalDate | start date in format YYYY-MM-DD
    LocalDate endDate = LocalDate.now(); // LocalDate | end date in format YYYY-MM-DD
    Integer limit = 100; // Integer | maximum number of results per page
    Integer page = 1; // Integer | page number
    try {
      ReportsWidgetResponse result = apiInstance.publisherReportsWidgetGet(token, startDate, endDate, limit, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ReportsApi#publisherReportsWidgetGet");
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
| **token** | **String**| Native Ads Publisher API authentication token | |
| **startDate** | **LocalDate**| start date in format YYYY-MM-DD | |
| **endDate** | **LocalDate**| end date in format YYYY-MM-DD | |
| **limit** | **Integer**| maximum number of results per page | [default to 100] |
| **page** | **Integer**| page number | [default to 1] |

### Return type

[**ReportsWidgetResponse**](ReportsWidgetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | report response |  -  |
| **400** | authentication error |  -  |

