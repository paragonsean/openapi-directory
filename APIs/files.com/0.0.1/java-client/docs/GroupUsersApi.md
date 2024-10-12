# GroupUsersApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteGroupUsersId**](GroupUsersApi.md#deleteGroupUsersId) | **DELETE** /group_users/{id} | Delete Group User |
| [**getGroupUsers**](GroupUsersApi.md#getGroupUsers) | **GET** /group_users | List Group Users |
| [**patchGroupUsersId**](GroupUsersApi.md#patchGroupUsersId) | **PATCH** /group_users/{id} | Update Group User |
| [**postGroupUsers**](GroupUsersApi.md#postGroupUsers) | **POST** /group_users | Create Group User |


<a id="deleteGroupUsersId"></a>
# **deleteGroupUsersId**
> deleteGroupUsersId(id, groupId, userId)

Delete Group User

Delete Group User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    GroupUsersApi apiInstance = new GroupUsersApi(defaultClient);
    Integer id = 56; // Integer | Group User ID.
    Integer groupId = 56; // Integer | Group ID from which to remove user.
    Integer userId = 56; // Integer | User ID to remove from group.
    try {
      apiInstance.deleteGroupUsersId(id, groupId, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupUsersApi#deleteGroupUsersId");
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
| **id** | **Integer**| Group User ID. | |
| **groupId** | **Integer**| Group ID from which to remove user. | |
| **userId** | **Integer**| User ID to remove from group. | |

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

<a id="getGroupUsers"></a>
# **getGroupUsers**
> List&lt;GroupUserEntity&gt; getGroupUsers(userId, cursor, perPage, groupId)

List Group Users

List Group Users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    GroupUsersApi apiInstance = new GroupUsersApi(defaultClient);
    Integer userId = 56; // Integer | User ID.  If provided, will return group_users of this user.
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Integer groupId = 56; // Integer | Group ID.  If provided, will return group_users of this group.
    try {
      List<GroupUserEntity> result = apiInstance.getGroupUsers(userId, cursor, perPage, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupUsersApi#getGroupUsers");
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
| **userId** | **Integer**| User ID.  If provided, will return group_users of this user. | [optional] |
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |
| **groupId** | **Integer**| Group ID.  If provided, will return group_users of this group. | [optional] |

### Return type

[**List&lt;GroupUserEntity&gt;**](GroupUserEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of GroupUsers objects. |  -  |
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

<a id="patchGroupUsersId"></a>
# **patchGroupUsersId**
> GroupUserEntity patchGroupUsersId(id, groupId, userId, admin)

Update Group User

Update Group User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    GroupUsersApi apiInstance = new GroupUsersApi(defaultClient);
    Integer id = 56; // Integer | Group User ID.
    Integer groupId = 56; // Integer | Group ID to add user to.
    Integer userId = 56; // Integer | User ID to add to group.
    Boolean admin = true; // Boolean | Is the user a group administrator?
    try {
      GroupUserEntity result = apiInstance.patchGroupUsersId(id, groupId, userId, admin);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupUsersApi#patchGroupUsersId");
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
| **id** | **Integer**| Group User ID. | |
| **groupId** | **Integer**| Group ID to add user to. | |
| **userId** | **Integer**| User ID to add to group. | |
| **admin** | **Boolean**| Is the user a group administrator? | [optional] |

### Return type

[**GroupUserEntity**](GroupUserEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The GroupUsers object. |  -  |
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

<a id="postGroupUsers"></a>
# **postGroupUsers**
> GroupUserEntity postGroupUsers(groupId, userId, admin)

Create Group User

Create Group User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupUsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    GroupUsersApi apiInstance = new GroupUsersApi(defaultClient);
    Integer groupId = 56; // Integer | Group ID to add user to.
    Integer userId = 56; // Integer | User ID to add to group.
    Boolean admin = true; // Boolean | Is the user a group administrator?
    try {
      GroupUserEntity result = apiInstance.postGroupUsers(groupId, userId, admin);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupUsersApi#postGroupUsers");
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
| **groupId** | **Integer**| Group ID to add user to. | |
| **userId** | **Integer**| User ID to add to group. | |
| **admin** | **Boolean**| Is the user a group administrator? | [optional] |

### Return type

[**GroupUserEntity**](GroupUserEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The GroupUsers object. |  -  |
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

