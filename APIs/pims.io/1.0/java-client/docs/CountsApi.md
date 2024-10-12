# CountsApi

All URIs are relative to *https://demo.pims.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchAllDetailedTicketCounts**](CountsApi.md#fetchAllDetailedTicketCounts) | **GET** /events/{event_id}/ticket-counts/detailed | Find all detailed ticket counts for one event |
| [**fetchAllTicketCounts**](CountsApi.md#fetchAllTicketCounts) | **GET** /events/{event_id}/ticket-counts | Find all ticket counts for one event |
| [**fetchOneDetailedTicketCount**](CountsApi.md#fetchOneDetailedTicketCount) | **GET** /events/{event_id}/ticket-counts/detailed/{ticket_count_id} | Get one detailed ticket count by ID |
| [**fetchOneTicketCount**](CountsApi.md#fetchOneTicketCount) | **GET** /events/{event_id}/ticket-counts/{ticket_count_id} | Get one ticket count by ID |


<a id="fetchAllDetailedTicketCounts"></a>
# **fetchAllDetailedTicketCounts**
> List&lt;TicketCountsDetailedEntity&gt; fetchAllDetailedTicketCounts(eventId, fromDate, toDate, showIgnored, showNotApproved, sort, pageSize)

Find all detailed ticket counts for one event

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    CountsApi apiInstance = new CountsApi(defaultClient);
    Integer eventId = 56; // Integer | ID of the targeted event.
    LocalDate fromDate = LocalDate.now(); // LocalDate | Find only the ticket counts after this date.
    LocalDate toDate = LocalDate.now(); // LocalDate | Find only the ticket counts before this date.
    Boolean showIgnored = false; // Boolean | If set to `false`, show only the [event-]categories/[event-]price ranges/[event]channels which are not ignored. If set to `true`, show everything.
    Boolean showNotApproved = false; // Boolean | If set to `false`, show only the approved ticket counts. If set to `true`, show all the ticket counts.
    String sort = "date"; // String | Sort the ticket counts in the corresponding order.
    Integer pageSize = 25; // Integer | Pagination size, i.e. maximum number of items to be displayed in the response.
    try {
      List<TicketCountsDetailedEntity> result = apiInstance.fetchAllDetailedTicketCounts(eventId, fromDate, toDate, showIgnored, showNotApproved, sort, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountsApi#fetchAllDetailedTicketCounts");
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
| **fromDate** | **LocalDate**| Find only the ticket counts after this date. | [optional] |
| **toDate** | **LocalDate**| Find only the ticket counts before this date. | [optional] |
| **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the [event-]categories/[event-]price ranges/[event]channels which are not ignored. If set to &#x60;true&#x60;, show everything. | [optional] [default to false] |
| **showNotApproved** | **Boolean**| If set to &#x60;false&#x60;, show only the approved ticket counts. If set to &#x60;true&#x60;, show all the ticket counts. | [optional] [default to false] |
| **sort** | **String**| Sort the ticket counts in the corresponding order. | [optional] [default to date] [enum: date, -date] |
| **pageSize** | **Integer**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25] |

### Return type

[**List&lt;TicketCountsDetailedEntity&gt;**](TicketCountsDetailedEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives an array of detailed ticket counts |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **422** | Unprocessable Entity |  -  |
| **500** | Unexpected error |  -  |

<a id="fetchAllTicketCounts"></a>
# **fetchAllTicketCounts**
> List&lt;TicketCountsEntity&gt; fetchAllTicketCounts(eventId, fromDate, toDate, showIgnored, showNotApproved, sort, pageSize)

Find all ticket counts for one event

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    CountsApi apiInstance = new CountsApi(defaultClient);
    Integer eventId = 56; // Integer | ID of the targeted event.
    LocalDate fromDate = LocalDate.now(); // LocalDate | Find only the ticket counts after this date.
    LocalDate toDate = LocalDate.now(); // LocalDate | Find only the ticket counts before this date.
    Boolean showIgnored = false; // Boolean | If set to `false`, show only the [event-]categories/[event-]price ranges/[event]channels which are not ignored. If set to `true`, show everything.
    Boolean showNotApproved = false; // Boolean | If set to `false`, show only the approved ticket counts. If set to `true`, show all the ticket counts.
    String sort = "date"; // String | Sort the ticket counts in the corresponding order.
    Integer pageSize = 25; // Integer | Pagination size, i.e. maximum number of items to be displayed in the response.
    try {
      List<TicketCountsEntity> result = apiInstance.fetchAllTicketCounts(eventId, fromDate, toDate, showIgnored, showNotApproved, sort, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountsApi#fetchAllTicketCounts");
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
| **fromDate** | **LocalDate**| Find only the ticket counts after this date. | [optional] |
| **toDate** | **LocalDate**| Find only the ticket counts before this date. | [optional] |
| **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the [event-]categories/[event-]price ranges/[event]channels which are not ignored. If set to &#x60;true&#x60;, show everything. | [optional] [default to false] |
| **showNotApproved** | **Boolean**| If set to &#x60;false&#x60;, show only the approved ticket counts. If set to &#x60;true&#x60;, show all the ticket counts. | [optional] [default to false] |
| **sort** | **String**| Sort the ticket counts in the corresponding order. | [optional] [default to date] [enum: date, -date] |
| **pageSize** | **Integer**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25] |

### Return type

[**List&lt;TicketCountsEntity&gt;**](TicketCountsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives an array of ticket counts |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **422** | Unprocessable Entity |  -  |
| **500** | Unexpected error |  -  |

<a id="fetchOneDetailedTicketCount"></a>
# **fetchOneDetailedTicketCount**
> TicketCountsDetailedEntity fetchOneDetailedTicketCount(eventId, ticketCountId, showIgnored)

Get one detailed ticket count by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    CountsApi apiInstance = new CountsApi(defaultClient);
    Integer eventId = 56; // Integer | ID of the targeted event.
    Integer ticketCountId = 56; // Integer | ID of the targeted ticket count.
    Boolean showIgnored = false; // Boolean | If set to `false`, show only the [event-]categories/[event-]price ranges/[event]channels which are not ignored. If set to `true`, show everything.
    try {
      TicketCountsDetailedEntity result = apiInstance.fetchOneDetailedTicketCount(eventId, ticketCountId, showIgnored);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountsApi#fetchOneDetailedTicketCount");
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
| **ticketCountId** | **Integer**| ID of the targeted ticket count. | |
| **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the [event-]categories/[event-]price ranges/[event]channels which are not ignored. If set to &#x60;true&#x60;, show everything. | [optional] [default to false] |

### Return type

[**TicketCountsDetailedEntity**](TicketCountsDetailedEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives one detailed ticket count |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **404** | Not Found |  -  |
| **500** | Unexpected error |  -  |

<a id="fetchOneTicketCount"></a>
# **fetchOneTicketCount**
> TicketCountsEntity fetchOneTicketCount(eventId, ticketCountId, showIgnored)

Get one ticket count by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    CountsApi apiInstance = new CountsApi(defaultClient);
    Integer eventId = 56; // Integer | ID of the targeted event.
    Integer ticketCountId = 56; // Integer | ID of the targeted ticket count.
    Boolean showIgnored = false; // Boolean | If set to `false`, show only the [event-]categories/[event-]price ranges/[event]channels which are not ignored. If set to `true`, show everything.
    try {
      TicketCountsEntity result = apiInstance.fetchOneTicketCount(eventId, ticketCountId, showIgnored);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CountsApi#fetchOneTicketCount");
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
| **ticketCountId** | **Integer**| ID of the targeted ticket count. | |
| **showIgnored** | **Boolean**| If set to &#x60;false&#x60;, show only the [event-]categories/[event-]price ranges/[event]channels which are not ignored. If set to &#x60;true&#x60;, show everything. | [optional] [default to false] |

### Return type

[**TicketCountsEntity**](TicketCountsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives one ticket count |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **404** | Not Found |  -  |
| **500** | Unexpected error |  -  |

