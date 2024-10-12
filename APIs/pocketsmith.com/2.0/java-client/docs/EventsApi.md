# EventsApi

All URIs are relative to *https://api.pocketsmith.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**eventsIdDelete**](EventsApi.md#eventsIdDelete) | **DELETE** /events/{id} | Delete event |
| [**eventsIdGet**](EventsApi.md#eventsIdGet) | **GET** /events/{id} | Get event |
| [**eventsIdPut**](EventsApi.md#eventsIdPut) | **PUT** /events/{id} | Update event |
| [**scenariosIdEventsGet**](EventsApi.md#scenariosIdEventsGet) | **GET** /scenarios/{id}/events | List events in scenario. |
| [**scenariosIdEventsPost**](EventsApi.md#scenariosIdEventsPost) | **POST** /scenarios/{id}/events | Create event in scenario |
| [**usersIdEventsGet**](EventsApi.md#usersIdEventsGet) | **GET** /users/{id}/events | List events in user. |


<a id="eventsIdDelete"></a>
# **eventsIdDelete**
> eventsIdDelete(id, behaviour)

Delete event

Deletes an event by its ID.

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
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String id = "42-1601942400"; // String | The unique identifier of the event.
    String behaviour = "one"; // String | Whether the delete applies only to this event, to all events within the series from this event or to all events within the series.
    try {
      apiInstance.eventsIdDelete(id, behaviour);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#eventsIdDelete");
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
| **id** | **String**| The unique identifier of the event. | |
| **behaviour** | **String**| Whether the delete applies only to this event, to all events within the series from this event or to all events within the series. | [enum: one, forward, all] |

### Return type

null (empty response body)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |

<a id="eventsIdGet"></a>
# **eventsIdGet**
> Event eventsIdGet(id)

Get event

Gets a particular event by its ID.

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
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String id = "42-1601942400"; // String | The unique identifier of the event.
    try {
      Event result = apiInstance.eventsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#eventsIdGet");
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
| **id** | **String**| The unique identifier of the event. | |

### Return type

[**Event**](Event.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

<a id="eventsIdPut"></a>
# **eventsIdPut**
> Event eventsIdPut(id, eventsIdPutRequest)

Update event

Updates an event by its ID.

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
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    EventsApi apiInstance = new EventsApi(defaultClient);
    String id = "42-1601942400"; // String | The unique identifier of the event.
    EventsIdPutRequest eventsIdPutRequest = new EventsIdPutRequest(); // EventsIdPutRequest | 
    try {
      Event result = apiInstance.eventsIdPut(id, eventsIdPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#eventsIdPut");
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
| **id** | **String**| The unique identifier of the event. | |
| **eventsIdPutRequest** | [**EventsIdPutRequest**](EventsIdPutRequest.md)|  | [optional] |

### Return type

[**Event**](Event.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |

<a id="scenariosIdEventsGet"></a>
# **scenariosIdEventsGet**
> List&lt;Event&gt; scenariosIdEventsGet(id, startDate, endDate)

List events in scenario.

Lists events belonging to a scenario by their ID.

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
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    EventsApi apiInstance = new EventsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the scenario.
    String startDate = "2020-10-01"; // String | Return the events from and including this date.
    String endDate = "2020-10-30"; // String | Return the events until and including this date.
    try {
      List<Event> result = apiInstance.scenariosIdEventsGet(id, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#scenariosIdEventsGet");
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
| **id** | **Integer**| The unique identifier of the scenario. | |
| **startDate** | **String**| Return the events from and including this date. | |
| **endDate** | **String**| Return the events until and including this date. | |

### Return type

[**List&lt;Event&gt;**](Event.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

<a id="scenariosIdEventsPost"></a>
# **scenariosIdEventsPost**
> Event scenariosIdEventsPost(id, scenariosIdEventsPostRequest)

Create event in scenario

Creates an event in a scenario by its ID.

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
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    EventsApi apiInstance = new EventsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the scenario.
    ScenariosIdEventsPostRequest scenariosIdEventsPostRequest = new ScenariosIdEventsPostRequest(); // ScenariosIdEventsPostRequest | 
    try {
      Event result = apiInstance.scenariosIdEventsPost(id, scenariosIdEventsPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#scenariosIdEventsPost");
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
| **id** | **Integer**| The unique identifier of the scenario. | |
| **scenariosIdEventsPostRequest** | [**ScenariosIdEventsPostRequest**](ScenariosIdEventsPostRequest.md)|  | [optional] |

### Return type

[**Event**](Event.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |

<a id="usersIdEventsGet"></a>
# **usersIdEventsGet**
> List&lt;Event&gt; usersIdEventsGet(id, startDate, endDate)

List events in user.

Lists events belonging to a user by their ID.

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
    defaultClient.setBasePath("https://api.pocketsmith.com/v2");
    
    // Configure API key authorization: developerKey
    ApiKeyAuth developerKey = (ApiKeyAuth) defaultClient.getAuthentication("developerKey");
    developerKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //developerKey.setApiKeyPrefix("Token");

    EventsApi apiInstance = new EventsApi(defaultClient);
    Integer id = 42; // Integer | The unique identifier of the user.
    String startDate = "2020-10-01"; // String | Return the events from and including this date.
    String endDate = "2020-10-30"; // String | Return the events until and including this date.
    try {
      List<Event> result = apiInstance.usersIdEventsGet(id, startDate, endDate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventsApi#usersIdEventsGet");
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
| **id** | **Integer**| The unique identifier of the user. | |
| **startDate** | **String**| Return the events from and including this date. | |
| **endDate** | **String**| Return the events until and including this date. | |

### Return type

[**List&lt;Event&gt;**](Event.md)

### Authorization

[developerKey](../README.md#developerKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **403** | Not Allowed |  -  |
| **404** | Not Found |  -  |

