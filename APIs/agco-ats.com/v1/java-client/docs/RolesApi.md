# RolesApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**rolesDeleteRole**](RolesApi.md#rolesDeleteRole) | **DELETE** /api/v2/Roles/{id} | Deletes a User Role |
| [**rolesGetRole**](RolesApi.md#rolesGetRole) | **GET** /api/v2/Roles/{id} | Gets a User Role |
| [**rolesGetRolePermissions**](RolesApi.md#rolesGetRolePermissions) | **GET** /api/v2/Roles/{id}/Permissions | Get the Permissions for a Role |
| [**rolesGetRoles**](RolesApi.md#rolesGetRoles) | **GET** /api/v2/Roles | List Roles |
| [**rolesPostRole**](RolesApi.md#rolesPostRole) | **POST** /api/v2/Roles | Adds a User Role |
| [**rolesPutRole**](RolesApi.md#rolesPutRole) | **PUT** /api/v2/Roles/{id} | Updates a User Role |
| [**rolesPutRolePermissions**](RolesApi.md#rolesPutRolePermissions) | **PUT** /api/v2/Roles/{id}/Permissions | Manage the Permissions for a Role |


<a id="rolesDeleteRole"></a>
# **rolesDeleteRole**
> rolesDeleteRole(id)

Deletes a User Role

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    RolesApi apiInstance = new RolesApi(defaultClient);
    Integer id = 56; // Integer | The role's id
    try {
      apiInstance.rolesDeleteRole(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#rolesDeleteRole");
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
| **id** | **Integer**| The role&#39;s id | |

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
| **204** | No Content |  -  |

<a id="rolesGetRole"></a>
# **rolesGetRole**
> APIModelsRole rolesGetRole(id)

Gets a User Role

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    RolesApi apiInstance = new RolesApi(defaultClient);
    Integer id = 56; // Integer | The role's id
    try {
      APIModelsRole result = apiInstance.rolesGetRole(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#rolesGetRole");
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
| **id** | **Integer**| The role&#39;s id | |

### Return type

[**APIModelsRole**](APIModelsRole.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="rolesGetRolePermissions"></a>
# **rolesGetRolePermissions**
> APIPagedResponseAPIModelsPermission rolesGetRolePermissions(id, name, limit, offset)

Get the Permissions for a Role

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    RolesApi apiInstance = new RolesApi(defaultClient);
    Integer id = 56; // Integer | The id of the Role
    String name = "name_example"; // String | Filter by permission name. Optional.
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    try {
      APIPagedResponseAPIModelsPermission result = apiInstance.rolesGetRolePermissions(id, name, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#rolesGetRolePermissions");
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
| **id** | **Integer**| The id of the Role | |
| **name** | **String**| Filter by permission name. Optional. | [optional] |
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |

### Return type

[**APIPagedResponseAPIModelsPermission**](APIPagedResponseAPIModelsPermission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="rolesGetRoles"></a>
# **rolesGetRoles**
> APIPagedResponseAPIModelsRole rolesGetRoles(limit, offset, name, permissionID, permissionName)

List Roles

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    RolesApi apiInstance = new RolesApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    String name = "name_example"; // String | Optional. Finds a role with the given name.
    Integer permissionID = 56; // Integer | 
    String permissionName = "permissionName_example"; // String | Optional. Filters roles by whether they contain the provided permission.
    try {
      APIPagedResponseAPIModelsRole result = apiInstance.rolesGetRoles(limit, offset, name, permissionID, permissionName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#rolesGetRoles");
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
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |
| **name** | **String**| Optional. Finds a role with the given name. | [optional] |
| **permissionID** | **Integer**|  | [optional] |
| **permissionName** | **String**| Optional. Filters roles by whether they contain the provided permission. | [optional] |

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

<a id="rolesPostRole"></a>
# **rolesPostRole**
> Integer rolesPostRole(apIModelsRole)

Adds a User Role

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    RolesApi apiInstance = new RolesApi(defaultClient);
    APIModelsRole apIModelsRole = new APIModelsRole(); // APIModelsRole | Role to add
    try {
      Integer result = apiInstance.rolesPostRole(apIModelsRole);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#rolesPostRole");
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
| **apIModelsRole** | [**APIModelsRole**](APIModelsRole.md)| Role to add | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="rolesPutRole"></a>
# **rolesPutRole**
> rolesPutRole(id, apIModelsRole)

Updates a User Role

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    RolesApi apiInstance = new RolesApi(defaultClient);
    Integer id = 56; // Integer | The role's id
    APIModelsRole apIModelsRole = new APIModelsRole(); // APIModelsRole | The Updated Role
    try {
      apiInstance.rolesPutRole(id, apIModelsRole);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#rolesPutRole");
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
| **id** | **Integer**| The role&#39;s id | |
| **apIModelsRole** | [**APIModelsRole**](APIModelsRole.md)| The Updated Role | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="rolesPutRolePermissions"></a>
# **rolesPutRolePermissions**
> rolesPutRolePermissions(id, apIModelsRolePermissionChange)

Manage the Permissions for a Role

No Documentation Found.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://secure.agco-ats.com");

    RolesApi apiInstance = new RolesApi(defaultClient);
    Integer id = 56; // Integer | The id of the Role
    List<APIModelsRolePermissionChange> apIModelsRolePermissionChange = Arrays.asList(); // List<APIModelsRolePermissionChange> | Permissions Changes for the Role
    try {
      apiInstance.rolesPutRolePermissions(id, apIModelsRolePermissionChange);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#rolesPutRolePermissions");
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
| **id** | **Integer**| The id of the Role | |
| **apIModelsRolePermissionChange** | [**List&lt;APIModelsRolePermissionChange&gt;**](APIModelsRolePermissionChange.md)| Permissions Changes for the Role | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

