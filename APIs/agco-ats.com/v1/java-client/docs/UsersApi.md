# UsersApi

All URIs are relative to *https://secure.agco-ats.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV2UsersIdGet**](UsersApi.md#apiV2UsersIdGet) | **GET** /api/v2/Users/{id} | Get a specific user |
| [**usersDelete**](UsersApi.md#usersDelete) | **DELETE** /api/v2/Users/{id} | Delete a user |
| [**usersGet**](UsersApi.md#usersGet) | **GET** /api/v2/Users | Get users |
| [**usersGetCurrentUser**](UsersApi.md#usersGetCurrentUser) | **GET** /api/v2/Users/Current | Gets the current user |
| [**usersPost**](UsersApi.md#usersPost) | **POST** /api/v2/Users | Create a user |
| [**usersPut**](UsersApi.md#usersPut) | **PUT** /api/v2/Users/{id} | Update a user |
| [**usersPutCurrentUser**](UsersApi.md#usersPutCurrentUser) | **PUT** /api/v2/Users/Current | Update a user |


<a id="apiV2UsersIdGet"></a>
# **apiV2UsersIdGet**
> APIModelsUser apiV2UsersIdGet(id)

Get a specific user

No Documentation Found.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | The user ID
    try {
      APIModelsUser result = apiInstance.apiV2UsersIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#apiV2UsersIdGet");
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
| **id** | **Integer**| The user ID | |

### Return type

[**APIModelsUser**](APIModelsUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="usersDelete"></a>
# **usersDelete**
> usersDelete(id)

Delete a user

No Documentation Found.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | The user id
    try {
      apiInstance.usersDelete(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersDelete");
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
| **id** | **Integer**| The user id | |

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

<a id="usersGet"></a>
# **usersGet**
> APIPagedResponseAPIModelsUser usersGet(username, email, name, hasRole, limit, offset)

Get users

No Documentation Found.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String username = "username_example"; // String | Optional. Search by username. Supports beginning and ending wildcards (*).
    String email = "email_example"; // String | Optional. Search by email. Supports beginning and ending wildcards (*).
    String name = "name_example"; // String | Optional. Search by name. Supports beginning and ending wildcards (*).
    String hasRole = "hasRole_example"; // String | Optional. Return only users having the provided role name.
    Integer limit = 56; // Integer | Optional. The page limit. The default page limit is 10.
    Integer offset = 56; // Integer | Optional. The page offset. The default page offset is 0.
    try {
      APIPagedResponseAPIModelsUser result = apiInstance.usersGet(username, email, name, hasRole, limit, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersGet");
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
| **username** | **String**| Optional. Search by username. Supports beginning and ending wildcards (*). | [optional] |
| **email** | **String**| Optional. Search by email. Supports beginning and ending wildcards (*). | [optional] |
| **name** | **String**| Optional. Search by name. Supports beginning and ending wildcards (*). | [optional] |
| **hasRole** | **String**| Optional. Return only users having the provided role name. | [optional] |
| **limit** | **Integer**| Optional. The page limit. The default page limit is 10. | [optional] |
| **offset** | **Integer**| Optional. The page offset. The default page offset is 0. | [optional] |

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

<a id="usersGetCurrentUser"></a>
# **usersGetCurrentUser**
> APIModelsUser usersGetCurrentUser()

Gets the current user

No Documentation Found.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    try {
      APIModelsUser result = apiInstance.usersGetCurrentUser();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersGetCurrentUser");
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

[**APIModelsUser**](APIModelsUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="usersPost"></a>
# **usersPost**
> APIModelsUser usersPost(apIModelsUser)

Create a user

No Documentation Found.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    APIModelsUser apIModelsUser = new APIModelsUser(); // APIModelsUser | The user to create.
    try {
      APIModelsUser result = apiInstance.usersPost(apIModelsUser);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersPost");
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
| **apIModelsUser** | [**APIModelsUser**](APIModelsUser.md)| The user to create. | |

### Return type

[**APIModelsUser**](APIModelsUser.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="usersPut"></a>
# **usersPut**
> usersPut(id, apIModelsUser)

Update a user

No Documentation Found.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 56; // Integer | The user id
    APIModelsUser apIModelsUser = new APIModelsUser(); // APIModelsUser | The user
    try {
      apiInstance.usersPut(id, apIModelsUser);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersPut");
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
| **id** | **Integer**| The user id | |
| **apIModelsUser** | [**APIModelsUser**](APIModelsUser.md)| The user | |

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

<a id="usersPutCurrentUser"></a>
# **usersPutCurrentUser**
> usersPutCurrentUser(apIModelsUser)

Update a user

No Documentation Found.

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
    defaultClient.setBasePath("https://secure.agco-ats.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    APIModelsUser apIModelsUser = new APIModelsUser(); // APIModelsUser | The user
    try {
      apiInstance.usersPutCurrentUser(apIModelsUser);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersPutCurrentUser");
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
| **apIModelsUser** | [**APIModelsUser**](APIModelsUser.md)| The user | |

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

