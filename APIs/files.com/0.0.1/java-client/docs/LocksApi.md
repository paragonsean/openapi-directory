# LocksApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteLocksPath**](LocksApi.md#deleteLocksPath) | **DELETE** /locks/{path} | Delete Lock |
| [**lockListForPath**](LocksApi.md#lockListForPath) | **GET** /locks/{path} | List Locks by path |
| [**postLocksPath**](LocksApi.md#postLocksPath) | **POST** /locks/{path} | Create Lock |


<a id="deleteLocksPath"></a>
# **deleteLocksPath**
> deleteLocksPath(path, token)

Delete Lock

Delete Lock

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    LocksApi apiInstance = new LocksApi(defaultClient);
    String path = "path_example"; // String | Path
    String token = "token_example"; // String | Lock token
    try {
      apiInstance.deleteLocksPath(path, token);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocksApi#deleteLocksPath");
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
| **path** | **String**| Path | |
| **token** | **String**| Lock token | |

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

<a id="lockListForPath"></a>
# **lockListForPath**
> List&lt;LockEntity&gt; lockListForPath(path, cursor, perPage, includeChildren)

List Locks by path

List Locks by path

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    LocksApi apiInstance = new LocksApi(defaultClient);
    String path = "path_example"; // String | Path to operate on.
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Boolean includeChildren = true; // Boolean | Include locks from children objects?
    try {
      List<LockEntity> result = apiInstance.lockListForPath(path, cursor, perPage, includeChildren);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocksApi#lockListForPath");
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
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |
| **includeChildren** | **Boolean**| Include locks from children objects? | [optional] |

### Return type

[**List&lt;LockEntity&gt;**](LockEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Locks objects. |  -  |
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

<a id="postLocksPath"></a>
# **postLocksPath**
> LockEntity postLocksPath(path, allowAccessByAnyUser, exclusive, recursive, timeout)

Create Lock

Create Lock

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LocksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    LocksApi apiInstance = new LocksApi(defaultClient);
    String path = "path_example"; // String | Path
    Boolean allowAccessByAnyUser = true; // Boolean | Allow lock to be updated by any user?
    Boolean exclusive = true; // Boolean | Is lock exclusive?
    String recursive = "recursive_example"; // String | Does lock apply to subfolders?
    Integer timeout = 56; // Integer | Lock timeout length
    try {
      LockEntity result = apiInstance.postLocksPath(path, allowAccessByAnyUser, exclusive, recursive, timeout);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LocksApi#postLocksPath");
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
| **path** | **String**| Path | |
| **allowAccessByAnyUser** | **Boolean**| Allow lock to be updated by any user? | [optional] |
| **exclusive** | **Boolean**| Is lock exclusive? | [optional] |
| **recursive** | **String**| Does lock apply to subfolders? | [optional] |
| **timeout** | **Integer**| Lock timeout length | [optional] |

### Return type

[**LockEntity**](LockEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The Locks object. |  -  |
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

