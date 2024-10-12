# UsersApi

All URIs are relative to *https://slack.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usersConversations**](UsersApi.md#usersConversations) | **GET** /users.conversations |  |
| [**usersDeletePhoto**](UsersApi.md#usersDeletePhoto) | **POST** /users.deletePhoto |  |
| [**usersGetPresence**](UsersApi.md#usersGetPresence) | **GET** /users.getPresence |  |
| [**usersIdentity**](UsersApi.md#usersIdentity) | **GET** /users.identity |  |
| [**usersInfo**](UsersApi.md#usersInfo) | **GET** /users.info |  |
| [**usersList**](UsersApi.md#usersList) | **GET** /users.list |  |
| [**usersLookupByEmail**](UsersApi.md#usersLookupByEmail) | **GET** /users.lookupByEmail |  |
| [**usersProfileGet_0**](UsersApi.md#usersProfileGet_0) | **GET** /users.profile.get |  |
| [**usersProfileSet_0**](UsersApi.md#usersProfileSet_0) | **POST** /users.profile.set |  |
| [**usersSetActive**](UsersApi.md#usersSetActive) | **POST** /users.setActive |  |
| [**usersSetPhoto**](UsersApi.md#usersSetPhoto) | **POST** /users.setPhoto |  |
| [**usersSetPresence**](UsersApi.md#usersSetPresence) | **POST** /users.setPresence |  |


<a id="usersConversations"></a>
# **usersConversations**
> UsersConversationsSuccessSchema usersConversations(token, user, types, excludeArchived, limit, cursor)



List conversations the calling user may access.

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `conversations:read`
    String user = "user_example"; // String | Browse conversations by a specific user ID's membership. Non-public channels are restricted to those where the calling user shares membership.
    String types = "types_example"; // String | Mix and match channel types by providing a comma-separated list of any combination of `public_channel`, `private_channel`, `mpim`, `im`
    Boolean excludeArchived = true; // Boolean | Set to `true` to exclude archived channels from the list
    Integer limit = 56; // Integer | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached. Must be an integer no larger than 1000.
    String cursor = "cursor_example"; // String | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more detail.
    try {
      UsersConversationsSuccessSchema result = apiInstance.usersConversations(token, user, types, excludeArchived, limit, cursor);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersConversations");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;conversations:read&#x60; | [optional] |
| **user** | **String**| Browse conversations by a specific user ID&#39;s membership. Non-public channels are restricted to those where the calling user shares membership. | [optional] |
| **types** | **String**| Mix and match channel types by providing a comma-separated list of any combination of &#x60;public_channel&#x60;, &#x60;private_channel&#x60;, &#x60;mpim&#x60;, &#x60;im&#x60; | [optional] |
| **excludeArchived** | **Boolean**| Set to &#x60;true&#x60; to exclude archived channels from the list | [optional] |
| **limit** | **Integer**| The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn&#39;t been reached. Must be an integer no larger than 1000. | [optional] |
| **cursor** | **String**| Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail. | [optional] |

### Return type

[**UsersConversationsSuccessSchema**](UsersConversationsSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response with only public channels. Note how &#x60;num_members&#x60; and &#x60;is_member&#x60; are not returned like typical &#x60;conversations&#x60; objects. |  -  |
| **0** | Typical error response |  -  |

<a id="usersDeletePhoto"></a>
# **usersDeletePhoto**
> UsersDeletePhotoSchema usersDeletePhoto(token)



Delete the user profile photo

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `users.profile:write`
    try {
      UsersDeletePhotoSchema result = apiInstance.usersDeletePhoto(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersDeletePhoto");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;users.profile:write&#x60; | |

### Return type

[**UsersDeletePhotoSchema**](UsersDeletePhotoSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="usersGetPresence"></a>
# **usersGetPresence**
> APIMethodUsersGetPresence usersGetPresence(token, user)



Gets user presence information.

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `users:read`
    String user = "user_example"; // String | User to get presence info on. Defaults to the authed user.
    try {
      APIMethodUsersGetPresence result = apiInstance.usersGetPresence(token, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersGetPresence");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;users:read&#x60; | |
| **user** | **String**| User to get presence info on. Defaults to the authed user. | [optional] |

### Return type

[**APIMethodUsersGetPresence**](APIMethodUsersGetPresence.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | When requesting information for a different user, this method just returns the current presence (either &#x60;active&#x60; or &#x60;away&#x60;). |  -  |
| **0** | Typical error response |  -  |

<a id="usersIdentity"></a>
# **usersIdentity**
> List&lt;UsersIdentitySchemaInner&gt; usersIdentity(token)



Get a user&#39;s identity.

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `identity.basic`
    try {
      List<UsersIdentitySchemaInner> result = apiInstance.usersIdentity(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersIdentity");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;identity.basic&#x60; | [optional] |

### Return type

[**List&lt;UsersIdentitySchemaInner&gt;**](UsersIdentitySchemaInner.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | You will receive at a minimum the following information: |  -  |
| **0** | Typical error response |  -  |

<a id="usersInfo"></a>
# **usersInfo**
> UsersInfoSuccessSchema usersInfo(token, includeLocale, user)



Gets information about a user.

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `users:read`
    Boolean includeLocale = true; // Boolean | Set this to `true` to receive the locale for this user. Defaults to `false`
    String user = "user_example"; // String | User to get info on
    try {
      UsersInfoSuccessSchema result = apiInstance.usersInfo(token, includeLocale, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersInfo");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;users:read&#x60; | |
| **includeLocale** | **Boolean**| Set this to &#x60;true&#x60; to receive the locale for this user. Defaults to &#x60;false&#x60; | [optional] |
| **user** | **String**| User to get info on | [optional] |

### Return type

[**UsersInfoSuccessSchema**](UsersInfoSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="usersList"></a>
# **usersList**
> UsersListSchema usersList(token, limit, cursor, includeLocale)



Lists all users in a Slack team.

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `users:read`
    Integer limit = 56; // Integer | The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn't been reached. Providing no `limit` value will result in Slack attempting to deliver you the entire result set. If the collection is too large you may experience `limit_required` or HTTP 500 errors.
    String cursor = "cursor_example"; // String | Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request's `response_metadata`. Default value fetches the first \"page\" of the collection. See [pagination](/docs/pagination) for more detail.
    Boolean includeLocale = true; // Boolean | Set this to `true` to receive the locale for users. Defaults to `false`
    try {
      UsersListSchema result = apiInstance.usersList(token, limit, cursor, includeLocale);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersList");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;users:read&#x60; | [optional] |
| **limit** | **Integer**| The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn&#39;t been reached. Providing no &#x60;limit&#x60; value will result in Slack attempting to deliver you the entire result set. If the collection is too large you may experience &#x60;limit_required&#x60; or HTTP 500 errors. | [optional] |
| **cursor** | **String**| Paginate through collections of data by setting the &#x60;cursor&#x60; parameter to a &#x60;next_cursor&#x60; attribute returned by a previous request&#39;s &#x60;response_metadata&#x60;. Default value fetches the first \&quot;page\&quot; of the collection. See [pagination](/docs/pagination) for more detail. | [optional] |
| **includeLocale** | **Boolean**| Set this to &#x60;true&#x60; to receive the locale for users. Defaults to &#x60;false&#x60; | [optional] |

### Return type

[**UsersListSchema**](UsersListSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="usersLookupByEmail"></a>
# **usersLookupByEmail**
> UsersLookupByEmailSuccessSchema usersLookupByEmail(token, email)



Find a user with an email address.

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `users:read.email`
    String email = "email_example"; // String | An email address belonging to a user in the workspace
    try {
      UsersLookupByEmailSuccessSchema result = apiInstance.usersLookupByEmail(token, email);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersLookupByEmail");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;users:read.email&#x60; | |
| **email** | **String**| An email address belonging to a user in the workspace | |

### Return type

[**UsersLookupByEmailSuccessSchema**](UsersLookupByEmailSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="usersProfileGet_0"></a>
# **usersProfileGet_0**
> UsersProfileGetSchema usersProfileGet_0(token, includeLabels, user)



Retrieves a user&#39;s profile information.

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `users.profile:read`
    Boolean includeLabels = true; // Boolean | Include labels for each ID in custom profile fields
    String user = "user_example"; // String | User to retrieve profile info for
    try {
      UsersProfileGetSchema result = apiInstance.usersProfileGet_0(token, includeLabels, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersProfileGet_0");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;users.profile:read&#x60; | |
| **includeLabels** | **Boolean**| Include labels for each ID in custom profile fields | [optional] |
| **user** | **String**| User to retrieve profile info for | [optional] |

### Return type

[**UsersProfileGetSchema**](UsersProfileGetSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="usersProfileSet_0"></a>
# **usersProfileSet_0**
> UsersProfileSetSchema usersProfileSet_0(token, name, profile, user, value)



Set the profile information for a user.

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `users.profile:write`
    String name = "name_example"; // String | Name of a single key to set. Usable only if `profile` is not passed.
    String profile = "profile_example"; // String | Collection of key:value pairs presented as a URL-encoded JSON hash. At most 50 fields may be set. Each field name is limited to 255 characters.
    String user = "user_example"; // String | ID of user to change. This argument may only be specified by team admins on paid teams.
    String value = "value_example"; // String | Value to set a single key to. Usable only if `profile` is not passed.
    try {
      UsersProfileSetSchema result = apiInstance.usersProfileSet_0(token, name, profile, user, value);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersProfileSet_0");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;users.profile:write&#x60; | |
| **name** | **String**| Name of a single key to set. Usable only if &#x60;profile&#x60; is not passed. | [optional] |
| **profile** | **String**| Collection of key:value pairs presented as a URL-encoded JSON hash. At most 50 fields may be set. Each field name is limited to 255 characters. | [optional] |
| **user** | **String**| ID of user to change. This argument may only be specified by team admins on paid teams. | [optional] |
| **value** | **String**| Value to set a single key to. Usable only if &#x60;profile&#x60; is not passed. | [optional] |

### Return type

[**UsersProfileSetSchema**](UsersProfileSetSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="usersSetActive"></a>
# **usersSetActive**
> UsersSetActiveSchema usersSetActive(token)



Marked a user as active. Deprecated and non-functional.

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `users:write`
    try {
      UsersSetActiveSchema result = apiInstance.usersSetActive(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersSetActive");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;users:write&#x60; | |

### Return type

[**UsersSetActiveSchema**](UsersSetActiveSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="usersSetPhoto"></a>
# **usersSetPhoto**
> UsersSetPhotoSchema usersSetPhoto(token, cropW, cropX, cropY, image)



Set the user profile photo

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `users.profile:write`
    String cropW = "cropW_example"; // String | Width/height of crop box (always square)
    String cropX = "cropX_example"; // String | X coordinate of top-left corner of crop box
    String cropY = "cropY_example"; // String | Y coordinate of top-left corner of crop box
    String image = "image_example"; // String | File contents via `multipart/form-data`.
    try {
      UsersSetPhotoSchema result = apiInstance.usersSetPhoto(token, cropW, cropX, cropY, image);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersSetPhoto");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;users.profile:write&#x60; | |
| **cropW** | **String**| Width/height of crop box (always square) | [optional] |
| **cropX** | **String**| X coordinate of top-left corner of crop box | [optional] |
| **cropY** | **String**| Y coordinate of top-left corner of crop box | [optional] |
| **image** | **String**| File contents via &#x60;multipart/form-data&#x60;. | [optional] |

### Return type

[**UsersSetPhotoSchema**](UsersSetPhotoSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

<a id="usersSetPresence"></a>
# **usersSetPresence**
> UsersSetPresenceSchema usersSetPresence(token, presence)



Manually sets user presence.

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
    defaultClient.setBasePath("https://slack.com/api");
    
    // Configure OAuth2 access token for authorization: slackAuth
    OAuth slackAuth = (OAuth) defaultClient.getAuthentication("slackAuth");
    slackAuth.setAccessToken("YOUR ACCESS TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String token = "token_example"; // String | Authentication token. Requires scope: `users:write`
    String presence = "presence_example"; // String | Either `auto` or `away`
    try {
      UsersSetPresenceSchema result = apiInstance.usersSetPresence(token, presence);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersSetPresence");
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
| **token** | **String**| Authentication token. Requires scope: &#x60;users:write&#x60; | |
| **presence** | **String**| Either &#x60;auto&#x60; or &#x60;away&#x60; | |

### Return type

[**UsersSetPresenceSchema**](UsersSetPresenceSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Typical success response |  -  |
| **0** | Typical error response |  -  |

