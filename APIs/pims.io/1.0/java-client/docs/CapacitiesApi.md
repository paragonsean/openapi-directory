# CapacitiesApi

All URIs are relative to *https://demo.pims.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchAllEventsCapacities**](CapacitiesApi.md#fetchAllEventsCapacities) | **GET** /events/{event_id}/capacities | Find all capacities for one event |
| [**fetchOneEventCapacity**](CapacitiesApi.md#fetchOneEventCapacity) | **GET** /events/{event_id}/capacities/{capacity_id} | Get one capacity by ID |


<a id="fetchAllEventsCapacities"></a>
# **fetchAllEventsCapacities**
> List&lt;EventsCapacitiesEntity&gt; fetchAllEventsCapacities(eventId, showIgnored, sort, pageSize)

Find all capacities for one event

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CapacitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    CapacitiesApi apiInstance = new CapacitiesApi(defaultClient);
    Integer eventId = 56; // Integer | ID of the targeted event.
    Boolean showIgnored = false; // Boolean | If set to `false`, show only the [event-]categories which are not ignored. If set to `true`, show everything.
    String sort = "date"; // String | Sort the capacities in the corresponding order.
    Integer pageSize = 25; // Integer | Pagination size, i.e. maximum number of items to be displayed in the response.
    try {
      List<EventsCapacitiesEntity> result = apiInstance.fetchAllEventsCapacities(eventId, showIgnored, sort, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CapacitiesApi#fetchAllEventsCapacities");
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
| **eventId** | **Integer**| ID of the targeted event. | |
| **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the [event-]categories which are not ignored. If set to &#x60;true&#x60;, show everything. | [optional] [default to false] |
| **sort** | **String**| Sort the capacities in the corresponding order. | [optional] [default to date] [enum: date, -date] |
| **pageSize** | **Integer**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25] |

### Return type

[**List&lt;EventsCapacitiesEntity&gt;**](EventsCapacitiesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives an array of events capacities |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **422** | Unprocessable Entity |  -  |
| **500** | Unexpected error |  -  |

<a id="fetchOneEventCapacity"></a>
# **fetchOneEventCapacity**
> EventsCapacitiesEntity fetchOneEventCapacity(eventId, capacityId, showIgnored)

Get one capacity by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CapacitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    CapacitiesApi apiInstance = new CapacitiesApi(defaultClient);
    Integer eventId = 56; // Integer | ID of the targeted event.
    Integer capacityId = 56; // Integer | ID of the targeted capacity.
    Boolean showIgnored = false; // Boolean | If set to `false`, show only the [event-]categories which are not ignored. If set to `true`, show everything.
    try {
      EventsCapacitiesEntity result = apiInstance.fetchOneEventCapacity(eventId, capacityId, showIgnored);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CapacitiesApi#fetchOneEventCapacity");
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
| **eventId** | **Integer**| ID of the targeted event. | |
| **capacityId** | **Integer**| ID of the targeted capacity. | |
| **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the [event-]categories which are not ignored. If set to &#x60;true&#x60;, show everything. | [optional] [default to false] |

### Return type

[**EventsCapacitiesEntity**](EventsCapacitiesEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives one event capacity |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **404** | Not Found |  -  |
| **500** | Unexpected error |  -  |

