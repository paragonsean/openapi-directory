# MonitorV1EventApi

All URIs are relative to *https://monitor.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchEvent**](MonitorV1EventApi.md#fetchEvent) | **GET** /v1/Events/{Sid} |  |
| [**listEvent**](MonitorV1EventApi.md#listEvent) | **GET** /v1/Events |  |


<a id="fetchEvent"></a>
# **fetchEvent**
> MonitorV1Event fetchEvent(sid)





### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonitorV1EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://monitor.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MonitorV1EventApi apiInstance = new MonitorV1EventApi(defaultClient);
    String sid = "sid_example"; // String | The SID of the Event resource to fetch.
    try {
      MonitorV1Event result = apiInstance.fetchEvent(sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorV1EventApi#fetchEvent");
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
| **sid** | **String**| The SID of the Event resource to fetch. | |

### Return type

[**MonitorV1Event**](MonitorV1Event.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listEvent"></a>
# **listEvent**
> ListEventResponse listEvent(actorSid, eventType, resourceSid, sourceIpAddress, startDate, endDate, pageSize, page, pageToken)



Returns a list of events in the account, sorted by event-date.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MonitorV1EventApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://monitor.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    MonitorV1EventApi apiInstance = new MonitorV1EventApi(defaultClient);
    String actorSid = "actorSid_example"; // String | Only include events initiated by this Actor. Useful for auditing actions taken by specific users or API credentials.
    String eventType = "eventType_example"; // String | Only include events of this [Event Type](https://www.twilio.com/docs/usage/monitor-events#event-types).
    String resourceSid = "resourceSid_example"; // String | Only include events that refer to this resource. Useful for discovering the history of a specific resource.
    String sourceIpAddress = "sourceIpAddress_example"; // String | Only include events that originated from this IP address. Useful for tracking suspicious activity originating from the API or the Twilio Console.
    OffsetDateTime startDate = OffsetDateTime.now(); // OffsetDateTime | Only include events that occurred on or after this date. Specify the date in GMT and [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    OffsetDateTime endDate = OffsetDateTime.now(); // OffsetDateTime | Only include events that occurred on or before this date. Specify the date in GMT and [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListEventResponse result = apiInstance.listEvent(actorSid, eventType, resourceSid, sourceIpAddress, startDate, endDate, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MonitorV1EventApi#listEvent");
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
| **actorSid** | **String**| Only include events initiated by this Actor. Useful for auditing actions taken by specific users or API credentials. | [optional] |
| **eventType** | **String**| Only include events of this [Event Type](https://www.twilio.com/docs/usage/monitor-events#event-types). | [optional] |
| **resourceSid** | **String**| Only include events that refer to this resource. Useful for discovering the history of a specific resource. | [optional] |
| **sourceIpAddress** | **String**| Only include events that originated from this IP address. Useful for tracking suspicious activity originating from the API or the Twilio Console. | [optional] |
| **startDate** | **OffsetDateTime**| Only include events that occurred on or after this date. Specify the date in GMT and [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] |
| **endDate** | **OffsetDateTime**| Only include events that occurred on or before this date. Specify the date in GMT and [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListEventResponse**](ListEventResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

