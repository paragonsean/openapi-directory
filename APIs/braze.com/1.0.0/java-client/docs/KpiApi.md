# KpiApi

All URIs are relative to *https://rest.iad-01.braze.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dailyActiveUsersByDate_0**](KpiApi.md#dailyActiveUsersByDate_0) | **GET** /kpi/dau/data_series | Daily Active Users by Date |
| [**dailyNewUsersByDate_0**](KpiApi.md#dailyNewUsersByDate_0) | **GET** /kpi/new_users/data_series | Daily New Users by Date |
| [**kpIsForDailyAppUninstallsByDate_0**](KpiApi.md#kpIsForDailyAppUninstallsByDate_0) | **GET** /kpi/uninstalls/data_series | KPIs for Daily App Uninstalls by Date |
| [**monthlyActiveUsersForLast30Days_0**](KpiApi.md#monthlyActiveUsersForLast30Days_0) | **GET** /kpi/mau/data_series | Monthly Active Users for Last 30 Days |


<a id="dailyActiveUsersByDate_0"></a>
# **dailyActiveUsersByDate_0**
> dailyActiveUsersByDate_0(length, endingAt, appId)

Daily Active Users by Date

This endpoint allows you to retrieve a daily series of the total number of unique active users on each date.   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) date as ISO 8601 date,             \&quot;dau\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KpiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.iad-01.braze.com");

    KpiApi apiInstance = new KpiApi(defaultClient);
    String length = "10"; // String | (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive
    String endingAt = "2018-06-28T23:59:59-5:00"; // String | (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request
    String appId = "{{app_identifier}}"; // String | (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned
    try {
      apiInstance.dailyActiveUsersByDate_0(length, endingAt, appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling KpiApi#dailyActiveUsersByDate_0");
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
| **length** | **String**| (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive | [optional] |
| **endingAt** | **String**| (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request | [optional] |
| **appId** | **String**| (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="dailyNewUsersByDate_0"></a>
# **dailyNewUsersByDate_0**
> dailyNewUsersByDate_0(length, endingAt, appId)

Daily New Users by Date

This endpoint allows you to retrieve a daily series of the total number of new users on each date.   ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) date as ISO 8601 date,             \&quot;new_users\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KpiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.iad-01.braze.com");

    KpiApi apiInstance = new KpiApi(defaultClient);
    String length = "14"; // String | (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive
    String endingAt = "2018-06-28T23:59:59-5:00"; // String | (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request
    String appId = "{{app_identifier}}"; // String | (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned
    try {
      apiInstance.dailyNewUsersByDate_0(length, endingAt, appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling KpiApi#dailyNewUsersByDate_0");
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
| **length** | **String**| (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive | [optional] |
| **endingAt** | **String**| (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request | [optional] |
| **appId** | **String**| (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="kpIsForDailyAppUninstallsByDate_0"></a>
# **kpIsForDailyAppUninstallsByDate_0**
> kpIsForDailyAppUninstallsByDate_0(length, endingAt, appId)

KPIs for Daily App Uninstalls by Date

This endpoint allows you to retrieve a daily series of the total number of uninstalls on each date.  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) date as ISO 8601 date,             \&quot;uninstalls\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KpiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.iad-01.braze.com");

    KpiApi apiInstance = new KpiApi(defaultClient);
    String length = "14"; // String | (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive
    String endingAt = "2018-06-28T23:59:59-5:00"; // String | (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request
    String appId = "{{app_identifier}}"; // String | (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned
    try {
      apiInstance.kpIsForDailyAppUninstallsByDate_0(length, endingAt, appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling KpiApi#kpIsForDailyAppUninstallsByDate_0");
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
| **length** | **String**| (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive | [optional] |
| **endingAt** | **String**| (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request | [optional] |
| **appId** | **String**| (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="monthlyActiveUsersForLast30Days_0"></a>
# **monthlyActiveUsersForLast30Days_0**
> monthlyActiveUsersForLast30Days_0(length, endingAt, appId)

Monthly Active Users for Last 30 Days

This endpoint allows you to retrieve a daily series of the total number of unique active users over a 30-day rolling window.  ## Response  &#x60;&#x60;&#x60;json Content-Type: application/json Authorization: Bearer YOUR-REST-API-KEY {     \&quot;message\&quot;: (required, string) the status of the export, returns &#39;success&#39; when completed without errors,     \&quot;data\&quot; : [         {             \&quot;time\&quot; : (string) date as ISO 8601 date,             \&quot;mau\&quot; : (int)         },         ...     ] } &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.KpiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rest.iad-01.braze.com");

    KpiApi apiInstance = new KpiApi(defaultClient);
    String length = "7"; // String | (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive
    String endingAt = "2018-06-28T23:59:59-05:00"; // String | (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request
    String appId = "{{app_identifier}}"; // String | (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned
    try {
      apiInstance.monthlyActiveUsersForLast30Days_0(length, endingAt, appId);
    } catch (ApiException e) {
      System.err.println("Exception when calling KpiApi#monthlyActiveUsersForLast30Days_0");
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
| **length** | **String**| (Required) Integer  Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive | [optional] |
| **endingAt** | **String**| (Optional) DateTime (ISO 8601 string)  Point in time when the data series should end - defaults to time of the request | [optional] |
| **appId** | **String**| (Optional) String  App API identifier; if excluded, results for all apps in app group will be returned | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

