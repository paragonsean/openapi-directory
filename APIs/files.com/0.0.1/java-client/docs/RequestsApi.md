# RequestsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteRequestsId**](RequestsApi.md#deleteRequestsId) | **DELETE** /requests/{id} | Delete Request |
| [**getRequests**](RequestsApi.md#getRequests) | **GET** /requests | List Requests |
| [**getRequestsFoldersPath**](RequestsApi.md#getRequestsFoldersPath) | **GET** /requests/folders/{path} | List Requests |
| [**postRequests**](RequestsApi.md#postRequests) | **POST** /requests | Create Request |


<a id="deleteRequestsId"></a>
# **deleteRequestsId**
> deleteRequestsId(id)

Delete Request

Delete Request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    RequestsApi apiInstance = new RequestsApi(defaultClient);
    Integer id = 56; // Integer | Request ID.
    try {
      apiInstance.deleteRequestsId(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestsApi#deleteRequestsId");
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
| **id** | **Integer**| Request ID. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No body. |  -  |
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

<a id="getRequests"></a>
# **getRequests**
> List&lt;RequestEntity&gt; getRequests(cursor, perPage, sortBy, mine, path)

List Requests

List Requests

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    RequestsApi apiInstance = new RequestsApi(defaultClient);
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Object sortBy = null; // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[destination]=desc`). Valid fields are `destination`.
    Boolean mine = true; // Boolean | Only show requests of the current user?  (Defaults to true if current user is not a site admin.)
    String path = "path_example"; // String | Path to show requests for.  If omitted, shows all paths. Send `/` to represent the root directory.
    try {
      List<RequestEntity> result = apiInstance.getRequests(cursor, perPage, sortBy, mine, path);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestsApi#getRequests");
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
| **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[destination]&#x3D;desc&#x60;). Valid fields are &#x60;destination&#x60;. | [optional] |
| **mine** | **Boolean**| Only show requests of the current user?  (Defaults to true if current user is not a site admin.) | [optional] |
| **path** | **String**| Path to show requests for.  If omitted, shows all paths. Send &#x60;/&#x60; to represent the root directory. | [optional] |

### Return type

[**List&lt;RequestEntity&gt;**](RequestEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Requests objects. |  -  |
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

<a id="getRequestsFoldersPath"></a>
# **getRequestsFoldersPath**
> List&lt;RequestEntity&gt; getRequestsFoldersPath(path, cursor, perPage, sortBy, mine)

List Requests

List Requests

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    RequestsApi apiInstance = new RequestsApi(defaultClient);
    String path = "path_example"; // String | Path to show requests for.  If omitted, shows all paths. Send `/` to represent the root directory.
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Object sortBy = null; // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[destination]=desc`). Valid fields are `destination`.
    Boolean mine = true; // Boolean | Only show requests of the current user?  (Defaults to true if current user is not a site admin.)
    try {
      List<RequestEntity> result = apiInstance.getRequestsFoldersPath(path, cursor, perPage, sortBy, mine);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestsApi#getRequestsFoldersPath");
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
| **path** | **String**| Path to show requests for.  If omitted, shows all paths. Send &#x60;/&#x60; to represent the root directory. | |
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |
| **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[destination]&#x3D;desc&#x60;). Valid fields are &#x60;destination&#x60;. | [optional] |
| **mine** | **Boolean**| Only show requests of the current user?  (Defaults to true if current user is not a site admin.) | [optional] |

### Return type

[**List&lt;RequestEntity&gt;**](RequestEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Requests objects. |  -  |
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

<a id="postRequests"></a>
# **postRequests**
> RequestEntity postRequests(destination, path, groupIds, userIds)

Create Request

Create Request

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    RequestsApi apiInstance = new RequestsApi(defaultClient);
    String destination = "destination_example"; // String | Destination filename (without extension) to request.
    String path = "path_example"; // String | Folder path on which to request the file.
    String groupIds = "groupIds_example"; // String | A list of group IDs to request the file from. If sent as a string, it should be comma-delimited.
    String userIds = "userIds_example"; // String | A list of user IDs to request the file from. If sent as a string, it should be comma-delimited.
    try {
      RequestEntity result = apiInstance.postRequests(destination, path, groupIds, userIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestsApi#postRequests");
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
| **destination** | **String**| Destination filename (without extension) to request. | |
| **path** | **String**| Folder path on which to request the file. | |
| **groupIds** | **String**| A list of group IDs to request the file from. If sent as a string, it should be comma-delimited. | [optional] |
| **userIds** | **String**| A list of user IDs to request the file from. If sent as a string, it should be comma-delimited. | [optional] |

### Return type

[**RequestEntity**](RequestEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The Requests object. |  -  |
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

