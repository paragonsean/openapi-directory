# AnalyticsStatisticsApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getStoreReportByCategory**](AnalyticsStatisticsApi.md#getStoreReportByCategory) | **POST** /v2/user/analytics/{storeId}/reports/bycategory | Get the report by category |
| [**getStoreReportByChannel**](AnalyticsStatisticsApi.md#getStoreReportByChannel) | **POST** /v2/user/analytics/{storeId}/reports/bychannel | Get the report by channel |
| [**getStoreReportByDay**](AnalyticsStatisticsApi.md#getStoreReportByDay) | **POST** /v2/user/analytics/{storeId}/reports/byday | Get the report by day for a StoreId |
| [**getStoreReportByDayPerStore**](AnalyticsStatisticsApi.md#getStoreReportByDayPerStore) | **POST** /v2/user/analytics/reports/byday | Get the report by day for a StoreId |
| [**getStoreReportByProduct**](AnalyticsStatisticsApi.md#getStoreReportByProduct) | **POST** /v2/user/analytics/{storeId}/reports/byproduct | Get the report by product |


<a id="getStoreReportByCategory"></a>
# **getStoreReportByCategory**
> ReportByCategoryResponse getStoreReportByCategory(storeId, reportByCategoryRequest)

Get the report by category

Get the report by category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsStatisticsApi apiInstance = new AnalyticsStatisticsApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    ReportByCategoryRequest reportByCategoryRequest = new ReportByCategoryRequest(); // ReportByCategoryRequest | 
    try {
      ReportByCategoryResponse result = apiInstance.getStoreReportByCategory(storeId, reportByCategoryRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsStatisticsApi#getStoreReportByCategory");
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
| **reportByCategoryRequest** | [**ReportByCategoryRequest**](ReportByCategoryRequest.md)|  | |

### Return type

[**ReportByCategoryResponse**](ReportByCategoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Your reporting by channel |  -  |
| **400** | Invalid request |  -  |
| **404** | Store or resource not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getStoreReportByChannel"></a>
# **getStoreReportByChannel**
> ReportByChannelResponse getStoreReportByChannel(storeId, reportByChannelRequest)

Get the report by channel

Get the report by channel

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsStatisticsApi apiInstance = new AnalyticsStatisticsApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    ReportByChannelRequest reportByChannelRequest = new ReportByChannelRequest(); // ReportByChannelRequest | 
    try {
      ReportByChannelResponse result = apiInstance.getStoreReportByChannel(storeId, reportByChannelRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsStatisticsApi#getStoreReportByChannel");
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
| **reportByChannelRequest** | [**ReportByChannelRequest**](ReportByChannelRequest.md)|  | |

### Return type

[**ReportByChannelResponse**](ReportByChannelResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Your reporting by channel |  -  |
| **400** | Invalid request |  -  |
| **404** | Store or resource not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getStoreReportByDay"></a>
# **getStoreReportByDay**
> ReportByDayResponse getStoreReportByDay(storeId, reportByDayRequest)

Get the report by day for a StoreId

Get the report by day for a StoreId

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsStatisticsApi apiInstance = new AnalyticsStatisticsApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    ReportByDayRequest reportByDayRequest = new ReportByDayRequest(); // ReportByDayRequest | 
    try {
      ReportByDayResponse result = apiInstance.getStoreReportByDay(storeId, reportByDayRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsStatisticsApi#getStoreReportByDay");
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
| **reportByDayRequest** | [**ReportByDayRequest**](ReportByDayRequest.md)|  | |

### Return type

[**ReportByDayResponse**](ReportByDayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Your reporting by day |  -  |
| **400** | Invalid request |  -  |
| **404** | Store or resource not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getStoreReportByDayPerStore"></a>
# **getStoreReportByDayPerStore**
> Map&lt;String, ReportByDayResponse&gt; getStoreReportByDayPerStore(reportByDayRequest)

Get the report by day for a StoreId

Get the report by day for a StoreId

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsStatisticsApi apiInstance = new AnalyticsStatisticsApi(defaultClient);
    ReportByDayRequest reportByDayRequest = new ReportByDayRequest(); // ReportByDayRequest | 
    try {
      Map<String, ReportByDayResponse> result = apiInstance.getStoreReportByDayPerStore(reportByDayRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsStatisticsApi#getStoreReportByDayPerStore");
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
| **reportByDayRequest** | [**ReportByDayRequest**](ReportByDayRequest.md)|  | |

### Return type

[**Map&lt;String, ReportByDayResponse&gt;**](ReportByDayResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Your reporting by day |  -  |
| **400** | Invalid request |  -  |
| **404** | Store or resource not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getStoreReportByProduct"></a>
# **getStoreReportByProduct**
> ReportByProductResponse getStoreReportByProduct(storeId, reportByProductRequest)

Get the report by product

Get the report by product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsStatisticsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsStatisticsApi apiInstance = new AnalyticsStatisticsApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    ReportByProductRequest reportByProductRequest = new ReportByProductRequest(); // ReportByProductRequest | 
    try {
      ReportByProductResponse result = apiInstance.getStoreReportByProduct(storeId, reportByProductRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsStatisticsApi#getStoreReportByProduct");
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
| **reportByProductRequest** | [**ReportByProductRequest**](ReportByProductRequest.md)|  | |

### Return type

[**ReportByProductResponse**](ReportByProductResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Your reporting by product |  -  |
| **400** | Invalid request |  -  |
| **404** | Store or resource not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

