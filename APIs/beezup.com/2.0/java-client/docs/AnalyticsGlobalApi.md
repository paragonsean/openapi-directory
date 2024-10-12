# AnalyticsGlobalApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**analyticsIndex**](AnalyticsGlobalApi.md#analyticsIndex) | **GET** /v2/user/analytics/ | Get the Analytics API operation index |
| [**analyticsStoreIndex**](AnalyticsGlobalApi.md#analyticsStoreIndex) | **GET** /v2/user/analytics/{storeId} | Get the Analytics API operation index for one store |


<a id="analyticsIndex"></a>
# **analyticsIndex**
> AnalyticsIndex analyticsIndex()

Get the Analytics API operation index

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsGlobalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsGlobalApi apiInstance = new AnalyticsGlobalApi(defaultClient);
    try {
      AnalyticsIndex result = apiInstance.analyticsIndex();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsGlobalApi#analyticsIndex");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AnalyticsIndex**](AnalyticsIndex.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Analytics API operation index |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="analyticsStoreIndex"></a>
# **analyticsStoreIndex**
> AnalyticsStoreIndex analyticsStoreIndex(storeId)

Get the Analytics API operation index for one store

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsGlobalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsGlobalApi apiInstance = new AnalyticsGlobalApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    try {
      AnalyticsStoreIndex result = apiInstance.analyticsStoreIndex(storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsGlobalApi#analyticsStoreIndex");
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

[**AnalyticsStoreIndex**](AnalyticsStoreIndex.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Analytics API operation index for one store |  -  |
| **404** | Store or resource not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

