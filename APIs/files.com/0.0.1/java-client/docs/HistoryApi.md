# HistoryApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**historyList**](HistoryApi.md#historyList) | **GET** /history | List site full action history. |
| [**historyListForFile**](HistoryApi.md#historyListForFile) | **GET** /history/files/{path} | List history for specific file. |
| [**historyListForFolder**](HistoryApi.md#historyListForFolder) | **GET** /history/folders/{path} | List history for specific folder. |
| [**historyListForUser**](HistoryApi.md#historyListForUser) | **GET** /history/users/{user_id} | List history for specific user. |
| [**historyListLogins**](HistoryApi.md#historyListLogins) | **GET** /history/login | List site login history. |


<a id="historyList"></a>
# **historyList**
> List&lt;ActionEntity&gt; historyList(startAt, endAt, display, cursor, perPage, sortBy, filter, filterPrefix)

List site full action history.

List site full action history.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    HistoryApi apiInstance = new HistoryApi(defaultClient);
    OffsetDateTime startAt = OffsetDateTime.now(); // OffsetDateTime | Leave blank or set to a date/time to filter earlier entries.
    OffsetDateTime endAt = OffsetDateTime.now(); // OffsetDateTime | Leave blank or set to a date/time to filter later entries.
    String display = "display_example"; // String | Display format. Leave blank or set to `full` or `parent`.
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Object sortBy = null; // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[path]=desc`). Valid fields are `path`, `folder`, `user_id` or `created_at`.
    Object filter = null; // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `user_id`, `folder` or `path`.
    Object filterPrefix = null; // Object | If set, return records where the specified field is prefixed by the supplied value. Valid fields are `path`.
    try {
      List<ActionEntity> result = apiInstance.historyList(startAt, endAt, display, cursor, perPage, sortBy, filter, filterPrefix);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoryApi#historyList");
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
| **startAt** | **OffsetDateTime**| Leave blank or set to a date/time to filter earlier entries. | [optional] |
| **endAt** | **OffsetDateTime**| Leave blank or set to a date/time to filter later entries. | [optional] |
| **display** | **String**| Display format. Leave blank or set to &#x60;full&#x60; or &#x60;parent&#x60;. | [optional] |
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |
| **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[path]&#x3D;desc&#x60;). Valid fields are &#x60;path&#x60;, &#x60;folder&#x60;, &#x60;user_id&#x60; or &#x60;created_at&#x60;. | [optional] |
| **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;user_id&#x60;, &#x60;folder&#x60; or &#x60;path&#x60;. | [optional] |
| **filterPrefix** | [**Object**](.md)| If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;path&#x60;. | [optional] |

### Return type

[**List&lt;ActionEntity&gt;**](ActionEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of History objects. |  -  |
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

<a id="historyListForFile"></a>
# **historyListForFile**
> List&lt;ActionEntity&gt; historyListForFile(path, startAt, endAt, display, cursor, perPage, sortBy)

List history for specific file.

List history for specific file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    HistoryApi apiInstance = new HistoryApi(defaultClient);
    String path = "path_example"; // String | Path to operate on.
    OffsetDateTime startAt = OffsetDateTime.now(); // OffsetDateTime | Leave blank or set to a date/time to filter earlier entries.
    OffsetDateTime endAt = OffsetDateTime.now(); // OffsetDateTime | Leave blank or set to a date/time to filter later entries.
    String display = "display_example"; // String | Display format. Leave blank or set to `full` or `parent`.
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Object sortBy = null; // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[user_id]=desc`). Valid fields are `user_id` and `created_at`.
    try {
      List<ActionEntity> result = apiInstance.historyListForFile(path, startAt, endAt, display, cursor, perPage, sortBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoryApi#historyListForFile");
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
| **path** | **String**| Path to operate on. | |
| **startAt** | **OffsetDateTime**| Leave blank or set to a date/time to filter earlier entries. | [optional] |
| **endAt** | **OffsetDateTime**| Leave blank or set to a date/time to filter later entries. | [optional] |
| **display** | **String**| Display format. Leave blank or set to &#x60;full&#x60; or &#x60;parent&#x60;. | [optional] |
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |
| **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[user_id]&#x3D;desc&#x60;). Valid fields are &#x60;user_id&#x60; and &#x60;created_at&#x60;. | [optional] |

### Return type

[**List&lt;ActionEntity&gt;**](ActionEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of History objects. |  -  |
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

<a id="historyListForFolder"></a>
# **historyListForFolder**
> List&lt;ActionEntity&gt; historyListForFolder(path, startAt, endAt, display, cursor, perPage, sortBy)

List history for specific folder.

List history for specific folder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    HistoryApi apiInstance = new HistoryApi(defaultClient);
    String path = "path_example"; // String | Path to operate on.
    OffsetDateTime startAt = OffsetDateTime.now(); // OffsetDateTime | Leave blank or set to a date/time to filter earlier entries.
    OffsetDateTime endAt = OffsetDateTime.now(); // OffsetDateTime | Leave blank or set to a date/time to filter later entries.
    String display = "display_example"; // String | Display format. Leave blank or set to `full` or `parent`.
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Object sortBy = null; // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[user_id]=desc`). Valid fields are `user_id` and `created_at`.
    try {
      List<ActionEntity> result = apiInstance.historyListForFolder(path, startAt, endAt, display, cursor, perPage, sortBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoryApi#historyListForFolder");
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
| **path** | **String**| Path to operate on. | |
| **startAt** | **OffsetDateTime**| Leave blank or set to a date/time to filter earlier entries. | [optional] |
| **endAt** | **OffsetDateTime**| Leave blank or set to a date/time to filter later entries. | [optional] |
| **display** | **String**| Display format. Leave blank or set to &#x60;full&#x60; or &#x60;parent&#x60;. | [optional] |
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |
| **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[user_id]&#x3D;desc&#x60;). Valid fields are &#x60;user_id&#x60; and &#x60;created_at&#x60;. | [optional] |

### Return type

[**List&lt;ActionEntity&gt;**](ActionEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of History objects. |  -  |
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

<a id="historyListForUser"></a>
# **historyListForUser**
> List&lt;ActionEntity&gt; historyListForUser(userId, startAt, endAt, display, cursor, perPage, sortBy)

List history for specific user.

List history for specific user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    HistoryApi apiInstance = new HistoryApi(defaultClient);
    Integer userId = 56; // Integer | User ID.
    OffsetDateTime startAt = OffsetDateTime.now(); // OffsetDateTime | Leave blank or set to a date/time to filter earlier entries.
    OffsetDateTime endAt = OffsetDateTime.now(); // OffsetDateTime | Leave blank or set to a date/time to filter later entries.
    String display = "display_example"; // String | Display format. Leave blank or set to `full` or `parent`.
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Object sortBy = null; // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[user_id]=desc`). Valid fields are `user_id` and `created_at`.
    try {
      List<ActionEntity> result = apiInstance.historyListForUser(userId, startAt, endAt, display, cursor, perPage, sortBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoryApi#historyListForUser");
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
| **userId** | **Integer**| User ID. | |
| **startAt** | **OffsetDateTime**| Leave blank or set to a date/time to filter earlier entries. | [optional] |
| **endAt** | **OffsetDateTime**| Leave blank or set to a date/time to filter later entries. | [optional] |
| **display** | **String**| Display format. Leave blank or set to &#x60;full&#x60; or &#x60;parent&#x60;. | [optional] |
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |
| **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[user_id]&#x3D;desc&#x60;). Valid fields are &#x60;user_id&#x60; and &#x60;created_at&#x60;. | [optional] |

### Return type

[**List&lt;ActionEntity&gt;**](ActionEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of History objects. |  -  |
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

<a id="historyListLogins"></a>
# **historyListLogins**
> List&lt;ActionEntity&gt; historyListLogins(startAt, endAt, display, cursor, perPage, sortBy)

List site login history.

List site login history.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HistoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    HistoryApi apiInstance = new HistoryApi(defaultClient);
    OffsetDateTime startAt = OffsetDateTime.now(); // OffsetDateTime | Leave blank or set to a date/time to filter earlier entries.
    OffsetDateTime endAt = OffsetDateTime.now(); // OffsetDateTime | Leave blank or set to a date/time to filter later entries.
    String display = "display_example"; // String | Display format. Leave blank or set to `full` or `parent`.
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Object sortBy = null; // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[user_id]=desc`). Valid fields are `user_id` and `created_at`.
    try {
      List<ActionEntity> result = apiInstance.historyListLogins(startAt, endAt, display, cursor, perPage, sortBy);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HistoryApi#historyListLogins");
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
| **startAt** | **OffsetDateTime**| Leave blank or set to a date/time to filter earlier entries. | [optional] |
| **endAt** | **OffsetDateTime**| Leave blank or set to a date/time to filter later entries. | [optional] |
| **display** | **String**| Display format. Leave blank or set to &#x60;full&#x60; or &#x60;parent&#x60;. | [optional] |
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |
| **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[user_id]&#x3D;desc&#x60;). Valid fields are &#x60;user_id&#x60; and &#x60;created_at&#x60;. | [optional] |

### Return type

[**List&lt;ActionEntity&gt;**](ActionEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of History objects. |  -  |
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

