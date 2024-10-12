# UsersFollowsApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkIfUserIsFollowing**](UsersFollowsApi.md#checkIfUserIsFollowing) | **GET** /users/{user_id}/following/{follow_user_id} | Check if a user is following another user |
| [**checkIfUserIsFollowingAlt1**](UsersFollowsApi.md#checkIfUserIsFollowingAlt1) | **GET** /me/following/{follow_user_id} | Check if a user is following another user |
| [**followUser**](UsersFollowsApi.md#followUser) | **PUT** /users/{user_id}/following/{follow_user_id} | Follow a specific user |
| [**followUserAlt1**](UsersFollowsApi.md#followUserAlt1) | **PUT** /me/following/{follow_user_id} | Follow a specific user |
| [**followUsers**](UsersFollowsApi.md#followUsers) | **POST** /users/{user_id}/following | Follow a list of users |
| [**followUsersAlt1**](UsersFollowsApi.md#followUsersAlt1) | **POST** /me/following | Follow a list of users |
| [**getFollowers**](UsersFollowsApi.md#getFollowers) | **GET** /users/{user_id}/followers | Get all the followers of a user |
| [**getFollowersAlt1**](UsersFollowsApi.md#getFollowersAlt1) | **GET** /me/followers | Get all the followers of a user |
| [**getUserFollowing**](UsersFollowsApi.md#getUserFollowing) | **GET** /users/{user_id}/following | Get all the users that a user is following |
| [**getUserFollowingAlt1**](UsersFollowsApi.md#getUserFollowingAlt1) | **GET** /me/following | Get all the users that a user is following |
| [**unfollowUser**](UsersFollowsApi.md#unfollowUser) | **DELETE** /users/{user_id}/following/{follow_user_id} | Unfollow a user |
| [**unfollowUserAlt1**](UsersFollowsApi.md#unfollowUserAlt1) | **DELETE** /me/following/{follow_user_id} | Unfollow a user |


<a id="checkIfUserIsFollowing"></a>
# **checkIfUserIsFollowing**
> checkIfUserIsFollowing(followUserId, userId)

Check if a user is following another user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersFollowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersFollowsApi apiInstance = new UsersFollowsApi(defaultClient);
    BigDecimal followUserId = new BigDecimal("3766357"); // BigDecimal | The ID of the following user.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      apiInstance.checkIfUserIsFollowing(followUserId, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersFollowsApi#checkIfUserIsFollowing");
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
| **followUserId** | **BigDecimal**| The ID of the following user. | |
| **userId** | **BigDecimal**| The ID of the user. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The authenticated user follows the user in question. |  -  |
| **404** | The user in question doesn&#39;t follow the authenticated user. |  -  |

<a id="checkIfUserIsFollowingAlt1"></a>
# **checkIfUserIsFollowingAlt1**
> checkIfUserIsFollowingAlt1(followUserId)

Check if a user is following another user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersFollowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersFollowsApi apiInstance = new UsersFollowsApi(defaultClient);
    BigDecimal followUserId = new BigDecimal("3766357"); // BigDecimal | The ID of the following user.
    try {
      apiInstance.checkIfUserIsFollowingAlt1(followUserId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersFollowsApi#checkIfUserIsFollowingAlt1");
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
| **followUserId** | **BigDecimal**| The ID of the following user. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The authenticated user follows the user in question. |  -  |
| **404** | The user in question doesn&#39;t follow the authenticated user. |  -  |

<a id="followUser"></a>
# **followUser**
> followUser(followUserId, userId)

Follow a specific user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersFollowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersFollowsApi apiInstance = new UsersFollowsApi(defaultClient);
    BigDecimal followUserId = new BigDecimal("3766357"); // BigDecimal | The ID of the following user.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      apiInstance.followUser(followUserId, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersFollowsApi#followUser");
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
| **followUserId** | **BigDecimal**| The ID of the following user. | |
| **userId** | **BigDecimal**| The ID of the user. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The user was followed. |  -  |
| **403** | The authenticated user can&#39;t add followers. |  -  |

<a id="followUserAlt1"></a>
# **followUserAlt1**
> followUserAlt1(followUserId)

Follow a specific user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersFollowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersFollowsApi apiInstance = new UsersFollowsApi(defaultClient);
    BigDecimal followUserId = new BigDecimal("3766357"); // BigDecimal | The ID of the following user.
    try {
      apiInstance.followUserAlt1(followUserId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersFollowsApi#followUserAlt1");
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
| **followUserId** | **BigDecimal**| The ID of the following user. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The user was followed. |  -  |
| **403** | The authenticated user can&#39;t add followers. |  -  |

<a id="followUsers"></a>
# **followUsers**
> followUsers(userId, followUsersAlt1Request)

Follow a list of users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersFollowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersFollowsApi apiInstance = new UsersFollowsApi(defaultClient);
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    FollowUsersAlt1Request followUsersAlt1Request = new FollowUsersAlt1Request(); // FollowUsersAlt1Request | 
    try {
      apiInstance.followUsers(userId, followUsersAlt1Request);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersFollowsApi#followUsers");
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
| **userId** | **BigDecimal**| The ID of the user. | |
| **followUsersAlt1Request** | [**FollowUsersAlt1Request**](FollowUsersAlt1Request.md)|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The users were followed. |  -  |
| **400** | * Error code 2205: The request body is empty. * Error code 2205: The &#x60;users&#x60; array is invalid. * Error code 2205: The list of users doesn&#39;t contain URIs. * Error code 2900: A user in the list doesn&#39;t exist. * Error code 2901: The list contains more than 100 users. |  -  |
| **401** | Error code 8000: The user access token is invalid. |  -  |
| **403** | Error code 3417: The current user can&#39;t follow other users. |  -  |
| **429** | Error code 9006: The current user is rate-limited from following other users. |  -  |
| **500** | Error code 4005: An unexpected error occurred. |  -  |

<a id="followUsersAlt1"></a>
# **followUsersAlt1**
> followUsersAlt1(followUsersAlt1Request)

Follow a list of users

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersFollowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersFollowsApi apiInstance = new UsersFollowsApi(defaultClient);
    FollowUsersAlt1Request followUsersAlt1Request = new FollowUsersAlt1Request(); // FollowUsersAlt1Request | 
    try {
      apiInstance.followUsersAlt1(followUsersAlt1Request);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersFollowsApi#followUsersAlt1");
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
| **followUsersAlt1Request** | [**FollowUsersAlt1Request**](FollowUsersAlt1Request.md)|  | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The users were followed. |  -  |
| **400** | * Error code 2205: The request body is empty. * Error code 2205: The &#x60;users&#x60; array is invalid. * Error code 2205: The list of users doesn&#39;t contain URIs. * Error code 2900: A user in the list doesn&#39;t exist. * Error code 2901: The list contains more than 100 users. |  -  |
| **401** | Error code 8000: The user access token is invalid. |  -  |
| **403** | Error code 3417: The current user can&#39;t follow other users. |  -  |
| **429** | Error code 9006: The current user is rate-limited from following other users. |  -  |
| **500** | Error code 4005: An unexpected error occurred. |  -  |

<a id="getFollowers"></a>
# **getFollowers**
> List&lt;User&gt; getFollowers(userId, direction, page, perPage, query, sort)

Get all the followers of a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersFollowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersFollowsApi apiInstance = new UsersFollowsApi(defaultClient);
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    String direction = "asc"; // String | The sort direction of the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String query = "Stop motion"; // String | The search query to use to filter the results.
    String sort = "alphabetical"; // String | The way to sort the results.
    try {
      List<User> result = apiInstance.getFollowers(userId, direction, page, perPage, query, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersFollowsApi#getFollowers");
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
| **userId** | **BigDecimal**| The ID of the user. | |
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **query** | **String**| The search query to use to filter the results. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: alphabetical, date] |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.user+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The user&#39;s followers were returned. |  -  |

<a id="getFollowersAlt1"></a>
# **getFollowersAlt1**
> List&lt;User&gt; getFollowersAlt1(direction, page, perPage, query, sort)

Get all the followers of a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersFollowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersFollowsApi apiInstance = new UsersFollowsApi(defaultClient);
    String direction = "asc"; // String | The sort direction of the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String query = "Stop motion"; // String | The search query to use to filter the results.
    String sort = "alphabetical"; // String | The way to sort the results.
    try {
      List<User> result = apiInstance.getFollowersAlt1(direction, page, perPage, query, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersFollowsApi#getFollowersAlt1");
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
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **query** | **String**| The search query to use to filter the results. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: alphabetical, date] |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.user+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The user&#39;s followers were returned. |  -  |

<a id="getUserFollowing"></a>
# **getUserFollowing**
> List&lt;User&gt; getUserFollowing(userId, direction, filter, page, perPage, query, sort)

Get all the users that a user is following

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersFollowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersFollowsApi apiInstance = new UsersFollowsApi(defaultClient);
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    String direction = "asc"; // String | The sort direction of the results.
    String filter = "online"; // String | The attribute by which to filter the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String query = "Stop motion"; // String | The search query to use to filter the results.
    String sort = "alphabetical"; // String | The way to sort the results.
    try {
      List<User> result = apiInstance.getUserFollowing(userId, direction, filter, page, perPage, query, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersFollowsApi#getUserFollowing");
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
| **userId** | **BigDecimal**| The ID of the user. | |
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **filter** | **String**| The attribute by which to filter the results. | [optional] [enum: online] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **query** | **String**| The search query to use to filter the results. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: alphabetical, date] |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.user+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The followed users were returned. |  -  |

<a id="getUserFollowingAlt1"></a>
# **getUserFollowingAlt1**
> List&lt;User&gt; getUserFollowingAlt1(direction, filter, page, perPage, query, sort)

Get all the users that a user is following

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersFollowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersFollowsApi apiInstance = new UsersFollowsApi(defaultClient);
    String direction = "asc"; // String | The sort direction of the results.
    String filter = "online"; // String | The attribute by which to filter the results.
    BigDecimal page = new BigDecimal("1"); // BigDecimal | The page number of the results to show.
    BigDecimal perPage = new BigDecimal("10"); // BigDecimal | The number of items to show on each page of results, up to a maximum of 100.
    String query = "Stop motion"; // String | The search query to use to filter the results.
    String sort = "alphabetical"; // String | The way to sort the results.
    try {
      List<User> result = apiInstance.getUserFollowingAlt1(direction, filter, page, perPage, query, sort);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersFollowsApi#getUserFollowingAlt1");
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
| **direction** | **String**| The sort direction of the results. | [optional] [enum: asc, desc] |
| **filter** | **String**| The attribute by which to filter the results. | [optional] [enum: online] |
| **page** | **BigDecimal**| The page number of the results to show. | [optional] |
| **perPage** | **BigDecimal**| The number of items to show on each page of results, up to a maximum of 100. | [optional] |
| **query** | **String**| The search query to use to filter the results. | [optional] |
| **sort** | **String**| The way to sort the results. | [optional] [enum: alphabetical, date] |

### Return type

[**List&lt;User&gt;**](User.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.user+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The followed users were returned. |  -  |

<a id="unfollowUser"></a>
# **unfollowUser**
> unfollowUser(followUserId, userId)

Unfollow a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersFollowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersFollowsApi apiInstance = new UsersFollowsApi(defaultClient);
    BigDecimal followUserId = new BigDecimal("3766357"); // BigDecimal | The ID of the following user.
    BigDecimal userId = new BigDecimal("152184"); // BigDecimal | The ID of the user.
    try {
      apiInstance.unfollowUser(followUserId, userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersFollowsApi#unfollowUser");
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
| **followUserId** | **BigDecimal**| The ID of the following user. | |
| **userId** | **BigDecimal**| The ID of the user. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The user was unfollowed. |  -  |

<a id="unfollowUserAlt1"></a>
# **unfollowUserAlt1**
> unfollowUserAlt1(followUserId)

Unfollow a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersFollowsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UsersFollowsApi apiInstance = new UsersFollowsApi(defaultClient);
    BigDecimal followUserId = new BigDecimal("3766357"); // BigDecimal | The ID of the following user.
    try {
      apiInstance.unfollowUserAlt1(followUserId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersFollowsApi#unfollowUserAlt1");
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
| **followUserId** | **BigDecimal**| The ID of the following user. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The user was unfollowed. |  -  |

