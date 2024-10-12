# AnalyticsReportsApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteReportFilter**](AnalyticsReportsApi.md#deleteReportFilter) | **DELETE** /v2/user/analytics/{storeId}/reports/filters/{reportFilterId} | Delete the report filter |
| [**getReportFilter**](AnalyticsReportsApi.md#getReportFilter) | **GET** /v2/user/analytics/{storeId}/reports/filters/{reportFilterId} | Get the report filter description |
| [**getReportFilters**](AnalyticsReportsApi.md#getReportFilters) | **GET** /v2/user/analytics/{storeId}/reports/filters | Get report filter list for the given store |
| [**saveReportFilter**](AnalyticsReportsApi.md#saveReportFilter) | **PUT** /v2/user/analytics/{storeId}/reports/filters/{reportFilterId} | Save the report filter |


<a id="deleteReportFilter"></a>
# **deleteReportFilter**
> deleteReportFilter(storeId, reportFilterId)

Delete the report filter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsReportsApi apiInstance = new AnalyticsReportsApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String reportFilterId = "reportFilterId_example"; // String | Your report filter identifier
    try {
      apiInstance.deleteReportFilter(storeId, reportFilterId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsReportsApi#deleteReportFilter");
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
| **storeId** | **String**| Your store identifier | |
| **reportFilterId** | **String**| Your report filter identifier | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Report filter deleted |  -  |
| **401** | This report filter is used by rule. In the error message you will find the rule identifier. |  -  |
| **404** | Report filter not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getReportFilter"></a>
# **getReportFilter**
> ReportFilter getReportFilter(storeId, reportFilterId)

Get the report filter description

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsReportsApi apiInstance = new AnalyticsReportsApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String reportFilterId = "reportFilterId_example"; // String | Your report filter identifier
    try {
      ReportFilter result = apiInstance.getReportFilter(storeId, reportFilterId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsReportsApi#getReportFilter");
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
| **storeId** | **String**| Your store identifier | |
| **reportFilterId** | **String**| Your report filter identifier | |

### Return type

[**ReportFilter**](ReportFilter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Report filter |  -  |
| **404** | Report filter not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getReportFilters"></a>
# **getReportFilters**
> ReportFilterList getReportFilters(storeId)

Get report filter list for the given store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsReportsApi apiInstance = new AnalyticsReportsApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    try {
      ReportFilterList result = apiInstance.getReportFilters(storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsReportsApi#getReportFilters");
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
| **storeId** | **String**| Your store identifier | |

### Return type

[**ReportFilterList**](ReportFilterList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Report filter list |  -  |
| **404** | Store or resource not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="saveReportFilter"></a>
# **saveReportFilter**
> saveReportFilter(storeId, reportFilterId, saveReportFilterRequest)

Save the report filter

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsReportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsReportsApi apiInstance = new AnalyticsReportsApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String reportFilterId = "reportFilterId_example"; // String | Your report filter identifier
    SaveReportFilterRequest saveReportFilterRequest = new SaveReportFilterRequest(); // SaveReportFilterRequest | 
    try {
      apiInstance.saveReportFilter(storeId, reportFilterId, saveReportFilterRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsReportsApi#saveReportFilter");
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
| **storeId** | **String**| Your store identifier | |
| **reportFilterId** | **String**| Your report filter identifier | |
| **saveReportFilterRequest** | [**SaveReportFilterRequest**](SaveReportFilterRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Report filter saved |  -  |
| **400** | Invalid request |  -  |
| **401** | This report filter is used by rule. In the error message you will find the rule identifier. |  -  |
| **403** | This report filter identifier is already used by another store, please check your identifiers. |  -  |
| **404** | Store or resource not found |  -  |
| **409** | Report filter name already exists |  -  |
| **0** | Occurs when something goes wrong |  -  |

