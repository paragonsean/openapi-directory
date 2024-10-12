# ExternalEventsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getExternalEvents**](ExternalEventsApi.md#getExternalEvents) | **GET** /external_events | List External Events |
| [**getExternalEventsId**](ExternalEventsApi.md#getExternalEventsId) | **GET** /external_events/{id} | Show External Event |
| [**postExternalEvents**](ExternalEventsApi.md#postExternalEvents) | **POST** /external_events | Create External Event |


<a id="getExternalEvents"></a>
# **getExternalEvents**
> List&lt;ExternalEventEntity&gt; getExternalEvents(cursor, perPage, sortBy, filter, filterGt, filterGteq, filterPrefix, filterLt, filterLteq)

List External Events

List External Events

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExternalEventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    ExternalEventsApi apiInstance = new ExternalEventsApi(defaultClient);
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Object sortBy = null; // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[remote_server_type]=desc`). Valid fields are `remote_server_type`, `site_id`, `folder_behavior_id`, `event_type`, `created_at` or `status`.
    Object filter = null; // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `created_at`, `event_type`, `remote_server_type`, `status` or `folder_behavior_id`. Valid field combinations are `[ event_type, status, created_at ]`, `[ event_type, created_at ]` or `[ status, created_at ]`.
    Object filterGt = null; // Object | If set, return records where the specified field is greater than the supplied value. Valid fields are `created_at`.
    Object filterGteq = null; // Object | If set, return records where the specified field is greater than or equal the supplied value. Valid fields are `created_at`.
    Object filterPrefix = null; // Object | If set, return records where the specified field is prefixed by the supplied value. Valid fields are `remote_server_type`.
    Object filterLt = null; // Object | If set, return records where the specified field is less than the supplied value. Valid fields are `created_at`.
    Object filterLteq = null; // Object | If set, return records where the specified field is less than or equal the supplied value. Valid fields are `created_at`.
    try {
      List<ExternalEventEntity> result = apiInstance.getExternalEvents(cursor, perPage, sortBy, filter, filterGt, filterGteq, filterPrefix, filterLt, filterLteq);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExternalEventsApi#getExternalEvents");
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
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |
| **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[remote_server_type]&#x3D;desc&#x60;). Valid fields are &#x60;remote_server_type&#x60;, &#x60;site_id&#x60;, &#x60;folder_behavior_id&#x60;, &#x60;event_type&#x60;, &#x60;created_at&#x60; or &#x60;status&#x60;. | [optional] |
| **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;created_at&#x60;, &#x60;event_type&#x60;, &#x60;remote_server_type&#x60;, &#x60;status&#x60; or &#x60;folder_behavior_id&#x60;. Valid field combinations are &#x60;[ event_type, status, created_at ]&#x60;, &#x60;[ event_type, created_at ]&#x60; or &#x60;[ status, created_at ]&#x60;. | [optional] |
| **filterGt** | [**Object**](.md)| If set, return records where the specified field is greater than the supplied value. Valid fields are &#x60;created_at&#x60;. | [optional] |
| **filterGteq** | [**Object**](.md)| If set, return records where the specified field is greater than or equal the supplied value. Valid fields are &#x60;created_at&#x60;. | [optional] |
| **filterPrefix** | [**Object**](.md)| If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;remote_server_type&#x60;. | [optional] |
| **filterLt** | [**Object**](.md)| If set, return records where the specified field is less than the supplied value. Valid fields are &#x60;created_at&#x60;. | [optional] |
| **filterLteq** | [**Object**](.md)| If set, return records where the specified field is less than or equal the supplied value. Valid fields are &#x60;created_at&#x60;. | [optional] |

### Return type

[**List&lt;ExternalEventEntity&gt;**](ExternalEventEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of ExternalEvents objects. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="getExternalEventsId"></a>
# **getExternalEventsId**
> ExternalEventEntity getExternalEventsId(id)

Show External Event

Show External Event

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExternalEventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    ExternalEventsApi apiInstance = new ExternalEventsApi(defaultClient);
    Integer id = 56; // Integer | External Event ID.
    try {
      ExternalEventEntity result = apiInstance.getExternalEventsId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExternalEventsApi#getExternalEventsId");
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
| **id** | **Integer**| External Event ID. | |

### Return type

[**ExternalEventEntity**](ExternalEventEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The ExternalEvents object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

<a id="postExternalEvents"></a>
# **postExternalEvents**
> ExternalEventEntity postExternalEvents(body, status)

Create External Event

Create External Event

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExternalEventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    ExternalEventsApi apiInstance = new ExternalEventsApi(defaultClient);
    String body = "body_example"; // String | Event body
    String status = "success"; // String | Status of event.
    try {
      ExternalEventEntity result = apiInstance.postExternalEvents(body, status);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExternalEventsApi#postExternalEvents");
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
| **body** | **String**| Event body | |
| **status** | **String**| Status of event. | [enum: success, failure, partial_failure, in_progress, skipped] |

### Return type

[**ExternalEventEntity**](ExternalEventEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ExternalEvents object. |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |
| **405** | Method Not Allowed |  -  |
| **409** | Conflict |  -  |
| **412** | Precondition Failed |  -  |
| **422** | Unprocessable Entity |  -  |
| **423** | Locked |  -  |
| **429** | Too Many Requests |  -  |

