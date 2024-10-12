# UsersApi

All URIs are relative to *https://dev.to/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOrgUsers_0**](UsersApi.md#getOrgUsers_0) | **GET** /api/organizations/{username}/users | Organization&#39;s users |
| [**getUser**](UsersApi.md#getUser) | **GET** /api/users/{id} | A User |
| [**getUserAllArticles_0**](UsersApi.md#getUserAllArticles_0) | **GET** /api/articles/me/all | User&#39;s all articles |
| [**getUserArticles_0**](UsersApi.md#getUserArticles_0) | **GET** /api/articles/me | User&#39;s articles |
| [**getUserMe**](UsersApi.md#getUserMe) | **GET** /api/users/me | The authenticated user |
| [**getUserPublishedArticles_0**](UsersApi.md#getUserPublishedArticles_0) | **GET** /api/articles/me/published | User&#39;s published articles |
| [**getUserUnpublishedArticles_0**](UsersApi.md#getUserUnpublishedArticles_0) | **GET** /api/articles/me/unpublished | User&#39;s unpublished articles |
| [**postAdminUsersCreate**](UsersApi.md#postAdminUsersCreate) | **POST** /api/admin/users | Invite a User |
| [**suspendUser**](UsersApi.md#suspendUser) | **PUT** /api/users/{id}/suspend | Suspend a User |
| [**unpublishUser**](UsersApi.md#unpublishUser) | **PUT** /api/users/{id}/unpublish | Unpublish a User&#39;s Articles and Comments |


<a id="getOrgUsers_0"></a>
# **getOrgUsers_0**
> List&lt;User&gt; getOrgUsers_0(username, page, perPage)

Organization&#39;s users

This endpoint allows the client to retrieve a list of users belonging to the organization  It supports pagination, each page will contain &#x60;30&#x60; users by default.

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
    defaultClient.setBasePath("https://dev.to/api");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String username = "username_example"; // String | 
    Integer page = 1; // Integer | Pagination page
    Integer perPage = 30; // Integer | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
    try {
      List<User> result = apiInstance.getOrgUsers_0(username, page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getOrgUsers_0");
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
| **username** | **String**|  | |
| **page** | **Integer**| Pagination page | [optional] [default to 1] |
| **perPage** | **Integer**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 30] |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An Organization&#39;s users |  -  |
| **404** | Not Found |  -  |

<a id="getUser"></a>
# **getUser**
> List&lt;User&gt; getUser(id)

A User

This endpoint allows the client to retrieve a single user, either by id or by the user&#39;s username.  For complete documentation, see the v0 API docs: https://developers.forem.com/api/v0#tag/users/operation/getUser

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      List<User> result = apiInstance.getUser(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUser");
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
| **id** | **String**|  | |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |

<a id="getUserAllArticles_0"></a>
# **getUserAllArticles_0**
> List&lt;ArticleIndex&gt; getUserAllArticles_0(page, perPage)

User&#39;s all articles

This endpoint allows the client to retrieve a list of all articles on behalf of an authenticated user.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.  It will return both published and unpublished articles with pagination.  Unpublished articles will be at the top of the list in reverse chronological creation order. Published articles will follow in reverse chronological publication order.  By default a page will contain 30 articles.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer page = 1; // Integer | Pagination page
    Integer perPage = 30; // Integer | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
    try {
      List<ArticleIndex> result = apiInstance.getUserAllArticles_0(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUserAllArticles_0");
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
| **page** | **Integer**| Pagination page | [optional] [default to 1] |
| **perPage** | **Integer**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 30] |

### Return type

[**List&lt;ArticleIndex&gt;**](ArticleIndex.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A List of the authenticated user&#39;s Articles |  -  |
| **401** | Unauthorized |  -  |

<a id="getUserArticles_0"></a>
# **getUserArticles_0**
> List&lt;ArticleIndex&gt; getUserArticles_0(page, perPage)

User&#39;s articles

This endpoint allows the client to retrieve a list of published articles on behalf of an authenticated user.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.  Published articles will be in reverse chronological publication order.  It will return published articles with pagination. By default a page will contain 30 articles.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer page = 1; // Integer | Pagination page
    Integer perPage = 30; // Integer | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
    try {
      List<ArticleIndex> result = apiInstance.getUserArticles_0(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUserArticles_0");
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
| **page** | **Integer**| Pagination page | [optional] [default to 1] |
| **perPage** | **Integer**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 30] |

### Return type

[**List&lt;ArticleIndex&gt;**](ArticleIndex.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A List of the authenticated user&#39;s Articles |  -  |
| **401** | Unauthorized |  -  |

<a id="getUserMe"></a>
# **getUserMe**
> List&lt;User&gt; getUserMe()

The authenticated user

This endpoint allows the client to retrieve information about the authenticated user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    try {
      List<User> result = apiInstance.getUserMe();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUserMe");
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

[**List&lt;User&gt;**](User.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful |  -  |
| **401** | Unauthorized |  -  |

<a id="getUserPublishedArticles_0"></a>
# **getUserPublishedArticles_0**
> List&lt;ArticleIndex&gt; getUserPublishedArticles_0(page, perPage)

User&#39;s published articles

This endpoint allows the client to retrieve a list of published articles on behalf of an authenticated user.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.  Published articles will be in reverse chronological publication order.  It will return published articles with pagination. By default a page will contain 30 articles.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer page = 1; // Integer | Pagination page
    Integer perPage = 30; // Integer | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
    try {
      List<ArticleIndex> result = apiInstance.getUserPublishedArticles_0(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUserPublishedArticles_0");
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
| **page** | **Integer**| Pagination page | [optional] [default to 1] |
| **perPage** | **Integer**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 30] |

### Return type

[**List&lt;ArticleIndex&gt;**](ArticleIndex.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A List of the authenticated user&#39;s Articles |  -  |
| **401** | Unauthorized |  -  |

<a id="getUserUnpublishedArticles_0"></a>
# **getUserUnpublishedArticles_0**
> List&lt;ArticleIndex&gt; getUserUnpublishedArticles_0(page, perPage)

User&#39;s unpublished articles

This endpoint allows the client to retrieve a list of unpublished articles on behalf of an authenticated user.  \&quot;Articles\&quot; are all the posts that users create on DEV that typically show up in the feed. They can be a blog post, a discussion question, a help thread etc. but is referred to as article within the code.  Unpublished articles will be in reverse chronological creation order.  It will return unpublished articles with pagination. By default a page will contain 30 articles.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer page = 1; // Integer | Pagination page
    Integer perPage = 30; // Integer | Page size (the number of items to return per page). The default maximum value can be overridden by \"API_PER_PAGE_MAX\" environment variable.
    try {
      List<ArticleIndex> result = apiInstance.getUserUnpublishedArticles_0(page, perPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#getUserUnpublishedArticles_0");
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
| **page** | **Integer**| Pagination page | [optional] [default to 1] |
| **perPage** | **Integer**| Page size (the number of items to return per page). The default maximum value can be overridden by \&quot;API_PER_PAGE_MAX\&quot; environment variable. | [optional] [default to 30] |

### Return type

[**List&lt;ArticleIndex&gt;**](ArticleIndex.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A List of the authenticated user&#39;s Articles |  -  |
| **401** | Unauthorized |  -  |

<a id="postAdminUsersCreate"></a>
# **postAdminUsersCreate**
> postAdminUsersCreate(userInviteParam)

Invite a User

This endpoint allows the client to trigger an invitation to the provided email address.          It requires a token from a user with &#x60;super_admin&#x60; privileges.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    UserInviteParam userInviteParam = new UserInviteParam(); // UserInviteParam | 
    try {
      apiInstance.postAdminUsersCreate(userInviteParam);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#postAdminUsersCreate");
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
| **userInviteParam** | [**UserInviteParam**](UserInviteParam.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |
| **401** | Unauthorized |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="suspendUser"></a>
# **suspendUser**
> suspendUser(id)

Suspend a User

This endpoint allows the client to suspend a user.  The user associated with the API key must have any &#39;admin&#39; or &#39;moderator&#39; role.  This specified user will be assigned the &#39;suspended&#39; role. Suspending a user will stop the user from posting new posts and comments. It doesn&#39;t delete any of the user&#39;s content, just prevents them from creating new content while suspended. Users are not notified of their suspension in the UI, so if you want them to know about this, you must notify them.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 1; // Integer | The ID of the user to suspend.
    try {
      apiInstance.suspendUser(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#suspendUser");
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
| **id** | **Integer**| The ID of the user to suspend. | |

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | User successfully unpublished |  -  |
| **401** | Unauthorized |  -  |
| **404** | Unknown User ID |  -  |

<a id="unpublishUser"></a>
# **unpublishUser**
> unpublishUser(id)

Unpublish a User&#39;s Articles and Comments

This endpoint allows the client to unpublish all of the articles and comments created by a user.  The user associated with the API key must have any &#39;admin&#39; or &#39;moderator&#39; role.  This specified user&#39;s articles and comments will be unpublished and will no longer be visible to the public. They will remain in the database and will set back to draft status on the specified user&#39;s  dashboard. Any notifications associated with the specified user&#39;s articles and comments will be deleted.  Note this endpoint unpublishes articles and comments asychronously: it will return a 204 NO CONTENT status code immediately, but the articles and comments will not be unpublished until the request is completed on the server.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    UsersApi apiInstance = new UsersApi(defaultClient);
    Integer id = 1; // Integer | The ID of the user to unpublish.
    try {
      apiInstance.unpublishUser(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#unpublishUser");
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
| **id** | **Integer**| The ID of the user to unpublish. | |

### Return type

null (empty response body)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | User&#39;s articles and comments successfully unpublished |  -  |
| **401** | Unauthorized |  -  |
| **404** | Unknown User ID (still accepted for async processing) |  -  |

