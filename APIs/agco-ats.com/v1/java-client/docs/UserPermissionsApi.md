# UserPermissionsApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV2RolesIdUsersPut**](UserPermissionsApi.md#apiV2RolesIdUsersPut) | **PUT** /api/v2/Roles/{id}/Users | Update a Role&#39;s users |
| [**apiV2UsersCurrentPermissionsGet**](UserPermissionsApi.md#apiV2UsersCurrentPermissionsGet) | **GET** /api/v2/Users/Current/Permissions | Get a user&#39;s permissions |
| [**userPermissionsGetCurrentUserRoles**](UserPermissionsApi.md#userPermissionsGetCurrentUserRoles) | **GET** /api/v2/Users/Current/Roles | Gets the current user&#39;s roles |
| [**userPermissionsGetPermissions**](UserPermissionsApi.md#userPermissionsGetPermissions) | **GET** /api/v2/Users/{id}/Permissions | Get a user&#39;s permissions |
| [**userPermissionsGetRoles**](UserPermissionsApi.md#userPermissionsGetRoles) | **GET** /api/v2/Users/{id}/Roles | Get a user&#39;s roles |
| [**userPermissionsGetUsers**](UserPermissionsApi.md#userPermissionsGetUsers) | **GET** /api/v2/Roles/{id}/Users | Get all user&#39;s in a role |
| [**userPermissionsPut**](UserPermissionsApi.md#userPermissionsPut) | **PUT** /api/v2/Users/{id}/Roles | Update a user&#39;s roles |


<a id="apiV2RolesIdUsersPut"></a>
# **apiV2RolesIdUsersPut**
> apiV2RolesIdUsersPut(id, apIModelsRoleUserChange)

Update a Role&#39;s users

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserPermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UserPermissionsApi apiInstance = new UserPermissionsApi(defaultClient);
    Integer id = 56; // Integer | The Role's ID
    List<APIModelsRoleUserChange> apIModelsRoleUserChange = Arrays.asList(); // List<APIModelsRoleUserChange> | A list of changes to the Role's Users
    try {
      apiInstance.apiV2RolesIdUsersPut(id, apIModelsRoleUserChange);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserPermissionsApi#apiV2RolesIdUsersPut");
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
| **id** | **Integer**| The Role&#39;s ID | |
| **apIModelsRoleUserChange** | [**List&lt;APIModelsRoleUserChange&gt;**](APIModelsRoleUserChange.md)| A list of changes to the Role&#39;s Users | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

<a id="apiV2UsersCurrentPermissionsGet"></a>
# **apiV2UsersCurrentPermissionsGet**
> APIPagedResponseAPIModelsUserEffectivePermission apiV2UsersCurrentPermissionsGet(permission, limit, offset)

Get a user&#39;s permissions

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserPermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UserPermissionsApi apiInstance = new UserPermissionsApi(defaultClient);
    String permission = "permission_example"; // String | Filter by permission name. Supports ending wildcard (*). Optional.
    Integer limit = 56; // Integer | The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | The page offset. The default page offset is 0.
    try {
      APIPagedResponseAPIModelsUserEffectivePermission result = apiInstance.apiV2UsersCurrentPermissionsGet(permission, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserPermissionsApi#apiV2UsersCurrentPermissionsGet");
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
| **permission** | **String**| Filter by permission name. Supports ending wildcard (*). Optional. | [optional] |
| **limit** | **Integer**| The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIPagedResponseAPIModelsUserEffectivePermission**](APIPagedResponseAPIModelsUserEffectivePermission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="userPermissionsGetCurrentUserRoles"></a>
# **userPermissionsGetCurrentUserRoles**
> APIPagedResponseAPIModelsRole userPermissionsGetCurrentUserRoles(role, limit, offset)

Gets the current user&#39;s roles

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserPermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UserPermissionsApi apiInstance = new UserPermissionsApi(defaultClient);
    String role = "role_example"; // String | Filter by role name. Supports ending wildcard (*). Optional.
    Integer limit = 56; // Integer | The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | The page offset. The default page offset is 0.
    try {
      APIPagedResponseAPIModelsRole result = apiInstance.userPermissionsGetCurrentUserRoles(role, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserPermissionsApi#userPermissionsGetCurrentUserRoles");
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
| **role** | **String**| Filter by role name. Supports ending wildcard (*). Optional. | [optional] |
| **limit** | **Integer**| The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIPagedResponseAPIModelsRole**](APIPagedResponseAPIModelsRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="userPermissionsGetPermissions"></a>
# **userPermissionsGetPermissions**
> APIPagedResponseAPIModelsUserEffectivePermission userPermissionsGetPermissions(id, permission, limit, offset)

Get a user&#39;s permissions

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserPermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UserPermissionsApi apiInstance = new UserPermissionsApi(defaultClient);
    Integer id = 56; // Integer | The User's ID
    String permission = "permission_example"; // String | Filter by permission name. Supports ending wildcard (*). Optional.
    Integer limit = 56; // Integer | The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | The page offset. The default page offset is 0.
    try {
      APIPagedResponseAPIModelsUserEffectivePermission result = apiInstance.userPermissionsGetPermissions(id, permission, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserPermissionsApi#userPermissionsGetPermissions");
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
| **id** | **Integer**| The User&#39;s ID | |
| **permission** | **String**| Filter by permission name. Supports ending wildcard (*). Optional. | [optional] |
| **limit** | **Integer**| The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIPagedResponseAPIModelsUserEffectivePermission**](APIPagedResponseAPIModelsUserEffectivePermission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="userPermissionsGetRoles"></a>
# **userPermissionsGetRoles**
> APIPagedResponseAPIModelsRole userPermissionsGetRoles(id, role, limit, offset)

Get a user&#39;s roles

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserPermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UserPermissionsApi apiInstance = new UserPermissionsApi(defaultClient);
    Integer id = 56; // Integer | The User's ID
    String role = "role_example"; // String | Filter by role name. Supports ending wildcard (*). Optional.
    Integer limit = 56; // Integer | The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | The page offset. The default page offset is 0.
    try {
      APIPagedResponseAPIModelsRole result = apiInstance.userPermissionsGetRoles(id, role, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserPermissionsApi#userPermissionsGetRoles");
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
| **id** | **Integer**| The User&#39;s ID | |
| **role** | **String**| Filter by role name. Supports ending wildcard (*). Optional. | [optional] |
| **limit** | **Integer**| The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIPagedResponseAPIModelsRole**](APIPagedResponseAPIModelsRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="userPermissionsGetUsers"></a>
# **userPermissionsGetUsers**
> APIPagedResponseAPIModelsUser userPermissionsGetUsers(id, limit, offset)

Get all user&#39;s in a role

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserPermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UserPermissionsApi apiInstance = new UserPermissionsApi(defaultClient);
    Integer id = 56; // Integer | The Role's ID
    Integer limit = 56; // Integer | The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | The page offset. The default page offset is 0.
    try {
      APIPagedResponseAPIModelsUser result = apiInstance.userPermissionsGetUsers(id, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserPermissionsApi#userPermissionsGetUsers");
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
| **id** | **Integer**| The Role&#39;s ID | |
| **limit** | **Integer**| The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIPagedResponseAPIModelsUser**](APIPagedResponseAPIModelsUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | API Error Response |  -  |

<a id="userPermissionsPut"></a>
# **userPermissionsPut**
> userPermissionsPut(id, apIModelsUserRoleChange)

Update a user&#39;s roles

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserPermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UserPermissionsApi apiInstance = new UserPermissionsApi(defaultClient);
    Integer id = 56; // Integer | The User's ID
    List<APIModelsUserRoleChange> apIModelsUserRoleChange = Arrays.asList(); // List<APIModelsUserRoleChange> | A list of changes to the User's Roles
    try {
      apiInstance.userPermissionsPut(id, apIModelsUserRoleChange);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserPermissionsApi#userPermissionsPut");
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
| **id** | **Integer**| The User&#39;s ID | |
| **apIModelsUserRoleChange** | [**List&lt;APIModelsUserRoleChange&gt;**](APIModelsUserRoleChange.md)| A list of changes to the User&#39;s Roles | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |
| **0** | API Error Response |  -  |

