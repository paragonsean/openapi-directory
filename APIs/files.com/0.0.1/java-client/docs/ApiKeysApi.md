# ApiKeysApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteApiKeysId**](ApiKeysApi.md#deleteApiKeysId) | **DELETE** /api_keys/{id} | Delete Api Key |
| [**getApiKeys**](ApiKeysApi.md#getApiKeys) | **GET** /api_keys | List Api Keys |
| [**getApiKeysId**](ApiKeysApi.md#getApiKeysId) | **GET** /api_keys/{id} | Show Api Key |
| [**patchApiKeysId**](ApiKeysApi.md#patchApiKeysId) | **PATCH** /api_keys/{id} | Update Api Key |
| [**postApiKeys**](ApiKeysApi.md#postApiKeys) | **POST** /api_keys | Create Api Key |


<a id="deleteApiKeysId"></a>
# **deleteApiKeysId**
> deleteApiKeysId(id)

Delete Api Key

Delete Api Key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    ApiKeysApi apiInstance = new ApiKeysApi(defaultClient);
    Integer id = 56; // Integer | Api Key ID.
    try {
      apiInstance.deleteApiKeysId(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiKeysApi#deleteApiKeysId");
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
| **id** | **Integer**| Api Key ID. | |

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

<a id="getApiKeys"></a>
# **getApiKeys**
> List&lt;ApiKeyEntity&gt; getApiKeys(userId, cursor, perPage, sortBy, filter, filterGt, filterGteq, filterLt, filterLteq)

List Api Keys

List Api Keys

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    ApiKeysApi apiInstance = new ApiKeysApi(defaultClient);
    Integer userId = 56; // Integer | User ID.  Provide a value of `0` to operate the current session's user.
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Object sortBy = null; // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[expires_at]=desc`). Valid fields are `expires_at`.
    Object filter = null; // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `expires_at`.
    Object filterGt = null; // Object | If set, return records where the specified field is greater than the supplied value. Valid fields are `expires_at`.
    Object filterGteq = null; // Object | If set, return records where the specified field is greater than or equal the supplied value. Valid fields are `expires_at`.
    Object filterLt = null; // Object | If set, return records where the specified field is less than the supplied value. Valid fields are `expires_at`.
    Object filterLteq = null; // Object | If set, return records where the specified field is less than or equal the supplied value. Valid fields are `expires_at`.
    try {
      List<ApiKeyEntity> result = apiInstance.getApiKeys(userId, cursor, perPage, sortBy, filter, filterGt, filterGteq, filterLt, filterLteq);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiKeysApi#getApiKeys");
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
| **userId** | **Integer**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] |
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |
| **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[expires_at]&#x3D;desc&#x60;). Valid fields are &#x60;expires_at&#x60;. | [optional] |
| **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;expires_at&#x60;. | [optional] |
| **filterGt** | [**Object**](.md)| If set, return records where the specified field is greater than the supplied value. Valid fields are &#x60;expires_at&#x60;. | [optional] |
| **filterGteq** | [**Object**](.md)| If set, return records where the specified field is greater than or equal the supplied value. Valid fields are &#x60;expires_at&#x60;. | [optional] |
| **filterLt** | [**Object**](.md)| If set, return records where the specified field is less than the supplied value. Valid fields are &#x60;expires_at&#x60;. | [optional] |
| **filterLteq** | [**Object**](.md)| If set, return records where the specified field is less than or equal the supplied value. Valid fields are &#x60;expires_at&#x60;. | [optional] |

### Return type

[**List&lt;ApiKeyEntity&gt;**](ApiKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of ApiKeys objects. |  -  |
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

<a id="getApiKeysId"></a>
# **getApiKeysId**
> ApiKeyEntity getApiKeysId(id)

Show Api Key

Show Api Key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    ApiKeysApi apiInstance = new ApiKeysApi(defaultClient);
    Integer id = 56; // Integer | Api Key ID.
    try {
      ApiKeyEntity result = apiInstance.getApiKeysId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiKeysApi#getApiKeysId");
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
| **id** | **Integer**| Api Key ID. | |

### Return type

[**ApiKeyEntity**](ApiKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The ApiKeys object. |  -  |
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

<a id="patchApiKeysId"></a>
# **patchApiKeysId**
> ApiKeyEntity patchApiKeysId(id, description, expiresAt, name, permissionSet)

Update Api Key

Update Api Key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    ApiKeysApi apiInstance = new ApiKeysApi(defaultClient);
    Integer id = 56; // Integer | Api Key ID.
    String description = "description_example"; // String | User-supplied description of API key.
    OffsetDateTime expiresAt = OffsetDateTime.now(); // OffsetDateTime | API Key expiration date
    String name = "name_example"; // String | Internal name for the API Key.  For your use.
    String permissionSet = "none"; // String | Permissions for this API Key.  Keys with the `desktop_app` permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know.
    try {
      ApiKeyEntity result = apiInstance.patchApiKeysId(id, description, expiresAt, name, permissionSet);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiKeysApi#patchApiKeysId");
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
| **id** | **Integer**| Api Key ID. | |
| **description** | **String**| User-supplied description of API key. | [optional] |
| **expiresAt** | **OffsetDateTime**| API Key expiration date | [optional] |
| **name** | **String**| Internal name for the API Key.  For your use. | [optional] |
| **permissionSet** | **String**| Permissions for this API Key.  Keys with the &#x60;desktop_app&#x60; permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know. | [optional] [enum: none, full, desktop_app, sync_app, office_integration, mobile_app] |

### Return type

[**ApiKeyEntity**](ApiKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The ApiKeys object. |  -  |
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

<a id="postApiKeys"></a>
# **postApiKeys**
> ApiKeyEntity postApiKeys(description, expiresAt, name, path, permissionSet, userId)

Create Api Key

Create Api Key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApiKeysApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    ApiKeysApi apiInstance = new ApiKeysApi(defaultClient);
    String description = "description_example"; // String | User-supplied description of API key.
    OffsetDateTime expiresAt = OffsetDateTime.now(); // OffsetDateTime | API Key expiration date
    String name = "name_example"; // String | Internal name for the API Key.  For your use.
    String path = "path_example"; // String | Folder path restriction for this api key.
    String permissionSet = "none"; // String | Permissions for this API Key.  Keys with the `desktop_app` permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know.
    Integer userId = 56; // Integer | User ID.  Provide a value of `0` to operate the current session's user.
    try {
      ApiKeyEntity result = apiInstance.postApiKeys(description, expiresAt, name, path, permissionSet, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApiKeysApi#postApiKeys");
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
| **description** | **String**| User-supplied description of API key. | [optional] |
| **expiresAt** | **OffsetDateTime**| API Key expiration date | [optional] |
| **name** | **String**| Internal name for the API Key.  For your use. | [optional] |
| **path** | **String**| Folder path restriction for this api key. | [optional] |
| **permissionSet** | **String**| Permissions for this API Key.  Keys with the &#x60;desktop_app&#x60; permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know. | [optional] [default to full] [enum: none, full, desktop_app, sync_app, office_integration, mobile_app] |
| **userId** | **Integer**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | [optional] |

### Return type

[**ApiKeyEntity**](ApiKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The ApiKeys object. |  -  |
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

