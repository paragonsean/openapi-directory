# GroupsApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteGroupsGroupIdMembershipsUserId**](GroupsApi.md#deleteGroupsGroupIdMembershipsUserId) | **DELETE** /groups/{group_id}/memberships/{user_id} | Delete Group User |
| [**deleteGroupsId**](GroupsApi.md#deleteGroupsId) | **DELETE** /groups/{id} | Delete Group |
| [**getGroups**](GroupsApi.md#getGroups) | **GET** /groups | List Groups |
| [**getGroupsGroupIdPermissions**](GroupsApi.md#getGroupsGroupIdPermissions) | **GET** /groups/{group_id}/permissions | List Permissions |
| [**getGroupsGroupIdUsers**](GroupsApi.md#getGroupsGroupIdUsers) | **GET** /groups/{group_id}/users | List Group Users |
| [**getGroupsId**](GroupsApi.md#getGroupsId) | **GET** /groups/{id} | Show Group |
| [**patchGroupsGroupIdMembershipsUserId**](GroupsApi.md#patchGroupsGroupIdMembershipsUserId) | **PATCH** /groups/{group_id}/memberships/{user_id} | Update Group User |
| [**patchGroupsId**](GroupsApi.md#patchGroupsId) | **PATCH** /groups/{id} | Update Group |
| [**postGroups**](GroupsApi.md#postGroups) | **POST** /groups | Create Group |
| [**postGroupsGroupIdUsers**](GroupsApi.md#postGroupsGroupIdUsers) | **POST** /groups/{group_id}/users | Create User |


<a id="deleteGroupsGroupIdMembershipsUserId"></a>
# **deleteGroupsGroupIdMembershipsUserId**
> deleteGroupsGroupIdMembershipsUserId(groupId, userId)

Delete Group User

Delete Group User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Integer groupId = 56; // Integer | Group ID from which to remove user.
    Integer userId = 56; // Integer | User ID to remove from group.
    try {
      apiInstance.deleteGroupsGroupIdMembershipsUserId(groupId, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#deleteGroupsGroupIdMembershipsUserId");
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

<a id="deleteGroupsId"></a>
# **deleteGroupsId**
> deleteGroupsId(id)

Delete Group

Delete Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Integer id = 56; // Integer | Group ID.
    try {
      apiInstance.deleteGroupsId(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#deleteGroupsId");
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
| **id** | **Integer**| Group ID. | |

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

<a id="getGroups"></a>
# **getGroups**
> List&lt;GroupEntity&gt; getGroups(cursor, perPage, sortBy, filter, filterPrefix, ids)

List Groups

List Groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Object sortBy = null; // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[name]=desc`). Valid fields are `name`.
    Object filter = null; // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `name`.
    Object filterPrefix = null; // Object | If set, return records where the specified field is prefixed by the supplied value. Valid fields are `name`.
    String ids = "ids_example"; // String | Comma-separated list of group ids to include in results.
    try {
      List<GroupEntity> result = apiInstance.getGroups(cursor, perPage, sortBy, filter, filterPrefix, ids);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#getGroups");
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
| **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[name]&#x3D;desc&#x60;). Valid fields are &#x60;name&#x60;. | [optional] |
| **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;name&#x60;. | [optional] |
| **filterPrefix** | [**Object**](.md)| If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;name&#x60;. | [optional] |
| **ids** | **String**| Comma-separated list of group ids to include in results. | [optional] |

### Return type

[**List&lt;GroupEntity&gt;**](GroupEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Groups objects. |  -  |
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

<a id="getGroupsGroupIdPermissions"></a>
# **getGroupsGroupIdPermissions**
> List&lt;PermissionEntity&gt; getGroupsGroupIdPermissions(groupId, cursor, perPage, sortBy, filter, filterPrefix, path, userId, includeGroups)

List Permissions

List Permissions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String groupId = "groupId_example"; // String | DEPRECATED: Group ID.  If provided, will scope permissions to this group. Use `filter[group_id]` instead.`
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Object sortBy = null; // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[group_id]=desc`). Valid fields are `group_id`, `path`, `user_id` or `permission`.
    Object filter = null; // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `group_id`, `user_id` or `path`. Valid field combinations are `[ group_id, path ]` and `[ user_id, path ]`.
    Object filterPrefix = null; // Object | If set, return records where the specified field is prefixed by the supplied value. Valid fields are `path`.
    String path = "path_example"; // String | DEPRECATED: Permission path.  If provided, will scope permissions to this path. Use `filter[path]` instead.
    String userId = "userId_example"; // String | DEPRECATED: User ID.  If provided, will scope permissions to this user. Use `filter[user_id]` instead.`
    Boolean includeGroups = true; // Boolean | If searching by user or group, also include user's permissions that are inherited from its groups?
    try {
      List<PermissionEntity> result = apiInstance.getGroupsGroupIdPermissions(groupId, cursor, perPage, sortBy, filter, filterPrefix, path, userId, includeGroups);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#getGroupsGroupIdPermissions");
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
| **groupId** | **String**| DEPRECATED: Group ID.  If provided, will scope permissions to this group. Use &#x60;filter[group_id]&#x60; instead.&#x60; | |
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |
| **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[group_id]&#x3D;desc&#x60;). Valid fields are &#x60;group_id&#x60;, &#x60;path&#x60;, &#x60;user_id&#x60; or &#x60;permission&#x60;. | [optional] |
| **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;group_id&#x60;, &#x60;user_id&#x60; or &#x60;path&#x60;. Valid field combinations are &#x60;[ group_id, path ]&#x60; and &#x60;[ user_id, path ]&#x60;. | [optional] |
| **filterPrefix** | [**Object**](.md)| If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;path&#x60;. | [optional] |
| **path** | **String**| DEPRECATED: Permission path.  If provided, will scope permissions to this path. Use &#x60;filter[path]&#x60; instead. | [optional] |
| **userId** | **String**| DEPRECATED: User ID.  If provided, will scope permissions to this user. Use &#x60;filter[user_id]&#x60; instead.&#x60; | [optional] |
| **includeGroups** | **Boolean**| If searching by user or group, also include user&#39;s permissions that are inherited from its groups? | [optional] |

### Return type

[**List&lt;PermissionEntity&gt;**](PermissionEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Permissions objects. |  -  |
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

<a id="getGroupsGroupIdUsers"></a>
# **getGroupsGroupIdUsers**
> List&lt;GroupUserEntity&gt; getGroupsGroupIdUsers(groupId, userId, cursor, perPage)

List Group Users

List Group Users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Integer groupId = 56; // Integer | Group ID.  If provided, will return group_users of this group.
    Integer userId = 56; // Integer | User ID.  If provided, will return group_users of this user.
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    try {
      List<GroupUserEntity> result = apiInstance.getGroupsGroupIdUsers(groupId, userId, cursor, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#getGroupsGroupIdUsers");
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
| **groupId** | **Integer**| Group ID.  If provided, will return group_users of this group. | |
| **userId** | **Integer**| User ID.  If provided, will return group_users of this user. | [optional] |
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |

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

<a id="getGroupsId"></a>
# **getGroupsId**
> GroupEntity getGroupsId(id)

Show Group

Show Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Integer id = 56; // Integer | Group ID.
    try {
      GroupEntity result = apiInstance.getGroupsId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#getGroupsId");
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
| **id** | **Integer**| Group ID. | |

### Return type

[**GroupEntity**](GroupEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Groups object. |  -  |
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

<a id="patchGroupsGroupIdMembershipsUserId"></a>
# **patchGroupsGroupIdMembershipsUserId**
> GroupUserEntity patchGroupsGroupIdMembershipsUserId(groupId, userId, admin)

Update Group User

Update Group User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Integer groupId = 56; // Integer | Group ID to add user to.
    Integer userId = 56; // Integer | User ID to add to group.
    Boolean admin = true; // Boolean | Is the user a group administrator?
    try {
      GroupUserEntity result = apiInstance.patchGroupsGroupIdMembershipsUserId(groupId, userId, admin);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#patchGroupsGroupIdMembershipsUserId");
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

<a id="patchGroupsId"></a>
# **patchGroupsId**
> GroupEntity patchGroupsId(id, adminIds, name, notes, userIds)

Update Group

Update Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Integer id = 56; // Integer | Group ID.
    String adminIds = "adminIds_example"; // String | A list of group admin user ids. If sent as a string, should be comma-delimited.
    String name = "name_example"; // String | Group name.
    String notes = "notes_example"; // String | Group notes.
    String userIds = "userIds_example"; // String | A list of user ids. If sent as a string, should be comma-delimited.
    try {
      GroupEntity result = apiInstance.patchGroupsId(id, adminIds, name, notes, userIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#patchGroupsId");
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
| **id** | **Integer**| Group ID. | |
| **adminIds** | **String**| A list of group admin user ids. If sent as a string, should be comma-delimited. | [optional] |
| **name** | **String**| Group name. | [optional] |
| **notes** | **String**| Group notes. | [optional] |
| **userIds** | **String**| A list of user ids. If sent as a string, should be comma-delimited. | [optional] |

### Return type

[**GroupEntity**](GroupEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Groups object. |  -  |
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

<a id="postGroups"></a>
# **postGroups**
> GroupEntity postGroups(adminIds, name, notes, userIds)

Create Group

Create Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    String adminIds = "adminIds_example"; // String | A list of group admin user ids. If sent as a string, should be comma-delimited.
    String name = "name_example"; // String | Group name.
    String notes = "notes_example"; // String | Group notes.
    String userIds = "userIds_example"; // String | A list of user ids. If sent as a string, should be comma-delimited.
    try {
      GroupEntity result = apiInstance.postGroups(adminIds, name, notes, userIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#postGroups");
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
| **adminIds** | **String**| A list of group admin user ids. If sent as a string, should be comma-delimited. | [optional] |
| **name** | **String**| Group name. | [optional] |
| **notes** | **String**| Group notes. | [optional] |
| **userIds** | **String**| A list of user ids. If sent as a string, should be comma-delimited. | [optional] |

### Return type

[**GroupEntity**](GroupEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The Groups object. |  -  |
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

<a id="postGroupsGroupIdUsers"></a>
# **postGroupsGroupIdUsers**
> UserEntity postGroupsGroupIdUsers(groupId, allowedIps, announcementsRead, attachmentsPermission, authenticateUntil, authenticationMethod, avatarDelete, avatarFile, billingPermission, bypassInactiveDisable, bypassSiteAllowedIps, changePassword, changePasswordConfirmation, company, davPermission, disabled, email, ftpPermission, grantPermission, groupIds, headerText, importedPasswordHash, language, name, notes, notificationDailySendTime, officeIntegrationEnabled, password, passwordConfirmation, passwordValidityDays, receiveAdminAlerts, require2fa, requirePasswordChange, restapiPermission, selfManaged, sftpPermission, siteAdmin, skipWelcomeScreen, sslRequired, ssoStrategyId, subscribeToNewsletter, timeZone, userRoot, username)

Create User

Create User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GroupsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    GroupsApi apiInstance = new GroupsApi(defaultClient);
    Integer groupId = 56; // Integer | Group ID to associate this user with.
    String allowedIps = "allowedIps_example"; // String | A list of allowed IPs if applicable.  Newline delimited
    Boolean announcementsRead = true; // Boolean | Signifies that the user has read all the announcements in the UI.
    Boolean attachmentsPermission = true; // Boolean | DEPRECATED: Can the user create Bundles (aka Share Links)? Use the bundle permission instead.
    OffsetDateTime authenticateUntil = OffsetDateTime.now(); // OffsetDateTime | Scheduled Date/Time at which user will be deactivated
    String authenticationMethod = "password"; // String | How is this user authenticated?
    Boolean avatarDelete = true; // Boolean | If true, the avatar will be deleted.
    File avatarFile = new File("/path/to/file"); // File | An image file for your user avatar.
    Boolean billingPermission = true; // Boolean | Allow this user to perform operations on the account, payments, and invoices?
    Boolean bypassInactiveDisable = true; // Boolean | Exempt this user from being disabled based on inactivity?
    Boolean bypassSiteAllowedIps = true; // Boolean | Allow this user to skip site-wide IP blacklists?
    String changePassword = "changePassword_example"; // String | Used for changing a password on an existing user.
    String changePasswordConfirmation = "changePasswordConfirmation_example"; // String | Optional, but if provided, we will ensure that it matches the value sent in `change_password`.
    String company = "company_example"; // String | User's company
    Boolean davPermission = true; // Boolean | Can the user connect with WebDAV?
    Boolean disabled = true; // Boolean | Is user disabled? Disabled users cannot log in, and do not count for billing purposes.  Users can be automatically disabled after an inactivity period via a Site setting.
    String email = "email_example"; // String | User's email.
    Boolean ftpPermission = true; // Boolean | Can the user access with FTP/FTPS?
    String grantPermission = "grantPermission_example"; // String | Permission to grant on the user root.  Can be blank or `full`, `read`, `write`, `list`, `read+write`, or `list+write`
    String groupIds = "groupIds_example"; // String | A list of group ids to associate this user with.  Comma delimited.
    String headerText = "headerText_example"; // String | Text to display to the user in the header of the UI
    String importedPasswordHash = "importedPasswordHash_example"; // String | Pre-calculated hash of the user's password. If supplied, this will be used to authenticate the user on first login. Supported hash menthods are MD5, SHA1, and SHA256.
    String language = "language_example"; // String | Preferred language
    String name = "name_example"; // String | User's full name
    String notes = "notes_example"; // String | Any internal notes on the user
    Integer notificationDailySendTime = 56; // Integer | Hour of the day at which daily notifications should be sent. Can be in range 0 to 23
    Boolean officeIntegrationEnabled = true; // Boolean | Enable integration with Office for the web?
    String password = "password_example"; // String | User password.
    String passwordConfirmation = "passwordConfirmation_example"; // String | Optional, but if provided, we will ensure that it matches the value sent in `password`.
    Integer passwordValidityDays = 56; // Integer | Number of days to allow user to use the same password
    Boolean receiveAdminAlerts = true; // Boolean | Should the user receive admin alerts such a certificate expiration notifications and overages?
    String require2fa = "use_system_setting"; // String | 2FA required setting
    Boolean requirePasswordChange = true; // Boolean | Is a password change required upon next user login?
    Boolean restapiPermission = true; // Boolean | Can this user access the REST API?
    Boolean selfManaged = true; // Boolean | Does this user manage it's own credentials or is it a shared/bot user?
    Boolean sftpPermission = true; // Boolean | Can the user access with SFTP?
    Boolean siteAdmin = true; // Boolean | Is the user an administrator for this site?
    Boolean skipWelcomeScreen = true; // Boolean | Skip Welcome page in the UI?
    String sslRequired = "use_system_setting"; // String | SSL required setting
    Integer ssoStrategyId = 56; // Integer | SSO (Single Sign On) strategy ID for the user, if applicable.
    Boolean subscribeToNewsletter = true; // Boolean | Is the user subscribed to the newsletter?
    String timeZone = "timeZone_example"; // String | User time zone
    String userRoot = "userRoot_example"; // String | Root folder for FTP (and optionally SFTP if the appropriate site-wide setting is set.)  Note that this is not used for API, Desktop, or Web interface.
    String username = "username_example"; // String | User's username
    try {
      UserEntity result = apiInstance.postGroupsGroupIdUsers(groupId, allowedIps, announcementsRead, attachmentsPermission, authenticateUntil, authenticationMethod, avatarDelete, avatarFile, billingPermission, bypassInactiveDisable, bypassSiteAllowedIps, changePassword, changePasswordConfirmation, company, davPermission, disabled, email, ftpPermission, grantPermission, groupIds, headerText, importedPasswordHash, language, name, notes, notificationDailySendTime, officeIntegrationEnabled, password, passwordConfirmation, passwordValidityDays, receiveAdminAlerts, require2fa, requirePasswordChange, restapiPermission, selfManaged, sftpPermission, siteAdmin, skipWelcomeScreen, sslRequired, ssoStrategyId, subscribeToNewsletter, timeZone, userRoot, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GroupsApi#postGroupsGroupIdUsers");
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
| **groupId** | **Integer**| Group ID to associate this user with. | |
| **allowedIps** | **String**| A list of allowed IPs if applicable.  Newline delimited | [optional] |
| **announcementsRead** | **Boolean**| Signifies that the user has read all the announcements in the UI. | [optional] |
| **attachmentsPermission** | **Boolean**| DEPRECATED: Can the user create Bundles (aka Share Links)? Use the bundle permission instead. | [optional] |
| **authenticateUntil** | **OffsetDateTime**| Scheduled Date/Time at which user will be deactivated | [optional] |
| **authenticationMethod** | **String**| How is this user authenticated? | [optional] [enum: password, unused_former_ldap, sso, none, email_signup, password_with_imported_hash] |
| **avatarDelete** | **Boolean**| If true, the avatar will be deleted. | [optional] |
| **avatarFile** | **File**| An image file for your user avatar. | [optional] |
| **billingPermission** | **Boolean**| Allow this user to perform operations on the account, payments, and invoices? | [optional] |
| **bypassInactiveDisable** | **Boolean**| Exempt this user from being disabled based on inactivity? | [optional] |
| **bypassSiteAllowedIps** | **Boolean**| Allow this user to skip site-wide IP blacklists? | [optional] |
| **changePassword** | **String**| Used for changing a password on an existing user. | [optional] |
| **changePasswordConfirmation** | **String**| Optional, but if provided, we will ensure that it matches the value sent in &#x60;change_password&#x60;. | [optional] |
| **company** | **String**| User&#39;s company | [optional] |
| **davPermission** | **Boolean**| Can the user connect with WebDAV? | [optional] |
| **disabled** | **Boolean**| Is user disabled? Disabled users cannot log in, and do not count for billing purposes.  Users can be automatically disabled after an inactivity period via a Site setting. | [optional] |
| **email** | **String**| User&#39;s email. | [optional] |
| **ftpPermission** | **Boolean**| Can the user access with FTP/FTPS? | [optional] |
| **grantPermission** | **String**| Permission to grant on the user root.  Can be blank or &#x60;full&#x60;, &#x60;read&#x60;, &#x60;write&#x60;, &#x60;list&#x60;, &#x60;read+write&#x60;, or &#x60;list+write&#x60; | [optional] |
| **groupIds** | **String**| A list of group ids to associate this user with.  Comma delimited. | [optional] |
| **headerText** | **String**| Text to display to the user in the header of the UI | [optional] |
| **importedPasswordHash** | **String**| Pre-calculated hash of the user&#39;s password. If supplied, this will be used to authenticate the user on first login. Supported hash menthods are MD5, SHA1, and SHA256. | [optional] |
| **language** | **String**| Preferred language | [optional] |
| **name** | **String**| User&#39;s full name | [optional] |
| **notes** | **String**| Any internal notes on the user | [optional] |
| **notificationDailySendTime** | **Integer**| Hour of the day at which daily notifications should be sent. Can be in range 0 to 23 | [optional] |
| **officeIntegrationEnabled** | **Boolean**| Enable integration with Office for the web? | [optional] |
| **password** | **String**| User password. | [optional] |
| **passwordConfirmation** | **String**| Optional, but if provided, we will ensure that it matches the value sent in &#x60;password&#x60;. | [optional] |
| **passwordValidityDays** | **Integer**| Number of days to allow user to use the same password | [optional] |
| **receiveAdminAlerts** | **Boolean**| Should the user receive admin alerts such a certificate expiration notifications and overages? | [optional] |
| **require2fa** | **String**| 2FA required setting | [optional] [enum: use_system_setting, always_require, never_require] |
| **requirePasswordChange** | **Boolean**| Is a password change required upon next user login? | [optional] |
| **restapiPermission** | **Boolean**| Can this user access the REST API? | [optional] |
| **selfManaged** | **Boolean**| Does this user manage it&#39;s own credentials or is it a shared/bot user? | [optional] |
| **sftpPermission** | **Boolean**| Can the user access with SFTP? | [optional] |
| **siteAdmin** | **Boolean**| Is the user an administrator for this site? | [optional] |
| **skipWelcomeScreen** | **Boolean**| Skip Welcome page in the UI? | [optional] |
| **sslRequired** | **String**| SSL required setting | [optional] [enum: use_system_setting, always_require, never_require] |
| **ssoStrategyId** | **Integer**| SSO (Single Sign On) strategy ID for the user, if applicable. | [optional] |
| **subscribeToNewsletter** | **Boolean**| Is the user subscribed to the newsletter? | [optional] |
| **timeZone** | **String**| User time zone | [optional] |
| **userRoot** | **String**| Root folder for FTP (and optionally SFTP if the appropriate site-wide setting is set.)  Note that this is not used for API, Desktop, or Web interface. | [optional] |
| **username** | **String**| User&#39;s username | [optional] |

### Return type

[**UserEntity**](UserEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The Users object. |  -  |
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

