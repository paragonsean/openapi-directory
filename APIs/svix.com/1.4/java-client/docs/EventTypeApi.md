# EventTypeApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createEventTypeApiV1EventTypePost**](EventTypeApi.md#createEventTypeApiV1EventTypePost) | **POST** /api/v1/event-type/ | Create Event Type |
| [**deleteEventTypeApiV1EventTypeEventTypeNameDelete**](EventTypeApi.md#deleteEventTypeApiV1EventTypeEventTypeNameDelete) | **DELETE** /api/v1/event-type/{event_type_name}/ | Archive Event Type |
| [**getEventTypeApiV1EventTypeEventTypeNameGet**](EventTypeApi.md#getEventTypeApiV1EventTypeEventTypeNameGet) | **GET** /api/v1/event-type/{event_type_name}/ | Get Event Type |
| [**listEventTypesApiV1EventTypeGet**](EventTypeApi.md#listEventTypesApiV1EventTypeGet) | **GET** /api/v1/event-type/ | List Event Types |
| [**updateEventTypeApiV1EventTypeEventTypeNamePut**](EventTypeApi.md#updateEventTypeApiV1EventTypeEventTypeNamePut) | **PUT** /api/v1/event-type/{event_type_name}/ | Update Event Type |


<a id="createEventTypeApiV1EventTypePost"></a>
# **createEventTypeApiV1EventTypePost**
> EventTypeOut createEventTypeApiV1EventTypePost(eventTypeIn, idempotencyKey)

Create Event Type

Create new or unarchive existing event type.  Unarchiving an event type will allow endpoints to filter on it and messages to be sent with it. Endpoints filtering on the event type before archival will continue to filter on it. This operation does not preserve the description and schemas.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    EventTypeApi apiInstance = new EventTypeApi(defaultClient);
    EventTypeIn eventTypeIn = new EventTypeIn(); // EventTypeIn | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      EventTypeOut result = apiInstance.createEventTypeApiV1EventTypePost(eventTypeIn, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventTypeApi#createEventTypeApiV1EventTypePost");
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
| **eventTypeIn** | [**EventTypeIn**](EventTypeIn.md)|  | |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**EventTypeOut**](EventTypeOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful Response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |

<a id="deleteEventTypeApiV1EventTypeEventTypeNameDelete"></a>
# **deleteEventTypeApiV1EventTypeEventTypeNameDelete**
> deleteEventTypeApiV1EventTypeEventTypeNameDelete(eventTypeName, expunge, idempotencyKey)

Archive Event Type

Archive an event type.  Endpoints already configured to filter on an event type will continue to do so after archival. However, new messages can not be sent with it and endpoints can not filter on it. An event type can be unarchived with the [create operation](#operation/create_event_type_api_v1_event_type__post).  If &#x60;expunge&#x3D;true&#x60; is set then the event type is deleted instead of archived. This can only be used in development environments.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    EventTypeApi apiInstance = new EventTypeApi(defaultClient);
    String eventTypeName = "user.signup"; // String | 
    Boolean expunge = false; // Boolean | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      apiInstance.deleteEventTypeApiV1EventTypeEventTypeNameDelete(eventTypeName, expunge, idempotencyKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventTypeApi#deleteEventTypeApiV1EventTypeEventTypeNameDelete");
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
| **eventTypeName** | **String**|  | |
| **expunge** | **Boolean**|  | [optional] [default to false] |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

null (empty response body)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful Response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |

<a id="getEventTypeApiV1EventTypeEventTypeNameGet"></a>
# **getEventTypeApiV1EventTypeEventTypeNameGet**
> EventTypeOut getEventTypeApiV1EventTypeEventTypeNameGet(eventTypeName, idempotencyKey)

Get Event Type

Get an event type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    EventTypeApi apiInstance = new EventTypeApi(defaultClient);
    String eventTypeName = "user.signup"; // String | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      EventTypeOut result = apiInstance.getEventTypeApiV1EventTypeEventTypeNameGet(eventTypeName, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventTypeApi#getEventTypeApiV1EventTypeEventTypeNameGet");
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
| **eventTypeName** | **String**|  | |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**EventTypeOut**](EventTypeOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |

<a id="listEventTypesApiV1EventTypeGet"></a>
# **listEventTypesApiV1EventTypeGet**
> ListResponseEventTypeOut listEventTypesApiV1EventTypeGet(iterator, limit, withContent, includeArchived, idempotencyKey)

List Event Types

Return the list of event types.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    EventTypeApi apiInstance = new EventTypeApi(defaultClient);
    String iterator = "user.signup"; // String | 
    Integer limit = 50; // Integer | 
    Boolean withContent = false; // Boolean | 
    Boolean includeArchived = false; // Boolean | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      ListResponseEventTypeOut result = apiInstance.listEventTypesApiV1EventTypeGet(iterator, limit, withContent, includeArchived, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventTypeApi#listEventTypesApiV1EventTypeGet");
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
| **iterator** | **String**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **withContent** | **Boolean**|  | [optional] [default to false] |
| **includeArchived** | **Boolean**|  | [optional] [default to false] |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**ListResponseEventTypeOut**](ListResponseEventTypeOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |

<a id="updateEventTypeApiV1EventTypeEventTypeNamePut"></a>
# **updateEventTypeApiV1EventTypeEventTypeNamePut**
> EventTypeOut updateEventTypeApiV1EventTypeEventTypeNamePut(eventTypeName, eventTypeUpdate, idempotencyKey)

Update Event Type

Update an event type.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EventTypeApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP bearer authorization: HTTPBearer
    HttpBearerAuth HTTPBearer = (HttpBearerAuth) defaultClient.getAuthentication("HTTPBearer");
    HTTPBearer.setBearerToken("BEARER TOKEN");

    EventTypeApi apiInstance = new EventTypeApi(defaultClient);
    String eventTypeName = "user.signup"; // String | 
    EventTypeUpdate eventTypeUpdate = new EventTypeUpdate(); // EventTypeUpdate | 
    String idempotencyKey = "idempotencyKey_example"; // String | The request's idempotency key
    try {
      EventTypeOut result = apiInstance.updateEventTypeApiV1EventTypeEventTypeNamePut(eventTypeName, eventTypeUpdate, idempotencyKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EventTypeApi#updateEventTypeApiV1EventTypeEventTypeNamePut");
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
| **eventTypeName** | **String**|  | |
| **eventTypeUpdate** | [**EventTypeUpdate**](EventTypeUpdate.md)|  | |
| **idempotencyKey** | **String**| The request&#39;s idempotency key | [optional] |

### Return type

[**EventTypeOut**](EventTypeOut.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful Response |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **409** | Conflict |  -  |
| **422** | Validation Error |  -  |
| **429** | Too Many Requests |  -  |

