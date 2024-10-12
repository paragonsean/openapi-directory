# EventsV1EventTypeApi

All URIs are relative to *https://events.twilio.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchEventType**](EventsV1EventTypeApi.md#fetchEventType) | **GET** /v1/Types/{Type} |  |
| [**listEventType**](EventsV1EventTypeApi.md#listEventType) | **GET** /v1/Types |  |


<a id="fetchEventType"></a>
# **fetchEventType**
> EventsV1EventType fetchEventType(type)



Fetch a specific Event Type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsV1EventTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    EventsV1EventTypeApi apiInstance = new EventsV1EventTypeApi(defaultClient);
    String type = "type_example"; // String | A string that uniquely identifies this Event Type.
    try {
      EventsV1EventType result = apiInstance.fetchEventType(type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsV1EventTypeApi#fetchEventType");
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
| **type** | **String**| A string that uniquely identifies this Event Type. | |

### Return type

[**EventsV1EventType**](EventsV1EventType.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listEventType"></a>
# **listEventType**
> ListEventTypeResponse listEventType(schemaId, pageSize, page, pageToken)



Retrieve a paginated list of all the available Event Types.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventsV1EventTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://events.twilio.com");
    
    // Configure HTTP basic authorization: accountSid_authToken
    HttpBasicAuth accountSid_authToken = (HttpBasicAuth) defaultClient.getAuthentication("accountSid_authToken");
    accountSid_authToken.setUsername("YOUR USERNAME");
    accountSid_authToken.setPassword("YOUR PASSWORD");

    EventsV1EventTypeApi apiInstance = new EventsV1EventTypeApi(defaultClient);
    String schemaId = "schemaId_example"; // String | A string parameter filtering the results to return only the Event Types using a given schema.
    Integer pageSize = 56; // Integer | How many resources to return in each list page. The default is 50, and the maximum is 1000.
    Integer page = 56; // Integer | The page index. This value is simply for client state.
    String pageToken = "pageToken_example"; // String | The page token. This is provided by the API.
    try {
      ListEventTypeResponse result = apiInstance.listEventType(schemaId, pageSize, page, pageToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsV1EventTypeApi#listEventType");
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
| **schemaId** | **String**| A string parameter filtering the results to return only the Event Types using a given schema. | [optional] |
| **pageSize** | **Integer**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] |
| **page** | **Integer**| The page index. This value is simply for client state. | [optional] |
| **pageToken** | **String**| The page token. This is provided by the API. | [optional] |

### Return type

[**ListEventTypeResponse**](ListEventTypeResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

