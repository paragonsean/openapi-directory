# BroadcastsApi

All URIs are relative to *https://rms.api.bbc.co.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**broadcastsGet**](BroadcastsApi.md#broadcastsGet) | **GET** /broadcasts | Broadcasts |
| [**broadcastsLatestGet**](BroadcastsApi.md#broadcastsLatestGet) | **GET** /broadcasts/latest | Latest Broadcasts |
| [**getBroadcastByPid**](BroadcastsApi.md#getBroadcastByPid) | **GET** /broadcasts/{pid} | Broadcasts by PID |


<a id="broadcastsGet"></a>
# **broadcastsGet**
> BroadcastsResponse broadcastsGet(xAPIKey, offset, limit, serviceId, date, sort)

Broadcasts

All broadcasts 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BroadcastsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    BroadcastsApi apiInstance = new BroadcastsApi(defaultClient);
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    String serviceId = "serviceId_example"; // String | Filter by Service ID. E.g. bbc_radio_fourfm
    String date = "date_example"; // String | Filter by date. E.g. 2016-06-17
    String sort = "start_at"; // String | Sort by provided query. E.g. 'start_at' sorts in ascending order, and '-start_at' sorts in descending order
    try {
      BroadcastsResponse result = apiInstance.broadcastsGet(xAPIKey, offset, limit, serviceId, date, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BroadcastsApi#broadcastsGet");
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
| **xAPIKey** | **String**| API_KEY | |
| **offset** | **Integer**| Paginated results offset | [optional] |
| **limit** | **Integer**| Paginated results limit | [optional] |
| **serviceId** | **String**| Filter by Service ID. E.g. bbc_radio_fourfm | [optional] |
| **date** | **String**| Filter by date. E.g. 2016-06-17 | [optional] |
| **sort** | **String**| Sort by provided query. E.g. &#39;start_at&#39; sorts in ascending order, and &#39;-start_at&#39; sorts in descending order | [optional] [enum: start_at, -start_at, end_at, -end_at] |

### Return type

[**BroadcastsResponse**](BroadcastsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | There was an error with the supplied &#x60;Authorization&#x60; header. |  -  |
| **0** | Unexpected error |  -  |

<a id="broadcastsLatestGet"></a>
# **broadcastsLatestGet**
> BroadcastsResponse broadcastsLatestGet(xAPIKey, offset, limit, serviceId, onAir, next, previous, sort)

Latest Broadcasts

Broadcasts for the current day 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BroadcastsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    BroadcastsApi apiInstance = new BroadcastsApi(defaultClient);
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    Integer offset = 56; // Integer | Paginated results offset
    Integer limit = 56; // Integer | Paginated results limit
    String serviceId = "serviceId_example"; // String | Filter by Service ID. E.g. bbc_radio_fourfm
    String onAir = "now"; // String | Filter what is on air. E.g. 'now' returns current programme being broadcasted.
    String next = "next_example"; // String | Filter what will be on air next in minutes. E.g. '240' returns programmes broadcasted in the next four hurs
    String previous = "previous_example"; // String | Filter what was on air previously in minutes. E.g. '240' returns programmes broadcasted in the previous four hurs
    String sort = "start_at"; // String | Sort by provided query. E.g. 'start_at' sorts in ascending order, and '-start_at' sorts in descending order
    try {
      BroadcastsResponse result = apiInstance.broadcastsLatestGet(xAPIKey, offset, limit, serviceId, onAir, next, previous, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BroadcastsApi#broadcastsLatestGet");
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
| **xAPIKey** | **String**| API_KEY | |
| **offset** | **Integer**| Paginated results offset | [optional] |
| **limit** | **Integer**| Paginated results limit | [optional] |
| **serviceId** | **String**| Filter by Service ID. E.g. bbc_radio_fourfm | [optional] |
| **onAir** | **String**| Filter what is on air. E.g. &#39;now&#39; returns current programme being broadcasted. | [optional] [enum: now, previous, next] |
| **next** | **String**| Filter what will be on air next in minutes. E.g. &#39;240&#39; returns programmes broadcasted in the next four hurs | [optional] |
| **previous** | **String**| Filter what was on air previously in minutes. E.g. &#39;240&#39; returns programmes broadcasted in the previous four hurs | [optional] |
| **sort** | **String**| Sort by provided query. E.g. &#39;start_at&#39; sorts in ascending order, and &#39;-start_at&#39; sorts in descending order | [optional] [enum: start_at, -start_at, end_at, -end_at] |

### Return type

[**BroadcastsResponse**](BroadcastsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | There was an error with the supplied &#x60;Authorization&#x60; header. |  -  |
| **0** | Unexpected error |  -  |

<a id="getBroadcastByPid"></a>
# **getBroadcastByPid**
> BroadcastsResponse getBroadcastByPid(xAPIKey, pid)

Broadcasts by PID

Find broadcast by PID 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BroadcastsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    BroadcastsApi apiInstance = new BroadcastsApi(defaultClient);
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String pid = "pid_example"; // String | pid
    try {
      BroadcastsResponse result = apiInstance.getBroadcastByPid(xAPIKey, pid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BroadcastsApi#getBroadcastByPid");
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
| **xAPIKey** | **String**| API_KEY | |
| **pid** | **String**| pid | |

### Return type

[**BroadcastsResponse**](BroadcastsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | There was an error with the supplied &#x60;Authorization&#x60; header. |  -  |
| **0** | Unexpected error |  -  |

