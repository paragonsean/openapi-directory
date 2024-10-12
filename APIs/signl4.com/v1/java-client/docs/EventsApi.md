# EventsApi

All URIs are relative to *https://connect.signl4.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**eventsEventIdOverviewGet**](EventsApi.md#eventsEventIdOverviewGet) | **GET** /events/{eventId}/overview | Get overview event |
| [**eventsEventIdParametersGet**](EventsApi.md#eventsEventIdParametersGet) | **GET** /events/{eventId}/parameters | Get event parameters |
| [**eventsPagedPost**](EventsApi.md#eventsPagedPost) | **POST** /events/paged | Get overview event paged. |


<a id="eventsEventIdOverviewGet"></a>
# **eventsEventIdOverviewGet**
> OverviewEvent eventsEventIdOverviewGet(eventId)

Get overview event

Get overview event by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String eventId = "eventId_example"; // String | Id of event to get.
    try {
      OverviewEvent result = apiInstance.eventsEventIdOverviewGet(eventId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#eventsEventIdOverviewGet");
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
| **eventId** | **String**| Id of event to get. | |

### Return type

[**OverviewEvent**](OverviewEvent.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns overview event with specific id. |  -  |
| **400** | Required parameters could not be found in the request/claims. |  -  |
| **404** | Event with specified id could not be found. |  -  |
| **500** | Internal general error occured. |  -  |

<a id="eventsEventIdParametersGet"></a>
# **eventsEventIdParametersGet**
> List&lt;EventParameterInfo&gt; eventsEventIdParametersGet(eventId)

Get event parameters

Get parameters of an event by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String eventId = "eventId_example"; // String | Event Id of the requested Alert.
    try {
      List<EventParameterInfo> result = apiInstance.eventsEventIdParametersGet(eventId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#eventsEventIdParametersGet");
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
| **eventId** | **String**| Event Id of the requested Alert. | |

### Return type

[**List&lt;EventParameterInfo&gt;**](EventParameterInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Required information could not be found in the request/claims. |  -  |
| **404** | Required entities could not be found in the database. |  -  |
| **500** | Internal general error occured. |  -  |

<a id="eventsPagedPost"></a>
# **eventsPagedPost**
> OverviewEventPagedResultsPublic eventsPagedPost(maxResults, eventFilter)

Get overview event paged.

Get overview event paged. If there are more results, you also get a continuation token which you can add to the event filter.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.signl4.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    EventsApi apiInstance = new EventsApi(defaultClient);
    Integer maxResults = 56; // Integer | Defines the limit of retrieved alert details per request. 1 to 100 are allowed per request.                   Number of alerts could be less if filtered but at least 1.
    EventFilter eventFilter = new EventFilter(); // EventFilter | The filter defines which alerts are supposed to be retrieved.
    try {
      OverviewEventPagedResultsPublic result = apiInstance.eventsPagedPost(maxResults, eventFilter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#eventsPagedPost");
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
| **maxResults** | **Integer**| Defines the limit of retrieved alert details per request. 1 to 100 are allowed per request.                   Number of alerts could be less if filtered but at least 1. | [optional] |
| **eventFilter** | [**EventFilter**](EventFilter.md)| The filter defines which alerts are supposed to be retrieved. | [optional] |

### Return type

[**OverviewEventPagedResultsPublic**](OverviewEventPagedResultsPublic.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/*+json, application/json, application/json-patch+json, text/json
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns paged result with found events and continuation token, if database holds more events. |  -  |
| **204** | No event could be found (with passed filter) |  -  |
| **400** | Required parameters could not be found in the request/claims. |  -  |
| **404** | Not Found |  -  |
| **500** | Internal general error occured. |  -  |

