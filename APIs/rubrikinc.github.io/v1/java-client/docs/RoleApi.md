# RoleApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createRole**](RoleApi.md#createRole) | **POST** /role | Create a new role |
| [**deleteRole**](RoleApi.md#deleteRole) | **DELETE** /role/{id} | Delete a role |
| [**getRole**](RoleApi.md#getRole) | **GET** /role/{id} | Get role information for the specified role |
| [**getRoles**](RoleApi.md#getRoles) | **GET** /role | Get all roles in an organization |
| [**updateRole**](RoleApi.md#updateRole) | **PATCH** /role/{id} | Update role information |


<a id="createRole"></a>
# **createRole**
> RoleInfo createRole(roleInfoCreate)

Create a new role

Create a new role in the current organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    RoleApi apiInstance = new RoleApi(defaultClient);
    RoleInfoCreate roleInfoCreate = new RoleInfoCreate(); // RoleInfoCreate | Information about the role.
    try {
      RoleInfo result = apiInstance.createRole(roleInfoCreate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleApi#createRole");
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
| **roleInfoCreate** | [**RoleInfoCreate**](RoleInfoCreate.md)| Information about the role. | |

### Return type

[**RoleInfo**](RoleInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about the newly created role. |  -  |

<a id="deleteRole"></a>
# **deleteRole**
> deleteRole(id)

Delete a role

Delete the role with the specified ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    RoleApi apiInstance = new RoleApi(defaultClient);
    String id = "id_example"; // String | ID of the role.
    try {
      apiInstance.deleteRole(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleApi#deleteRole");
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
| **id** | **String**| ID of the role. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successfully deleted role. |  -  |

<a id="getRole"></a>
# **getRole**
> RoleInfo getRole(id)

Get role information for the specified role

Get role information for the role with the specified ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    RoleApi apiInstance = new RoleApi(defaultClient);
    String id = "id_example"; // String | ID of the role.
    try {
      RoleInfo result = apiInstance.getRole(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleApi#getRole");
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
| **id** | **String**| ID of the role. | |

### Return type

[**RoleInfo**](RoleInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about the role. |  -  |

<a id="getRoles"></a>
# **getRoles**
> RoleInfoListResponse getRoles(limit, offset, sortBy, sortOrder, organizationId, name, roleTemplate)

Get all roles in an organization

Get a list of role information for all roles in the specified organization. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    RoleApi apiInstance = new RoleApi(defaultClient);
    Integer limit = 56; // Integer | Maximum number of results to return.
    Integer offset = 56; // Integer | Starting offset of the results to return.
    String sortBy = "Name"; // String | Attribute used to sort the role list.
    String sortOrder = "asc"; // String | Sort order used, ascending or descending.
    String organizationId = "organizationId_example"; // String | The ID of the organization the roles are a part of. When empty, the Rubrik cluster infers the organization from the session. 
    String name = "name_example"; // String | The name of the role.
    List<String> roleTemplate = Arrays.asList(); // List<String> | List of comma-separated role templates by which to filter the roles. 
    try {
      RoleInfoListResponse result = apiInstance.getRoles(limit, offset, sortBy, sortOrder, organizationId, name, roleTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleApi#getRoles");
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
| **limit** | **Integer**| Maximum number of results to return. | [optional] |
| **offset** | **Integer**| Starting offset of the results to return. | [optional] |
| **sortBy** | **String**| Attribute used to sort the role list. | [optional] [default to Name] [enum: Name, Description, RoleTemplate] |
| **sortOrder** | **String**| Sort order used, ascending or descending. | [optional] [default to asc] [enum: asc, desc] |
| **organizationId** | **String**| The ID of the organization the roles are a part of. When empty, the Rubrik cluster infers the organization from the session.  | [optional] |
| **name** | **String**| The name of the role. | [optional] |
| **roleTemplate** | [**List&lt;String&gt;**](String.md)| List of comma-separated role templates by which to filter the roles.  | [optional] |

### Return type

[**RoleInfoListResponse**](RoleInfoListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about the requested roles. |  -  |

<a id="updateRole"></a>
# **updateRole**
> RoleInfo updateRole(id, roleInfoUpdate)

Update role information

Update the role information for the specified role.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    RoleApi apiInstance = new RoleApi(defaultClient);
    String id = "id_example"; // String | ID of the role.
    RoleInfoUpdate roleInfoUpdate = new RoleInfoUpdate(); // RoleInfoUpdate | Information about the role.
    try {
      RoleInfo result = apiInstance.updateRole(id, roleInfoUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoleApi#updateRole");
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
| **id** | **String**| ID of the role. | |
| **roleInfoUpdate** | [**RoleInfoUpdate**](RoleInfoUpdate.md)| Information about the role. | |

### Return type

[**RoleInfo**](RoleInfo.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Information about the updated role. |  -  |

