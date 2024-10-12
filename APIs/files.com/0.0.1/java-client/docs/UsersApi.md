# UsersApi

All URIs are relative to *http://app.files.com/api/rest/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteUsersId**](UsersApi.md#deleteUsersId) | **DELETE** /users/{id} | Delete User |
| [**getUsers**](UsersApi.md#getUsers) | **GET** /users | List Users |
| [**getUsersId**](UsersApi.md#getUsersId) | **GET** /users/{id} | Show User |
| [**getUsersUserIdApiKeys**](UsersApi.md#getUsersUserIdApiKeys) | **GET** /users/{user_id}/api_keys | List Api Keys |
| [**getUsersUserIdCipherUses**](UsersApi.md#getUsersUserIdCipherUses) | **GET** /users/{user_id}/cipher_uses | List User Cipher Uses |
| [**getUsersUserIdGroups**](UsersApi.md#getUsersUserIdGroups) | **GET** /users/{user_id}/groups | List Group Users |
| [**getUsersUserIdPermissions**](UsersApi.md#getUsersUserIdPermissions) | **GET** /users/{user_id}/permissions | List Permissions |
| [**getUsersUserIdPublicKeys**](UsersApi.md#getUsersUserIdPublicKeys) | **GET** /users/{user_id}/public_keys | List Public Keys |
| [**patchUsersId**](UsersApi.md#patchUsersId) | **PATCH** /users/{id} | Update User |
| [**postUsers**](UsersApi.md#postUsers) | **POST** /users | Create User |
| [**postUsersId2faReset**](UsersApi.md#postUsersId2faReset) | **POST** /users/{id}/2fa/reset | Trigger 2FA Reset process for user who has lost access to their existing 2FA methods. |
| [**postUsersIdResendWelcomeEmail**](UsersApi.md#postUsersIdResendWelcomeEmail) | **POST** /users/{id}/resend_welcome_email | Resend user welcome email |
| [**postUsersIdUnlock**](UsersApi.md#postUsersIdUnlock) | **POST** /users/{id}/unlock | Unlock user who has been locked out due to failed logins. |
| [**postUsersUserIdApiKeys**](UsersApi.md#postUsersUserIdApiKeys) | **POST** /users/{user_id}/api_keys | Create Api Key |
| [**postUsersUserIdPublicKeys**](UsersApi.md#postUsersUserIdPublicKeys) | **POST** /users/{user_id}/public_keys | Create Public Key |


<a id="deleteUsersId"></a>
# **deleteUsersId**
> deleteUsersId(id)

Delete User

Delete User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | User ID.
    try {
      apiInstance.deleteUsersId(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#deleteUsersId");
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
| **id** | **Integer**| User ID. | |

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

<a id="getUsers"></a>
# **getUsers**
> List&lt;UserEntity&gt; getUsers(cursor, perPage, sortBy, filter, filterGt, filterGteq, filterPrefix, filterLt, filterLteq, ids, qUsername, qEmail, qNotes, qAdmin, qAllowedIps, qPasswordValidityDays, qSslRequired, search)

List Users

List Users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Object sortBy = null; // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[authenticate_until]=desc`). Valid fields are `authenticate_until`, `active`, `email`, `last_desktop_login_at`, `last_login_at`, `username`, `company`, `name`, `site_admin`, `receive_admin_alerts`, `password_validity_days`, `ssl_required` or `not_site_admin`.
    Object filter = null; // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `username`, `email`, `company`, `site_admin`, `password_validity_days`, `ssl_required`, `last_login_at`, `authenticate_until` or `not_site_admin`. Valid field combinations are `[ not_site_admin, username ]`.
    Object filterGt = null; // Object | If set, return records where the specified field is greater than the supplied value. Valid fields are `password_validity_days`, `last_login_at` or `authenticate_until`.
    Object filterGteq = null; // Object | If set, return records where the specified field is greater than or equal the supplied value. Valid fields are `password_validity_days`, `last_login_at` or `authenticate_until`.
    Object filterPrefix = null; // Object | If set, return records where the specified field is prefixed by the supplied value. Valid fields are `username`, `email` or `company`.
    Object filterLt = null; // Object | If set, return records where the specified field is less than the supplied value. Valid fields are `password_validity_days`, `last_login_at` or `authenticate_until`.
    Object filterLteq = null; // Object | If set, return records where the specified field is less than or equal the supplied value. Valid fields are `password_validity_days`, `last_login_at` or `authenticate_until`.
    String ids = "ids_example"; // String | comma-separated list of User IDs
    String qUsername = "qUsername_example"; // String | List users matching username.
    String qEmail = "qEmail_example"; // String | List users matching email.
    String qNotes = "qNotes_example"; // String | List users matching notes field.
    String qAdmin = "qAdmin_example"; // String | If `true`, list only admin users.
    String qAllowedIps = "qAllowedIps_example"; // String | If set, list only users with overridden allowed IP setting.
    String qPasswordValidityDays = "qPasswordValidityDays_example"; // String | If set, list only users with overridden password validity days setting.
    String qSslRequired = "qSslRequired_example"; // String | If set, list only users with overridden SSL required setting.
    String search = "search_example"; // String | Searches for partial matches of name, username, or email.
    try {
      List<UserEntity> result = apiInstance.getUsers(cursor, perPage, sortBy, filter, filterGt, filterGteq, filterPrefix, filterLt, filterLteq, ids, qUsername, qEmail, qNotes, qAdmin, qAllowedIps, qPasswordValidityDays, qSslRequired, search);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUsers");
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
| **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[authenticate_until]&#x3D;desc&#x60;). Valid fields are &#x60;authenticate_until&#x60;, &#x60;active&#x60;, &#x60;email&#x60;, &#x60;last_desktop_login_at&#x60;, &#x60;last_login_at&#x60;, &#x60;username&#x60;, &#x60;company&#x60;, &#x60;name&#x60;, &#x60;site_admin&#x60;, &#x60;receive_admin_alerts&#x60;, &#x60;password_validity_days&#x60;, &#x60;ssl_required&#x60; or &#x60;not_site_admin&#x60;. | [optional] |
| **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;username&#x60;, &#x60;email&#x60;, &#x60;company&#x60;, &#x60;site_admin&#x60;, &#x60;password_validity_days&#x60;, &#x60;ssl_required&#x60;, &#x60;last_login_at&#x60;, &#x60;authenticate_until&#x60; or &#x60;not_site_admin&#x60;. Valid field combinations are &#x60;[ not_site_admin, username ]&#x60;. | [optional] |
| **filterGt** | [**Object**](.md)| If set, return records where the specified field is greater than the supplied value. Valid fields are &#x60;password_validity_days&#x60;, &#x60;last_login_at&#x60; or &#x60;authenticate_until&#x60;. | [optional] |
| **filterGteq** | [**Object**](.md)| If set, return records where the specified field is greater than or equal the supplied value. Valid fields are &#x60;password_validity_days&#x60;, &#x60;last_login_at&#x60; or &#x60;authenticate_until&#x60;. | [optional] |
| **filterPrefix** | [**Object**](.md)| If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;username&#x60;, &#x60;email&#x60; or &#x60;company&#x60;. | [optional] |
| **filterLt** | [**Object**](.md)| If set, return records where the specified field is less than the supplied value. Valid fields are &#x60;password_validity_days&#x60;, &#x60;last_login_at&#x60; or &#x60;authenticate_until&#x60;. | [optional] |
| **filterLteq** | [**Object**](.md)| If set, return records where the specified field is less than or equal the supplied value. Valid fields are &#x60;password_validity_days&#x60;, &#x60;last_login_at&#x60; or &#x60;authenticate_until&#x60;. | [optional] |
| **ids** | **String**| comma-separated list of User IDs | [optional] |
| **qUsername** | **String**| List users matching username. | [optional] |
| **qEmail** | **String**| List users matching email. | [optional] |
| **qNotes** | **String**| List users matching notes field. | [optional] |
| **qAdmin** | **String**| If &#x60;true&#x60;, list only admin users. | [optional] |
| **qAllowedIps** | **String**| If set, list only users with overridden allowed IP setting. | [optional] |
| **qPasswordValidityDays** | **String**| If set, list only users with overridden password validity days setting. | [optional] |
| **qSslRequired** | **String**| If set, list only users with overridden SSL required setting. | [optional] |
| **search** | **String**| Searches for partial matches of name, username, or email. | [optional] |

### Return type

[**List&lt;UserEntity&gt;**](UserEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Users objects. |  -  |
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

<a id="getUsersId"></a>
# **getUsersId**
> UserEntity getUsersId(id)

Show User

Show User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | User ID.
    try {
      UserEntity result = apiInstance.getUsersId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUsersId");
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
| **id** | **Integer**| User ID. | |

### Return type

[**UserEntity**](UserEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The Users object. |  -  |
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

<a id="getUsersUserIdApiKeys"></a>
# **getUsersUserIdApiKeys**
> List&lt;ApiKeyEntity&gt; getUsersUserIdApiKeys(userId, cursor, perPage, sortBy, filter, filterGt, filterGteq, filterLt, filterLteq)

List Api Keys

List Api Keys

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
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
      List<ApiKeyEntity> result = apiInstance.getUsersUserIdApiKeys(userId, cursor, perPage, sortBy, filter, filterGt, filterGteq, filterLt, filterLteq);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUsersUserIdApiKeys");
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
| **userId** | **Integer**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | |
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

<a id="getUsersUserIdCipherUses"></a>
# **getUsersUserIdCipherUses**
> List&lt;UserCipherUseEntity&gt; getUsersUserIdCipherUses(userId, cursor, perPage)

List User Cipher Uses

List User Cipher Uses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer userId = 56; // Integer | User ID.  Provide a value of `0` to operate the current session's user.
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    try {
      List<UserCipherUseEntity> result = apiInstance.getUsersUserIdCipherUses(userId, cursor, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUsersUserIdCipherUses");
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
| **userId** | **Integer**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | |
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |

### Return type

[**List&lt;UserCipherUseEntity&gt;**](UserCipherUseEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of UserCipherUses objects. |  -  |
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

<a id="getUsersUserIdGroups"></a>
# **getUsersUserIdGroups**
> List&lt;GroupUserEntity&gt; getUsersUserIdGroups(userId, cursor, perPage, groupId)

List Group Users

List Group Users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer userId = 56; // Integer | User ID.  If provided, will return group_users of this user.
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Integer groupId = 56; // Integer | Group ID.  If provided, will return group_users of this group.
    try {
      List<GroupUserEntity> result = apiInstance.getUsersUserIdGroups(userId, cursor, perPage, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUsersUserIdGroups");
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
| **userId** | **Integer**| User ID.  If provided, will return group_users of this user. | |
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

<a id="getUsersUserIdPermissions"></a>
# **getUsersUserIdPermissions**
> List&lt;PermissionEntity&gt; getUsersUserIdPermissions(userId, cursor, perPage, sortBy, filter, filterPrefix, path, groupId, includeGroups)

List Permissions

List Permissions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | DEPRECATED: User ID.  If provided, will scope permissions to this user. Use `filter[user_id]` instead.`
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    Object sortBy = null; // Object | If set, sort records by the specified field in either `asc` or `desc` direction (e.g. `sort_by[group_id]=desc`). Valid fields are `group_id`, `path`, `user_id` or `permission`.
    Object filter = null; // Object | If set, return records where the specified field is equal to the supplied value. Valid fields are `group_id`, `user_id` or `path`. Valid field combinations are `[ group_id, path ]` and `[ user_id, path ]`.
    Object filterPrefix = null; // Object | If set, return records where the specified field is prefixed by the supplied value. Valid fields are `path`.
    String path = "path_example"; // String | DEPRECATED: Permission path.  If provided, will scope permissions to this path. Use `filter[path]` instead.
    String groupId = "groupId_example"; // String | DEPRECATED: Group ID.  If provided, will scope permissions to this group. Use `filter[group_id]` instead.`
    Boolean includeGroups = true; // Boolean | If searching by user or group, also include user's permissions that are inherited from its groups?
    try {
      List<PermissionEntity> result = apiInstance.getUsersUserIdPermissions(userId, cursor, perPage, sortBy, filter, filterPrefix, path, groupId, includeGroups);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUsersUserIdPermissions");
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
| **userId** | **String**| DEPRECATED: User ID.  If provided, will scope permissions to this user. Use &#x60;filter[user_id]&#x60; instead.&#x60; | |
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |
| **sortBy** | [**Object**](.md)| If set, sort records by the specified field in either &#x60;asc&#x60; or &#x60;desc&#x60; direction (e.g. &#x60;sort_by[group_id]&#x3D;desc&#x60;). Valid fields are &#x60;group_id&#x60;, &#x60;path&#x60;, &#x60;user_id&#x60; or &#x60;permission&#x60;. | [optional] |
| **filter** | [**Object**](.md)| If set, return records where the specified field is equal to the supplied value. Valid fields are &#x60;group_id&#x60;, &#x60;user_id&#x60; or &#x60;path&#x60;. Valid field combinations are &#x60;[ group_id, path ]&#x60; and &#x60;[ user_id, path ]&#x60;. | [optional] |
| **filterPrefix** | [**Object**](.md)| If set, return records where the specified field is prefixed by the supplied value. Valid fields are &#x60;path&#x60;. | [optional] |
| **path** | **String**| DEPRECATED: Permission path.  If provided, will scope permissions to this path. Use &#x60;filter[path]&#x60; instead. | [optional] |
| **groupId** | **String**| DEPRECATED: Group ID.  If provided, will scope permissions to this group. Use &#x60;filter[group_id]&#x60; instead.&#x60; | [optional] |
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

<a id="getUsersUserIdPublicKeys"></a>
# **getUsersUserIdPublicKeys**
> List&lt;PublicKeyEntity&gt; getUsersUserIdPublicKeys(userId, cursor, perPage)

List Public Keys

List Public Keys

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer userId = 56; // Integer | User ID.  Provide a value of `0` to operate the current session's user.
    String cursor = "cursor_example"; // String | Used for pagination.  When a list request has more records available, cursors are provided in the response headers `X-Files-Cursor-Next` and `X-Files-Cursor-Prev`.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination.
    Integer perPage = 56; // Integer | Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended).
    try {
      List<PublicKeyEntity> result = apiInstance.getUsersUserIdPublicKeys(userId, cursor, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUsersUserIdPublicKeys");
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
| **userId** | **Integer**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | |
| **cursor** | **String**| Used for pagination.  When a list request has more records available, cursors are provided in the response headers &#x60;X-Files-Cursor-Next&#x60; and &#x60;X-Files-Cursor-Prev&#x60;.  Send one of those cursor value here to resume an existing list from the next available record.  Note: many of our SDKs have iterator methods that will automatically handle cursor-based pagination. | [optional] |
| **perPage** | **Integer**| Number of records to show per page.  (Max: 10,000, 1,000 or less is recommended). | [optional] |

### Return type

[**List&lt;PublicKeyEntity&gt;**](PublicKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of PublicKeys objects. |  -  |
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

<a id="patchUsersId"></a>
# **patchUsersId**
> UserEntity patchUsersId(id, allowedIps, announcementsRead, attachmentsPermission, authenticateUntil, authenticationMethod, avatarDelete, avatarFile, billingPermission, bypassInactiveDisable, bypassSiteAllowedIps, changePassword, changePasswordConfirmation, company, davPermission, disabled, email, ftpPermission, grantPermission, groupId, groupIds, headerText, importedPasswordHash, language, name, notes, notificationDailySendTime, officeIntegrationEnabled, password, passwordConfirmation, passwordValidityDays, receiveAdminAlerts, require2fa, requirePasswordChange, restapiPermission, selfManaged, sftpPermission, siteAdmin, skipWelcomeScreen, sslRequired, ssoStrategyId, subscribeToNewsletter, timeZone, userRoot, username)

Update User

Update User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | User ID.
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
    Integer groupId = 56; // Integer | Group ID to associate this user with.
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
      UserEntity result = apiInstance.patchUsersId(id, allowedIps, announcementsRead, attachmentsPermission, authenticateUntil, authenticationMethod, avatarDelete, avatarFile, billingPermission, bypassInactiveDisable, bypassSiteAllowedIps, changePassword, changePasswordConfirmation, company, davPermission, disabled, email, ftpPermission, grantPermission, groupId, groupIds, headerText, importedPasswordHash, language, name, notes, notificationDailySendTime, officeIntegrationEnabled, password, passwordConfirmation, passwordValidityDays, receiveAdminAlerts, require2fa, requirePasswordChange, restapiPermission, selfManaged, sftpPermission, siteAdmin, skipWelcomeScreen, sslRequired, ssoStrategyId, subscribeToNewsletter, timeZone, userRoot, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#patchUsersId");
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
| **id** | **Integer**| User ID. | |
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
| **groupId** | **Integer**| Group ID to associate this user with. | [optional] |
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
| **200** | The Users object. |  -  |
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

<a id="postUsers"></a>
# **postUsers**
> UserEntity postUsers(allowedIps, announcementsRead, attachmentsPermission, authenticateUntil, authenticationMethod, avatarDelete, avatarFile, billingPermission, bypassInactiveDisable, bypassSiteAllowedIps, changePassword, changePasswordConfirmation, company, davPermission, disabled, email, ftpPermission, grantPermission, groupId, groupIds, headerText, importedPasswordHash, language, name, notes, notificationDailySendTime, officeIntegrationEnabled, password, passwordConfirmation, passwordValidityDays, receiveAdminAlerts, require2fa, requirePasswordChange, restapiPermission, selfManaged, sftpPermission, siteAdmin, skipWelcomeScreen, sslRequired, ssoStrategyId, subscribeToNewsletter, timeZone, userRoot, username)

Create User

Create User

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
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
    Integer groupId = 56; // Integer | Group ID to associate this user with.
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
      UserEntity result = apiInstance.postUsers(allowedIps, announcementsRead, attachmentsPermission, authenticateUntil, authenticationMethod, avatarDelete, avatarFile, billingPermission, bypassInactiveDisable, bypassSiteAllowedIps, changePassword, changePasswordConfirmation, company, davPermission, disabled, email, ftpPermission, grantPermission, groupId, groupIds, headerText, importedPasswordHash, language, name, notes, notificationDailySendTime, officeIntegrationEnabled, password, passwordConfirmation, passwordValidityDays, receiveAdminAlerts, require2fa, requirePasswordChange, restapiPermission, selfManaged, sftpPermission, siteAdmin, skipWelcomeScreen, sslRequired, ssoStrategyId, subscribeToNewsletter, timeZone, userRoot, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#postUsers");
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
| **groupId** | **Integer**| Group ID to associate this user with. | [optional] |
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

<a id="postUsersId2faReset"></a>
# **postUsersId2faReset**
> postUsersId2faReset(id)

Trigger 2FA Reset process for user who has lost access to their existing 2FA methods.

Trigger 2FA Reset process for user who has lost access to their existing 2FA methods.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | User ID.
    try {
      apiInstance.postUsersId2faReset(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#postUsersId2faReset");
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
| **id** | **Integer**| User ID. | |

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

<a id="postUsersIdResendWelcomeEmail"></a>
# **postUsersIdResendWelcomeEmail**
> postUsersIdResendWelcomeEmail(id)

Resend user welcome email

Resend user welcome email

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | User ID.
    try {
      apiInstance.postUsersIdResendWelcomeEmail(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#postUsersIdResendWelcomeEmail");
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
| **id** | **Integer**| User ID. | |

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

<a id="postUsersIdUnlock"></a>
# **postUsersIdUnlock**
> postUsersIdUnlock(id)

Unlock user who has been locked out due to failed logins.

Unlock user who has been locked out due to failed logins.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | User ID.
    try {
      apiInstance.postUsersIdUnlock(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#postUsersIdUnlock");
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
| **id** | **Integer**| User ID. | |

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

<a id="postUsersUserIdApiKeys"></a>
# **postUsersUserIdApiKeys**
> ApiKeyEntity postUsersUserIdApiKeys(userId, description, expiresAt, name, path, permissionSet)

Create Api Key

Create Api Key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer userId = 56; // Integer | User ID.  Provide a value of `0` to operate the current session's user.
    String description = "description_example"; // String | User-supplied description of API key.
    OffsetDateTime expiresAt = OffsetDateTime.now(); // OffsetDateTime | API Key expiration date
    String name = "name_example"; // String | Internal name for the API Key.  For your use.
    String path = "path_example"; // String | Folder path restriction for this api key.
    String permissionSet = "none"; // String | Permissions for this API Key.  Keys with the `desktop_app` permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know.
    try {
      ApiKeyEntity result = apiInstance.postUsersUserIdApiKeys(userId, description, expiresAt, name, path, permissionSet);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#postUsersUserIdApiKeys");
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
| **userId** | **Integer**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | |
| **description** | **String**| User-supplied description of API key. | [optional] |
| **expiresAt** | **OffsetDateTime**| API Key expiration date | [optional] |
| **name** | **String**| Internal name for the API Key.  For your use. | [optional] |
| **path** | **String**| Folder path restriction for this api key. | [optional] |
| **permissionSet** | **String**| Permissions for this API Key.  Keys with the &#x60;desktop_app&#x60; permission set only have the ability to do the functions provided in our Desktop App (File and Share Link operations).  Additional permission sets may become available in the future, such as for a Site Admin to give a key with no administrator privileges.  If you have ideas for permission sets, please let us know. | [optional] [default to full] [enum: none, full, desktop_app, sync_app, office_integration, mobile_app] |

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

<a id="postUsersUserIdPublicKeys"></a>
# **postUsersUserIdPublicKeys**
> PublicKeyEntity postUsersUserIdPublicKeys(userId, publicKey, title)

Create Public Key

Create Public Key

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://app.files.com/api/rest/v1");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer userId = 56; // Integer | User ID.  Provide a value of `0` to operate the current session's user.
    String publicKey = "publicKey_example"; // String | Actual contents of SSH key.
    String title = "title_example"; // String | Internal reference for key.
    try {
      PublicKeyEntity result = apiInstance.postUsersUserIdPublicKeys(userId, publicKey, title);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#postUsersUserIdPublicKeys");
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
| **userId** | **Integer**| User ID.  Provide a value of &#x60;0&#x60; to operate the current session&#39;s user. | |
| **publicKey** | **String**| Actual contents of SSH key. | |
| **title** | **String**| Internal reference for key. | |

### Return type

[**PublicKeyEntity**](PublicKeyEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The PublicKeys object. |  -  |
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

