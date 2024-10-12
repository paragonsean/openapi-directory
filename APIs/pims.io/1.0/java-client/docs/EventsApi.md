# EventsApi

All URIs are relative to *https://demo.pims.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**fetchAllEvents**](EventsApi.md#fetchAllEvents) | **GET** /events | Find all events |
| [**fetchAllSeriesEvents**](EventsApi.md#fetchAllSeriesEvents) | **GET** /series/{series_id}/events | Find all events for one series |
| [**fetchAllVenuesEvents**](EventsApi.md#fetchAllVenuesEvents) | **GET** /venues/{venue_id}/events | Find all events for one venue |
| [**fetchOneEvent**](EventsApi.md#fetchOneEvent) | **GET** /events/{event_id} | Get one event by ID |


<a id="fetchAllEvents"></a>
# **fetchAllEvents**
> List&lt;EventsEntity&gt; fetchAllEvents(label, fromDatetime, toDatetime, city, sort, pageSize, acceptLanguage)

Find all events

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
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String label = "label_example"; // String | Find only the events whose label contains this value.
    LocalDate fromDatetime = LocalDate.now(); // LocalDate | Find only the events starting after this date.
    LocalDate toDatetime = LocalDate.now(); // LocalDate | Find only the events starting before this date.
    String city = "city_example"; // String | Find only the events whose venue city (or metropolitan area) contains this value.
    String sort = "label"; // String | Sort the events in the corresponding order.
    Integer pageSize = 25; // Integer | Pagination size, i.e. maximum number of items to be displayed in the response.
    String acceptLanguage = "de"; // String | Language used for the translatable labels.
    try {
      List<EventsEntity> result = apiInstance.fetchAllEvents(label, fromDatetime, toDatetime, city, sort, pageSize, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#fetchAllEvents");
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
| **label** | **String**| Find only the events whose label contains this value. | [optional] |
| **fromDatetime** | **LocalDate**| Find only the events starting after this date. | [optional] |
| **toDatetime** | **LocalDate**| Find only the events starting before this date. | [optional] |
| **city** | **String**| Find only the events whose venue city (or metropolitan area) contains this value. | [optional] |
| **sort** | **String**| Sort the events in the corresponding order. | [optional] [default to label] [enum: label, -label, datetime, -datetime, venue_label, -venue_label, city, -city] |
| **pageSize** | **Integer**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25] |
| **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to en] [enum: de, en, fr] |

### Return type

[**List&lt;EventsEntity&gt;**](EventsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives an array of events |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **422** | Unprocessable Entity |  -  |
| **500** | Unexpected error |  -  |

<a id="fetchAllSeriesEvents"></a>
# **fetchAllSeriesEvents**
> List&lt;EventsEntity&gt; fetchAllSeriesEvents(seriesId, fromDatetime, toDatetime, city, sort, pageSize, acceptLanguage)

Find all events for one series

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
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    EventsApi apiInstance = new EventsApi(defaultClient);
    Integer seriesId = 56; // Integer | ID of the targeted series.
    LocalDate fromDatetime = LocalDate.now(); // LocalDate | Find only the events starting after this date.
    LocalDate toDatetime = LocalDate.now(); // LocalDate | Find only the events starting before this date.
    String city = "city_example"; // String | Find only the events whose venue city (or metropolitan area) contains this value.
    String sort = "label"; // String | Sort the events in the corresponding order.
    Integer pageSize = 25; // Integer | Pagination size, i.e. maximum number of items to be displayed in the response.
    String acceptLanguage = "de"; // String | Language used for the translatable labels.
    try {
      List<EventsEntity> result = apiInstance.fetchAllSeriesEvents(seriesId, fromDatetime, toDatetime, city, sort, pageSize, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#fetchAllSeriesEvents");
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
| **seriesId** | **Integer**| ID of the targeted series. | |
| **fromDatetime** | **LocalDate**| Find only the events starting after this date. | [optional] |
| **toDatetime** | **LocalDate**| Find only the events starting before this date. | [optional] |
| **city** | **String**| Find only the events whose venue city (or metropolitan area) contains this value. | [optional] |
| **sort** | **String**| Sort the events in the corresponding order. | [optional] [default to label] [enum: label, -label, datetime, -datetime, venue_label, -venue_label, city, -city] |
| **pageSize** | **Integer**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25] |
| **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to en] [enum: de, en, fr] |

### Return type

[**List&lt;EventsEntity&gt;**](EventsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives an array of events |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **422** | Unprocessable Entity |  -  |
| **500** | Unexpected error |  -  |

<a id="fetchAllVenuesEvents"></a>
# **fetchAllVenuesEvents**
> List&lt;EventsEntity&gt; fetchAllVenuesEvents(venueId, fromDatetime, toDatetime, city, sort, pageSize, acceptLanguage)

Find all events for one venue

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
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    EventsApi apiInstance = new EventsApi(defaultClient);
    Integer venueId = 56; // Integer | ID of the targeted venue.
    LocalDate fromDatetime = LocalDate.now(); // LocalDate | Find only the events starting after this date.
    LocalDate toDatetime = LocalDate.now(); // LocalDate | Find only the events starting before this date.
    String city = "city_example"; // String | Find only the events whose venue city (or metropolitan area) contains this value.
    String sort = "label"; // String | Sort the events in the corresponding order.
    Integer pageSize = 25; // Integer | Pagination size, i.e. maximum number of items to be displayed in the response.
    String acceptLanguage = "de"; // String | Language used for the translatable labels.
    try {
      List<EventsEntity> result = apiInstance.fetchAllVenuesEvents(venueId, fromDatetime, toDatetime, city, sort, pageSize, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#fetchAllVenuesEvents");
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
| **venueId** | **Integer**| ID of the targeted venue. | |
| **fromDatetime** | **LocalDate**| Find only the events starting after this date. | [optional] |
| **toDatetime** | **LocalDate**| Find only the events starting before this date. | [optional] |
| **city** | **String**| Find only the events whose venue city (or metropolitan area) contains this value. | [optional] |
| **sort** | **String**| Sort the events in the corresponding order. | [optional] [default to label] [enum: label, -label, datetime, -datetime, venue_label, -venue_label, city, -city] |
| **pageSize** | **Integer**| Pagination size, i.e. maximum number of items to be displayed in the response. | [optional] [default to 25] |
| **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to en] [enum: de, en, fr] |

### Return type

[**List&lt;EventsEntity&gt;**](EventsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives an array of events |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **422** | Unprocessable Entity |  -  |
| **500** | Unexpected error |  -  |

<a id="fetchOneEvent"></a>
# **fetchOneEvent**
> EventsEntity fetchOneEvent(eventId, acceptLanguage)

Get one event by ID

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
    defaultClient.setBasePath("https://demo.pims.io/api/v1");
    
    // Configure HTTP basic authorization: Basic Auth
    HttpBasicAuth Basic Auth = (HttpBasicAuth) defaultClient.getAuthentication("Basic Auth");
    Basic Auth.setUsername("YOUR USERNAME");
    Basic Auth.setPassword("YOUR PASSWORD");

    EventsApi apiInstance = new EventsApi(defaultClient);
    Integer eventId = 56; // Integer | ID of the targeted event.
    String acceptLanguage = "de"; // String | Language used for the translatable labels.
    try {
      EventsEntity result = apiInstance.fetchOneEvent(eventId, acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#fetchOneEvent");
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
| **acceptLanguage** | **String**| Language used for the translatable labels. | [optional] [default to en] [enum: de, en, fr] |

### Return type

[**EventsEntity**](EventsEntity.md)

### Authorization

[Basic Auth](../README.md#Basic Auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/hal+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation, gives one event |  -  |
| **401** | Unauthorized, no authentication was made |  -  |
| **403** | Forbidden, the authentication is wrong |  -  |
| **404** | Not Found |  -  |
| **500** | Unexpected error |  -  |

