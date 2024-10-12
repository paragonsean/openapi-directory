# PermissionsApi

All URIs are relative to */story*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**storyIdCollaboratorsUseridPermissiontypeGet**](PermissionsApi.md#storyIdCollaboratorsUseridPermissiontypeGet) | **GET** /{id}/collaborators/authorize/{story_collaborator_userid}/{permissiontype} | Permissions: Story Authorization for a User |
| [**storyPermissionTypesGet**](PermissionsApi.md#storyPermissionTypesGet) | **GET** /permission_types | Permissions: List Permission Types |


<a id="storyIdCollaboratorsUseridPermissiontypeGet"></a>
# **storyIdCollaboratorsUseridPermissiontypeGet**
> storyIdCollaboratorsUseridPermissiontypeGet(id, storyCollaboratorUserid, permissiontype)

Permissions: Story Authorization for a User

Check whether user have certain types of permissions.  Use http status codes to understand if permission is granted - 204 &#x3D; Granted, 403 &#x3D; Forbidden

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    PermissionsApi apiInstance = new PermissionsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | the id from the story object
    UUID storyCollaboratorUserid = UUID.randomUUID(); // UUID | The presalytics userid (NOT the Id of the story_collaborator object)
    String permissiontype = "permissiontype_example"; // String | the type of permission requested.  can be a permission_type object name (e.g., owner, editor, create, viewer, admin) or a permission type field (e.g., can_edit, can_view, can_add_collaborators, can_delete)
    try {
      apiInstance.storyIdCollaboratorsUseridPermissiontypeGet(id, storyCollaboratorUserid, permissiontype);
    } catch (ApiException e) {
      System.err.println("Exception when calling PermissionsApi#storyIdCollaboratorsUseridPermissiontypeGet");
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
| **id** | **UUID**| the id from the story object | |
| **storyCollaboratorUserid** | **UUID**| The presalytics userid (NOT the Id of the story_collaborator object) | |
| **permissiontype** | **String**| the type of permission requested.  can be a permission_type object name (e.g., owner, editor, create, viewer, admin) or a permission type field (e.g., can_edit, can_view, can_add_collaborators, can_delete) | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |

<a id="storyPermissionTypesGet"></a>
# **storyPermissionTypesGet**
> List&lt;PermissionType&gt; storyPermissionTypesGet()

Permissions: List Permission Types

Returns a list of possible user permission types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PermissionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/story");

    PermissionsApi apiInstance = new PermissionsApi(defaultClient);
    try {
      List<PermissionType> result = apiInstance.storyPermissionTypesGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PermissionsApi#storyPermissionTypesGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List&lt;PermissionType&gt;**](PermissionType.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Array of all possible permission types |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |

