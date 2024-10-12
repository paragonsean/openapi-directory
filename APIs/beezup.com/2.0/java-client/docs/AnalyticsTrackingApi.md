# AnalyticsTrackingApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getStoreTrackedClicks**](AnalyticsTrackingApi.md#getStoreTrackedClicks) | **GET** /v2/user/analytics/{storeId}/tracking/clicks | Get the latest tracked clicks |
| [**getStoreTrackedExternalOrders**](AnalyticsTrackingApi.md#getStoreTrackedExternalOrders) | **GET** /v2/user/analytics/{storeId}/tracking/externalorders | Get the latest tracked external orders |
| [**getStoreTrackedOrders**](AnalyticsTrackingApi.md#getStoreTrackedOrders) | **GET** /v2/user/analytics/{storeId}/tracking/orders | Get the latest tracked orders |
| [**getStoreTrackingStatus**](AnalyticsTrackingApi.md#getStoreTrackingStatus) | **GET** /v2/user/analytics/{storeId}/tracking/status | Get the synchronization status of clicks and orders of a store |
| [**getTrackingStatus**](AnalyticsTrackingApi.md#getTrackingStatus) | **GET** /v2/user/analytics/tracking/status | Get the global synchronization status of clicks and orders |


<a id="getStoreTrackedClicks"></a>
# **getStoreTrackedClicks**
> TrackedClicks getStoreTrackedClicks(storeId, count)

Get the latest tracked clicks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsTrackingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsTrackingApi apiInstance = new AnalyticsTrackingApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    Integer count = 56; // Integer | The amount of clicks to retrieve
    try {
      TrackedClicks result = apiInstance.getStoreTrackedClicks(storeId, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsTrackingApi#getStoreTrackedClicks");
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
| **count** | **Integer**| The amount of clicks to retrieve | [optional] |

### Return type

[**TrackedClicks**](TrackedClicks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Click list |  -  |
| **404** | Store or resource not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getStoreTrackedExternalOrders"></a>
# **getStoreTrackedExternalOrders**
> TrackedExternalOrders getStoreTrackedExternalOrders(storeId, count)

Get the latest tracked external orders

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsTrackingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsTrackingApi apiInstance = new AnalyticsTrackingApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    Integer count = 56; // Integer | The amount of external orders to retrieve
    try {
      TrackedExternalOrders result = apiInstance.getStoreTrackedExternalOrders(storeId, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsTrackingApi#getStoreTrackedExternalOrders");
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
| **count** | **Integer**| The amount of external orders to retrieve | [optional] |

### Return type

[**TrackedExternalOrders**](TrackedExternalOrders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | External Order list |  -  |
| **400** | Invalid request |  -  |
| **404** | Store or resource not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getStoreTrackedOrders"></a>
# **getStoreTrackedOrders**
> TrackedOrders getStoreTrackedOrders(storeId, count)

Get the latest tracked orders

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsTrackingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsTrackingApi apiInstance = new AnalyticsTrackingApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    Integer count = 56; // Integer | The amount of orders to retrieve
    try {
      TrackedOrders result = apiInstance.getStoreTrackedOrders(storeId, count);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsTrackingApi#getStoreTrackedOrders");
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
| **count** | **Integer**| The amount of orders to retrieve | [optional] |

### Return type

[**TrackedOrders**](TrackedOrders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Order list |  -  |
| **400** | Invalid request |  -  |
| **404** | Store or resource not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getStoreTrackingStatus"></a>
# **getStoreTrackingStatus**
> StoreTrackingStatus getStoreTrackingStatus(storeId)

Get the synchronization status of clicks and orders of a store

Clicks and orders are eventually consistent. \\ This operation gets the current state of projections for a store. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsTrackingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsTrackingApi apiInstance = new AnalyticsTrackingApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    try {
      StoreTrackingStatus result = apiInstance.getStoreTrackingStatus(storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsTrackingApi#getStoreTrackingStatus");
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

[**StoreTrackingStatus**](StoreTrackingStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Store Tracking Status |  -  |
| **404** | Store or resource not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getTrackingStatus"></a>
# **getTrackingStatus**
> TrackingStatus getTrackingStatus()

Get the global synchronization status of clicks and orders

Clicks and orders are eventually consistent. \\ This operation gets the current global state of projections. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsTrackingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsTrackingApi apiInstance = new AnalyticsTrackingApi(defaultClient);
    try {
      TrackingStatus result = apiInstance.getTrackingStatus();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsTrackingApi#getTrackingStatus");
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

[**TrackingStatus**](TrackingStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tracking status informations |  -  |
| **0** | Occurs when something goes wrong |  -  |

