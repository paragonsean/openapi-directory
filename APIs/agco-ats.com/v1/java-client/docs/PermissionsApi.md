# PermissionsApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**permissionsDeletePermission**](PermissionsApi.md#permissionsDeletePermission) | **DELETE** /api/v2/Permissions/{id} | Deletes a Permission |
| [**permissionsGetPermission**](PermissionsApi.md#permissionsGetPermission) | **GET** /api/v2/Permissions/{id} | Gets a Permission |
| [**permissionsGetPermissions**](PermissionsApi.md#permissionsGetPermissions) | **GET** /api/v2/Permissions | List Permissions |
| [**permissionsPostPermission**](PermissionsApi.md#permissionsPostPermission) | **POST** /api/v2/Permissions | Adds a Permission |
| [**permissionsPutPermission**](PermissionsApi.md#permissionsPutPermission) | **PUT** /api/v2/Permissions/{id} | Updates a Permission |


<a id="permissionsDeletePermission"></a>
# **permissionsDeletePermission**
> permissionsDeletePermission(id)

Deletes a Permission

No Documentation Found.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PermissionsApi apiInstance = new PermissionsApi(defaultClient);
    Integer id = 56; // Integer | Id of Permission
    try {
      apiInstance.permissionsDeletePermission(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling PermissionsApi#permissionsDeletePermission");
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
| **id** | **Integer**| Id of Permission | |

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

<a id="permissionsGetPermission"></a>
# **permissionsGetPermission**
> APIModelsPermission permissionsGetPermission(id)

Gets a Permission

No Documentation Found.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PermissionsApi apiInstance = new PermissionsApi(defaultClient);
    Integer id = 56; // Integer | Id of Permission
    try {
      APIModelsPermission result = apiInstance.permissionsGetPermission(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PermissionsApi#permissionsGetPermission");
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
| **id** | **Integer**| Id of Permission | |

### Return type

[**APIModelsPermission**](APIModelsPermission.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="permissionsGetPermissions"></a>
# **permissionsGetPermissions**
> APIPagedResponseAPIModelsPermission permissionsGetPermissions(limit, offset, name)

List Permissions

No Documentation Found.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PermissionsApi apiInstance = new PermissionsApi(defaultClient);
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    String name = "name_example"; // String | Filter by permission name. Supports ending wildcard (*). Optional.
    try {
      APIPagedResponseAPIModelsPermission result = apiInstance.permissionsGetPermissions(limit, offset, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PermissionsApi#permissionsGetPermissions");
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
| **name** | **String**| Filter by permission name. Supports ending wildcard (*). Optional. | [optional] |

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

<a id="permissionsPostPermission"></a>
# **permissionsPostPermission**
> Integer permissionsPostPermission(apIModelsPermission)

Adds a Permission

No Documentation Found.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PermissionsApi apiInstance = new PermissionsApi(defaultClient);
    APIModelsPermission apIModelsPermission = new APIModelsPermission(); // APIModelsPermission | Permission to add
    try {
      Integer result = apiInstance.permissionsPostPermission(apIModelsPermission);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PermissionsApi#permissionsPostPermission");
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
| **apIModelsPermission** | [**APIModelsPermission**](APIModelsPermission.md)| Permission to add | |

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

<a id="permissionsPutPermission"></a>
# **permissionsPutPermission**
> permissionsPutPermission(id, apIModelsPermission)

Updates a Permission

No Documentation Found.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    PermissionsApi apiInstance = new PermissionsApi(defaultClient);
    Integer id = 56; // Integer | Id of Permission
    APIModelsPermission apIModelsPermission = new APIModelsPermission(); // APIModelsPermission | The Updated Permission
    try {
      apiInstance.permissionsPutPermission(id, apIModelsPermission);
    } catch (ApiException e) {
      System.err.println("Exception when calling PermissionsApi#permissionsPutPermission");
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
| **id** | **Integer**| Id of Permission | |
| **apIModelsPermission** | [**APIModelsPermission**](APIModelsPermission.md)| The Updated Permission | |

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

